import unittest

from cryptography.hazmat.primitives.asymmetric import mlkem

import crypto_test1


class GenerateTestMlkemKeyTests(unittest.TestCase):
    """Covers RelixQ finding 01a21b4d-cb15-76a2-b370-5d76e5792ab5 (RSA -> ML-KEM-768)."""

    def test_returns_mlkem768_private_key(self):
        key = crypto_test1.generate_test_mlkem_key()
        self.assertIsInstance(key, mlkem.MLKEM768PrivateKey)

    def test_key_round_trips_encapsulation(self):
        key = crypto_test1.generate_test_mlkem_key()
        shared_secret, ciphertext = key.public_key().encapsulate()
        self.assertEqual(len(shared_secret), 32)
        self.assertEqual(key.decapsulate(ciphertext), shared_secret)


if __name__ == "__main__":
    unittest.main()
