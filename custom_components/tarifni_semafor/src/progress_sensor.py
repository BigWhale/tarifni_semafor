import logging
from typing import Self

from .current_block_sensor import CurrentBlockSensor

_LOGGER = logging.getLogger(__name__)


class BlockProgressSensor(CurrentBlockSensor):
    @property
    def name(self: Self) -> str:
        return "Tarifni Semafor Progress"

    @property
    def unique_id(self: Self) -> str:
        return "tarifni_semafor_progress"

    @property
    def state(self: Self) -> float:
        return self.calculate_progress()

    @property
    def unit_of_measurement(self: Self) -> str:
        return "%"

    @property
    def device_class(self: Self) -> str:
        return "number"
