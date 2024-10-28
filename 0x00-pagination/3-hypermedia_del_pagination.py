#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        deletion-resilient pagination by returning a page of data starting
        from given index and handling possible gaps caused by deleted entries.

        Args:
            index (int): The start index for pagination.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Optional[int | List[List]]]: A dictionary containing the
            current index, page data, page size, and the next index.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        assert index < len(indexed_data)

        data = []
        current_idx = index
        while len(data) < page_size and current_idx < len(indexed_data):
            if current_idx in indexed_data:
                data.append(indexed_data[current_idx])
            current_idx += 1

        next_index = current_idx if current_idx < len(indexed_data) else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
