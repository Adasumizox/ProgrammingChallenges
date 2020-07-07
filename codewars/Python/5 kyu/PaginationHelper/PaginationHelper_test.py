from PaginationHelper import PaginationHelper
import unittest

class TestPaginationHelper(unittest.TestCase):
    
    def test(self):
        collection = range(1,25)
        helper = PaginationHelper(collection, 10)
        self.assertEqual(helper.page_count(), 3, 'page_count is returning incorrect value.')
        self.assertEqual(helper.page_item_count(1), 10, 'page_item_count is returning incorrect value.')
        self.assertEqual(helper.page_item_count(2), 4, 'page_item_count is returning incorrect value')
        self.assertEqual(helper.page_item_count(3), -1, 'page_item_count is returning incorrect value')
        self.assertEqual(helper.page_index(0), 0, 'page_index returned incorrect value')
        self.assertEqual(helper.page_index(23), 2, 'page_index returned incorrect value')
        self.assertEqual(helper.page_index(24), -1, 'page_index returned incorrect value when provided a item_index argument that was out of range')
        self.assertEqual(helper.page_index(40), -1, 'page_index returned incorrect value when provided a item_index argument that was out of range')
        self.assertEqual(helper.page_index(3), 0, 'page_index returned incorrect value')
        self.assertEqual(helper.page_index(-1), -1, 'page_index returned incorrect value when provided a itemIndex argument that was out of range. pageIndex(-1) should return -1')
        self.assertEqual(helper.page_index(-23), -1, 'page_index returned incorrect value when provided a item_index argument that was out of range. pageIndex(-23) shoudl return -1')
        self.assertEqual(helper.page_index(-15), -1, 'page_index returned incorrect value when provided a item_index argument that was out of range.')
        self.assertEqual(helper.item_count(), 24, 'item_count returned incorrect value')
        helper = PaginationHelper([], 10)
        self.assertEqual(helper.page_index(0), -1, 'pageIndex(0) called when there was an empty collection')

if __name__ == '__main__':
    unittest.main()