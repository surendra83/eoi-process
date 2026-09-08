# Data Dictionary for TS Fields

Below is a categorized data dictionary for the fields provided. Descriptions are inferred from common insurance, subgroup, broker, and underwriting data naming conventions.

# 1. Primary Record Information

| Field Name | Description |
|------------|-------------|
| TS_ID | Unique system-generated record identifier. |
| TS_UUID | Universally Unique Identifier (UUID) for the record. |
| TS_ISSUEID | Associated issue, ticket, or workflow identifier. |
| TS_TITLE | Title or name of the subgroup record/request. |
| TS_LINK_TO_SOLD_CASE | Reference to related sold case or opportunity. |

---

# 2. Subgroup Information

| Field Name | Description |
|------------|-------------|
| TS_ASSOCIATED_SUBGROUPS | Related subgroup identifiers or names. |
| TS_SUBGROUP_NAME | Name of the subgroup. |
| TS_SUBGROUP_NUMBER | Unique subgroup number or code. |
| TS_SUBGROUP_PURPOSE | Business purpose or reason for subgroup creation. |
| TS_SUBGROUP_TAXID | Tax identification number assigned to the subgroup. |
| TS_COMMENTS_SUBGROUP | Additional comments or notes regarding the subgroup. |
| TS_ACTIVEINACTIVE | Indicates whether the subgroup is active or inactive. |

---

# 3. Contact Information (Contact 1)

| Field Name | Description |
|------------|-------------|
| TS_NAME_CON1 | Name of Contact 1. |
| TS_TITLE_CON1 | Job title of Contact 1. |
| TS_TYPE_CON1 | Contact role/type (e.g., HR, Benefits Admin). |
| TS_COMPANY_NAME_CON1 | Company name associated with Contact 1. |
| TS_ADDRESS_CON1 | Address of Contact 1. |
| TS_CSZ_CON1 | City, State, Zip information for Contact 1. |
| TS_PHONE_CON1 | Phone number of Contact 1. |
| TS_FAX_CON1 | Fax number of Contact 1. |
| TS_EMAIL_CON1 | Email address of Contact 1. |

---

# 4. Contact Information (Contact 2)

| Field Name | Description |
|------------|-------------|
| TS_NAME_CON2 | Name of Contact 2. |
| TS_TITLE_CON2 | Job title of Contact 2. |
| TS_TYPE_CON2 | Contact role/type. |
| TS_COMPANY_NAME_CON2 | Company name associated with Contact 2. |
| TS_ADDRESS_CON2 | Address of Contact 2. |
| TS_CSZ_CON2 | City, State, Zip information for Contact 2. |
| TS_PHONE_CON2 | Phone number of Contact 2. |
| TS_FAX_CON2 | Fax number of Contact 2. |
| TS_EMAIL_CON2 | Email address of Contact 2. |
| TS_CONTACT_2_ADDRESS | Additional address information for Contact 2. |

---

# 5. Tax and Compliance Information

| Field Name | Description |
|------------|-------------|
| TS_TAXID | Employer or group Tax Identification Number (TIN). |
| TS_CHECK_TYPE_S_OF_CONTACT_S_ | Contact validation/check type performed on contacts. |

---

# 6. Important Business Dates

| Field Name | Description |
|------------|-------------|
| TS_EFFECTIVE_DATE | Date when coverage or subgroup becomes effective. |
| TS_TERMINATION_DATE | Date when subgroup or coverage terminates. |
| TS_REINSTATEMENT_DATE | Date subgroup or coverage is reinstated. |
| TS_SUBMITDATE | Record submission date. |
| TS_LASTMODIFIEDDATE | Last update timestamp. |

---

# 7. Audit and Workflow Fields

| Field Name | Description |
|------------|-------------|
| TS_SUBMITTER | User who submitted the request. |
| TS_LASTMODIFIER | User who last modified the record. |

---

# 8. Umbrella Group Information (UMB)

| Field Name | Description |
|------------|-------------|
| TS_IS_SBGRP_PART_UMBRELLA | Indicates whether subgroup belongs to an umbrella group. |
| TS_SITUS_STATE_UMB | Situs (governing) state for the umbrella group. |
| TS_POLICY_ANNIV_RENEWAL_UMB | Policy anniversary or renewal date. |
| TS_SIC_CODE_UMB | Standard Industrial Classification (SIC) code. |
| TS_NO_OF_ELIGIBLE_EES_UMB | Number of eligible employees. |
| TS_UNDERWRITING_COMPANY_UMB | Underwriting company providing coverage. |
| TS_PRODUCTS_SOLD_UMB | Products sold under the umbrella account. |
| TS_SALES_REGION_UMB | Sales region responsible for the group. |

---

# 9. eAdmin User Information

| Field Name | Description |
|------------|-------------|
| TS_EADMIN_USER_NAME_UMB | eAdmin system user name. |
| TS_EADMIN_USER_PHONE_NO_UMB | eAdmin user phone number. |
| TS_EADMIN_USER_EMAIL_UMB | eAdmin user email address. |

---

# 10. Sales Representative Information

| Field Name | Description |
|------------|-------------|
| TS_SALES_REP_1_NAME_UMB | Name of Sales Representative 1. |
| TS_SALES_REP_1_TYPE_UMB | Type/classification of Sales Rep 1. |
| TS_SALES_REP_1_OFF_STATE_UMB | Office state of Sales Rep 1. |
| TS_SALES_REP_1_EE_ID_UMB | Employee ID of Sales Rep 1. |
| TS_SALES_REP_2_NAME_UMB | Name of Sales Representative 2. |
| TS_SALES_REP_2_TYPE_UMB | Type/classification of Sales Rep 2. |
| TS_SALES_REP_2_OFF_STATE_UMB | Office state of Sales Rep 2. |
| TS_SALES_REP_2_EE_ID_UMB | Employee ID of Sales Rep 2. |

---

# 11. Health Plan and Coverage Attributes

| Field Name | Description |
|------------|-------------|
| TS_UHG_FI_SPND_HEALTH_PL_UMB | Indicates UHG fully insured sponsored health plan participation. |
| TS_UHG_SELF_INSRD_SPNSD_UMB | Indicates UHG self-insured sponsored plan participation. |
| TS_PCHSD_OHCS_W_OHBS_BS_UMB | Purchased OHCS with OHBS benefit solution indicator. |
| TS_PCHSD_OHCS_CARE_SOL_UMB | Purchased OHCS care solution indicator. |
| TS_MEDICAL_PLATFORM_UMB | Medical platform or administration platform used. |

---

# 12. Broker Information

| Field Name | Description |
|------------|-------------|
| TS_BROKER_NAME_UMB | Broker name. |
| TS_COMMISSIONS_PAYABLE_TO_UMB | Entity receiving broker commissions. |
| TS_BROKER_ADDRESS_UMB | Broker address. |
| TS_BROKER_CITY_STATE_ZIP_UMB | Broker city, state, and ZIP code. |
| TS_BROKER_EMAIL_UMB | Broker email address. |
| TS_BROKER_PHONE_UMB | Broker phone number. |
| TS_BROKER_FAX_UMB | Broker fax number. |
| TS_BROKER_PRODUCER_ID_UMB | Broker producer/license identifier. |
| TS_BROKER_SSN_UMB | Broker Social Security Number (sensitive data). |

---

# 13. Commission Information

| Field Name | Description |
|------------|-------------|
| TS_CRITICAL_ILLNESS_COMM_UMB | Critical illness product commission information. |
| TS_EXPLAIN_CI_COMM_UMB | Explanation/details for critical illness commission. |
| TS_ACCIDENT_COMMISSIONS_UMB | Accident insurance commission information. |
| TS_EXPLAIN_ACCIDENT_COMM_UMB | Explanation/details for accident commission. |

---

# 14. Agency Information

| Field Name | Description |
|------------|-------------|
| TS_AGENCY_NAME_UMB | Agency name. |
| TS_AGENCY_ADDRESS_UMB | Agency address. |
| TS_AGENCY_ADDRESS_SAA_UMB | Secondary or special agency address. |
| TS_AGENCY_CITY_STATE_ZIP_UMB | Agency city, state, and ZIP code. |
| TS_AGENCY_PHONE_UMB | Agency phone number. |
| TS_AGENCY_FAX_UMB | Agency fax number. |
| TS_AGENCY_PRODUCER_ID_UMB | Agency producer/license identifier. |
| TS_AGENCY_TAX_ID_NO_UMB | Agency Tax Identification Number. |

---

## Summary by Category

| Category | Fields Count |
|-----------|-------------|
| Primary Record Information | 5 |
| Subgroup Information | 7 |
| Contact Information | 19 |
| Tax & Compliance | 2 |
| Business Dates | 5 |
| Audit Information | 2 |
| Umbrella Group Information | 8 |
| eAdmin User Information | 3 |
| Sales Representative Information | 8 |
| Health Plan & Coverage | 5 |
| Broker Information | 9 |
| Commission Information | 4 |
| Agency Information | 8 |
