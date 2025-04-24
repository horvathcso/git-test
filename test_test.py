import unittest
from fibonacci import fib_iterative, fib_recursive, fib_memo

# Language: python

class TestFibonacci(unittest.TestCase):
    '''Added test suite to test the Fibonacci implementations'''
    def test_fib_iterative(self):
        test_cases = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 5,
            10: 55
        }
        for n, expected in test_cases.items():
            with self.subTest(n=n):
                self.assertEqual(fib_iterative(n), expected)

    def test_fib_recursive(self):
        test_cases = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 5,
            10: 55
        }
        for n, expected in test_cases.items():
            with self.subTest(n=n):
                self.assertEqual(fib_recursive(n), expected)

    def test_fib_memo(self):
        test_cases = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 5,
            10: 55,
            15: 610
        }
        for n, expected in test_cases.items():
            with self.subTest(n=n):
                self.assertEqual(fib_memo(n), expected)

    def test_negative_input(self):
        for func in (fib_iterative, fib_recursive, fib_memo):
            with self.subTest(func=func.__name__):
                with self.assertRaises(ValueError):
                    func(-1)

if __name__ == "__main__":
    unittest.main()