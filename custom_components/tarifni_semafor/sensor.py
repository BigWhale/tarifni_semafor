import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DOMAIN
from .src.current_block_sensor import CurrentBlockSensor
from .src.next_block_sensor import NextBlockSensor
from .src.progress_sensor import BlockProgressSensor
from .src.season_sensor import SeasonSensor

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Tarifni Semafor sensors from a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            CurrentBlockSensor(coordinator),
            NextBlockSensor(coordinator),
            BlockProgressSensor(coordinator),
            SeasonSensor(coordinator),
        ],
        True,
    )
