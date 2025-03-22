from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .coordinator import TarifniSemaforCoordinator

DOMAIN = "tarifni_semafor"


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up Tarifni Semafor from YAML (not used)."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Tarifni Semafor from a config entry."""

    # Initialize the coordinator and fetch the first data.
    data_coordinator = TarifniSemaforCoordinator(hass)
    await data_coordinator.async_config_entry_first_refresh()

    # Store the coordinator in hass.data
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = data_coordinator

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    hass.data[DOMAIN].pop(entry.entry_id, None)
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
