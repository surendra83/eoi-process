from sqlalchemy import Column, Integer, String, Date
from database.base import Base

class UldLifeDi(Base):
    __tablename__ = "ULD_LIFE_DI"

    TS_ID = Column(Integer, primary_key=True)

    TS_SITUS_STATE = Column(String)
    TS_GROUP_NAME = Column(String)
    TS_GROUP_POLICY_NUMBER = Column(String)
    TS_GROUP_EFFECTIVE_DATE = Column(Date)
    TS_GROUP_TERM_DATE = Column(Date)
    TS_PLAN_ANNIV_DATE = Column(Date)

    TS_1_BENE_LEVEL_EQUALS_SDLS = Column(String)
    TS_BENEFIT_PERCENTAGE_LTD_BUP = Column(String)
    TS_BENEFIT_PERCENTAGE_STD = Column(String)

    TS_COMMENTS_BADD = Column(String)
    TS_COMMENTS_BL = Column(String)
    TS_COMMENTS_BUSTD = Column(String)
    TS_COMMENTS_DADD = Column(String)
    TS_COMMENTS_DL = Column(String)
    TS_COMMENTS_GI = Column(String)
    TS_COMMENTS_LTD = Column(String)
    TS_COMMENTS_LTDBU = Column(String)
    TS_COMMENTS_SADD = Column(String)
    TS_COMMENTS_SDADD = Column(String)
    TS_COMMENTS_SDL = Column(String)
    TS_COMMENTS_SL = Column(String)
    TS_COMMENTS_STD = Column(String)

    TS_CURRENT_EE_INCREASE_AMT_SD = Column(String)
    TS_CURRENT_EE_NO_BL_SDL = Column(String)
    TS_DEFINE_EARNINGS_SL = Column(String)

    TS_EFFECTIVE_DATE_SDL = Column(Date)
    TS_EFFECTIVE_DATE_SL = Column(Date)
    TS_EFFECTIVE_DATE_STD = Column(Date)

    TS_ELIM_PERIOD_INJ_STD = Column(String)
    TS_ELIM_PERIOD_SICK_STD = Column(String)

    TS_EOI_COV_31_DAYS_SDLS = Column(String)
    TS_EOI_FOR_1_BENE_LVL_SDLS = Column(String)
    TS_EOI_FOR_INCR_COV_SDLS = Column(String)
    TS_EOI_NEW_HIRE_OVER_GI_SDLS = Column(String)
    TS_EOI_REQ_IF_ELECT_COV_OESDL = Column(String)
    TS_EOI_REQ_NEWLY_ELIG_EE_SDLS = Column(String)

    TS_GUAR_ISS_ONETIME_OE_LTDBU = Column(String)
    TS_GUAR_ISSUE_AMT_BL = Column(String)
    TS_GUAR_ISSUE_AMT_SL = Column(String)
    TS_GUAR_ISSUE_ANNUAL_OE_LTDBU = Column(String)
    TS_GUARANTEED_ISSUE_LIMITS__N = Column(String)

    TS_IS_SUPP_SPOUSE_DL_AMT_LIM = Column(String)
    TS_LTD_BUYUP_OPTION = Column(String)
    TS_MAX_MONTH_BEN_LTD = Column(String)
    TS_MAX_MONTH_BU_OPTION_LTD = Column(String)
    TS_EXP_MAX_WEEK_BENE_STD = Column(String)
    TS_MAX_WEEK_BENE_STD = Column(String)

    TS_MUST_EE_COVERED_FOR_SDL = Column(String)
    TS_NA_TAKEOVER_FOR_EE_SDLS = Column(String)
    TS_OE_OFFER_LTDBU = Column(String)
    TS_OE_TERM_DATE_LTDBU = Column(Date)
    TS_OTHER_EOI_SDLS = Column(String)
    TS_PART_REQ_MET_SDL = Column(String)

    TS_EXP_REDUCE_SCH_SL = Column(String)
    TS_EXP_ROUNDING_SL = Column(String)

    TS_STD_GUARANTEE_STD = Column(String)
    TS_STD_MIN_PARTICIPATE_STD = Column(String)

    TS_TERMINATION_DATE_SDL = Column(Date)
    TS_TERMINATION_DATE_SL = Column(Date)
    TS_TERMINATION_DATE_STD = Column(Date)

    TS_VIRGIN_LINE_COVERAGE_SL = Column(String)
    TS_BUY_UP_OPTION_STD = Column(String)
    TS_MAX_BENE_PERIOD_WKS_STDBU = Column(String)
    TS_STD_MIN_PARTICIPATE_STDBU = Column(String)

    TS_UNDERWRITING_COMPANY = Column(String)
    TS_UHC_POLICY_NUMBER = Column(String)