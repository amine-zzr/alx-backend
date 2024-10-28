#!/usr/bin/env python3
"""
This module provides a function for calculating the start and end index
for paginating a list given a page number and page size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for items to display on a given page
    with a specified page size.

    Args:
        page (int): The current page number, 1-indexed.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index for
        the items to display.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
