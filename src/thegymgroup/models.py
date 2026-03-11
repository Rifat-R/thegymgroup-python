from dataclasses import dataclass


@dataclass(frozen=True)
class HistoricalBusyness:
    hour: str
    percentage: int


@dataclass(frozen=True)
class GymOccupancy:
    gym_location_id: str
    gym_location_name: str
    current_capacity: int
    current_percentage: int
    historical: list[HistoricalBusyness]
    status: str
