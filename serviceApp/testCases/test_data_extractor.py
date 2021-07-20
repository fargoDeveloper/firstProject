import unittest

from serviceApp.data_extractor import DataExtractor


class TestDataExtractor(unittest.TestCase):

    def setUp(self):
        self.from_resource1 = ["# Namespaces are one honking great idea -- let's do more of those!"]
        self.line_from_resource2 = ["# Unless explicitly silenced."]
        self.line_from_resource3 = ["# If the implementation is easy to explain, it may be a good idea."]
        self.test_d_e1 = DataExtractor(self.from_resource1)
        self.test_d_e2 = DataExtractor(self.line_from_resource2)
        self.test_d_e3 = DataExtractor(self.line_from_resource3)

    def test_data_extractor(self):
        self.assertEqual(61, len(self.test_d_e1.extract_special_char()[0]))
        self.assertEqual(26, len(self.test_d_e2.extract_special_char()[0]))
        self.assertEqual(62, len(self.test_d_e3.extract_special_char()[0]))


if __name__ == "__main__":
    unittest.main()
