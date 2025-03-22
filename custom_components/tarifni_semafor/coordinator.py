import logging
from typing import Self, Any

import aiohttp

from datetime import datetime, timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers.event import async_call_later

_LOGGER = logging.getLogger(__name__)

API_URL = "https://www.uro.si/o/api/tarifnisemafor/v1/casovniblok"
UPDATE_INTERVAL = timedelta(minutes=15)


class TarifniSemaforCoordinator(DataUpdateCoordinator):
    """Coordinator for Tarifni semafor.

    This coordinator will update the data from the URO REST API. For now
    this is a simple fetch from the API every 15 minutes. With a scheduled
    fetch one second after new block has started.

    In the future update interval will be removed. Probably.
    """

    def __init__(self: Self, hass: HomeAssistant):
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name="Tarifni Semafor Coordinator",
            update_interval=UPDATE_INTERVAL,
        )

    async def _async_update_data(self: Self):
        """Fetch data from the Tarifni Semafor API."""
        _LOGGER.debug("Fetching data from Tarifni Semafor API")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(API_URL, timeout=10) as response:
                    if response.status != 200:
                        raise UpdateFailed(f"API returned HTTP {response.status}")
                    data = await response.json()
                    _LOGGER.debug("API Response is JSON, party on.")

                    self._schedule_next_refresh(data)

                    return data
        except Exception as err:
            raise UpdateFailed(f"Error fetching data: {err}")

    def _schedule_next_refresh(self: Self, data: dict[str, Any]) -> None:
        """Schedule next refresh.

        Next refresh needs to be forced after the next block was started.
        """
        block_info = data.get("casovniBlokTrenutni", {}).get("casovniBlok", {})
        hour_to = block_info.get("uraDo")
        if hour_to is not None:
            now = datetime.now()
            block_end = now.replace(hour=hour_to, minute=0, second=1, microsecond=0)
            if block_end <= now:
                block_end += timedelta(days=1)

            # There is probably a better way of doing this, meh.
            delay = (block_end - now).total_seconds()
            delay_td = timedelta(seconds=int(delay))
            hours, remainder = divmod(delay_td.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            _LOGGER.debug(
                f"Scheduling additional refresh in {hours}h {minutes}m {seconds}s (at block end)"
            )
            async_call_later(self.hass, delay, lambda _: self.async_request_refresh())
