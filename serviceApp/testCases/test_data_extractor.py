import unittest

from serviceApp.data_extractor import DataExtractor


class TestDataExtractor(unittest.TestCase):

    def setUp(self):
        self.test_d_e = DataExtractor()

    def test_data_extractor(self):
        self.list_from_resource = ["# Namespaces are one honking great idea -- let's do more of those!"]
        self.assertEqual(61, len(self.test_d_e.extract_special_char(self.list_from_resource)[0]))

        self.list_from_resource = ["# Unless explicitly silenced."]
        self.assertEqual(26, len(self.test_d_e.extract_special_char(self.list_from_resource)[0]))

        self.list_from_resource = ["# If the implementation is easy to explain, it may be a good idea."]
        self.assertEqual(62, len(self.test_d_e.extract_special_char(self.list_from_resource)[0]))
