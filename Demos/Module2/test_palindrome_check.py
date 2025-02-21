import unittest

from Demos.Module2.palindrome_check import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_check(self):
        # s = "hello"
        # answer = is_palindrome(s)
        # print(answer)
        # self.assertFalse(answer)

        eg1 = "A man a plan a canal Panama"
        self.assertTrue(is_palindrome(eg1))

        eg2 = "a Man$na *A"
        self.assertFalse(is_palindrome(eg2))

        eg3 = " "
        self.assertTrue(is_palindrome(eg3))

        eg4 = "r"
        self.assertTrue(is_palindrome(eg4))

        eg5 = "1234321"
        self.assertTrue(is_palindrome(eg5))

        eg6 = "12t4 t21"
        self.assertTrue(is_palindrome(eg6))



if __name__ == '__main__':
    unittest.main()