# services/life_di_group_service.py
from repositories.life_di_group_repository import LifeDIGroupRepository
from core.logger import app_logger
from utility.sbm_format import format_date, date_formate_in_yyyy_mm_dd

class LifeDIGroupService:
    def __init__(self, db):
        self.db = db

    def get_life_di_group_serv(self, group_id: str, group_name: str):     
        data = LifeDIGroupRepository.get_by_group_repo(self.db, group_id, group_name)
        if not data:
            app_logger.warning(f"No life DI group data found for group_id: {group_id}, group_name: {group_name}")
            return {}
        
        subgroup_data = LifeDIGroupRepository.get_subgroup_repo(self.db, data.get("TS_ID"))
        if not subgroup_data:
            app_logger.warning(f"No subgroup data found for ts_id: {data.get('TS_ID')}")
            subgroup_data=[]

        app_logger.info(f"Getting eligibility data for ts_id: {data.get('TS_ID')}")
        eligibility_data = LifeDIGroupRepository.get_eligibility_repo(self.db, data.get("TS_ID"))
        app_logger.info(f"Getting eligibility data: {eligibility_data}")
        if not eligibility_data:
            app_logger.warning(f"No eligibility data found for ts_id: {data.get('TS_ID')}")
            eligibility_data =[]

        sold_class_benefits_rates_information = LifeDIGroupRepository.get_sold_class_benefits_rates_information_repo(self.db, data.get("TS_ID"))
        if not sold_class_benefits_rates_information:
            app_logger.warning(f"No sold class benefits rates information found for ts_id: {data.get('TS_ID')}")
            sold_class_benefits_rates_information =[]

        return {
            "group_information": self._group_info(data),
            "contact_information": self._contact_information(subgroup_data),
            "product_information": {
                "short_term_disability_std": self._short_term_disability_std(data),
                "supplemental_dependent_life": self._supplemental_dependent_life(data),
                "supplemental_life": self._supplemental_life(data),
                "long_term_disability_ltd": self._long_term_disability_ltd(data)
            },
            "eligibility": self._get_eligibility(eligibility_data),
            "sold_class_benefits_rates_information": self._sold_class_benefits_rates_information(sold_class_benefits_rates_information), 
            "evidence_of_insurability": self._evidence_of_insurability(data),
            "guaranteed_issue": self._benefit_and_guaranteed_issue(data),
            "accidental_death_and_dismemberment": self._accidental_death_and_dismemberment(data),
            "life_insurance": self._life_insurance(data)
        }

    def _group_info(self, data):
        return {
            "group_name": data.get("TS_GROUP_NAME"),
            "group_policy_number": data.get("TS_GROUP_POLICY_NUMBER"),
            "plan_anniversary_date": format_date(data.get("TS_PLAN_ANNIV_DATE")),
            "group_effective_date": format_date(data.get("TS_GROUP_EFFECTIVE_DATE")),
            "group_termination_date": format_date(data.get("TS_GROUP_TERM_DATE")),
            "situs_state":self._get_label_value(data.get("TS_SITUS_STATE"))
        }

    def _contact_information(self, subgroup_data):
        contact_information = []
        for index, item in enumerate(subgroup_data):
            contact_information.append({
                "division_information": self._division_information(item),
                "primary_contact": self._primary_contact(item),
                "secondary_contact": self._secondary_contact(item),
                "comments_subgroup": item.get("TS_COMMENTS_SUBGROUP")
            })

        return contact_information  
    
    def _division_information(self, data):
        return  {
                "division_number": data.get("TS_SUBGROUP_NUMBER"),
                "division_name": data.get("TS_SUBGROUP_NAME"),
                "effective_date": format_date(data.get("TS_EFFECTIVE_DATE")),
                "termination_date": format_date(data.get("TS_TERMINATION_DATE"))
            }
    
    def _primary_contact(self, subgroup_data):
        contact_type = self._get_value_list(subgroup_data.get("TS_TYPE_CON1"))
        return {
                "contact_type": contact_type,
                "contact_name": subgroup_data.get("TS_NAME_CON1"),
                "contact_title": subgroup_data.get("TS_TITLE_CON1"),
                "contact_email": subgroup_data.get("TS_EMAIL_CON1"),
                "contact_address": subgroup_data.get("TS_ADDRESS_CON1"),
                "contact_city_state_zip": subgroup_data.get("TS_CSZ_CON1"),
                "contact_phone": subgroup_data.get("TS_PHONE_CON1"),
                "contact_fax": subgroup_data.get("TS_FAX_CON1")
            } 

    def _secondary_contact(self, subgroup_data):
        contact_type2 = self._get_value_list(subgroup_data.get("TS_TYPE_CON2"))
        return {
                "contact_type": contact_type2,
                "contact_name": subgroup_data.get("TS_NAME_CON2"),
                "contact_title": subgroup_data.get("TS_TITLE_CON2"),
                "contact_email": subgroup_data.get("TS_EMAIL_CON2"),
                "contact_address": subgroup_data.get("TS_ADDRESS_CON2"),
                "contact_city_state_zip": subgroup_data.get("TS_CSZ_CON2"),
                "contact_phone": subgroup_data.get("TS_PHONE_CON2"),
                "contact_fax": subgroup_data.get("TS_FAX_CON2")
            }    

    def _short_term_disability_std(self, data):
        return {
            "benefit_percentage_std": self._get_label_value(data.get("TS_BENEFIT_PERCENTAGE_STD")),
            "effective_date_std": format_date(data.get("TS_EFFECTIVE_DATE_STD")),
            "termination_date_std": format_date(data.get("TS_TERMINATION_DATE_STD")),
            "std_minimum_participation_std": self._get_label_value(data.get("TS_STD_MIN_PARTICIPATE_STD")),
            "std_guarantee_issue_benefit_std": self._get_label_value(data.get("TS_STD_GUARANTEE_STD")),
            "elimination_period_for_injury_std": self._get_label_value(data.get("TS_ELIM_PERIOD_INJ_STD")),
            "elimination_period_for_sickness_std": self._get_label_value(data.get("TS_ELIM_PERIOD_SICK_STD")),
            "explain_maximum_weekly_benefit_std": data.get("TS_EXP_MAX_WEEK_BENE_STD"),
            "maximum_weekly_benefit_std": self._get_label_value(data.get("TS_MAX_WEEK_BENE_STD")),
            "buy_up_option_std": self._get_label_value(data.get("TS_BUY_UP_OPTION_STD")),
            "maximum_benefit_period_weeks_std_buyup": data.get("TS_MAX_BENE_PERIOD_WKS_STDBU"),
            "minimum_participation_std_buyup": self._get_label_value(data.get("TS_STD_MIN_PARTICIPATE_STDBU")),
            "comments_std": data.get("TS_COMMENTS_STD")
        }

    def _supplemental_dependent_life(self, data):
        return {
            "effective_date_sdl": format_date(data.get("TS_EFFECTIVE_DATE_SDL")),
            "termination_date_sdl": data.get("TS_TERMINATION_DATE_SDL"),
            "current_employee_increase_am-ount_sd": self._get_label_value(data.get("TS_CURRENT_EE_INCREASE_AMT_SD")),
            "current_employee_no_bl_sdl": self._get_label_value(data.get("TS_CURRENT_EE_NO_BL_SDL")),
            "must_employee_covered_for_sdl": self._get_label_value(data.get("TS_MUST_EE_COVERED_FOR_SDL")),
            "na_takeover_for_employee_sdls": self._get_label_value(data.get("TS_NA_TAKEOVER_FOR_EE_SDLS")),
            "participation_requirement_sdl": self._get_label_value(data.get("TS_PART_REQ_MET_SDL")),
            "comments_sdl": data.get("TS_COMMENTS_SDL")
        }

    def _supplemental_life(self, data):
        return {
            "benefit_earnings_sl":self._get_label_value(data.get("TS_DEFINE_EARNINGS_SL")),
            "effective_date_sl": format_date(data.get("TS_EFFECTIVE_DATE_SL")),
            "termination_date_sl": format_date(data.get("TS_TERMINATION_DATE_SL")),
            "guaranteed_issue_amount_sl": data.get("TS_GUAR_ISSUE_AMT_SL"),
            "additional_comment_sl": data.get("TS_COMMENTS_SL"),
            "benifit_reduction_schedule_sl": data.get("TS_EXP_REDUCE_SCH_SL"),
            "exp_rounding_sl": data.get("TS_EXP_ROUNDING_SL"),
            "virgin_line_coverage_sl":self._get_label_value(data.get("TS_VIRGIN_LINE_COVERAGE_SL"))
        }

    def _long_term_disability_ltd(self, data):
        return {
            "benefit_percentage_ltd_buyup": self._get_label_value(data.get("TS_BENEFIT_PERCENTAGE_LTD_BUP")),
            "maximum_month_benefit_ltd":self._get_label_value(data.get("TS_MAX_MONTH_BEN_LTD")),
            "ltd_buyup_option": self._get_label_value(data.get("TS_LTD_BUYUP_OPTION")),
            "maximum_month_buyup_option_ltd":self._get_label_value(data.get("TS_MAX_MONTH_BU_OPTION_LTD")),
            "open_enrollment_offered_ltd_buyup": self._get_label_value(data.get("TS_OE_OFFER_LTDBU")),
            "open_enrollment_termination_date_ltd_buyup": data.get("TS_OE_TERM_DATE_LTDBU"),
            "guaranteed_issue_onetime_open_enrollment_ltd_buyup": data.get("TS_GUAR_ISS_ONETIME_OE_LTDBU"),
            "comments_ltd_buyup": data.get("TS_COMMENTS_LTDBU"),
            "comments_ltd": data.get("TS_COMMENTS_LTD")
        }    

    def _evidence_of_insurability(self, data):
        return {
            "eoi_coverage_within_31_days_sdls": self._get_label_value(data.get("TS_EOI_COV_31_DAYS_SDLS")),
            "eoi_one_benefit_level_sdls": self._get_label_value(data.get("TS_EOI_FOR_1_BENE_LVL_SDLS")),
            "eoi_for_increase_coverage_amount_sdls": self._get_label_value(data.get("TS_EOI_FOR_INCR_COV_SDLS")),
            "eoi_new_hire_over_guaranteed_issue_sdls": self._get_label_value(data.get("TS_EOI_NEW_HIRE_OVER_GI_SDLS")),
            "eoi_required_if_elected_coverage_open_enrollment_sdls": self._get_label_value(data.get("TS_EOI_REQ_IF_ELECT_COV_OESDL")),
            "eoi_required_for_newly_eligible_employees_sdls":self._get_label_value(data.get("TS_EOI_REQ_NEWLY_ELIG_EE_SDLS")),
            "eoi_other_eoi_rules_sdls": self._get_label_value(data.get("TS_OTHER_EOI_SDLS"))
        }

    def _get_eligibility(self, data):
        eligibility_result = []
        for index, item in enumerate(data):
            eligibility_result.append({
                "full_time_employees_effective_on": item.get("TS_FT_EMPLOYEE_EFFECT"),
                "non_standard_detail": item.get("TS_NON_STANDARD_DETAIL"),
                "waiting_period_design": self._get_label_value(item.get("TS_WP_DESIGN")),
                "waiting_period_prefix": self._get_label_value(item.get("TS_WP_PREFIX"))
            })
            
        return eligibility_result

    def _sold_class_benefits_rates_information(self, data):
        sold_class_benefits_rates_information_result = []
        for item in data:
            sold_class_benefits_rates_information_result.append({
                "product_type": self._get_label_value(item.get("TS_PRODUCT")),
                "class_code": item.get("TS_CLASS_CODE"),
                "full_benefit_description": item.get("TS_AMOUNT_AND_MAX_BENEFIT"),
                "insurance_class_of_ee": item.get("TS_INSURANCE_CLASS_OF_EE"),
                "comments": item.get("TS_COMMENTS")
            })
        return sold_class_benefits_rates_information_result


    def _benefit_and_guaranteed_issue(self, data):
        return {
            "one_benefit_level_equals_sdls": data.get("TS_1_BENE_LEVEL_EQUALS_SDLS"),  
            "guarantee_issue_limits_n_ltd_byup": self._get_label_value(data.get("TS_GUARANTEED_ISSUE_LIMITS__N")),
            "guarantee_issue_amount_basic_life": data.get("TS_GUAR_ISSUE_AMT_BL"),
            "guarantee_issue_for_one_time_open_enrollment_ltd_buyup": data.get("TS_GUAR_ISS_ONETIME_OE_LTDBU"),
            "guaranteed_issue_annual_open_enrollment_ltd_buyup": data.get("TS_GUAR_ISSUE_ANNUAL_OE_LTDBU")
        }

    def _accidental_death_and_dismemberment(self, data):
        return {
            "comments_badd": data.get("TS_COMMENTS_BADD"),
            "comments_dadd": data.get("TS_COMMENTS_DADD"),
            "comments_sadd": data.get("TS_COMMENTS_SADD"),
            "comments_sdadd": data.get("TS_COMMENTS_SDADD")
        }

    def _life_insurance(self, data):
        return {
            "comments_basic_life_bl": data.get("TS_COMMENTS_BL"),
            "comments_dependent_life_dl": data.get("TS_COMMENTS_DL"),
            "comments_general_info_gi": data.get("TS_COMMENTS_GI"),
            "supplemental_dependent_spouse_life_amount_limit_by_ee_life_coverage": self._get_label_value(data.get("TS_IS_SUPP_SPOUSE_DL_AMT_LIM"))
        }

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