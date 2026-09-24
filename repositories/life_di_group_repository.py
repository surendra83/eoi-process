# repositories/life_di_group_repository.py
import uuid
from sqlalchemy import text
from sqlalchemy.orm import Session
from core.logger import app_logger
from sqlalchemy import bindparam

class LifeDIGroupRepository:

    @staticmethod
    def get_by_group_repo(db: Session, group_id: str):
        app_logger.bind(
            log_id=str(uuid.uuid4()),
            execute_method="get_by_group_repo"
        ).info(f"Fetching UDL_LIFE_DI: {group_id}")
        query = text("""
            SELECT TOP 1
                TS_ID,
                TS_SITUS_STATE,
                TS_GROUP_NAME,
                TS_GROUP_POLICY_NUMBER,
                TS_GROUP_EFFECTIVE_DATE,
                TS_GROUP_TERM_DATE,
                TS_1_BENE_LEVEL_EQUALS_SDLS,
                TS_BENEFIT_PERCENTAGE_STD,
                TS_COMMENTS_BADD,
                TS_COMMENTS_BL,
                TS_COMMENTS_BUSTD,
                TS_COMMENTS_DL,
                TS_COMMENTS_GI,
                TS_ADDITIONAL_BENEFITS_LTD,
                TS_BEN_PERCENT_LTD,
                TS_EFFECTIVE_DATE_LTD,
                TS_EXP_MAX_MONTH_BEN_LTD,
                TS_DEFINE_EARNINGS_LTD,
                TS_ELIM_PERIOD_LTD,
                TS_LTD_GUARANT_ISS_BEN,
                TS_LTD_MIN_PARTICIPATE,
                TS_MAX_BENE_PERIOD_LTD,
                TS_TERMINATION_DATE_LTD,
                TS_COMMENTS_LTD,
                TS_MAX_MONTH_BEN_LTD,
                TS_GUAR_ISSUE_ANNUAL_OE_LTD,
                TS_GUAR_ISSUE_ONETIME_OE_LTD,
                TS_OE_TERM_DATE_LTD,
                TS_OE_OFFER_LTD,
                TS_BENEFIT_PERCENTAGE_LTD_BUP,
                TS_MIN_MONTH_BEN_BU_LTD,
                TS_COMMENTS_LTDBU,
                TS_OTHER_OPTIONAL_BENE_LTD,
                TS_COMMENTS_SDL,
                TS_EXP_PORT_BENE_SL,
                TS_COMMENTS_SL,
                TS_COMMENTS_STD,
                TS_CURRENT_EE_INCREASE_AMT_SD,
                TS_CURRENT_EE_NO_BL_SDL,
                TS_DEFINE_EARNINGS_SL,
                TS_PART_REQ_MET_SL,
                TS_NA_TAKEOVER_FOR_EE_SL,
                TS_EOI_REQ_NEWLY_ELIG_EE_SL,
                TS_EOI_NEW_HIRE_OVER_GI_SL,
                TS_EOI_COV_31_DAYS_SL,
                TS_EOI_FOR_INCR_COV_SL,
                TS_EOI_FOR_1_BENE_LVL_SL,
                TS_ONE_BENEFIT_LEVEL_SL,
                TS_OTHER_EOI_SL,
                TS_EOI_SALARY_OVER_GI_SL,
                TS_AMOUNT_OVER_GI_SL,
                TS_AMOUNTS_ABOVE_GI_SL,
                TS_OTHER_SP_SL,
                TS_EOI_REQ_IF_ELECT_COV_OE_SL,
                TS_CURRENT_EE_NO_BL_SL,
                TS_CURRENT_EE_INCREASE_AMT_SL,
                TS_EFFECTIVE_DATE_SDL,
                TS_TERMINATION_DATE_SDL,
                TS_VIRGIN_LINE_COVERAGE_SDL,
                TS_SP_GUAR_ISSUE_AMT_SDL,
                TS_SPOUSE_AGE_REDUC_SDL,
                TS_EFFECTIVE_DATE_SL,
                TS_EFFECTIVE_DATE_STD,
                TS_PORT_BENE_SDL,
                TS_ELIM_PERIOD_INJ_STD,
                TS_ELIM_PERIOD_SICK_STD,
                TS_EOI_COV_31_DAYS_SDLS,
                TS_EOI_FOR_1_BENE_LVL_SDLS,
                TS_EOI_FOR_INCR_COV_SDLS,
                TS_EOI_NEW_HIRE_OVER_GI_SDLS,
                TS_EOI_REQ_IF_ELECT_COV_OESDL,
                TS_EOI_REQ_NEWLY_ELIG_EE_SDLS,
                TS_GUAR_ISS_ONETIME_OE_LTDBU,
                TS_GUAR_ISSUE_AMT_BL,
                TS_GUAR_ISSUE_AMT_SL,
                TS_GUAR_ISSUE_ANNUAL_OE_LTDBU,
                TS_GUARANTEED_ISSUE_LIMITS__N,
                TS_IS_SUPP_SPOUSE_DL_AMT_LIM,
                TS_LTD_BUYUP_OPTION,
                TS_EOI_REQ_NEWLY_ELIG_EE_LTD,
                TS_NA_TAKEOVER_FOR_EE_LTD,
                TS_EOI_NEW_HIRE_OVER_GI_LTD,
                TS_EOI_COV_31_DAYS_LTD,
                TS_OTHER_LTD,
                TS_NA_TAKEOVER_FOR_EE_LTDBU,
                TS_EOI_REQ_NEWLY_ELIG_EELTDBU,
                TS_EOI_NEW_HIRE_OVER_GI_LTDBU,
                TS_EOI_COV_31_DAYS_LTDBU,
                TS_EOI_FOR_INCR_COV_LTDBU,
                TS_OTHER_LTDBU,
                TS_BUY_UP_BILLING_METHOD__LTD,
                TS_MAX_MONTH_BU_OPTION_LTD,
                TS_EXP_MAX_WEEK_BENE_STD,
                TS_MAX_WEEK_BENE_STD,
                TS_OE_TERM_DATE_STD,
                TS_STD_EARNINGS_DEF_STD,
                TS_EOI_COV_31_DAYS_STD,
                TS_MAX_BENE_PERIOD_STD,
                TS_EOI_NEW_HIRE_OVER_GI_STD,
                TS_NA_TAKEOVER_FOR_EE_STD,
                TS_OTHER_STD,
                TS_EOI_REQ_NEWLY_ELIG_EE_STD,
                TS_OE_OFFER_STD,
                TS_BEN_PERCENT_BU_STD,
                TS_ELIM_PERIOD_INJ_STDBU,
                TS_ELIM_PERIOD_SICK_STDBU,
                TS_OE_TERM_DATE_STDBU,
                TS_OE_OFFER_STDBU,
                TS_MAX_WEEK_BENE_STDBU,
                TS_STD_GUARANTEE_STDBU,
                TS_MIN_WEEK_BENE_STDBU,
                TS_EXP_STDBU_MIN_PART,
                TS_EOI_REQ_IF_ELECT_COV_OESTD,
                TS_CURRENT_EE_NO_BL_STD,
                TS_CURRENT_EE_INCREASE_AMTSTD,
                TS_EOI_COV_31_DAYS_STDBU,
                TS_EOI_FOR_INCR_COV_STDBU,
                TS_NA_TAKEOVER_FOR_EE_STDBU,
                TS_EOI_REQ_NEWLY_ELIG_EESTDB,
                TS_EOI_NEW_HIRE_OVER_GI_STDBU,
                TS_OTHER_STDBU,
                TS_MUST_EE_COVERED_FOR_SDL,
                TS_NA_TAKEOVER_FOR_EE_SDLS,
                TS_OE_OFFER_LTDBU,
                TS_OE_TERM_DATE_LTDBU,
                TS_EOI_REQ_IF_ELECT_COV_OELTD,
                TS_CURRENT_EE_NO_BL_LTD,
                TS_CURRENT_EE_INCREASE_AMTLTD,
                TS_OTHER_EOI_SDLS,
                TS_PART_REQ_MET_SDL,
                TS_PLAN_ANNIV_DATE,
                TS_EXP_REDUCE_SCH_SL,
                TS_PORT_BENE_SL,
                TS_ACC_DEATH_BENEFIT_SL,
                TS_ROUNDING_SL,
                TS_REDUCE_SCH_SL,
                TS_STD_GUARANTEE_STD,
                TS_STD_MIN_PARTICIPATE_STD,
                TS_TERMINATION_DATE_SL,
                TS_TERMINATION_DATE_STD,
                TS_VIRGIN_LINE_COVERAGE_SL,
                TS_OPEN_ENROLLMENT_OFFERED_SL,
                TS_OPEN_ENROLL_INITIAL_SL,
                TS_GI_RESTRICTION_SL,
                TS_OPEN_ENROLL_ANNIV_SL,
                TS_OE_TERM_DATE_SL,
                TS_OPEN_ENROLL_OFFERED_SDL,
                TS_OPEN_ENROLL_INITIAL_SDL,
                TS_GI_RESTRICTION_SDL,
                TS_OE_TERM_DATE_SDL,
                TS_OPEN_ENROLL_ANNIV_SDL,
                TS_BUY_UP_OPTION_STD,
                TS_MAX_BENE_PERIOD_WKS_STDBU,
                TS_STD_MIN_PARTICIPATE_STDBU,
                TS_UNDERWRITING_COMPANY,
                TS_UHC_POLICY_NUMBER,
                TS_PRODUCTS_ON_UHC,
                TS_EFFFECTIVE_DATE_BL,
                TS_TERMINATION_DATE_BL,
                TS_ROUNDING_BL,
                TS_DEFINE_EARNINGS_BL,
                TS_GUAR_ISSUE_ONETIME_OE_BL,
                TS_GUAR_ISSUE_ANNUAL_OENROLL,
                TS_OE_TERM_DATE_BL,
                TS_OPEN_ENROLLMENT_OFFERED_BL,
                TS_FOR_CONTRIB_PLANS__MEDICAL,
                TS_MED_UW_NEW_EE_OVER_GI_BL,
                TS_MED_UW_SALARY_OVER_GI_BL,
                TS_NA_TAKEOVER_FOR_EE_BL,
                TS_EOI_REQ_NEWLY_ELIG_EE_BL,
                TS_OTHER_BL,
                TS_CURRENT_EE_NO_BL_BL,
                TS_CURRENT_EE_INCREASE_AMT_BL,
                TS_EOI_REQ_IF_ELECT_COV_OE_BL,
                TS_ACC_DEATH_BENEFITS_BL,
                TS_EFFECTIVE_DATE_DL,
                TS_TERMINATION_DATE_DL,
                TS_DOM_PARTNER_COV_DL,
                TS_SPOUSE_AGE_REDUC_DL,
                TS_EOI_REQ_IF_ELECT_COV_OE_DL,
                TS_CURRENT_EE_NO_BL_DL,
                TS_CURRENT_EE_INCREASE_AMT_DL,
                TS_BASIC_LIFE,
                TS_DEP_LIFE,
                TS_SUPP_LIFE,
                TS_SUPP_DEP_LIFE,
                TS_STD,
                TS_LTD,
                TS_LASTMODIFIER
            FROM ULD_LIFE_DI
            WHERE TS_GROUP_POLICY_NUMBER = CAST(:group_id AS NVARCHAR(50))
        """)
        result = db.execute(query,{"group_id": group_id})
        row = result.mappings().first()
        if not row:
            return None

        return dict(row)

    @staticmethod
    def get_subgroup_repo(db, ts_id: str):
        app_logger.bind(
            log_id=str(uuid.uuid4()),
            execute_method="get_subgroup_repo"
        ).info(f"Fetching ULD_SUBGROUPS for ts_id: {ts_id}")
        query = text("""
            SELECT
                TS_ID,
                TS_ISSUEID,
                TS_SUBGROUP_NAME,
                TS_SUBGROUP_NUMBER,
                TS_TERMINATION_DATE,
                TS_EFFECTIVE_DATE,
                TS_NAME_CON1,
                TS_TYPE_CON1,
                TS_TITLE_CON1,
                TS_EMAIL_CON1,
                TS_ADDRESS_CON1,
                TS_CSZ_CON1,
                TS_PHONE_CON1,
                TS_FAX_CON1,
                TS_NAME_CON2,
                TS_TYPE_CON2,
                TS_TITLE_CON2,
                TS_EMAIL_CON2,
                TS_ADDRESS_CON2,
                TS_CSZ_CON2,
                TS_PHONE_CON2,
                TS_FAX_CON2,
                TS_COMPANY_NAME_CON1,
                TS_COMPANY_NAME_CON2,
                TS_CONTACT_2_ADDRESS,
                TS_COMMENTS_SUBGROUP,
                TS_LASTMODIFIER
            FROM ULD_SUBGROUPS
            WHERE TS_LINK_TO_SOLD_CASE = :ts_id
            AND TS_TERMINATION_DATE IS NULL
        """)
        result = db.execute(query, {"ts_id": ts_id})
        rows = result.mappings().all()
        if not rows:
            return []

        return [dict(row) for row in rows]  

    @staticmethod
    def get_eligibility_repo(db, ts_id: str):
        app_logger.bind(
            log_id=str(uuid.uuid4()),
            execute_method="get_eligibility_repo"
        ).info(f"Fetching ULD_ELIGIBILITY for ts_id: {ts_id}")
        query = text("""
            SELECT
                TS_ID,
                TS_LINK_TO_SOLD_CASE,
                TS_TERMINATION_DATE,
                TS_FT_EMPLOYEE_EFFECT,
                TS_NON_STANDARD_DETAIL,
                TS_WP_DESIGN,
                TS_WP_PREFIX,
                TS_FULL_TIME_HOURS_PER_WEEK,
                TS_EXPLAIN_REHIRE_PROVISION,
                TS_REHIRE_PROVISION,
                TS_COMMENTS
            FROM ULD_ELIGIBILITY
            WHERE TS_LINK_TO_SOLD_CASE = :ts_id
        """)
        result = db.execute(query, {"ts_id": ts_id})
        rows = result.mappings().all()
        if not rows:
            return []

        return [dict(row) for row in rows]

    @staticmethod
    def get_value_list_repo(db, ts_ids: list[int]):
        if not ts_ids:
            return []

        query = text("""
           SELECT TS_NAME
            FROM TS_SELECTIONS
            WHERE TS_ID IN :ts_ids
        """).bindparams(bindparam("ts_ids", expanding=True))
        result = db.execute(query, {"ts_ids":ts_ids}) 
        return [dict(row) for row in result.mappings().all()]
    

    @staticmethod
    def get_label_value_repo(db, ts_id: str):
        query = text("""
           SELECT TS_NAME
            FROM TS_SELECTIONS
            WHERE TS_ID = :ts_id
        """)
        result = db.execute(query, {"ts_id": ts_id})
        row = result.mappings().first()
        if not row:
            return None

        return dict(row)
    
    @staticmethod
    def get_sold_class_benefits_rates_information_repo(db, ts_id: str):
        app_logger.info(f"Fetching ULD_SOLD_RATES for ts_id: {ts_id}")
        query = text("""
            SELECT TS_ID,
                TS_PRODUCT,
                TS_EFFECTIVE_DATE,
                TS_TERMINATION_DATE,
                TS_CLASS_CODE,
                TS_INSURANCE_CLASS_OF_EE,
                TS_AMOUNT_AND_MAX_BENEFIT,
                TS_COMMENTS
            FROM ULD_SOLD_RATES
            WHERE TS_LINK_TO_SOLD_CASE = :ts_id
            AND TS_TERMINATION_DATE IS NULL
        """)
        result = db.execute(query, {"ts_id": ts_id})
        rows = result.mappings().all()
        if not rows:
            return []

        return [dict(row) for row in rows]


    @staticmethod
    def selected_product_type_repo(db):
        app_logger.info(f"Fetching selected product types")
        query = text("""
            Select TS_ID, 
            TS_TABLEID,
            TS_NAME, 
            TS_DBNAME 
            from TS_FIELDS 
            where TS_DBNAME IN ('BASIC_LIFE','DEP_LIFE','SUPP_LIFE','SUPP_DEP_LIFE','STD','LTD') 
            AND TS_TABLEID IN (select TS_ID From TS_TABLES Where TS_DBNAME ='ULD_LIFE_DI')
        """)
        result = db.execute(query)
        rows = result.mappings().all()
        if not rows:    
            return []

        return [dict(row) for row in rows]

    
    @staticmethod
    def get_billing_enrollment_info_repo(db, ts_id: str):
        app_logger.info(f"Fetching ULD_BILLING_ENROLL for ts_id: {ts_id}")
        query = text("""
            SELECT 
                TS_ID,
                TS_SELF_BILL_TEMP,
                TS_LIFEADD_BILL_METH,
                TS_EMPLOYEE_PAID_BL,
                TS_EMPLOYEE_PAID_DL,
                TS_EMPLOYEE_PAID_SL,
                TS_EMPLOYEE_PAID_SDL,
                TS_EMPLOYEE_PAID_LTD,
                TS_EMPLOYEE_PAID_STD,
                TS_EMPLOYEE_PAID_STDBU,
                TS_EMPLOYEE_PAID_LTDBU,
                TS_EMPLOYER_PAID_BL,
                TS_EMPLOYER_PAID_DL,
                TS_EMPLOYER_PAID_SL,
                TS_EMPLOYER_PAID_SDL,
                TS_EMPLOYER_PAID_LTD,
                TS_EMPLOYER_PAID_STD,
                TS_EMPLOYER_PAID_STDBU,
                TS_EMPLOYER_PAID_LTDBU,
                TS_COMMENTS
                FROM ULD_BILLING_ENROLL 
                WHERE TS_LINK_TO_PRIMARY = :ts_id
        """)
        result = db.execute(query, {"ts_id": ts_id})
        rows = result.mappings().all()
        if not rows:
            return []

        return [dict(row) for row in rows]


    @staticmethod
    def get_label_value_wp_design_repo(db, ts_id: str):
        query = text("""
           SELECT TS_TITLE
            FROM ULD_DI_WP_DESIGN
            WHERE TS_ID = :ts_id
        """)
        result = db.execute(query, {"ts_id": ts_id})
        row = result.mappings().first()
        if not row:
            return None
        return dict(row)    


    @staticmethod
    def get_label_value_wp_prefix_repo(db, ts_id: str):
        query = text("""
           SELECT TS_TITLE
            FROM ULD_DI_WP_PREFIX
            WHERE TS_ID = :ts_id
        """)
        result = db.execute(query, {"ts_id": ts_id})
        row = result.mappings().first()
        if not row:
            return None
        return dict(row) 


    @staticmethod
    def get_label_value_wp_nonstandard_repo(db, ts_id_list: list):
        if not ts_id_list:
            return []
        query = text("""
           SELECT TS_TITLE
            FROM ULD_DI_NONSTANDARDWP
            WHERE TS_ID IN :ts_id_list
        """).bindparams(bindparam("ts_id_list", expanding=True))
        result = db.execute(query, {"ts_id_list":ts_id_list}) 
        return [dict(row) for row in result.mappings().all()]
