# ULD_Contact Table – Field Descriptions

## 1. Record Identification Fields

| Field | Description |
|---------|-------------|
| TS_ID | Unique record identifier for the contact. |
| TS_UUID | Universally unique identifier (UUID) for the contact record. |
| TS_ISSUEID | Workflow or issue tracking identifier. |
| TS_OHID | Organizational hierarchy or system-specific identifier. |

## 2. Contact Information Fields

| Field | Description |
|---------|-------------|
| TS_NAME | Contact name. |
| TS_TITLE | Contact title or designation. |
| TS_CONTACT_TYPE | Type of contact (Broker, Agency, Sales Rep, General Agent, etc.). |
| TS_PHONE | Primary phone number. |
| TS_EMAIL | Primary email address. |
| TS_FAX | Primary fax number. |
| TS_ADDRESS | Primary mailing address. |
| TS_CSZ_CONTACT | City, State, and ZIP code of contact. |
| TS_COMMENTS | General comments or notes. |
| TS_ASSOCIATED_CONTACTS | Related contacts associated with this record. |
| TS_LINK_TO_SOLD_CASE | Link/reference to sold insurance case. |

## 3. Day-to-Day Contact Fields

| Field | Description |
|---------|-------------|
| TS_NAME_DTD | Day-to-day contact name. |
| TS_ADDRESS_DTD | Day-to-day contact address. |
| TS_DAY_TO_DAY_CONTACT_ADDRESS | Complete address of day-to-day contact. |
| TS_PHONE_DTD | Day-to-day contact phone number. |
| TS_EMAIL_DTD | Day-to-day contact email address. |
| TS_FAX_DTD | Day-to-day contact fax number. |
| TS_CSZ_DTD | City, State, ZIP of day-to-day contact. |

## 4. Broker Information Fields

| Field | Description |
|---------|-------------|
| TS_NAME_BROKER | Broker name. |
| TS_BROKER_IDENTIFIER | Unique broker identifier. |
| TS_BROKER_SSN | Broker Social Security Number. |
| TS_BROKER_PRODUCER_ID | Broker producer license ID. |
| TS_BROKER_EMAIL | Broker email address. |
| TS_BROKER_PHONE | Broker phone number. |

## 5. Agency Information Fields

| Field | Description |
|---------|-------------|
| TS_NAME_AFF_AGENCY | Affiliated agency name. |
| TS_ADDRESS_AFF_AGENT | Affiliated agency/agent address. |
| TS_AGENCY_ADDRESS | Agency address. |
| TS_PHONE_AFF_AGENCY | Agency phone number. |
| TS_FAX_AFF_AGENCY | Agency fax number. |
| TS_TAXID_AFF_AGENCY | Agency tax identification number. |
| TS_CSZ_AFF_AGENCY | City, State, ZIP of affiliated agency. |
| TS_AGENCY_PRODUCER_ID | Agency producer ID. |

## 6. Sales Representative Fields

| Field | Description |
|---------|-------------|
| TS_NAME_SALES_REP | Primary sales representative name. |
| TS_EMPLOYEE_ID_SALES | Sales representative employee ID. |
| TS_TYPE_SALES | Sales representative type/classification. |
| TS_SALES_OFFICE_STATE | Sales office state. |
| TS_PACIFICARE_RENEWAL | PacifiCare renewal indicator. |
| TS_SALES_REP_2_TYPE | Secondary sales representative type. |
| TS_SALES_REP_2_NAME | Secondary sales representative name. |
| TS_SALES_REP_2_EMPLOYEE_ID | Secondary sales representative employee ID. |
| TS_SALES_REP_2_OFFICE_STATE | Secondary sales representative office state. |
| TS_SALES_REP_2_PACIFICARE_RNW | Secondary sales representative PacifiCare renewal flag. |

## 7. General Agent Fields

| Field | Description |
|---------|-------------|
| TS_GENERAL_AGENT | General agent indicator/reference. |
| TS_NAME_GENERAL_AGENT | General agent name. |
| TS_PHONE_GENERAL_AGENT | General agent phone number. |
| TS_TAX_ID_GENERAL_AGENT | General agent tax ID. |
| TS_ADDRESS_GENERAL_AGENT | General agent address. |
| TS_CITY_STATE_ZIP_GEN_AGENT | General agent city, state, ZIP. |
| TS_FAX_GENERAL_AGENT | General agent fax number. |
| TS_GENERAL_AGENT_PLATFORM | General agent platform/system. |
| TS_GENERAL_AGENT_PRODUCER_ID | General agent producer ID. |
| TS_GENERAL_AGENT_COMM_PERCENT | General agent commission percentage. |

## 8. Commission Fields

| Field | Description |
|---------|-------------|
| TS_COMM_LIFE | Life Insurance commission percentage. |
| TS_COMM_LTD | Long-Term Disability commission percentage. |
| TS_COMM_STD | Short-Term Disability commission percentage. |
| TS_COMM_CI | Critical Illness commission percentage. |
| TS_COMM_UHA | UHA commission percentage. |
| TS_ACCIDENT_COMM | Accident product commission percentage. |
| TS_FMLA_LEAVE_MGMT_COMM | FMLA Leave Management commission. |
| TS_COMMISSIONS_SPLIT | Commission split percentage. |
| TS_COMMISSIONS_PAYABLE_TO | Person/entity receiving commissions. |
| TS_EXP_LIFE_COMM | Explanation of Life commission. |
| TS_EXP_LTD_COMM | Explanation of LTD commission. |
| TS_EXP_STD_COMM | Explanation of STD commission. |
| TS_EXP_CI_COMM | Explanation of Critical Illness commission. |
| TS_EXPLAIN_UHA_COMM | Explanation of UHA commission. |
| TS_EXPLAIN_COMMISSIONS_SPLIT | Details of commission split arrangement. |
| TS_EXPLAIN_FLMA_LEA_MGMT_COMM | Explanation of FMLA commission. |
| TS_EXPLAIN_ACCIDENT_COMMISS | Explanation of Accident commission. |
| TS_EXPL_HOSP_INDEMNITY_COMM | Explanation of Hospital Indemnity commission. |
| TS_EXPLAIN_SUPP_HEALTH_COMBO_ | Explanation of Supplemental Health Combo commission. |
| TS_EXPLAIN_STATE_PAID_LEAVE_C | Explanation of State Paid Leave commission. |

## 9. Product & Report Configuration Fields

| Field | Description |
|---------|-------------|
| TS_REPORTS_NEEDED_FOR_PRODUCT | Reports required for products. |
| TS_LIFE_AD_D_REPORT_LIST | Life and AD&D report list. |
| TS_EVIDENCE_OF_INSUR_WOUT_SSN | Evidence of Insurability report without SSN. |
| TS_EVIDENCE_OF_INSUR_WITH_SSN | Evidence of Insurability report with SSN. |
| TS_FULLY_INSURED_LONG_TERM_DI | Fully Insured Long-Term Disability option. |
| TS_FULLY_INSURED_SHORT_TERM_D | Fully Insured Short-Term Disability option. |
| TS_SELF_INSURED_LONG_TERM_DIS | Self-Insured Long-Term Disability option. |
| TS_SELF_INSURED_SHORT_TERM_DI | Self-Insured Short-Term Disability option. |
| TS_CRITICAL_ILLNESS_REPORT_SU | Critical Illness reporting option. |
| TS_ACCIDENT_PROTECTION_REPORT | Accident Protection report option. |
| TS_HOSPITAL_INDEMNITY | Hospital Indemnity product option. |
| TS_SUPP_HEALTH_COMBO | Supplemental Health Combo product option. |
| TS_STATE_PAID_LEAVE | State Paid Leave product option. |
| TS_LIST_STATES_WITH_STATE_PAI | List of states supporting State Paid Leave. |

## 10. Access & Administration Fields

| Field | Description |
|---------|-------------|
| TS_GROUP_ACCESS_LEVEL__CHOOSE | Group access level selected. |
| TS_FOR_SUBGROUP_LEVEL_USERS_E | Subgroup level user permissions. |
| TS_EADMINISTRATION_OPTIONS__C | eAdministration configuration options. |

## 11. Lifecycle & Audit Fields

| Field | Description |
|---------|-------------|
| TS_EFFECTIVE_DATE | Record effective date. |
| TS_TERMINATION_DATE | Record termination date. |
| TS_SUBMITDATE | Date record was submitted. |
| TS_SUBMITTER | User who submitted the record. |
| TS_ACTIVEINACTIVE | Active/Inactive status of the record. |
| TS_LASTMODIFIEDDATE | Last modification date. |
| TS_LASTMODIFIER | User who last modified the record. |
