from string import ascii_letters, digits
from random import choice
from data import DATA, NAME, PREP, DATE, COMP
def generate_login(name):
    """
    Generate reduced login.
    Example: name='Super Cool Man'
    login = Super_CM
    """
    if ' ' not in name: return name

    p = name.split(' ')
    first = p[0]
    red = "".join(map(lambda i: i[0].upper(), p[1:]))
    return f"{first}_{red}"



def generate_password():
    """Generate 10 symbols password by [A-z0-9]"""
    ln = 10
    symbols = ascii_letters + digits
    return "".join([choice(symbols) for _ in range(ln)])

LOGIN = 'login'
PASS = 'pass'

# Generating login and password
for r in DATA:
    r[LOGIN] = generate_login(r[NAME])
    r[PASS] = generate_password()

# generating result file
with open("scientist_password.csv", 'w', encoding='utf-8') as f:
    f.write("ScientistName,preparation,date,components,login,password\n")
    f.write(
        "\n".join(map(lambda r: f"{r[NAME]},{r[PREP]},{str(r[DATE])},{' '.join(r[COMP])},{r[LOGIN]},{r[PASS]}", DATA))
    )
