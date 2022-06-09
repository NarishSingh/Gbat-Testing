from dataclasses import dataclass


@dataclass
class f1a_input:
    boro: str  # may be boro code or zip code
    addrNo: str  # may be in hnd or hnd format
    stName: str  # will also hold freeform strings
    # optionals
    using_tpad: str = "y"
    browse_flag: str = "p"  # p, f, r, black
    unit: str = ""
