import requests


def api_sync(api_url: str) -> dict:
    """
    Fetches data from an external API
    and returns a normalized summary.
    """

    response = requests.get(api_url, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, list):
        raise ValueError("Expected list response from API")

    record_count = len(data)

    return {
        "source": api_url,
        "records_fetched": record_count,
        "sample_record": data[0] if record_count > 0 else None,
        "status": "sync_completed"
    }
