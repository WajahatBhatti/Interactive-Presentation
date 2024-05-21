# authentication/utils.py

import string
import random


def generate_random_pw(length: int = 16) -> str:
    """
    Generates a random password.

    Parameters
    ----------
    length: int
        The length of the returned password.
    Returns
    -------
    str
        The randomly generated password.
    """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))