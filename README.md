# thegymgroup

WIP, unofficial SDK for TheGymGroup API (Mobile).
Not affiliated with The Gym Group.

## Status

This package is not published on PyPI yet (goal is to publish there).

## Requirements

- Python >= 3.13
- `requests`

## Install

From source (local):

```bash
pip install .
```

Editable install for development:

```bash
pip install -e .
```

## Quick start

```python
from thegymgroup import Client

client = Client.login("you@example.com", "1234")
hours = client.get_hours_in_gym()
print(hours)
```

## Notes

- This SDK targets the mobile API endpoints and may break if the upstream API changes.
- Use at your own risk;
