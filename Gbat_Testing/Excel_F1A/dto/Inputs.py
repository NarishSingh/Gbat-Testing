# These are "structs"/data classes meant to hold expected input data
# If a batch job queries any of the user's own inputs, Desktop GBAT will copy them into the output table
# These classes aim to standardize what inputs parameters are permitted for each function type
# Optional parameters are given default values

from dataclasses import dataclass


@dataclass
class F1aInput:
    boro: str
    addrNo: str  # may be in hnd or hnd format
    stName: str  # may also be freeform (address no + st name) strings
    # optionals
    zip: str = ""
    using_tpad: str = "y"
    browse_flag: str = "p"  # p, f, r, blank
    unit: str = ""


@dataclass
class F1bInput:
    pass


@dataclass
class F1eInput:
    pass


@dataclass
class FapInput:
    pass


# todo add more
