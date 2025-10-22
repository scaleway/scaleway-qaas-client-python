def is_valid_iana(time_zone: str) -> bool:
    import pytz

    if not time_zone:
        return False
    try:
        pytz.timezone(time_zone)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False


def get_local_iana_timezone() -> str:
    import tzlocal

    try:
        tz_name = tzlocal.get_localzone_name()
        return tz_name
    except Exception:
        return "UTC"
