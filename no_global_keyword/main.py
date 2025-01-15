"""
$ python main.py
Generating random number
main.py globalstate.random_number=0.5461971288915216
lib.py globalstate.random_number=0.5461971288915216
lib.py x=0.5461971288915216
main.py globalstate.random_number=42
lib.py globalstate.random_number=42
lib.py x=0.5461971288915216
"""

import globalstate
import lib


def log_from_main():
    print(f"main.py {globalstate.random_number=}")


# Note:
# - globalstate.f() is called exactly once even though main and lib both import
#   it and f() is called in the top level of globalstate
# - main.globalstate.random_number, lib.globalstate.random_number and
#   lib.globalstate.x all have the same value
log_from_main()
lib.log_from_lib()

# Now let's mutate globalstate.random_number from here to prove it is mutable
# global state (with no global keyword)
globalstate.random_number = 42


# Note:
# - both views of the random_number variable are the same. This is shared
#   mutable state.
# - lib.x has not changed for the same reason "x=1, y=x, x=2" does not set y to
#   2.
log_from_main()
lib.log_from_lib()
