# Deserialization container for expected json response - F1A only

from Excel_F1A.dto.Inputs import F1aInput
from Excel_F1A.dto.Str_Helper import *


class F1A:
    def __init__(self, ID: str, input: F1aInput, response: dict):
        wa2: str = "wa2f1ax"

        self.ID: str = ID

        # inputs
        self.boro: str = input.boro
        self.addrNo: str = input.addrNo
        self.stName: str = input.stName
        self.unit: str = input.unit

        # region Non-Work Area Fields (root)
        self.out_b10sc_toString: str = response["root"]["out_b10sc_toString"]
        self.out_bbl_toString: str = response["root"]["out_bbl_toString"]
        self.out_bid_toString: str = response["root"]["out_bid_toString"]
        self.out_bin_toString: str = response["root"]["out_bin_toString"]
        self.out_business_area_toString: str = response["root"]["out_business_area_toString"]
        self.out_dof_map_toString: str = response["root"]["out_dof_map_toString"]
        self.out_sanborn_toString: str = response["root"]["out_sanborn_toString"]
        # endregion

        # region WA1
        self.in_auxseg_switch: str = response["root"]["wa1"]["in_auxseg_switch"]
        self.in_b10sc1: str = get_in_b10sc1(response)
        self.in_b10sc2: str = get_in_b10sc2(response)
        self.in_b10sc3: str = get_in_b10sc3(response)
        self.in_bbl: str = get_in_bbl(response)
        self.in_bin: str = get_in_bin(response)
        self.in_bin_string: str = response["root"]["wa1"]["in_bin_string"]
        self.in_boro1: str = response["root"]["wa1"]["in_boro1"]
        self.in_boro2: str = response["root"]["wa1"]["in_boro2"]
        self.in_boro3: str = response["root"]["wa1"]["in_boro3"]
        self.in_browse_flag: str = response["root"]["wa1"]["in_browse_flag"]
        self.in_compass_dir: str = response["root"]["wa1"]["in_compass_dir"]
        self.in_compass_dir2: str = response["root"]["wa1"]["in_compass_dir2"]
        self.in_filler01: str = response["root"]["wa1"]["in_filler01"]
        self.in_filler03: str = response["root"]["wa1"]["in_filler03"]
        self.in_func_code: str = response["root"]["wa1"]["in_func_code"]
        self.in_hn_justification: str = response["root"]["wa1"]["in_hn_justification"]
        self.in_hn_norm_override: str = response["root"]["wa1"]["in_hn_norm_override"]
        self.in_hnd: str = response["root"]["wa1"]["in_hnd"]
        self.in_hnl: str = response["root"]["wa1"]["in_hnl"]
        self.in_hns: str = response["root"]["wa1"]["in_hns"]
        self.in_legacy_grc_flag: str = response["root"]["wa1"]["in_legacy_grc_flag"]
        self.in_long_wa2_flag: str = response["root"]["wa1"]["in_long_wa2_flag"]
        self.in_low_hnd: str = response["root"]["wa1"]["in_low_hnd"]
        self.in_low_hns: str = response["root"]["wa1"]["in_low_hns"]
        self.in_mode_switch: str = response["root"]["wa1"]["in_mode_switch"]
        self.in_node: str = response["root"]["wa1"]["in_node"]
        self.in_platform_ind: str = response["root"]["wa1"]["in_platform_ind"]
        self.in_real_street_only: str = response["root"]["wa1"]["in_real_street_only"]
        self.in_roadbed_request_switch: str = response["root"]["wa1"]["in_roadbed_request_switch"]
        self.in_snl: str = response["root"]["wa1"]["in_snl"]
        self.in_stname1: str = response["root"]["wa1"]["in_stname1"]
        self.in_stname2: str = response["root"]["wa1"]["in_stname2"]
        self.in_stname3: str = response["root"]["wa1"]["in_stname3"]
        self.in_stname_normalization: str = response["root"]["wa1"]["in_stname_normalization"]
        self.in_tpad_switch: str = response["root"]["wa1"]["in_tpad_switch"]
        self.in_unit: str = response["root"]["wa1"]["in_unit"]
        self.in_xstreet_names_flag: str = response["root"]["wa1"]["in_xstreet_names_flag"]
        self.in_zip_code: str = response["root"]["wa1"]["in_zip_code"]
        self.out_b10sc1: str = get_out_b10sc1(response)
        self.out_b10sc2: str = get_out_b10sc2(response)
        self.out_b10sc3: str = get_out_b10sc3(response)
        self.out_bbl: str = get_out_bbl(response)
        self.out_bin: str = get_out_bin(response)
        self.out_boro_name1: str = response["root"]["wa1"]["out_boro_name1"]
        self.out_error_message: str = response["root"]["wa1"]["out_error_message"]
        self.out_error_message2: str = response["root"]["wa1"]["out_error_message2"]
        self.out_filler02: str = response["root"]["wa1"]["out_filler02"]
        self.out_filler03: str = response["root"]["wa1"]["out_filler03"]
        self.out_grc: str = response["root"]["wa1"]["out_grc"]
        self.out_grc2: str = response["root"]["wa1"]["out_grc2"]
        self.out_hnd: str = response["root"]["wa1"]["out_hnd"]
        self.out_hns: str = response["root"]["wa1"]["out_hns"]
        self.out_low_hnd: str = response["root"]["wa1"]["out_low_hnd"]
        self.out_low_hns: str = response["root"]["wa1"]["out_low_hns"]
        self.out_node: str = response["root"]["wa1"]["out_node"]
        self.out_number_of_stcodes: str = response["root"]["wa1"]["out_number_of_stcodes"]
        self.out_reason_code: str = response["root"]["wa1"]["out_reason_code"]
        self.out_reason_code2: str = response["root"]["wa1"]["out_reason_code2"]
        self.out_reason_code_qualifier: str = response["root"]["wa1"]["out_reason_code_qualifier"]
        self.out_reason_code_qualifier2: str = response["root"]["wa1"]["out_reason_code_qualifier2"]
        self.out_st_attr: str = response["root"]["wa1"]["out_st_attr"]
        self.out_stname1: str = response["root"]["wa1"]["out_stname1"]
        self.out_stname2: str = response["root"]["wa1"]["out_stname2"]
        self.out_stname3: str = response["root"]["wa1"]["out_stname3"]
        self.out_unit: str = response["root"]["wa1"]["out_unit"]
        self.out_units: str = get_out_units(response)
        self.out_warning_code: str = response["root"]["wa1"]["out_warning_code"]
        self.out_warning_code2: str = response["root"]["wa1"]["out_warning_code2"]
        # endregion

        # region WA2F1AX
        self.DCP_Zoning_Map: str = response["root"]["wa2f1ax"]["DCP_Zoning_Map"]
        self.TPAD_bin_status: str = response["root"]["wa2f1ax"]["TPAD_bin_status"]
        self.TPAD_conflict_flag: str = response["root"]["wa2f1ax"]["TPAD_conflict_flag"]
        self.TPAD_new_bin: str = get_tpad_new_bin(response, wa2)
        self.TPAD_new_bin_status: str = response["root"]["wa2f1ax"]["TPAD_new_bin_status"]
        self.addr_overflow_flag: str = response["root"]["wa2f1ax"]["addr_overflow_flag"]
        self.bbl: str = get_bbl(response, wa2)
        self.bid_id: str = get_bid_id(response, wa2)
        self.bin: str = get_bin(response, wa2)
        self.business_area: str = get_business_area(response, wa2)
        self.condo_base_bbl: str = get_condo_base_bbl(response, wa2)
        self.condo_bill_bbl: str = get_condo_bill_bbl(response, wa2)
        self.condo_bill_scc: str = response["root"]["wa2f1ax"]["condo_bill_scc"]
        self.condo_flag: str = response["root"]["wa2f1ax"]["condo_flag"]
        self.condo_hi_bbl: str = get_condo_hi_bbl(response, wa2)
        self.condo_lo_bbl: str = get_condo_lo_bbl(response, wa2)
        self.condo_num: str = response["root"]["wa2f1ax"]["condo_num"]
        self.cont_parity_ind: str = response["root"]["wa2f1ax"]["cont_parity_ind"]
        self.coop_num: str = response["root"]["wa2f1ax"]["coop_num"]
        self.corner_code: str = response["root"]["wa2f1ax"]["corner_code"]
        self.dof_map: str = get_dof_map(response, wa2)
        self.filler1: str = response["root"]["wa2f1ax"]["filler1"]
        self.filler10: str = response["root"]["wa2f1ax"]["filler10"]
        self.filler11: str = response["root"]["wa2f1ax"]["filler11"]
        self.filler2: str = response["root"]["wa2f1ax"]["filler2"]
        self.filler3: str = response["root"]["wa2f1ax"]["filler3"]
        self.filler4: str = response["root"]["wa2f1ax"]["filler4"]
        self.filler5: str = response["root"]["wa2f1ax"]["filler5"]
        self.filler6: str = response["root"]["wa2f1ax"]["filler6"]
        self.filler7: str = response["root"]["wa2f1ax"]["filler7"]
        self.filler8: str = response["root"]["wa2f1ax"]["filler8"]
        self.filler9: str = response["root"]["wa2f1ax"]["filler9"]
        self.grc: str = response["root"]["wa2f1ax"]["grc"]
        self.gridkey1: str = get_gridkey1(response, wa2)
        self.interior_flag: str = response["root"]["wa2f1ax"]["interior_flag"]
        self.irreg_flag: str = response["root"]["wa2f1ax"]["irreg_flag"]
        self.latitude: str = response["root"]["wa2f1ax"]["latitude"]
        self.lohns: str = response["root"]["wa2f1ax"]["lohns"]
        self.longitude: str = response["root"]["wa2f1ax"]["longitude"]
        self.mh_ri_flag: str = response["root"]["wa2f1ax"]["mh_ri_flag"]
        self.num_of_addrs: str = response["root"]["wa2f1ax"]["num_of_addrs"]
        self.num_of_bldgs: str = response["root"]["wa2f1ax"]["num_of_bldgs"]
        self.num_of_blockfaces: str = response["root"]["wa2f1ax"]["num_of_blockfaces"]
        self.reason_code: str = response["root"]["wa2f1ax"]["reason_code"]
        self.reason_code_qualifier: str = response["root"]["wa2f1ax"]["reason_code_qualifier"]
        self.res_internal_use: str = response["root"]["wa2f1ax"]["res_internal_use"]
        self.rpad_bldg_class: str = response["root"]["wa2f1ax"]["rpad_bldg_class"]
        self.rpad_scc: str = response["root"]["wa2f1ax"]["rpad_scc"]
        self.sanborn: str = get_sanborn(response, wa2)
        self.stroll_key: str = response["root"]["wa2f1ax"]["stroll_key"]
        self.vacant_flag: str = response["root"]["wa2f1ax"]["vacant_flag"]
        self.warning_code: str = response["root"]["wa2f1ax"]["warning_code"]
        self.x_coord: str = response["root"]["wa2f1ax"]["x_coord"]
        self.y_coord: str = response["root"]["wa2f1ax"]["y_coord"]
        # endregion

        self.similar_names_list: list[str] = get_similar_names_list(response)
