import unittest
import count_characters


class TestCase1(unittest.TestCase):
    def test_count_characters(self):
        # Create a text file
        file_path = '../temp/test.txt'
        f = open(file_path, 'w')
        f.write('Hello world!\n')
        f.write('How are you?\n')
        f.write('你好吗？\n')
        f.close()
        # Validate the count of characters
        dict0 = {'好': 1, 'o': 4, 'd': 1, 'l': 3, '!': 1, 'count': 31, 'y': 1, '？': 1, 'a': 1,
                 '吗': 1, 'e': 2, '你': 1, 'H': 2, ' ': 3, 'u': 1, '\n': 3, '?': 1, 'w': 2, 'r': 2}
        dict1 = jlpy.jlfile.count_characters(file_path)
        self.assertTrue(dict0 == dict1)


if __name__ == '__main__':
    unittest.main()
