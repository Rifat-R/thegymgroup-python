# thegymgroup-python

Unofficial Python SDK for The Gym Group mobile API.

This project is not affiliated with The Gym Group.

## Requirements

- Python >= 3.13
- `requests`

## Install

From source:

```bash
pip install .
```

Editable install for development:

```bash
pip install -e .
```

## Login

```python
from thegymgroup import Client

client = Client.login("you@example.com", "1234")
```

## Example: Gym occupancy (with percentage, capacity, and historical loop)

```python
from thegymgroup import Client, Locations

client = Client.login("you@example.com", "1234")
occupancy = client.get_gym_occupancy(Locations.SHEFFIELD_KELHAM_ISLAND)

print(f"Gym: {occupancy.gym_location_name}")
print(f"Status: {occupancy.status}")
print(f"Current: {occupancy.current_percentage}% ({occupancy.current_capacity} people)")

for point in occupancy.historical:
    print(f"{point.hour}: {point.percentage}%")
```

## Example: Get latest check-in

```python
from thegymgroup import Client

client = Client.login("you@example.com", "1234")
latest = client.get_latest_check_in()
print(latest)
```

## Example: Get hours in gym over a date range

```python
from datetime import date

from thegymgroup import Client

client = Client.login("you@example.com", "1234")
hours = client.get_hours_in_gym(
    start=date(2026, 3, 1),
    end=date(2026, 3, 11),
)
print(f"Hours in gym: {hours}")
```

## Example: Get classes for a location and time window

```python
from datetime import datetime

from thegymgroup import Client, Locations

client = Client.login("you@example.com", "1234")
classes = client.get_classes(
    location=Locations.SHEFFIELD_KELHAM_ISLAND,
    start=datetime(2026, 3, 11, 0, 0),
    end=datetime(2026, 3, 11, 23, 59),
)

print(f"Found {len(classes.get('classes', []))} classes")
```

## Notes

- This SDK targets mobile API endpoints and may break if upstream APIs change.
- Use at your own risk.
