"""
$ python main.py
lib.py config=Config(random_number=None)
lib.py config=Config(random_number=42)
lib.py config=ImmutableConfig(random_number=0.6302451416027498)
Failed to mutate ImmutableConfig, i.e. the system works!
lib.py config=ImmutableConfig(random_number=3.14)
"""

from dataclasses import FrozenInstanceError, replace
import random

from config import Config, ImmutableConfig

import lib

c = Config()
lib.log_config(c)
# Attaching newly learned information to config object, and proving that
# information propagates into a module that has a reference to config.
c.random_number = 42
# Note we have to pass it to any function that needs access to it.
lib.log_config(c)


# Note the attributes must all be known at instantiation for a frozen dataclass.
ic = ImmutableConfig(random.random())
lib.log_config(ic)
try:
    # Your type checker should complain about this line.
    ic.random_number = 42
except FrozenInstanceError:
    print("Failed to mutate ImmutableConfig, i.e. the system works!")

# There are libraries that make it possible to explicitly and temporarily
# unfreeze frozen dataclass-like objects (e.g. attrs, pydantic) and mutate them
# inplace. But we can just create a new instance. This is fine because our API
# requires the config instance to be passed to a function on invokation. It is
# not a global object we need to mutate.
ic = replace(ic, random_number=3.14)
lib.log_config(ic)
