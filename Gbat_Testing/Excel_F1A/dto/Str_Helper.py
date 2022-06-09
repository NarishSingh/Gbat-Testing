# Many return fields in json response come back as internal dictionaries
# This class aims to "flatten" them into one string, which is how desktop gbat processes them before persistence

# region WA1
def get_in_bbl(response: dict) -> str:
    bbl: dict = response["root"]["wa1"]["in_bbl"]
    return f"{bbl['boro']}{bbl['block']}{bbl['lot']}"


def get_out_bbl(response: dict) -> str:
    bbl: dict = response["root"]["wa1"]["out_bbl"]
    return f"{bbl['boro']}{bbl['block']}{bbl['lot']}"


def get_in_bin(response: dict) -> str:
    bin_dict: dict = response["root"]["wa1"]["in_bin"]
    return f"{bin_dict['boro']}{bin_dict['binnum']}"


def get_out_bin(response: dict) -> str:
    bin_dict: dict = response["root"]["wa1"]["out_bin"]
    return f"{bin_dict['boro']}{bin_dict['binnum']}"


def get_in_b10sc1(response: dict) -> str:
    b10: dict = response["root"]["wa1"]["in_b10sc1"]
    return f"{b10['boro']}{b10['sc5']}{b10['lgc']}{b10['spv']}"


def get_in_b10sc2(response: dict) -> str:
    b10: dict = response["root"]["wa1"]["in_b10sc2"]
    return f"{b10['boro']}{b10['sc5']}{b10['lgc']}{b10['spv']}"


def get_in_b10sc3(response: dict) -> str:
    b10: dict = response["root"]["wa1"]["in_b10sc3"]
    return f"{b10['boro']}{b10['sc5']}{b10['lgc']}{b10['spv']}"


def get_out_b10sc1(response: dict) -> str:
    b10: dict = response["root"]["wa1"]["out_b10sc1"]
    return f"{b10['boro']}{b10['sc5']}{b10['lgc']}{b10['spv']}"


def get_out_b10sc2(response: dict) -> str:
    b10: dict = response["root"]["wa1"]["out_b10sc2"]
    return f"{b10['boro']}{b10['sc5']}{b10['lgc']}{b10['spv']}"


def get_out_b10sc3(response: dict) -> str:
    b10: dict = response["root"]["wa1"]["out_b10sc3"]
    return f"{b10['boro']}{b10['sc5']}{b10['lgc']}{b10['spv']}"


def get_out_units(response: dict) -> str:
    unt: dict = response["root"]["wa1"]["out_units"]
    return f"{unt['unit_type']}{unt['unit_identifier']}"


def get_similar_names_list(response: dict) -> list[str]:
    """
    Process the similar names list for an error response
    :param response: dictionary with the deserialized response from geo
    :return: list of strings with the similar name and b7sc
    """
    names: list[str] = response["root"]["wa1"]["out_stname_list"]
    b7scs: list[str] = []

    for b7 in response["root"]["wa1"]["out_b7sc_list"]:
        b7scs.append(f"{b7['boro']}{b7['sc5']}{b7['lgc']}")

    sim_names: list[str] = []

    for i, name in enumerate(names):
        sim_names.append(name)
        sim_names.append(b7scs[i])  # name and b7sc list are guaranteed to be the same length

    return sim_names


# endregion

# Note: rest of the funcs need to have their wa2 name specified to properly locate the json dict from response
def get_bbl(response: dict, wa2: str) -> str:
    bbl: dict = response["root"][wa2]["bbl"]
    return f"{bbl['boro']}{bbl['block']}{bbl['lot']}"


def get_tpad_new_bin(response: dict, wa2: str) -> str:
    new_bin: dict = response["root"][wa2]["TPAD_new_bin"]
    return f"{new_bin['boro']}{new_bin['binnum']}"


def get_bid_id(response: dict, wa2: str) -> str:
    bid: dict = response["root"][wa2]["bid_id"]
    return f"{bid['boro']}{bid['sc5']}"


def get_bin(response: dict, wa2: str) -> str:
    bin_dict: dict = response["root"][wa2]["bin"]
    return f"{bin_dict['boro']}{bin_dict['binnum']}"


def get_business_area(response: dict, wa2: str) -> str:
    ba: dict = response["root"][wa2]["business_area"]
    return f"{ba['boro']}{ba['district_number']}"


def get_condo_base_bbl(response: dict, wa2: str) -> str:
    bbl: dict = response["root"][wa2]["condo_base_bbl"]
    return f"{bbl['boro']}{bbl['block']}{bbl['lot']}"


def get_condo_bill_bbl(response: dict, wa2: str) -> str:
    bbl: dict = response["root"][wa2]["condo_bill_bbl"]
    return f"{bbl['boro']}{bbl['block']}{bbl['lot']}"


def get_condo_hi_bbl(response: dict, wa2: str) -> str:
    bbl: dict = response["root"][wa2]["condo_hi_bbl"]
    return f"{bbl['boro']}{bbl['block']}{bbl['lot']}"


def get_condo_lo_bbl(response: dict, wa2: str) -> str:
    bbl: dict = response["root"][wa2]["condo_lo_bbl"]
    return f"{bbl['boro']}{bbl['block']}{bbl['lot']}"


def get_dof_map(response: dict, wa2: str) -> str:
    dof: dict = response["root"][wa2]["dof_map"]
    return f"{dof['boro']}{dof['section_volume']}{dof['page']}"


def get_gridkey1(response: dict, wa2: str) -> str:
    gk: dict = response["root"][wa2]["gridkey1"]
    gk_b5sc: str = f"{gk['b5sc']['boro']}{gk['b5sc']['sc5']}"
    return f"{gk['record_type']}{gk_b5sc}{gk['parity']}{gk['hi_hns']}"


def get_sanborn(response: dict, wa2: str) -> str:
    sb: dict = response["root"][wa2]["sanborn"]
    return f"{sb['boro']}{sb['page']}{sb['page_suffix']}{sb['volume']}{sb['volume_suffix']}"
