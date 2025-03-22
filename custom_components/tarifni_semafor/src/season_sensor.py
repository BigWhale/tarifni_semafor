import logging
from enum import IntEnum
from typing import Any

from homeassistant.components.sensor import Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

_LOGGER = logging.getLogger(__name__)


class Season(IntEnum):
    HIGH = 1
    LOW = 2

    def label(self) -> str:
        return {Season.LOW: "Low Season", Season.HIGH: "High Season"}[self]


class SeasonSensor(CoordinatorEntity, Entity):
    def __init__(self, coordinator: CoordinatorEntity) -> None:
        CoordinatorEntity.__init__(self, coordinator)
        Entity.__init__(self)
        self.coordinator = coordinator

    @property
    def name(self) -> str:
        return "Tarifni Semafor Season"

    @property
    def unique_id(self) -> str:
        return "tarifni_semafor_season"

    @property
    def state(self) -> str:
        season_id = (
            self.coordinator.data.get("casovniBlokTrenutni", {})
            .get("sezonaCasovnegaBloka", {})
            .get("sezonaID", 1)
        )
        return Season(season_id).label()

    @property
    def options(self) -> str:
        return [s.label() for s in Season]

    @property
    def device_class(self) -> str:
        return "enum"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        season_id = (
            self.coordinator.data.get("casovniBlokTrenutni", {})
            .get("sezonaCasovnegaBloka", {})
            .get("sezonaID", 1)
        )
        return {"season_id": season_id}
