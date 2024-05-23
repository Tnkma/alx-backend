import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """that takes two integer arguments page with
        default value 1 and page_size with default value 10.

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        # First we assert if page and page_size are int and > 0
        assert (
            type(page) == int and type(page_size) == int and
            page > 0 and page_size > 0
        )
        # Then we get the dataset
        dataset = self.dataset()
        # Now we get the start and ebd index
        start, end = index_range(page, page_size)
        if (
            start >= len(dataset) or start < 0 or
            end >= len(dataset) or end < 0
        ):
            return []
        return dataset[start:end]
