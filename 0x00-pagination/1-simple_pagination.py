#!/usr/bin/env python3
"""
This module provides a Server class for paginating a database.
"""

import csv
from typing import List, Tuple


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from a CSV file.

        Returns:
            List[List]: The loaded dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of baby name data with pagination.

        Args:
            page (int): The page number, starting from 1.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows for the specified page, or an empty list
            if the page or page_size is out of range.
        """
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
