# ULD_LIFE_DI Table Field Dictionary

## 1. Key / System Fields

| Field | Description |
|---------|-------------|
| TS_ID | Unique record identifier |
| TS_UUID | Universally unique identifier |
| TS_ISSUEID | Workflow/Issue tracking ID |
| TS_PROJECTID | Related project ID |
| TS_OWNER | Record owner |
| TS_STATE | Workflow status |
| TS_ISSUETYPE | Issue type |
| TS_TITLE | Record title |
| TS_ACTIVEINACTIVE | Active/Inactive status |
| TS_SUBMITDATE | Submission date |
| TS_LASTMODIFIEDDATE | Last modified date |
| TS_LASTMODIFIER | User who last modified |
| TS_CLOSEDATE | Case close date |

## 2. Group / Policy Information
| Field    | Description  |
|----------|--------------|
| TS_GROUP_NAME| Employer group name |
| TS_GROUP_POLICY_NUMBER| Policy number |
| TS_UHC_POLICY_NUMBER| UHC policy number |
| TS_GROUP_EFFECTIVE_DATE| Group effective date |
| TS_GROUP_TERM_DATE| Group termination date |
| TS_GROUP_REINSTATEMENT_DATE| Group reinstatement date |
| TS_SITUS_STATE| Situs state |
| TS_TAXID_NUMBER_GI| Employer Tax ID |
| TS_NUM_OF_EE| Number of employees |
| TS_PLAN_ANNIV_DATE| Plan anniversary date|

## 3. Underwriting Information
| Field    | Description  |
|----------|--------------|
| TS_UNDERWRITER |  Assigned underwriter |
| TS_UNDERWRITING_COMPANY | Underwriting company|
| TS_UW_REGION | Underwriting region |
| TS_GRP_UW_RECEIVED | Group UW received |
| TS_GRP_UW_SUBTASK | UW subtask |
| TS_UW_APPROVAL_REQUIRED | Approval required indicator |

## 4. Account Manager Information
| Field    | Description  |
|----------|--------------|
| TS_ACCT_MGR_NAME|  Account Manager name |
| TS_ACCT_MGR_EMAIL | Account Manager email |
| TS_ACCT_MGR_PHONE | Account Manager phone |
| TS_ACCOUNT_MANAGER | Account manager |

## 5. Coverage/Product Indicators
| Field    | Description  |
|----------|--------------|
| TS_BASIC_LIFE | Basic Life coverage |
| TS_SUPP_LIFE | Supplemental Life |
| TS_DEP_LIFE | Dependent Life |
| TS_BASIC_AD_D| Basic AD&D |
| TS_SUPP_AD_D | Supplemental AD&D |
| TS_ACCIDENT | Accident coverage |
| TS_CRITICAL_ILLNESS | Critical Illness |
| TS_HOSPITAL_INDEMNITY | Hospital Indemnity |
| TS_STD | Short Term Disability |
| TS_LTD | Long Term Disability |
| TS_FMLA_LEAVE_MANAGEMENT | FMLA Management |
| TS_EAP |  Employee Assistance Program |

## 6. Disability Fields

### STD (Short Term Disability)
| Field    | Description  |
|----------|--------------|
| TS_STD_* | STD related attributes |
| TS_STDBU_* | STD Buy-Up attributes
| TS_BENEFIT_PERCENTAGE_STD | STD benefit percentage |
| TS_MAX_WEEK_BENE_STD | Maximum weekly benefit |
| TS_MIN_WEEK_BENE_STD | Minimum weekly benefit |

### LTD (Long Term Disability)
| Field    | Description  |
|----------|--------------|
| TS_LTD_* | LTD related attributes |
| TS_LTDBU_* | LTD Buy-Up attributes |
| TS_BEN_PERCENT_LTD | LTD benefit percentage |
| TS_MAX_MONTH_BEN_LTD | Maximum monthly benefit |
| TS_MIN_MONTH_BEN_LTD | Minimum monthly benefit |

## 7. Life Insurance Products

### BL = Basic Life
### SL = Supplemental Life
### DL = Dependent Life
### SDL = Supplemental Dependent Life

Common fields include Coverage Terms, Guaranteed Issue Amount, Portability, Rate Guarantee, Waiver of Premium and Reduction Schedule.

## 8. AD&D Products

- BADD = Basic AD&D
- SADD = Supplemental AD&D
- DADD = Dependent AD&D
- SDADD = Supplemental Dependent AD&D

Examples:
- TS_COVERAGE_BADD
- TS_SEATBELT_BADD
- TS_EDUCATION_BENFT_BADD
- TS_REPARTRIATION_BENFT_BADD

## 9. Enrollment & EOI

EOI = Evidence of Insurability
| Field    | Description  |
|----------|--------------|
| TS_EOI_* | EOI requirement details |
| TS_EOI_NEW_HIRE_* | New hire EOI rules |
| TS_EOI_COV_31_DAYS_* | Coverage after 31 days |
| TS_EOI_FOR_INCR_COV_* | Increased coverage EOI |

## 10. Portability & Conversion
| Field    | Description  |
|----------|--------------|
| TS_PORTABILITY_* | Portability provisions |
| TS_PORT_BENE_* | Portable benefits |
| TS_PORT_RATES_* | Portability rates |
| TS_CONVERSION_COVERAGE_APPLIE | Conversion coverage indicator |

## 11. Billing Fields

- TS_BILLING
- TS_BILLING_TEMPLATE
- TS_BILLING_SUBTASK
- TS_BILLING_SIGNOFF
- TS_GROUP_BILLING_METHODOLOGY
- TS_PORTABILITY_BILLING

## 12. Contracts Fields

- TS_CONTRACTS
- TS_CONTRACT_SUBTASK
- TS_CONTRACTS_DUE_DATE
- TS_CONTRACTS_RECEIVED_DATE
- TS_CONTRACTS_DRAFTED_DATE
- TS_FINAL_ISSUANCE_OF_CONTRACT

## 13. Change Request Fields

- TS_CHANGE_REQUEST_TYPE
- TS_PRODUCTS_AFFECTED
- TS_ORIGINAL_VALUES
- TS_CHANGED_VALUES
- TS_*_CR fields belong to Change Request process

## 14. EDI & Eligibility Fields

- TS_EDI_* : EDI processing fields
- TS_ELIGIBILITY_* : Eligibility fields
- TS_STRUCTURE_* : Structure build/setup fields
- TS_VENDOR_* : Vendor information

## Common Abbreviations

| Code | Meaning |
|------|---------|
| BL | Basic Life |
| SL | Supplemental Life |
| DL | Dependent Life |
| SDL | Supplemental Dependent Life |
| BADD | Basic AD&D |
| SADD | Supplemental AD&D |
| DADD | Dependent AD&D |
| SDADD | Supplemental Dependent AD&D |
| STD | Short Term Disability |
| STDBU | STD Buy-Up |
| LTD | Long Term Disability |
| LTDBU | LTD Buy-Up |
| GI | Guaranteed Issue |
| EOI | Evidence of Insurability |
| EAP | Employee Assistance Program |
| FMLA | Family Medical Leave Act |
| UHC | UnitedHealthcare |
| ASO | Administrative Services Only |
