import logging
from datetime import datetime, timedelta
from typing import Any, Self

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

_LOGGER = logging.getLogger(__name__)


class BaseBlockSensor(CoordinatorEntity, SensorEntity):
    def __init__(self: Self, coordinator):
        CoordinatorEntity.__init__(self, coordinator)
        SensorEntity.__init__(self)
        self.coordinator = coordinator
        _LOGGER.debug("Base sensor entity initialized")

    def get_block_data(self):
        """Must be implemented by subclasses: return dict with block info."""
        raise NotImplementedError

    @property
    def _block_id(self: Self) -> str:
        return self.get_block_data().get("casovniBlokId")

    @property
    def _block_start(self: Self) -> str:
        hour = self.get_block_data().get("uraOd")
        return f"{hour:02d}:00" if hour is not None else None

    @property
    def _block_end(self: Self) -> str:
        hour = self.get_block_data().get("uraDo")
        return f"{hour:02d}:00" if hour is not None else None

    def calculate_progress(self: Self) -> float:
        now = datetime.now()
        try:
            start = datetime.strptime(self._block_start, "%H:%M").replace(
                year=now.year, month=now.month, day=now.day
            )
            end = datetime.strptime(self._block_end, "%H:%M").replace(
                year=now.year, month=now.month, day=now.day
            )
            if end <= start:
                end += timedelta(days=1)
            total = (end - start).total_seconds()
            elapsed = (now - start).total_seconds()
            progress = (elapsed / total) * 100 if total > 0 else 0
            return round(min(max(progress, 0), 100), 1)
        except Exception:  # :eyeroll:
            return 0.0

    @property
    def device_class(self: Self) -> str:
        return "enum"

    @property
    def state(self: Self) -> str:
        return f"Block {self._block_id}"

    @property
    def extra_state_attributes(self: Self) -> dict[str, Any]:
        return {
            "block_id": self._block_id,
            "block_start": self._block_start,
            "block_end": self._block_end,
        }
