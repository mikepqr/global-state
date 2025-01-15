from dataclasses import dataclass

@dataclass
class Config:
    random_number: float | None = None

"""
Instances of this class are immutable, but you must know all the attributes at
instantiation time, no filling in the details later.
"""
@dataclass(frozen=True)
class ImmutableConfig:
    random_number: float
