# Utilities.
#


def trim(lst):
    """Trim and return the first element of a list.  Otherwise, return an empty string."""
    return lst[0].strip() if lst else ''
