from datetime import datetime, date, time


def __ensure_datetime(value: datetime | date, *, end_of_day: bool = False) -> datetime:
    if isinstance(value, datetime):
        return value
    elif isinstance(value, date):
        return datetime.combine(value, time.max if end_of_day else time.min)


def to_epoch_millis(value: datetime | date, *, end_of_day: bool = False) -> int:
    dt = __ensure_datetime(value, end_of_day=end_of_day)
    return int(dt.timestamp() * 1000)


def to_api_iso(value: datetime | date, *, end_of_day: bool = False) -> str:
    dt = __ensure_datetime(value, end_of_day=end_of_day)
    return dt.strftime("%Y-%m-%dT%H:%M:%S")
