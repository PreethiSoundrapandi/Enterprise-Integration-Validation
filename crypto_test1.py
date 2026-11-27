
import hashlib
from cryptography.hazmat.primitives.asymmetric import mlkem


def generate_test_mlkem_key():
    """Generate an ML-KEM-768 key for QA testing only."""
    # RelixQ finding 01a21b4d-cb15-76a2-b370-5d76e5792ab5: RSA-2048 is
    # quantum-vulnerable; key generation moved to ML-KEM-768 (FIPS 203).
    private_key = mlkem.MLKEM768PrivateKey.generate()
    print("ML-KEM-768 key generation: PASS")
    print("Private key generated in memory; not saved.")
    return private_key


def test_sha1_hashing():
    """Exercise SHA-1 hashing for security scanner testing."""
    sample = b"RelixQ public repository QA test data"
    digest = hashlib.sha1(sample).hexdigest()

    print("SHA-1 test digest:", digest)
    print("SHA-1 hashing test: Pass")


if __name__ == "__main__":
    generate_test_mlkem_key()
    test_sha1_hashing()
