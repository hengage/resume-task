"""
Simple Python program to print my name.
"""

def print_name(first_name, last_name, middle_name=''):
    """
    I pass in 2 positional parameters, 'first_name' and 'last_name'
    and a dafualt parameter(optional) for middle name.
    """
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

myName = print_name(first_name='henry', last_name='chizoba')

print(myName.title())


