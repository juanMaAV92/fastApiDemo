
import random
import string


def random_lower_string( k = 32 ) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=k ))

def random_email() -> str:
    return f"{random_lower_string(6)}@{random_lower_string(4)}.com"

def random_phone() -> str:
    return "".join(str(random.randint(1000000000, 9999999999)))

def random_identification_type() -> str:
    identification_type = [ 'CC', 'NIT', 'TI', 'PP' ]
    return random.choice( identification_type )


