import globalstate


def log_from_lib():
    print(f"lib.py {globalstate.random_number=}")
    print(f"lib.py {x=}")


x = globalstate.random_number
