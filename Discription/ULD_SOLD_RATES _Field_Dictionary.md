# ULD_SOLD_RATES Field Dictionary

---

# 1. System & Audit Fields

| Field Name | Data Description |
|------------|------------------|
| TS_ID | Unique system-generated identifier for the Sold Rates record. |
| TS_UUID | Globally unique identifier (UUID) used to uniquely identify the record across systems. |
| TS_ISSUEID | Workflow, ticket, or issue tracking identifier associated with the record. |
| TS_SUBMITDATE | Date and time the Sold Rates record was submitted. |
| TS_SUBMITTER | User ID or name of the person who submitted the record. |
| TS_LASTMODIFIEDDATE | Date and time the record was last updated. |
| TS_LASTMODIFIER | User ID or name of the person who last modified the record. |
| TS_ACTIVEINACTIVE | Indicates whether the record is currently Active or Inactive. |
| TS_OHID | Internal organizational or operational identifier used by the application. |

---

# 2. Contact & Broker Information

| Field Name | Data Description |
|------------|------------------|
| TS_NAME | Primary contact or business name associated with the record. |
| TS_TITLE | Professional title or designation of the contact. |
| TS_CONTACT_TYPE | Classification of contact (Broker, Agency, Sales Representative, General Agent, etc.). |
| TS_ASSOCIATED_CONTACTS | Related contacts linked to the Sold Rates record. |
| TS_BROKER_IDENTIFIER | Unique identifier assigned to the broker. |
| TS_BROKER_SSN | Broker Social Security Number used for tax and commission processing. |
| TS_BROKER_PRODUCER_ID | State-issued Producer License ID of the broker. |
| TS_NAME_BROKER | Full legal name of the broker. |
| TS_BROKER_EMAIL | Email address of the broker. |
| TS_BROKER_PHONE | Phone number of the broker. |
| TS_EMAIL | Primary email address for communications. |
| TS_PHONE | Primary contact phone number. |
| TS_FAX | Primary contact fax number. |
| TS_ADDRESS | Primary mailing/business address. |
| TS_CSZ_CONTACT | Contact City, State, and Zip Code information. |

---

# 3. Day-to-Day Contact Information

| Field Name | Data Description |
|------------|------------------|
| TS_NAME_DTD | Name of the designated day-to-day contact. |
| TS_ADDRESS_DTD | Address of the day-to-day contact. |
| TS_CSZ_DTD | City, State, and Zip Code of the day-to-day contact. |
| TS_EMAIL_DTD | Email address of the day-to-day contact. |
| TS_PHONE_DTD | Phone number of the day-to-day contact. |
| TS_FAX_DTD | Fax number of the day-to-day contact. |
| TS_DAY_TO_DAY_CONTACT_ADDRESS | Complete mailing address of the day-to-day contact. |

---

# 4. Agency Information

| Field Name | Data Description |
|------------|------------------|
| TS_NAME_AFF_AGENCY | Name of the affiliated agency. |
| TS_ADDRESS_AFF_AGENT | Address of the affiliated agency. |
| TS_CSZ_AFF_AGENCY | City, State, and Zip Code of the affiliated agency. |
| TS_PHONE_AFF_AGENCY | Agency contact phone number. |
| TS_FAX_AFF_AGENCY | Agency fax number. |
| TS_TAXID_AFF_AGENCY | Federal Tax Identification Number (TIN) of the agency. |
| TS_AGENCY_ADDRESS | Full agency address. |
| TS_AGENCY_PRODUCER_ID | Producer license identifier assigned to the agency. |

---

# 5. Sales Representative Information

| Field Name | Data Description |
|------------|------------------|
| TS_NAME_SALES_REP | Full name of the primary sales representative. |
| TS_EMPLOYEE_ID_SALES | Employee identifier of the sales representative. |
| TS_TYPE_SALES | Type or role of sales representative. |
| TS_SALES_OFFICE_STATE | State where the sales office is located. |
| TS_SALES_REP_2_TYPE | Role of secondary sales representative. |
| TS_SALES_REP_2_NAME | Name of secondary sales representative. |
| TS_SALES_REP_2_EMPLOYEE_ID | Employee ID of secondary sales representative. |
| TS_SALES_REP_2_OFFICE_STATE | Office state of secondary sales representative. |
| TS_SALES_REP_2_PACIFICARE_RNW | Indicates secondary sales representative responsibility for Pacificare renewals. |

---

# 6. General Agent Information

| Field Name | Data Description |
|------------|------------------|
| TS_GENERAL_AGENT | Indicator or identifier for the assigned General Agent. |
| TS_NAME_GENERAL_AGENT | Name of the General Agent. |
| TS_PHONE_GENERAL_AGENT | General Agent phone number. |
| TS_FAX_GENERAL_AGENT | General Agent fax number. |
| TS_ADDRESS_GENERAL_AGENT | General Agent business address. |
| TS_CITY_STATE_ZIP_GEN_AGENT | City, State, and Zip Code of the General Agent. |
| TS_TAX_ID_GENERAL_AGENT | Tax Identification Number of the General Agent. |
| TS_GENERAL_AGENT_PLATFORM | Platform or business channel through which the General Agent operates. |
| TS_GENERAL_AGENT_COMM_PERCENT | Commission percentage allocated to the General Agent. |
| TS_GENERAL_AGENT_PRODUCER_ID | Producer License ID of the General Agent. |

---

# 7. Sold Case & Business Information

| Field Name | Data Description |
|------------|------------------|
| TS_LINK_TO_SOLD_CASE | Reference link or identifier associated with the Sold Case record. |
| TS_EFFECTIVE_DATE | Effective date of coverage, commission arrangement, or sold case. |
| TS_TERMINATION_DATE | Termination or expiration date of coverage or business arrangement. |
| TS_COMMENTS | General notes, remarks, or business comments. |

---

# 8. Commission & Compensation Information

| Field Name | Data Description |
|------------|------------------|
| TS_COMM_CI | Commission percentage for Critical Illness products. |
| TS_COMM_LIFE | Commission percentage for Life Insurance products. |
| TS_COMM_LTD | Commission percentage for Long-Term Disability products. |
| TS_COMM_STD | Commission percentage for Short-Term Disability products. |
| TS_COMM_UHA | Commission percentage for UHA products. |
| TS_ACCIDENT_COMM | Commission percentage for Accident Insurance products. |
| TS_HOSPITAL_INDEMNITY | Commission percentage for Hospital Indemnity products. |
| TS_SUPP_HEALTH_COMBO | Commission percentage for Supplemental Health products. |
| TS_STATE_PAID_LEAVE | Commission percentage associated with State Paid Leave products. |
| TS_FMLA_LEAVE_MGMT_COMM | Commission percentage for FMLA Leave Management services. |
| TS_EXP_CI_COMM | Detailed explanation regarding Critical Illness commission structure. |
| TS_EXP_LIFE_COMM | Detailed explanation regarding Life commission structure. |
| TS_EXP_LTD_COMM | Detailed explanation regarding LTD commission structure. |
| TS_EXP_STD_COMM | Detailed explanation regarding STD commission structure. |
| TS_EXPLAIN_UHA_COMM | Explanation of UHA-related commission arrangement. |
| TS_EXPLAIN_ACCIDENT_COMMISS | Explanation of Accident product commission arrangement. |
| TS_EXPL_HOSP_INDEMNITY_COMM | Explanation of Hospital Indemnity commission arrangement. |
| TS_EXPLAIN_SUPP_HEALTH_COMBO_ | Explanation of Supplemental Health commission arrangement. |
| TS_EXPLAIN_STATE_PAID_LEAVE_C | Explanation of State Paid Leave commission arrangement. |
| TS_EXPLAIN_FLMA_LEA_MGMT_COMM | Explanation of FMLA Leave Management commission arrangement. |
| TS_COMMISSIONS_PAYABLE_TO | Entity or individual to whom commissions are paid. |
| TS_COMMISSIONS_SPLIT | Percentage split of commissions between parties. |
| TS_EXPLAIN_COMMISSIONS_SPLIT | Explanation supporting commission split arrangement. |

---

# 9. Renewal & Product Management

| Field Name | Data Description |
|------------|------------------|
| TS_PACIFICARE_RENEWAL | Indicates responsibility for Pacificare renewal business. |
| TS_REPORTS_NEEDED_FOR_PRODUCT | Product-specific reporting requirements. |
| TS_LIST_STATES_WITH_STATE_PAI | List of states where State Paid Leave coverage or commissions apply. |

---

# 10. eAdministration & Access Control

| Field Name | Data Description |
|------------|------------------|
| TS_GROUP_ACCESS_LEVEL__CHOOSE | Security or access level assigned to the group. |
| TS_FOR_SUBGROUP_LEVEL_USERS_E | Access configuration applicable to subgroup-level users. |
| TS_EADMINISTRATION_OPTIONS__C | Electronic administration options enabled for the account or product. |

---

# 11. Insurance Product Report Requirements

## Life & Disability Reports

| Field Name | Data Description |
|------------|------------------|
| TS_LIFE_AD_D_REPORT_LIST | Reporting requirements for Life and AD&D products. |
| TS_FULLY_INSURED_LONG_TERM_DI | Reporting option for Fully Insured Long-Term Disability coverage. |
| TS_FULLY_INSURED_SHORT_TERM_D | Reporting option for Fully Insured Short-Term Disability coverage. |
| TS_SELF_INSURED_LONG_TERM_DIS | Reporting option for Self-Insured Long-Term Disability coverage. |
| TS_SELF_INSURED_SHORT_TERM_DI | Reporting option for Self-Insured Short-Term Disability coverage. |

---

## Evidence of Insurability

| Field Name | Data Description |
|------------|------------------|
| TS_EVIDENCE_OF_INSUR_WITH_SSN | Indicates Evidence of Insurability process requiring SSN information. |
| TS_EVIDENCE_OF_INSUR_WOUT_SSN | Indicates Evidence of Insurability process without SSN information. |

---

## Product-Specific Reports

| Field Name | Data Description |
|------------|------------------|
| TS_CRITICAL_ILLNESS_REPORT_SU | Reporting setup or requirements for Critical Illness products. |
| TS_ACCIDENT_PROTECTION_REPORT | Reporting setup or requirements for Accident Protection products. |

---
# Recommended Business Fields for Reporting

## 1. Broker & Agency
- TS_NAME_BROKER
- TS_BROKER_IDENTIFIER
- TS_BROKER_PRODUCER_ID
- TS_NAME_AFF_AGENCY
- TS_AGENCY_PRODUCER_ID

## 2. Sales Ownership
- TS_NAME_SALES_REP
- TS_EMPLOYEE_ID_SALES
- TS_SALES_OFFICE_STATE
- TS_NAME_GENERAL_AGENT
- Sold Case Tracking
- TS_LINK_TO_SOLD_CASE
- TS_EFFECTIVE_DATE
- TS_TERMINATION_DATE
- TS_ACTIVEINACTIVE

## 3. Commission Management
- TS_COMM_LIFE
- TS_COMM_LTD
- TS_COMM_STD
- TS_COMM_CI
- TS_ACCIDENT_COMM
- TS_COMMISSIONS_PAYABLE_TO
- TS_COMMISSIONS_SPLIT

## 4. Compliance & Administration
- TS_GROUP_ACCESS_LEVEL__CHOOSE
- TS_EADMINISTRATION_OPTIONS__C
- TS_REPORTS_NEEDED_FOR_PRODUCT
