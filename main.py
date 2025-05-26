"""Provides a function to convert a dictionary of objects."""


def demo(d: dict[str, object]) -> dict[str, object]:
    """Convert a dictionary of objects to a dictionary of their item representations."""
    result: dict[str, object] = {}
    for k, v in d.items():
        if hasattr(v, "item"):
            result[k] = v.item()
        else:
            result[k] = v
    return result
