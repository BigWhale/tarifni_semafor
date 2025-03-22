import logging
from typing import Any, Self

from .base_sensor import BaseBlockSensor

_LOGGER = logging.getLogger(__name__)


class NextBlockSensor(BaseBlockSensor):
    @property
    def name(self: Self) -> str:
        return "Tarifni Semafor Next Block"

    @property
    def unique_id(self: Self) -> str:
        return "tarifni_semafor_next_block"

    def get_block_data(self: Self) -> dict[str, Any]:
        _LOGGER.debug("get_block_data for NextBlockSensor")
        return self.coordinator.data.get("casovniBlokNaslednji", {}).get(
            "casovniBlok", {}
        )
