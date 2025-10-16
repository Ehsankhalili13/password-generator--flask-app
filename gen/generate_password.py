from string import *
from random import *

def generate_password(length_password):
    password = ascii_letters + digits + "!@#$%&*"
    password_list = []
    for passChar in range(length_password):
        pass_random = choice(password)
        password_list.append(pass_random)
    final_pasword = "".join(password_list)
    return final_pasword
