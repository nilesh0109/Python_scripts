import unittest
from helpers import helpers

class TestHelpers(unittest.TestCase):

    def test_is_valid_image(self):
        valid = helpers.is_a_valid_image('https://unsplash.com/photos/3RAl7RNLMTU/download?force=true')
        invalid = helpers.is_a_valid_image('https://unsplash.com/photos/3RAl7RNLMTU')

        self.assertEqual(valid, True, "Should be True")
        self.assertEqual(invalid, False, "Should be False")
    #
    def test_get_file_name(self):
        fileName1 = helpers.get_file_name('attachment; filename="myfilename.txt"', 'test.com')
        fileName2 = helpers.get_file_name('attachment;', 'https://images.dreamlines.de/exploreraussen-130055.jpg')
        fileName3 = helpers.get_file_name('', 'https://google.com/icon.ico')
        self.assertEqual(fileName1, 'myfilename.txt', "Should be myfilename.txt")
        self.assertEqual(fileName2, 'exploreraussen-130055.jpg', "Should be exploreraussen-130055.jpg")
        self.assertEqual(fileName3, 'icon.ico', "Should be icon.ico")


if __name__ == '__main__':
    unittest.main()