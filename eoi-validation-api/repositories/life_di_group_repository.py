# repositories/life_di_group_repository.py
from sqlalchemy import text
from sqlalchemy.orm import Session
from core.logger import app_logger
from sqlalchemy import bindparam

class LifeDIGroupRepository:

    @staticmethod
    def get_by_group_repo(db: Session, group_id: str, group_name: str):
        query = text("""
            SELECT
                TS_ID,
                TS_SITUS_STATE,
                TS_GROUP_NAME,
                TS_GROUP_POLICY_NUMBER,
                TS_SITUS_STATE,
                TS_GROUP_EFFECTIVE_DATE,
                TS_GROUP_TERM_DATE,
                TS_1_BENE_LEVEL_EQUALS_SDLS,
                TS_BENEFIT_PERCENTAGE_LTD_BUP,
                TS_BENEFIT_PERCENTAGE_STD,
                TS_COMMENTS_BADD,
                TS_COMMENTS_BL,
                TS_COMMENTS_BUSTD,
                TS_COMMENTS_DADD,
                TS_COMMENTS_DL,
                TS_COMMENTS_GI,
                TS_COMMENTS_LTD,
                TS_MAX_MONTH_BEN_LTD,
                TS_COMMENTS_LTDBU,
                TS_COMMENTS_SADD,
                TS_COMMENTS_SDADD,
                TS_COMMENTS_SDL,
                TS_COMMENTS_SL,
                TS_COMMENTS_STD,
                TS_CURRENT_EE_INCREASE_AMT_SD,
                TS_CURRENT_EE_NO_BL_SDL,
                TS_DEFINE_EARNINGS_SL,
                TS_EFFECTIVE_DATE_SDL,
                TS_EFFECTIVE_DATE_SL,
                TS_EFFECTIVE_DATE_STD,
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
                TS_MAX_MONTH_BU_OPTION_LTD,
                TS_EXP_MAX_WEEK_BENE_STD,
                TS_MAX_WEEK_BENE_STD,
                TS_MUST_EE_COVERED_FOR_SDL,
                TS_NA_TAKEOVER_FOR_EE_SDLS,
                TS_OE_OFFER_LTDBU,
                TS_OE_TERM_DATE_LTDBU,
                TS_OTHER_EOI_SDLS,
                TS_PART_REQ_MET_SDL,
                TS_PLAN_ANNIV_DATE,
                TS_EXP_REDUCE_SCH_SL,
                TS_EXP_ROUNDING_SL,
                TS_STD_GUARANTEE_STD,
                TS_STD_MIN_PARTICIPATE_STD,
                TS_TERMINATION_DATE_SDL,
                TS_TERMINATION_DATE_SL,
                TS_TERMINATION_DATE_STD,
                TS_VIRGIN_LINE_COVERAGE_SL,
                TS_BUY_UP_OPTION_STD,
                TS_MAX_BENE_PERIOD_WKS_STDBU,
                TS_STD_MIN_PARTICIPATE_STDBU,
                TS_UNDERWRITING_COMPANY,
                TS_UHC_POLICY_NUMBER
            FROM ULD_LIFE_DI
            WHERE TS_GROUP_POLICY_NUMBER = :group_id AND TS_GROUP_NAME = :group_name
        """)
        result = db.execute(query,{"group_id": group_id, "group_name": group_name})
        row = result.mappings().first()
        if not row:
            return None

        return dict(row)

    @staticmethod
    def get_subgroup_repo(db, ts_id: str):
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
        query = text("""
            SELECT
                TS_ID,
                TS_LINK_TO_SOLD_CASE,
                TS_COMMENTS,
                TS_FT_EMPLOYEE_EFFECT,
                TS_NON_STANDARD_DETAIL,
                TS_WP_DESIGN,
                TS_WP_PREFIX
            FROM ULD_ELIGIBILITY
            WHERE TS_LINK_TO_SOLD_CASE = :ts_id
        """)
        result = db.execute(query, {"ts_id": ts_id})
        rows = result.mappings().all()
        app_logger.info(f"Retrieved eligibility data for ts_id: {ts_id}: {rows}")
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
        query = text("""
            SELECT TS_ID,
                TS_PRODUCT,
                TS_CLASS_CODE,
                TS_AMOUNT_AND_MAX_BENEFIT,
                TS_INSURANCE_CLASS_OF_EE,
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
