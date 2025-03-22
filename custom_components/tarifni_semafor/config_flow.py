"""Config flow for Tarifni Semafor integration."""

from typing import Self

from homeassistant import config_entries
from . import DOMAIN


class TarifniSemaforConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Tarifni Semafor.

    We're not doing anything here.
    """

    async def async_step_user(self: Self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Tarifni Semafor", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=None,
            description_placeholders={
                "info": "This integration fetches electricity tariff blocks from uro.si"
            },
        )
