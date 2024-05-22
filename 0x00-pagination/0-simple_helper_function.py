#!/usr/bin/env python3
""" Simple helper function """


def index_range(page: int, page_size: int) -> tuple:
    """ Return a tuple of size two containing a start index and an end index

    Args:
        page (int): the current page
        page_size (int): total size of the page

    Returns:
        tuple: two size containing start index and end index
    """
    # Calculate the start index
    start_page = (page - 1) * page_size
    # Calculate the end index
    end_page = page * page_size
    return (start_page, end_page)
