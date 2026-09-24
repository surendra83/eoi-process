# services/life_di_group_service.py
from repositories.life_di_group_repository import LifeDIGroupRepository
from core.logger import app_logger
from utility.sbm_format import format_date, date_formate_in_yyyy_mm_dd, number_percentage_format

class LifeDIGroupService:
    def __init__(self, db):
        self.db = db

    def get_life_di_group_serv(self, group_id: str):     
        data = LifeDIGroupRepository.get_by_group_repo(self.db, group_id)
        if not data:
             app_logger.warning(f"No life DI group data found for group_id: {group_id}")
             return {}
        
        subgroup_data = LifeDIGroupRepository.get_subgroup_repo(self.db, data.get("TS_ID"))
        if not subgroup_data:
             app_logger.warning(f"No subgroup data found for ts_id: {data.get('TS_ID')}")
             subgroup_data=[]

        app_logger.info(f"Getting eligibility data for ts_id: {data.get('TS_ID')}")
        eligibility_data = LifeDIGroupRepository.get_eligibility_repo(self.db, data.get("TS_ID"))
        app_logger.info(f"eligibility data for ts_id: {data.get('TS_ID')}")
        if not eligibility_data:
             app_logger.warning(f"No eligibility data found for ts_id: {data.get('TS_ID')}")
             eligibility_data =[]

        sold_class_benefits_rates_information = LifeDIGroupRepository.get_sold_class_benefits_rates_information_repo(self.db, data.get("TS_ID"))
        if not sold_class_benefits_rates_information:
             app_logger.warning(f"No sold class benefits rates information found for ts_id: {data.get('TS_ID')}")
             sold_class_benefits_rates_information =[]

        billing_enrollment_info = LifeDIGroupRepository.get_billing_enrollment_info_repo(self.db, data.get("TS_ID"))
        if not billing_enrollment_info:
             app_logger.warning(f"No billing enrollment info found for ts_id: {data.get('TS_ID')}")
             billing_enrollment_info =[]
      

        return {
             "group_information": self._group_info(data),
             "contact_information": self._contact_information(subgroup_data),
             "eligibility": self._get_eligibility(eligibility_data),
             "product_information": self._product_information(data,billing_enrollment_info, sold_class_benefits_rates_information)
        }

    def _group_info(self, data):
        return {
             "group_name": data.get("TS_GROUP_NAME"),
             "group_policy_number": data.get("TS_GROUP_POLICY_NUMBER"),
             "group_effective_date": format_date(data.get("TS_GROUP_EFFECTIVE_DATE")),
             "group_termination_date": format_date(data.get("TS_GROUP_TERM_DATE")),
             "situs_state":self._get_label_value(data.get("TS_SITUS_STATE")),
             "plan_anniversary_date": data.get("TS_PLAN_ANNIV_DATE") or '',
             "underwriting_company": self._get_label_value(data.get("TS_UNDERWRITING_COMPANY")),
             "products_on_uhc":self._get_value_list(data.get("TS_PRODUCTS_ON_UHC")),
             "uhc_policy_number": data.get("TS_UHC_POLICY_NUMBER"),
             "comments_general_info_gi": data.get("TS_COMMENTS_GI") or ''
        }

    def _product_information(self, data, billing_enrollment_info, sold_class_benefits_rates_information):
        result = {}
        if self._get_label_value(data.get("TS_BASIC_LIFE")) =='Yes':
            result["basic_life"] = self._basic_life(data, sold_class_benefits_rates_information)
        if self._get_label_value(data.get("TS_DEP_LIFE")) =='Yes':
            result["basic_dependent_life"] = self._basic_dependent_life(data, sold_class_benefits_rates_information)
        if self._get_label_value(data.get("TS_SUPP_LIFE")) =='Yes':
            result["supplemental_life"] = self._supplemental_life(data, sold_class_benefits_rates_information)
        if self._get_label_value(data.get("TS_SUPP_DEP_LIFE")) =='Yes':
            result["supplemental_dependent_life"] = self._supplemental_dependent_life(data, sold_class_benefits_rates_information)
        if self._get_label_value(data.get("TS_STD")) =='Yes' or self._get_label_value(data.get("TS_STD")) =='Termed':
            result["short_term_disability_std"] = self._short_term_disability_std(data,sold_class_benefits_rates_information)
        if self._get_label_value(data.get("TS_LTD")) =='Yes' or self._get_label_value(data.get("TS_LTD")) =='Termed':
            result["long_term_disability_ltd"] = self._long_term_disability_ltd(data, sold_class_benefits_rates_information)

        result["billing_enrollment_info"] = self._billing_enrollment_info(billing_enrollment_info)
        return result


    def _contact_information(self, subgroup_data):
        contact_information = []
        for index, item in enumerate(subgroup_data):
            contact_information.append({
                    "division_information": self._division_information(item),
                    "eoi_primary_contact": self._eoi_primary_contact(item),
                    "eoi_secondary_contact": self._eoi_secondary_contact(item),
                    "comments_subgroup": item.get("TS_COMMENTS_SUBGROUP") or ''
                })

        return contact_information
    
    def _division_information(self, data):
        return  {
                 "division_number": data.get("TS_SUBGROUP_NUMBER"),
                 "division_name": data.get("TS_SUBGROUP_NAME"),
                 "effective_date": format_date(data.get("TS_EFFECTIVE_DATE")),
                 "termination_date": format_date(data.get("TS_TERMINATION_DATE"))
            }
    
    def _eoi_primary_contact(self, subgroup_data):
        contact_type = self._get_value_list(subgroup_data.get("TS_TYPE_CON1"))
        contact_type2= self._get_value_list(subgroup_data.get("TS_TYPE_CON2"))
        if "EOI" in contact_type.split(",") or ("EOI" in contact_type2.split(",") and self._get_value_list(subgroup_data.get("TS_CONTACT_2_ADDRESS"))=='Same as Above'):
            return {
                    "contact_type": contact_type,
                    "contact_name": subgroup_data.get("TS_NAME_CON1") or '',
                    "contact_title": subgroup_data.get("TS_TITLE_CON1") or '',
                    "contact_email": subgroup_data.get("TS_EMAIL_CON1") or '',
                    "contact_company_name": subgroup_data.get("TS_COMPANY_NAME_CON1") or '',
                    "contact_address": subgroup_data.get("TS_ADDRESS_CON1") or '',
                    "contact_city_state_zip": subgroup_data.get("TS_CSZ_CON1") or '',
                    "contact_phone": subgroup_data.get("TS_PHONE_CON1") or '',
                    "contact_fax": subgroup_data.get("TS_FAX_CON1") or ''
                } 
        return None

    def _eoi_secondary_contact(self, subgroup_data):
        contact_type2 = self._get_value_list(subgroup_data.get("TS_TYPE_CON2"))
        if "EOI" in contact_type2.split(","):
            return {
                     "contact_type": contact_type2,
                     "contact_name": subgroup_data.get("TS_NAME_CON2") or '',
                     "contact_title": subgroup_data.get("TS_TITLE_CON2") or '',
                     "contact_email": subgroup_data.get("TS_EMAIL_CON2") or '',
                     "contact2_company_name": subgroup_data.get("TS_COMPANY_NAME_CON2") or '',
                     "contact2_address": self._get_value_list(subgroup_data.get("TS_CONTACT_2_ADDRESS")),
                     "contact_address": subgroup_data.get("TS_ADDRESS_CON2") or '',
                     "contact_city_state_zip": subgroup_data.get("TS_CSZ_CON2") or '',
                     "contact_phone": subgroup_data.get("TS_PHONE_CON2") or '',
                     "contact_fax": subgroup_data.get("TS_FAX_CON2") or ''
                }  
        return None

    def _basic_life(self, data, sold_class_benefits_rates_information):
        # selected_product_types = ["Basic Life", "Basic Dep Life", "Supp Life", "Supp Dep Life", "STD", "LTD","STD Buy-up","LTD Buy-up"]
        return {
                 "effective_date_basic_life": format_date(data.get("TS_EFFFECTIVE_DATE_BL")),
                 "termination_date_basic_life": format_date(data.get("TS_TERMINATION_DATE_BL")),
                 "guarantee_issue_amount_basic_life": data.get("TS_GUAR_ISSUE_AMT_BL") or '',
                 "define_earnings_basic_life": self._get_label_value(data.get("TS_DEFINE_EARNINGS_BL")),
                 "rounding_basic_life": self._get_label_value(data.get("TS_ROUNDING_BL")),
                 "open_enrollment": {
                    "open_enrollment_offered_basic_life": self._get_label_value(data.get("TS_OPEN_ENROLLMENT_OFFERED_BL")),
                    "open_enrollment_term_date_basic_life": format_date(data.get("TS_OE_TERM_DATE_BL")),
                    "guarantee_issue_onetime_open_enrollment_basic_life": data.get("TS_GUAR_ISSUE_ONETIME_OE_BL") or '',
                    "guarantee_issue_annual_open_enrollment_basic_life": data.get("TS_GUAR_ISSUE_ANNUAL_OENROLL") or ''
                 },
                 "underwriting": {
                    # Evidence of Insurability
                    "na_takeover_for_ee_basic_life": self._get_label_value(data.get("TS_NA_TAKEOVER_FOR_EE_BL")),
                    "eoi_req_newly_elig_ee_basic_life": self._get_label_value(data.get("TS_EOI_REQ_NEWLY_ELIG_EE_BL")),
                    "med_uw_new_ee_over_gi_basic_life": self._get_label_value(data.get("TS_MED_UW_NEW_EE_OVER_GI_BL")),
                    "med_uw_salary_over_gi_basic_life": self._get_label_value(data.get("TS_MED_UW_SALARY_OVER_GI_BL")),
                    "for_contrib_plans_medical": self._get_label_value(data.get("TS_FOR_CONTRIB_PLANS__MEDICAL")),
                    "other_basic_life": self._get_label_value(data.get("TS_OTHER_BL")),
                    # Open Enrollment Evidence of Insurability
                    "eoi_req_if_elect_cov_oe_basic_life": self._get_label_value(data.get("TS_EOI_REQ_IF_ELECT_COV_OE_BL")),
                    "current_ee_no_bl_basic_life": self._get_label_value(data.get("TS_CURRENT_EE_NO_BL_BL")),
                    "current_ee_increase_amt_basic_life": self._get_label_value(data.get("TS_CURRENT_EE_INCREASE_AMT_BL"))
                 },
                 "benefit_and_rate_information": self._sold_class_benefits_rates_information(sold_class_benefits_rates_information, ["Basic Life"]),
                 "comments_basic_life_bl": data.get("TS_COMMENTS_BL") or ''
            }
            
    def _basic_dependent_life(self, data, sold_class_benefits_rates_information):
        # selected_product_types = ["Basic Life", "Basic Dep Life", "Supp Life", "Supp Dep Life", "STD", "LTD","STD Buy-up","LTD Buy-up"]
        return {
            "effective_date_dependent_life": format_date(data.get("TS_EFFECTIVE_DATE_DL")),
            "termination_date_dependent_life": format_date(data.get("TS_TERMINATION_DATE_DL")),
            "domestic_partners_covered_dependent_life": self._get_label_value(data.get("TS_DOM_PARTNER_COV_DL")),
            "spouse_age_reductions_apply_dependent_life": self._get_label_value(data.get("TS_SPOUSE_AGE_REDUC_DL")),
            "underwriting":{
                 "is_eoi_required_if_electing_coverage_open_enrollment_dependent_life": self._get_label_value(data.get("TS_EOI_REQ_IF_ELECT_COV_OE_DL")),
                 "current_employee_no_bl_dependent_life": self._get_label_value(data.get("TS_CURRENT_EE_NO_BL_DL")),
                 "current_employee_increase_amount_dependent_life": self._get_label_value(data.get("TS_CURRENT_EE_INCREASE_AMT_DL"))
            },
            "benefit_and_rate_information": self._sold_class_benefits_rates_information(sold_class_benefits_rates_information, ["Basic Dep Life"]),
            "comments_dependent_life_dl": data.get("TS_COMMENTS_DL") or ''
        }
        
    def _supplemental_dependent_life(self, data, sold_class_benefits_rates_information):
        # selected_product_types = ["Basic Life", "Basic Dep Life", "Supp Life", "Supp Dep Life", "STD", "LTD","STD Buy-up","LTD Buy-up"]
        return {
            "effective_date_sdl": format_date(data.get("TS_EFFECTIVE_DATE_SDL")),
            "termination_date_sdl": format_date(data.get("TS_TERMINATION_DATE_SDL")),
            "virgin_line_coverage_sdl": self._get_label_value(data.get("TS_VIRGIN_LINE_COVERAGE_SDL")),
            "spouse_guaranteed_issue_amount_sdl": data.get("TS_SP_GUAR_ISSUE_AMT_SDL") or '',
            "spouse_age_reduction_sdl": self._get_label_value(data.get("TS_SPOUSE_AGE_REDUC_SDL")),
            "open_enrollment":{
                 "open_enroll_offered_sdl": self._get_label_value(data.get("TS_OPEN_ENROLL_OFFERED_SDL")),
                 "open_enroll_initial_sdl": self._get_label_value(data.get("TS_OPEN_ENROLL_INITIAL_SDL")),
                 "gi_restriction_sdl": data.get("TS_GI_RESTRICTION_SDL") or '',
                 "open_enroll_anniv_sdl": self._get_label_value(data.get("TS_OPEN_ENROLL_ANNIV_SDL")),
                 "oe_term_date_sdl": format_date(data.get("TS_OE_TERM_DATE_SDL")) 
                 },
            "underwriting":{
                 "must_employee_covered_for_sdl": self._get_label_value(data.get("TS_MUST_EE_COVERED_FOR_SDL")),
                 "is_supp_spouse_dl_amt_limited": self._get_label_value(data.get("TS_IS_SUPP_SPOUSE_DL_AMT_LIM")),
                 "participation_requirement_sdl": self._get_label_value(data.get("TS_PART_REQ_MET_SDL")),
                 "current_employee_no_bl_sdl": self._get_label_value(data.get("TS_CURRENT_EE_NO_BL_SDL")),
                 "current_employee_increase_am-ount_sd": self._get_label_value(data.get("TS_CURRENT_EE_INCREASE_AMT_SD")),
                 "na_takeover_for_employee_sdls": self._get_label_value(data.get("TS_NA_TAKEOVER_FOR_EE_SDLS")),
                 "eoi_new_hire_over_guaranteed_issue_sdls": self._get_label_value(data.get("TS_EOI_NEW_HIRE_OVER_GI_SDLS")),
                 "eoi_other_eoi_rules_sdls": data.get("TS_OTHER_EOI_SDLS") or '',
                 "eoi_for_increase_coverage_amount_sdls": self._get_label_value(data.get("TS_EOI_FOR_INCR_COV_SDLS")),
                 "eoi_one_benefit_level_sdls": self._get_label_value(data.get("TS_EOI_FOR_1_BENE_LVL_SDLS")),
                 "eoi_coverage_within_31_days_sdls": self._get_label_value(data.get("TS_EOI_COV_31_DAYS_SDLS")),
                 "eoi_required_for_newly_eligible_employees_sdls":self._get_label_value(data.get("TS_EOI_REQ_NEWLY_ELIG_EE_SDLS")),
                 "eoi_required_if_elected_coverage_open_enrollment_sdls": self._get_label_value(data.get("TS_EOI_REQ_IF_ELECT_COV_OESDL")),
                 "one_benefit_level_equals_sdls": data.get("TS_1_BENE_LEVEL_EQUALS_SDLS") or ''
            },
            "benefit_and_rate_information": self._sold_class_benefits_rates_information(sold_class_benefits_rates_information, ["Supp Dep Life"]),
            "comments_sdl": data.get("TS_COMMENTS_SDL") or ''
        }

    def _supplemental_life(self, data, sold_class_benefits_rates_information):
        # selected_product_types = ["Basic Life", "Basic Dep Life", "Supp Life", "Supp Dep Life", "STD", "LTD","STD Buy-up","LTD Buy-up"]
        return {
            "effective_date_sl": format_date(data.get("TS_EFFECTIVE_DATE_SL")),
            "termination_date_sl": format_date(data.get("TS_TERMINATION_DATE_SL")),
            "virgin_line_coverage_sl":self._get_label_value(data.get("TS_VIRGIN_LINE_COVERAGE_SL")),
            "guaranteed_issue_amount_sl": data.get("TS_GUAR_ISSUE_AMT_SL") or '',
            "reduce_sch_sl": self._get_label_value(data.get("TS_REDUCE_SCH_SL")),
            "definition_of_earnings_sl":self._get_label_value(data.get("TS_DEFINE_EARNINGS_SL")),
            "rounding_sl": self._get_label_value(data.get("TS_ROUNDING_SL")),
            "expected_reduce_sch_sl": data.get("TS_EXP_REDUCE_SCH_SL") or '',
            "open_enrollment": {
                    "open_enrollment_offered": self._get_label_value(data.get("TS_OPEN_ENROLLMENT_OFFERED_SL")),
                    "open_enrollment_initial": self._get_label_value(data.get("TS_OPEN_ENROLL_INITIAL_SL")),
                    "gi_restriction": data.get("TS_GI_RESTRICTION_SL") or '',
                    "open_enrollment_subsequent_anniversaries": self._get_label_value(data.get("TS_OPEN_ENROLL_ANNIV_SL")),
                    "open_enrollment_termination_date": format_date(data.get("TS_OE_TERM_DATE_SL"))
            },
            "underwriting": {
                    "participation_requirement_met_sl": self._get_label_value(data.get("TS_PART_REQ_MET_SL")),
                    # evidence_of_insurability
                    "na_takeover_for_ee_sl": self._get_label_value(data.get("TS_NA_TAKEOVER_FOR_EE_SL")),
                    "eoi_req_newly_elig_ee_sl": self._get_label_value(data.get("TS_EOI_REQ_NEWLY_ELIG_EE_SL")),
                    "eoi_new_hire_over_gi_sl": self._get_label_value(data.get("TS_EOI_NEW_HIRE_OVER_GI_SL")),
                    "eoi_cov_31_days_sl": self._get_label_value(data.get("TS_EOI_COV_31_DAYS_SL")),
                    "eoi_for_incr_cov_sl": self._get_label_value(data.get("TS_EOI_FOR_INCR_COV_SL")),
                    "eoi_for_1_bene_lvl_sl": self._get_label_value(data.get("TS_EOI_FOR_1_BENE_LVL_SL")),
                    "one_benefit_level_sl": data.get("TS_ONE_BENEFIT_LEVEL_SL") or '',
                    "other_eoi_sl": data.get("TS_OTHER_EOI_SL") or '',
                    # Salary Based Plan
                    "eoi_salary_over_gi_sl": self._get_label_value(data.get("TS_EOI_SALARY_OVER_GI_SL")),
                    "amount_over_gi_sl": data.get("TS_AMOUNT_OVER_GI_SL") or '',
                    "amounts_above_gi_sl": self._get_label_value(data.get("TS_AMOUNTS_ABOVE_GI_SL")),
                    "other_special_provisions_sl": self._get_label_value(data.get("TS_OTHER_SP_SL")),
                    # Open Enrollment Evidence of Insurability
                    "eoi_req_if_elect_cov_oe_sl": self._get_label_value(data.get("TS_EOI_REQ_IF_ELECT_COV_OE_SL")),
                    "current_ee_no_bl_sl": self._get_label_value(data.get("TS_CURRENT_EE_NO_BL_SL")),
                    "current_ee_increase_amt_sl": self._get_label_value(data.get("TS_CURRENT_EE_INCREASE_AMT_SL"))
            },
            "benefit_and_rate_information": self._sold_class_benefits_rates_information(sold_class_benefits_rates_information, ["Supp Life"]),
            "comments_sl": data.get("TS_COMMENTS_SL") or ''
        }

    def _short_term_disability_std(self, data, sold_class_benefits_rates_information):
        # selected_product_types = ["Basic Life", "Basic Dep Life", "Supp Life", "Supp Dep Life", "STD", "LTD","STD Buy-up","LTD Buy-up"]
        return {
            "benefit_percentage_std": self._get_label_value(data.get("TS_BENEFIT_PERCENTAGE_STD")),
            "effective_date_std": format_date(data.get("TS_EFFECTIVE_DATE_STD")),
            "elimination_period_for_injury_std": self._get_label_value(data.get("TS_ELIM_PERIOD_INJ_STD")),
            "define_earnings_std": self._get_label_value(data.get("TS_STD_EARNINGS_DEF_STD")),
            "max_bene_period_std": data.get("TS_MAX_BENE_PERIOD_STD") or '',
            "termination_date_std": format_date(data.get("TS_TERMINATION_DATE_STD")),
            "elimination_period_for_sickness_std": self._get_label_value(data.get("TS_ELIM_PERIOD_SICK_STD")),
            "maximum_weekly_benefit_std": self._get_label_value(data.get("TS_MAX_WEEK_BENE_STD")),
            "std_minimum_participation_std": self._get_label_value(data.get("TS_STD_MIN_PARTICIPATE_STD")),
            "std_guarantee_issue_benefit_std": self._get_label_value(data.get("TS_STD_GUARANTEE_STD")),
            "explain_maximum_weekly_benefit_std": data.get("TS_EXP_MAX_WEEK_BENE_STD") or '',
            "open_enrollment": {
                 "oe_term_date_std": format_date(data.get("TS_OE_TERM_DATE_STD")),
                 "open_enroll_offer_std":self._get_label_value(data.get("TS_OE_OFFER_STD"))
            },
            "buy_up":{
                 "buy_up_option_std": self._get_label_value(data.get("TS_BUY_UP_OPTION_STD")),
                 "maximum_benefit_period_weeks_std_buyup": data.get("TS_MAX_BENE_PERIOD_WKS_STDBU"),
                 "minimum_participation_std_buyup": self._get_label_value(data.get("TS_STD_MIN_PARTICIPATE_STDBU")),
                 "benefit_percentage_std_buyup": self._get_label_value(data.get("TS_BEN_PERCENT_BU_STD")),
                 "elim_period_inj_std_buyup": self._get_label_value(data.get("TS_ELIM_PERIOD_INJ_STDBU")),
                 "elim_period_sick_std_buyup": self._get_label_value(data.get("TS_ELIM_PERIOD_SICK_STDBU")),
                 "oe_term_date_std_buyup": format_date(data.get("TS_OE_TERM_DATE_STDBU")),
                 "oe_offer_std_buyup": self._get_label_value(data.get("TS_OE_OFFER_STDBU")),
                 "max_week_bene_std_buyup": self._get_label_value(data.get("TS_MAX_WEEK_BENE_STDBU")),
                 "std_guarantee_std_buyup": self._get_label_value(data.get("TS_STD_GUARANTEE_STDBU")),
                 "expected_std_buyup_min_part": data.get("TS_EXP_STDBU_MIN_PART") or '',
                 "minimum_week_benefit_std_buyup": self._get_label_value(data.get("TS_MIN_WEEK_BENE_STDBU")),
                 "comments_std_buyup": data.get("TS_COMMENTS_BUSTD") or ''
            },
            "underwriting": {
                 # Evidence of Insurability
                 "eoi_coverage_31_days_std": self._get_label_value(data.get("TS_EOI_COV_31_DAYS_STD")),
                 "eoi_new_hire_over_gi_std": self._get_label_value(data.get("TS_EOI_NEW_HIRE_OVER_GI_STD")),
                 "na_takeover_for_ee_std": self._get_label_value(data.get("TS_NA_TAKEOVER_FOR_EE_STD")),
                 "other_std": self._get_label_value(data.get("TS_OTHER_STD")),
                 "eoi_req_newly_elig_ee_std": self._get_label_value(data.get("TS_EOI_REQ_NEWLY_ELIG_EE_STD")),
                 #Open Enrollment Evidence of Insurability 
                 "eoi_req_if_elect_cov_oe_std": self._get_label_value(data.get("TS_EOI_REQ_IF_ELECT_COV_OESTD")),
                 "current_ee_no_bl_std": self._get_label_value(data.get("TS_CURRENT_EE_NO_BL_STD")),
                 "current_ee_increase_amt_std": self._get_label_value(data.get("TS_CURRENT_EE_INCREASE_AMTSTD")),
                 # Evidence of Insurability - STD Buy-up
                 "eoi_coverage_31_days_std_buyup": self._get_label_value(data.get("TS_EOI_COV_31_DAYS_STDBU")),
                 "eoi_for_incr_cov_std_buyup": self._get_label_value(data.get("TS_EOI_FOR_INCR_COV_STDBU")),
                 "na_takeover_for_ee_std_buyup": self._get_label_value(data.get("TS_NA_TAKEOVER_FOR_EE_STDBU")),
                 "eoi_req_newly_elig_ee_std_buyup": self._get_label_value(data.get("TS_EOI_REQ_NEWLY_ELIG_EESTDB")),
                 "eoi_new_hire_over_gi_std_buyup": self._get_label_value(data.get("TS_EOI_NEW_HIRE_OVER_GI_STDBU")),
                 "other_std_buyup": self._get_label_value(data.get("TS_OTHER_STDBU"))
            },
            "benefit_and_rate_information": self._sold_class_benefits_rates_information(sold_class_benefits_rates_information, ["STD", "STD Buy-up"]),
            "comments_std": data.get("TS_COMMENTS_STD") or ''
        }
 
    def _long_term_disability_ltd(self, data, sold_class_benefits_rates_information):
        # selected_product_types = ["Basic Life", "Basic Dep Life", "Supp Life", "Supp Dep Life", "STD", "LTD","STD Buy-up","LTD Buy-up"]
        return {
            "effective_date_ltd": format_date(data.get("TS_EFFECTIVE_DATE_LTD")),
            "termination_date_ltd": format_date(data.get("TS_TERMINATION_DATE_LTD")),
            "maximum_month_benefit_ltd":self._get_label_value(data.get("TS_MAX_MONTH_BEN_LTD")),
            "benefit_percentage_ltd": self._get_label_value(data.get("TS_BEN_PERCENT_LTD")),
            "exp_max_month_ben_ltd": data.get("TS_EXP_MAX_MONTH_BEN_LTD") or '',
            "define_earnings_ltd": self._get_label_value(data.get("TS_DEFINE_EARNINGS_LTD")),
            "elim_period_ltd": self._get_label_value(data.get("TS_ELIM_PERIOD_LTD")),
            "ltd_guarant_iss_ben": self._get_label_value(data.get("TS_LTD_GUARANT_ISS_BEN")),
            "ltd_min_participate": self._get_label_value(data.get("TS_LTD_MIN_PARTICIPATE")),
            "max_bene_period_ltd": self._get_label_value(data.get("TS_MAX_BENE_PERIOD_LTD")),
            "open_enrollment":{
                "open_enrollment_offered": self._get_label_value(data.get("TS_OE_OFFER_LTD")),
                "open_enrollment_termination_date": format_date(data.get("TS_OE_TERM_DATE_LTD")),
                "guaranteed_issue_annual_open_enrollment": data.get("TS_GUAR_ISSUE_ANNUAL_OE_LTD") or '',
                "guaranteed_issue_onetime_open_enrollment": data.get("TS_GUAR_ISSUE_ONETIME_OE_LTD") or ''
            }, 
            "buy_up": {
                 "ltd_buyup_option": self._get_label_value(data.get("TS_LTD_BUYUP_OPTION")),
                 "open_enrollment_offered_ltd_buyup": self._get_label_value(data.get("TS_OE_OFFER_LTDBU")),
                 "guarantee_issue_limits_n_ltd_byup": self._get_label_value(data.get("TS_GUARANTEED_ISSUE_LIMITS__N")),
                 "open_enrollment_termination_date_ltd_buyup": format_date(data.get("TS_OE_TERM_DATE_LTDBU")),
                 "guaranteed_issue_annual_open_enrollment_ltd_buyup": data.get("TS_GUAR_ISSUE_ANNUAL_OE_LTDBU") or '',
                 "guaranteed_issue_onetime_open_enrollment_ltd_buyup": data.get("TS_GUAR_ISS_ONETIME_OE_LTDBU") or '',
                 "benefit_percentage_ltd_buyup": self._get_label_value(data.get("TS_BENEFIT_PERCENTAGE_LTD_BUP")),
                 "maximum_month_buyup_option_ltd":self._get_label_value(data.get("TS_MAX_MONTH_BU_OPTION_LTD")),
                 "minimum_month_benefit_ltd_buyup": self._get_label_value(data.get("TS_MIN_MONTH_BEN_BU_LTD")),
                 "comments_ltd_buyup": data.get("TS_COMMENTS_LTDBU") or ''
            },
            "underwriting":{
                 # Evidence of Insurability LTD
                 "eoi_req_newly_elig_ee_ltd": self._get_label_value(data.get("TS_EOI_REQ_NEWLY_ELIG_EE_LTD")),
                 "na_takeover_for_ee_ltd": self._get_label_value(data.get("TS_NA_TAKEOVER_FOR_EE_LTD")),
                 "eoi_new_hire_over_gi_ltd": self._get_label_value(data.get("TS_EOI_NEW_HIRE_OVER_GI_LTD")),
                 "eoi_cov_31_days_ltd": self._get_label_value(data.get("TS_EOI_COV_31_DAYS_LTD")),
                 "other_ltd": data.get("TS_OTHER_LTD") or '',
                 # Open Enrollment Evidence of Insurability LTD
                 "eoi_req_if_elect_cov_oe_ltd": self._get_label_value(data.get("TS_EOI_REQ_IF_ELECT_COV_OELTD")),
                 "current_ee_no_bl_ltd": self._get_label_value(data.get("TS_CURRENT_EE_NO_BL_LTD")),
                 "current_ee_increase_amt_ltd": self._get_label_value(data.get("TS_CURRENT_EE_INCREASE_AMTLTD")),
                 # Evidence of Insurability – LTD Buy-up
                 "na_takeover_for_ee_ltd_buyup": self._get_label_value(data.get("TS_NA_TAKEOVER_FOR_EE_LTDBU")),
                 "eoi_req_newly_elig_ee_ltd_buyup": self._get_label_value(data.get("TS_EOI_REQ_NEWLY_ELIG_EELTDBU")),
                 "eoi_new_hire_over_gi_ltd_buyup": self._get_label_value(data.get("TS_EOI_NEW_HIRE_OVER_GI_LTDBU")),
                 "eoi_cov_31_days_ltd_buyup": self._get_label_value(data.get("TS_EOI_COV_31_DAYS_LTDBU")),
                 "eoi_for_incr_cov_ltd_buyup": self._get_label_value(data.get("TS_EOI_FOR_INCR_COV_LTDBU")),
                 "other_ltd_buyup": data.get("TS_OTHER_LTDBU") or '',
                 "buy_up_billing_method_ltd":  self._get_label_value(data.get("TS_BUY_UP_BILLING_METHOD__LTD"))
            },
            "benefit_and_rate_information": self._sold_class_benefits_rates_information(sold_class_benefits_rates_information, ["LTD", "LTD Buy-up"]),
            "comments_ltd": data.get("TS_COMMENTS_LTD") or ''
        }    

    def _get_eligibility(self, data):
        eligibility_result = []
        for index, item in enumerate(data):
            eligibility_result.append({
                "full_time_employees_effective_on": item.get("TS_FT_EMPLOYEE_EFFECT"),
                "waiting_period_design": self._get_label_value_wp_nonstandard(item.get("TS_NON_STANDARD_DETAIL")),
                "waiting_period_description": self._get_label_value_wp_design(item.get("TS_WP_DESIGN")),
                "waiting_period_prefix": self._get_label_value_wp_prefix(item.get("TS_WP_PREFIX")),
                "full_time_hours_per_week": item.get("TS_FULL_TIME_HOURS_PER_WEEK") or '',
                "rehire_provision": self._get_label_value(item.get("TS_REHIRE_PROVISION")),
                "explain_rehire_provision": item.get("TS_EXPLAIN_REHIRE_PROVISION") or '',
                "comments": item.get("TS_COMMENTS") or ''
            })
            
        return eligibility_result

    def _sold_class_benefits_rates_information(self, data, selected_product_types):
        sold_class_benefits_rates_information_result = []
        for item in data:
            product_type = self._get_label_value(item.get("TS_PRODUCT"))
            if product_type in selected_product_types:
                    sold_class_benefits_rates_information_result.append({
                        "product_type": product_type,
                        "effective_date": format_date(item.get("TS_EFFECTIVE_DATE")),
                        "termination_date": format_date(item.get("TS_TERMINATION_DATE")),
                        "class_code": item.get("TS_CLASS_CODE") or '',
                        "insurance_class_of_ee": item.get("TS_INSURANCE_CLASS_OF_EE") or '',
                        "full_benefit_description": item.get("TS_AMOUNT_AND_MAX_BENEFIT") or '',
                        "comments": item.get("TS_COMMENTS") or ''
                    })

        return sold_class_benefits_rates_information_result

    def _billing_enrollment_info(self, data):
        billing_enrollment_info_result = []
        for item in data:
            billing_enrollment_info_result.append({
                "self_bill_temp": self._get_label_value(item.get("TS_SELF_BILL_TEMP")),
                "lifeadd_bill_meth": self._get_label_value(item.get("TS_LIFEADD_BILL_METH")),
                "employee_paid":{
                    "employee_paid_bl": number_percentage_format(item.get("TS_EMPLOYEE_PAID_BL")),
                    "employee_paid_dl": number_percentage_format(item.get("TS_EMPLOYEE_PAID_DL")),
                    "employee_paid_sl": number_percentage_format(item.get("TS_EMPLOYEE_PAID_SL")),
                    "employee_paid_sdl": number_percentage_format(item.get("TS_EMPLOYEE_PAID_SDL")),
                    "employee_paid_ltd": number_percentage_format(item.get("TS_EMPLOYEE_PAID_LTD")),
                    "employee_paid_std": number_percentage_format(item.get("TS_EMPLOYEE_PAID_STD")),
                    "employee_paid_std_buyup": number_percentage_format(item.get("TS_EMPLOYEE_PAID_STDBU")),
                    "employee_paid_ltd_buyup": number_percentage_format(item.get("TS_EMPLOYEE_PAID_LTDBU"))
                },
                "employer_paid": {
                    "employer_paid_bl": number_percentage_format(item.get("TS_EMPLOYER_PAID_BL")),
                    "employer_paid_dl": number_percentage_format(item.get("TS_EMPLOYER_PAID_DL")),
                    "employer_paid_sl": number_percentage_format(item.get("TS_EMPLOYER_PAID_SL")),
                    "employer_paid_sdl": number_percentage_format(item.get("TS_EMPLOYER_PAID_SDL")),
                    "employer_paid_ltd": number_percentage_format(item.get("TS_EMPLOYER_PAID_LTD")),
                    "employer_paid_std": number_percentage_format(item.get("TS_EMPLOYER_PAID_STD")),
                    "employer_paid_std_buyup": number_percentage_format(item.get("TS_EMPLOYER_PAID_STDBU")),
                    "employer_paid_ltd_buyup": number_percentage_format(item.get("TS_EMPLOYER_PAID_LTDBU"))
                },
                "comments": item.get("TS_COMMENTS") or ''
            })

        return billing_enrollment_info_result

    def _get_label_value(self, value_id):
        if not value_id:
            return None

        lavel_value = LifeDIGroupRepository.get_label_value_repo(self.db, value_id)
        return lavel_value.get("TS_NAME")

    def _get_value_list(self, value_id_list: str):
        if not value_id_list:
            return ""
            
        value_ids = [int(value) for value in value_id_list.strip(",").split(",") if value]
        value_result_list = LifeDIGroupRepository.get_value_list_repo(self.db, value_ids)
        result = ",".join([item.get("TS_NAME") for item in value_result_list])
        return result


    def _get_label_value_wp_design(self, value_id):
        if not value_id:
            return '(None)'
        lavel_value = LifeDIGroupRepository.get_label_value_wp_design_repo(self.db, value_id)
        title = lavel_value.get("TS_TITLE")
        if not title or str(title).strip().lower() == "null":
            title = '(None)'
        return title

    def _get_label_value_wp_prefix(self, value_id):
        if not value_id:
            return '(None)'
        lavel_value = LifeDIGroupRepository.get_label_value_wp_prefix_repo(self.db, value_id)
        title = lavel_value.get("TS_TITLE")
        if not title or str(title).strip().lower() == "null":
            title = '(None)'
        return title


    def _get_label_value_wp_nonstandard(self, value_id_list: str):  
        if not value_id_list:
            return ""

        value_ids = [int(value) for value in value_id_list.strip(",").split(",") if value]
        value_result_list = LifeDIGroupRepository.get_label_value_wp_nonstandard_repo(self.db, value_ids)
        result = ",".join([item.get("TS_TITLE") for item in value_result_list])
        return result or '(None)'

