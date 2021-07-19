import unittest

from serviceApp.resource_loader import ResourceLoader


class TestResourceLoader(unittest.TestCase):

    def setUp(self):
        self.test_rl = ResourceLoader()

    def test_load_from_file(self):
        name_file = "test_file.txt"
        self.assertEqual(7, len(self.test_rl.load_from_file(name_file)))


if __name__ == "__main__":
    unittest.main()