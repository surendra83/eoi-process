# ULD_ELIGIBILITY Field Dictionary

## Primary Identifiers

| Field Name | Description |
|------------|-------------|
| TS_ID | Unique identifier for the eligibility record. |
| TS_UUID | Universally Unique Identifier (UUID) for the record. |
| TS_ISSUEID | Identifier of the related issue, ticket, or workflow. |

## General Information

| Field Name | Description |
|------------|-------------|
| TS_TITLE | Title or name of the eligibility configuration/case. |
| TS_LINK_TO_SOLD_CASE | Reference or link to the related sold case. |
| TS_ASSOCIATED_PRODUCTS | Products associated with the eligibility rule. |
| TS_COVEARAGE_EXPCEPTIONS | Coverage exceptions or exclusions. |
| TS_COMMENTS | General comments or notes. |

## Eligibility Rules

| Field Name | Description |
|------------|-------------|
| TS_ASSOCIATED_ELIGIBILITY | Eligibility criteria associated with the policy or product. |
| TS_ELIGIBILITY_VERIFICATION | Process or requirement for eligibility verification. |
| TS_FT_EMPLOYEE_EFFECT | Impact of full-time employee status on eligibility. |
| TS_PT_EE_COVERED | Indicates whether part-time employees are covered. |
| TS_FULL_TIME_HOURS_PER_WEEK | Hours required per week for full-time status. |
| TS_PART_TIME_HOURS | Hours used to define part-time status. |
| TS_RETIREES_COVERED | Indicates whether retirees are covered. |
| TS_REHIRE_PROVISION | Rehire eligibility provision. |
| TS_EXPLAIN_REHIRE_PROVISION | Details of the rehire provision. |
| TS_TERMINATION_DATE | Termination-related eligibility condition or effective date. |
| TS_EXPLAIN_TERMINATION_DATE | Explanation of termination rules. |

## Coverage and Benefit Rules

| Field Name | Description |
|------------|-------------|
| TS_LIFE_NONMED_LOA | Life insurance eligibility during non-medical leave of absence (LOA). |
| TS_STD_LTD_NONMED_LOA | STD/LTD eligibility during non-medical LOA. |
| TS_EXP_LIFE_NONMED | Explanation of life insurance non-medical LOA rules. |
| TS_EXP_STD_LTD_NOMED | Explanation of STD/LTD non-medical LOA rules. |
| TS_CI_NONMED_REAS_LOA | Critical illness eligibility during non-medical LOA. |
| TS_EXPLAIN_CI_NOMED | Explanation of critical illness non-medical LOA rules. |
| TS_ACC_NON_MEDICAL_LOA_OR_LAY | Accident coverage during non-medical LOA or layoff. |
| TS_EXPLAIN_OTHER_ACCIDENT | Additional accident coverage details. |
| TS_HIPP_NON_MED_LOA_LAYOFF | HIPP eligibility during non-medical LOA or layoff. |
| TS_EXPLAIN_OTHER_HIPP | Explanation of HIPP eligibility exceptions. |
| TS_SUPP_HEALTH_COMBO_NON_MEDI | Supplemental health combo eligibility during non-medical leave. |
| TS_EXPLAIN_OTHER_SHC | Explanation of supplemental health coverage rules. |
| TS_EXPLAIN_OTHER_HIP | Explanation of hospital indemnity plan exceptions. |
| TS_EXPLAIN_OTHER_SHC_ | Additional supplemental health coverage notes. |
| TS_STATE_PAID_LEAVE_NON_MEDIC | State paid leave eligibility during non-medical leave. |
| TS_EXPLAIN_OTHER_SPL | Explanation of state paid leave exceptions. |

## Design and Configuration

| Field Name | Description |
|------------|-------------|
| TS_WP_DESIGN | Work package design classification. |
| TS_WP_PREFIX | Work package prefix or category code. |
| TS_WP_DESCRIPTION | Description of the work package design. |
| TS_NON_STANDARD_DESIGN_DETAIL | Details of non-standard design configuration. |
| TS_NON_STANDARD_DETAIL | Additional non-standard eligibility details. |

## Audit Fields

| Field Name | Description |
|------------|-------------|
| TS_SUBMITDATE | Date the record was submitted. |
| TS_SUBMITTER | User who submitted the record. |
| TS_ACTIVEINACTIVE | Active or inactive status indicator. |
| TS_LASTMODIFIEDDATE | Date the record was last modified. |
| TS_LASTMODIFIER | User who last modified the record. |
