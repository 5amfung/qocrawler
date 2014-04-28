# Utilities.
#


def trim(lst):
    """Trim strings in the list.

    Args:
        lst: A list of string.
    Returns:
        A list of trimmed string.
    """
    results = map(lambda x: x.strip(), lst)
    return results[0] if len(results) == 1 else results


def extract(sel):
    """Call extract on selector and remove leading and trailing spaces from results.

    Args:
        sel: A Selector object.
    Returns:
        Return a string or a list of string depending on the what are returned from the selector.
    """
    return trim(sel.extract())
