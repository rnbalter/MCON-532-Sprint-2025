import unittest

from Demos.Module2.palindrome_check import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_check(self):
        s = "hello"
        answer = is_palindrome(s)
        print(answer)

        self.assertFalse(answer)


        eg1 = "A man a plan a canal Panama"
        self.assertTrue(is_palindrome(eg1))

        eg2 = "a Man$na *A"
        self.assertFalse(is_palindrome(eg2))






if __name__ == '__main__':
    unittest.main()