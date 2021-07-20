import unittest

from serviceApp.resource_loader import ResourceLoader


class TestResourceLoader(unittest.TestCase):

    def setUp(self):
        name_file1 = "test_file.txt"
        name_file2 = "test_empty_file.txt"
        name_file3 = "test_some_file.txt"
        self.test_rl_file = ResourceLoader(name_file1)
        self.test_rl_empty_file = ResourceLoader(name_file2)
        self.test_rl_some_file = ResourceLoader(name_file3)

    def test_load_from_file(self):
        self.assertEqual(7, len(self.test_rl_file.load_from_file()))

    def test_load_from_empty_file(self):
        self.assertEqual(0, len(self.test_rl_empty_file.load_from_file()))

    def test_load_some_file(self):
        self.assertRaises(TypeError, self.test_rl_some_file.load_from_file())


if __name__ == "__main__":
    unittest.main()
