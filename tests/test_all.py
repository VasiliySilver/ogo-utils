
from tests.test_decryption import test_decryption
from tests.test_encryption import test_encryption


def test_all():
    test_encryption()
    test_decryption()
