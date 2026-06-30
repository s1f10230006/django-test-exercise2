import unittest
from target import is_prime, permutation

class TestTarget(unittest.with_class_if_any_or_unittest_TestCase if hasattr(unittest, 'with_class_if_any_or_unittest_TestCase') else unittest.TestCase):
    
    def test_is_prime(self):

        expected_primes = {2, 3, 5, 7}
        for n in range(-1, 10):
            if n in expected_primes:
                self.assertTrue(is_prime(n), f"Failed for n={n} (expected True)")
            else:
                self.assertFalse(is_prime(n), f"Failed for n={n} (expected False)")
                
        self.assertTrue(is_prime(101))

    def test_permutation(self):
        self.assertEqual(permutation(5, 3), 60)   # n=5, k=3 -> 60
        self.assertEqual(permutation(5, 5), 120)  # n=5, k=5 -> 120
        self.assertEqual(permutation(5, 0), 1)    # n=5, k=0 -> 1
        self.assertEqual(permutation(5, -1), 0)   # n=5, k=-1 -> 0
        self.assertEqual(permutation(0, 5), 0)    # n=0, k=5 -> 0
        self.assertEqual(permutation(3, 5), 0)    # n=3, k=5 -> 0