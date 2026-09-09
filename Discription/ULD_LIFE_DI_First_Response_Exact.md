# ULD_LIFE_DI Data Dictionary (Categorized Overview)

The **ULD_LIFE_DI** table appears to be a **Life & Disability Insurance Implementation / Case Setup data model** containing policy, underwriting, billing, enrollment, EDI, contract, and product configuration information.

Since there are more than 1,000 fields, the best approach is to **segregate them into logical business domains** and provide field descriptions based on the naming convention.

# 1. Case Management & Workflow Fields

| Field | Description |
|---------|-------------|
| TS_ID | Unique record identifier |
| TS_UUID | Universally unique identifier |
| TS_ISSUEID | Issue/Ticket ID |
| TS_TITLE | Case title |
| TS_OWNER | Current owner of case |
| TS_STATE | Current workflow state |
| TS_ISSUETYPE | Type of issue/case |
| TS_ACTIVEINACTIVE | Active/Inactive status |
| TS_PROJECTID | Associated project |
| TS_SUBMITDATE | Date submitted |
| TS_LASTMODIFIEDDATE | Last updated date |
| TS_LASTSTATECHANGEDATE | Date state changed |
| TS_LASTSTATECHANGER | User who changed state |
| TS_LASTMODIFIER | Last user who modified record |

# 2. Sold Case Administration

| Field | Description |
|---------|-------------|
| TS_UNDERWRITER | Assigned underwriter |
| TS_CASE_SETUP | Case setup owner |
| TS_SUBMITTER | Person submitting case |
| TS_IMPL_MGR | Implementation Manager |
| TS_VOLUNTARY_IMPL_MGR | Voluntary Product Implementation Manager |
| TS_GENERALIST | Assigned Case Generalist |
| TS_ACCOUNT_MANAGER | Account Manager |
| TS_ACCT_MGR_NAME | Account Manager Name |
| TS_ACCT_MGR_EMAIL | Account Manager Email |
| TS_ACCT_MGR_PHONE | Account Manager Phone |

# 3. Group Information

| Field | Description |
|---------|-------------|
| TS_GROUP_NAME | Employer/Group Name |
| TS_GROUP_POLICY_NUMBER | Policy Number |
| TS_UHC_POLICY_NUMBER | UHC Policy Number |
| TS_GROUP_EFFECTIVE_DATE | Policy Effective Date |
| TS_GROUP_TERM_DATE | Group Termination Date |
| TS_GROUP_REINSTATEMENT_DATE | Group Reinstatement Date |
| TS_SITUS_STATE | Situs State |
| TS_TAXID_NUMBER_GI | Group Tax ID |
| TS_NUM_OF_EE | Number of Employees |
| TS_TYPE_OF_BUSINESS | Business Type |
| TS_NATURE_BUSINESS | Nature of Business |
| TS_SIC_CODE | SIC Industry Code |

# 4. Product Indicators

| Field | Description |
|---------|-------------|
| TS_BASIC_LIFE | Basic Life Coverage |
| TS_DEP_LIFE | Dependent Life |
| TS_SUPP_LIFE | Supplemental Life |
| TS_BASIC_AD_D | Basic AD&D |
| TS_SUPP_AD_D | Supplemental AD&D |
| TS_DEP_ADD | Dependent AD&D |
| TS_SUPP_DEP_AD_D | Supplemental Dependent AD&D |
| TS_SUPP_DEP_LIFE | Supplemental Dependent Life |
| TS_LTD | Long Term Disability |
| TS_STD | Short Term Disability |
| TS_ACCIDENT | Accident Product |
| TS_CRITICAL_ILLNESS | Critical Illness |
| TS_EAP | Employee Assistance Program |
| TS_HOSPITAL_INDEMNITY | Hospital Indemnity |
| TS_BENEFIT_ASSIST | Benefit Assist |
| TS_MATERNITY_ASSIST | Maternity Assist |
| TS_FMLA_LEAVE_MANAGEMENT | FMLA Service |

# 5. Coverage Types

| Abbreviation | Meaning |
|-------------|---------|
| BL | Basic Life |
| SL | Supplemental Life |
| DL | Dependent Life |
| SDL | Supplemental Dependent Life |
| BADD | Basic AD&D |
| SADD | Supplemental AD&D |
| DADD | Dependent AD&D |
| SDADD | Supplemental Dependent AD&D |
| LTD | Long Term Disability |
| LTDBU | LTD Buy-Up |
| STD | Short Term Disability |
| STDBU | STD Buy-Up |

# 6. Coverage Configuration Fields

| Field | Description |
|---------|-------------|
| TS_COVERAGE_BADD | Basic AD&D Coverage |
| TS_COVERAGE_SADD | Supplemental AD&D Coverage |
| TS_COVERAGE_SDADD | Supplemental Dependent AD&D Coverage |
| TS_COVERAGE_TERMS_BL | Basic Life Coverage Terms |
| TS_COVERAGE_TERMS_SL | Supplemental Life Coverage Terms |
| TS_COVERAGE_TERMS_BADD | Basic AD&D Coverage Terms |
| TS_COVERAGE_TERMS_SADD | Supplemental AD&D Coverage Terms |

# 7. Effective Dates

| Field | Description |
|---------|-------------|
| TS_EFFECTIVE_DATE_BL | Basic Life Effective Date |
| TS_EFFECTIVE_DATE_SL | Supplemental Life Effective Date |
| TS_EFFECTIVE_DATE_DL | Dependent Life Effective Date |
| TS_EFFECTIVE_DATE_SDL | Supp. Dependent Life Effective Date |
| TS_EFFECTIVE_DATE_STD | STD Effective Date |
| TS_EFFECTIVE_DATE_LTD | LTD Effective Date |
| TS_EFFECTIVE_DATE_BADD | Basic AD&D Effective Date |
| TS_EFFECTIVE_DATE_SADD | Supplemental AD&D Effective Date |
| TS_EFFECTIVE_DATE_DADD | Dependent AD&D Effective Date |
| TS_EFFECTIVE_DATE_SDADD | Supp. Dependent AD&D Effective Date |

# 8. Termination & Reinstatement Dates

| Field | Description |
|---------|-------------|
| TS_TERMINATION_DATE_BL | Basic Life Termination Date |
| TS_TERMINATION_DATE_SL | Supplemental Life Termination Date |
| TS_TERMINATION_DATE_DL | Dependent Life Termination Date |
| TS_TERMINATION_DATE_STD | STD Termination Date |
| TS_TERMINATION_DATE_LTD | LTD Termination Date |
| TS_GROUP_REINSTATE_DATE_STD | STD Reinstatement Date |
| TS_GROUP_REINSTATE_DATE_LTD | LTD Reinstatement Date |

# 9. Disability Plan Design (STD/LTD)

| Field | Description |
|---------|-------------|
| TS_BENEFIT_PERCENTAGE_STD | STD Benefit % |
| TS_BEN_PERCENT_LTD | LTD Benefit % |
| TS_ELIM_PERIOD_LTD | LTD Elimination Period |
| TS_ELIM_PERIOD_LTDBU | LTD Buy-Up Elimination Period |
| TS_ELIM_PERIOD_INJ_STD | STD Injury Elimination Period |
| TS_ELIM_PERIOD_SICK_STD | STD Sickness Elimination Period |
| TS_MAX_BENE_PERIOD_LTD | LTD Maximum Benefit Period |

# 10. Underwriting / Guaranteed Issue Fields

| Field | Description |
|---------|-------------|
| TS_GUARANTEED_ISSUE_LIMITS__N | Guaranteed Issue Limits |
| TS_GUAR_ISSUE_AMT_BL | GI Amount Basic Life |
| TS_GUAR_ISSUE_AMT_SL | GI Amount Supplemental Life |
| TS_EOI_NEW_HIRE_OVER_GI_BL | Evidence of Insurability for New Hires |
| TS_EOI_FOR_INCR_COV_SL | EOI for Increased Coverage |

# 11. Portability & Conversion

| Field | Description |
|---------|-------------|
| TS_PORTABILITY_BL | Basic Life Portability |
| TS_PORTABILITY_SL | Supplemental Life Portability |
| TS_PORTABILITY_SDL | Supplemental Dependent Life Portability |
| TS_PORTABILITY_LTD | LTD Portability |
| TS_PORT_BENE_SL | Portability Benefit |
| TS_PORT_RATES_SL | Portability Rates |

# 12. Open Enrollment Fields

| Field | Description |
|---------|-------------|
| TS_OPEN_ENROLLMENT_OFFERED_SL | Open Enrollment Offered |
| TS_OPEN_ENROLLMENT_OFFERED_BL | Open Enrollment Offered |
| TS_OPEN_ENROLL_INITIAL_SL | Initial Open Enrollment |
| TS_OPEN_ENROLL_ANNIV_SL | Anniversary Open Enrollment |
| TS_OE_TERM_DATE_SL | OE Termination Date |

# 13. Billing Fields

| Field | Description |
|---------|-------------|
| TS_BILLING | Billing Owner |
| TS_BILLING_TEMPLATE | Billing Template |
| TS_BILLING_SUBTASK | Billing Task |
| TS_GROUP_BILLING_METHODOLOGY | Billing Methodology |
| TS_BILLING_SIGNOFF | Billing Signoff |

# 14. Contracts Fields

| Field | Description |
|---------|-------------|
| TS_CONTRACTS | Contracts Owner |
| TS_CONTRACTS_DUE_DATE | Contract Due Date |
| TS_CONTRACTS_RECEIVED_DATE | Contracts Received Date |
| TS_CONTRACTS_SIGNOFF | Contracts Signoff |

# 15. Enrollment & Eligibility

| Field | Description |
|---------|-------------|
| TS_ENROLLMENT | Enrollment Team |
| TS_ENROLLMENT_SUBTASK | Enrollment Subtask |
| TS_ELIGIBILITY_SIGNOFF | Eligibility Signoff |

# 16. EDI Integration Fields

| Field | Description |
|---------|-------------|
| TS_EDI_SUBTASK | EDI Setup Task |
| TS_EDI_EFFECTIVE_DATE | EDI Effective Date |
| TS_VENDOR_PLATFORM | Vendor Platform |
| TS_FILE_PLATFORM | File Platform |
| TS_EDI_COMMENTS | EDI Comments |

# 17. Commissions

| Field | Description |
|---------|-------------|
| TS_COMMISSIONS | Commissions Owner |
| TS_COMMISSIONS_SUBTASK | Commission Task |
| TS_COMMISSIONS_SIGNOFF | Commission Signoff |

# 18. Welcome Letter & Communications

| Field | Description |
|---------|-------------|
| TS_WELCOME_LETTER | Welcome Letter Owner |
| TS_WELCOME_LTR_SUBTASK | Welcome Letter Task |
| TS_WELCOME_LETTER_SIGNOFF | Welcome Letter Approval |
| TS_WELCOME_KIT_SENT_DATE | Welcome Kit Sent Date |

# 19. Audit & Quality Controls

| Field | Description |
|---------|-------------|
| TS_SELF_AUDIT_SUBTASK | Self Audit Task |
| TS_CASE_SETUP_AUDIT_SC | Case Setup Audit |
| TS_CASE_SETUP_AUDIT_CR | Change Request Audit |
| TS_AUDIT_COMPLETE_DATE | Audit Completion Date |

# 20. Common Field Prefix Meanings

| Prefix | Meaning |
|----------|---------|
| TS_EXP_ | Explanation/Comments for field |
| TS_EOI_ | Evidence of Insurability |
| TS_GUAR_ | Guaranteed Issue |
| TS_PORT_ | Portability |
| TS_RENEW_ | Renewal |
| TS_TRANS_ | Transition |
| TS_UW_ | Underwriting |
| TS_OE_ | Open Enrollment |
| TS_IM_ | Implementation |
| TS_EDI_ | Electronic Data Interchange |
| TS_PA_ | Product Add Process |
| TS_CR_ | Change Request Process |
| TS_RW_ | Rework Process |
| TS_SC_ | Sold Case Process |

## Overall Table Purpose

**ULD_LIFE_DI** is a comprehensive **Life, AD&D, Disability, Enrollment, Billing, Contracting, EDI, and Implementation case management table** used during the sale, installation, implementation, maintenance, and change management lifecycle of Life & Disability insurance products.
