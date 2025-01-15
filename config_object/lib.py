from config import Config, ImmutableConfig

def log_config(config: Config | ImmutableConfig):
    print(f"lib.py {config=}")
