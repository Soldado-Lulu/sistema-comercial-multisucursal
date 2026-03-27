import random
import string


def generate_company_code(length: int = 8) -> str:
    """
    Genera un código simple para identificar la empresa.
    Se usará para que empleados se registren con ese código.
    """
    chars = string.ascii_uppercase + string.digits
    return "".join(random.choices(chars, k=length))
