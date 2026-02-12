def cleanup_task(raw_items: list) -> dict:
    """
    Cleans raw input data by:
    - removing empty values
    - normalizing strings
    """

    if not isinstance(raw_items, list):
        raise ValueError("raw_items must be a list")

    cleaned_items = []

    for item in raw_items:
        if not item:
            continue

        if isinstance(item, str):
            cleaned_items.append(item.strip().lower())
        else:
            cleaned_items.append(item)

    return {
        "input_count": len(raw_items),
        "output_count": len(cleaned_items),
        "cleaned_items": cleaned_items,
        "status": "cleanup_completed"
    }
