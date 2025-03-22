import logging
from typing import Self

from .base_sensor import BaseBlockSensor

_LOGGER = logging.getLogger(__name__)


class CurrentBlockSensor(BaseBlockSensor):
    @property
    def name(self: Self) -> str:
        return "Tarifni Semafor Current Block"

    @property
    def unique_id(self: Self) -> str:
        return "tarifni_semafor_current_block"

    def get_block_data(self: Self) -> dict:
        _LOGGER.debug("get_block_data for CurrentBlockSensor")
        return self.coordinator.data.get("casovniBlokTrenutni", {}).get(
            "casovniBlok", {}
        )
