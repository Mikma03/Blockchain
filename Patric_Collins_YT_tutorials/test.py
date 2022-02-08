# check if we are into virtual env

# https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv#:~:text=The%20most%20reliable%20way%20to,they%20are%20unequal%2C%20you%20are.




# import sys

# def get_base_prefix_compat():
#     """Get base/real prefix, or sys.prefix if there is none."""
#     return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

# def in_virtualenv():
#     return get_base_prefix_compat() != sys.prefix



# sys.prefix == sys.base_prefix

import sys


def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if is_venv():
    print('inside virtualenv or venv')
else:
    print('outside virtualenv or venv')