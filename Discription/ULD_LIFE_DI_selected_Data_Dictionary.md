# ULD_LIFE_DI Data Dictionary

## General Information

| Field Name | Description |
|------------|-------------|
| TS_GROUP_NAME | Name of the employer group or policyholder group. |
| TS_GROUP_POLICY_NUMBER | Unique policy number assigned to the group. |
| TS_GROUP_EFFECTIVE_DATE | Date when the group policy became effective. |
| TS_PLAN_ANNIV_DATE | Policy or plan anniversary date. |
| TS_SITUS_STATE | State in which the policy is issued or governed. |

## Short-Term Disability (STD)

| Field Name | Description |
|------------|-------------|
| TS_BENEFIT_PERCENTAGE_STD | Percentage of earnings payable as STD benefit. |
| TS_COMMENTS_STD | Additional comments related to STD coverage. |
| TS_EFFECTIVE_DATE_STD | Effective date of STD coverage. |
| TS_TERMINATION_DATE_STD | Termination date of STD coverage. |
| TS_ELIM_PERIOD_INJ_STD | Elimination period for disability caused by injury. |
| TS_ELIM_PERIOD_SICK_STD | Elimination period for disability caused by sickness. |
| TS_EXP_MAX_WEEK_BENE_STD | Maximum number of weeks STD benefits are payable. |
| TS_STD_GUARANTEE_STD | Guaranteed issue or underwriting provision for STD. |
| TS_STD_MIN_PARTICIPATE_STD | Minimum participation requirement for STD. |

## Supplemental Disability Life (SDL)

| Field Name | Description |
|------------|-------------|
| TS_COMMENTS_SDL | Additional comments related to SDL coverage. |
| TS_EFFECTIVE_DATE_SDL | Effective date of SDL coverage. |
| TS_TERMINATION_DATE_SDL | Termination date of SDL coverage. |
| TS_CURRENT_EE_INCREASE_AMT_SD | Current employee increase amount for disability coverage. |
| TS_CURRENT_EE_NO_BL_SDL | Indicates employee eligibility without benefit level restrictions. |
| TS_MUST_EE_COVERED_FOR_SDL | Indicates employee must already be covered to elect SDL. |
| TS_NA_TAKEOVER_FOR_EE_SDLS | Indicates takeover provision applicability for employees. |
| TS_PART_REQ_MET_SDL | Participation requirements for SDL have been met. |

## Salary Continuance / Supplemental Life (SL)

| Field Name | Description |
|------------|-------------|
| TS_DEFINE_EARNINGS_SL | Definition of earnings used for determining benefits. |
| TS_EFFECTIVE_DATE_SL | Effective date of SL coverage. |
| TS_TERMINATION_DATE_SL | Termination date of SL coverage. |
| TS_GUAR_ISSUE_AMT_SL | Guaranteed issue amount for SL coverage. |
| TS_COMMENTS_SL | Additional comments related to SL coverage. |
| TS_EXP_REDUCE_SCH_SL | Benefit reduction schedule applicable to SL coverage. |
| TS_EXP_ROUNDING_SL | Rounding rules applied to benefit calculations. |
| TS_VIRGIN_LINE_COVERAGE_SL | Indicates whether coverage is provided under Virgin Line provisions. |

## Long-Term Disability (LTD)

| Field Name | Description |
|------------|-------------|
| TS_BENEFIT_PERCENTAGE_LTD_BUP | Benefit percentage under LTD Buy-Up option. |
| TS_COMMENTS_LTD | Additional comments related to LTD coverage. |
| TS_COMMENTS_LTDBU | Additional comments related to LTD Buy-Up coverage. |
| TS_LTD_BUYUP_OPTION | Indicates whether LTD Buy-Up option is available. |
| TS_MAX_MONTH_BU_OPTION_LTD | Maximum benefit duration in months for LTD Buy-Up. |
| TS_OE_OFFER_LTDBU | Indicates LTD Buy-Up is offered during Open Enrollment. |
| TS_OE_TERM_DATE_LTDBU | Open Enrollment termination date for LTD Buy-Up. |
| TS_GUAR_ISS_ONETIME_OE_LTDBU | One-time guaranteed issue amount during Open Enrollment. |
| TS_GUAR_ISSUE_ANNUAL_OE_LTDBU | Annual Open Enrollment guaranteed issue amount. |

## Evidence of Insurability (EOI)

| Field Name | Description |
|------------|-------------|
| TS_EOI_COV_31_DAYS_SDLS | EOI requirement for coverage elected within 31 days. |
| TS_EOI_FOR_1_BENE_LVL_SDLS | EOI requirement when selecting first benefit level. |
| TS_EOI_FOR_INCR_COV_SDLS | EOI required for increased coverage amounts. |
| TS_EOI_NEW_HIRE_OVER_GI_SDLS | EOI required for new hires electing over Guaranteed Issue limits. |
| TS_EOI_REQ_IF_ELECT_COV_OESDL | EOI required when electing coverage during Open Enrollment. |
| TS_EOI_REQ_NEWLY_ELIG_EE_SDLS | EOI required for newly eligible employees. |
| TS_OTHER_EOI_SDLS | Other Evidence of Insurability requirements. |

## Benefit Levels & Guaranteed Issue

| Field Name | Description |
|------------|-------------|
| TS_1_BENE_LEVEL_EQUALS_SDLS | Indicates Level 1 benefit equals standard coverage level. |
| TS_GUARANTEED_ISSUE_LIMITS__N | Guaranteed Issue coverage limits. |
| TS_GUAR_ISSUE_AMT_BL | Guaranteed Issue amount for Benefit Level coverage. |

## Accidental Death & Dismemberment (ADD)

| Field Name | Description |
|------------|-------------|
| TS_COMMENTS_BADD | Comments related to Basic AD&D coverage. |
| TS_COMMENTS_DADD | Comments related to Dependent AD&D coverage. |
| TS_COMMENTS_SADD | Comments related to Supplemental AD&D coverage. |
| TS_COMMENTS_SDADD | Comments related to Supplemental Dependent AD&D coverage. |

## Life Insurance

| Field Name | Description |
|------------|-------------|
| TS_COMMENTS_BL | Comments related to Basic Life coverage. |
| TS_COMMENTS_DL | Comments related to Dependent Life coverage. |
| TS_COMMENTS_GI | Comments related to Guaranteed Issue provisions. |
| TS_IS_SUPP_SPOUSE_DL_AMT_LIM | Indicates whether supplemental spouse dependent life amount limits apply. |
