# ULD_BILLING_ENROLL Data Dictionary

## Relevant Billing & Enrollment Fields

### Primary Identifiers
| Field | Description |
|---------|-------------|
| TS_ID | Unique identifier for the billing enrollment record.|
| TS_UUID | Universally unique identifier (UUID).|
| TS_TITLE | Billing enrollment title.|
| TS_GROUP_NAME_BILLING_ENROLL | Group name associated with billing enrollment.|
| TS_ASSOCIATED_BILL_GROUPS | Related billing groups.|

### Billing Configuration
| Field | Description |
|---------|-------------|
| TS_DATA_SOURCE | Source of billing/enrollment data.|
| TS_EXP_DATA_SOURCE | Expected billing data source.|
| TS_PREMIUMS_PAID | Indicates how premiums are paid.|
| TS_PREM_PAID_VIA | Premium payment method.|
| TS_SELF_BILL_DELIVERY | Self-bill delivery method.|
| TS_LIST_BILL_DELIVERY | Billing delivery method.|
| TS_PAYROLL_PERIODS | Payroll periods used for billing.|

### Billing Dates & Adjustments
| Field | Description |
|---------|-------------|
| TS_BILL_ADJUST_PERIOD | Billing adjustment period.|
| TS_EXP_BILL_ADJ_PERIOD | Expected adjustment period.|
| TS_EXPECTED_BILLING_DUE_DATE_ | Expected billing due date.|
| TS_GRACE_PERIOD | Grace period for payment.|
| TS_EXP_GRACE_PERIOD | Expected grace period.|

### Premium & Deposit Information
| Field | Description |
|---------|-------------|
| TS_PREM_DEP_AMT | Premium deposit amount.|
| TS_PREM_DEP_CHECK | Premium deposit check indicator.|
| TS_ASO_CLAIM_DEP_AMT | ASO claim deposit amount.|
| TS_ASO_DEPOSIT_TYPE | ASO deposit type.|

### Product Billing Methods
| Field | Description |
|---------|-------------|
| TS_CI_BILL_METH | Critical Illness billing method.|
| TS_DI_BILL_METH | Disability billing method.|
| TS_EAP_BILL_METH | EAP billing method.|
| TS_FMLA_BILL_METH | FMLA billing method.|
| TS_LIFEADD_BILL_METH |Life & AD&D billing method.|
| TS_ACCIDENT_BILLING_METHOD | Accident billing method.|
| TS_HOSP_INDEMNITY_BILL_METH | Hospital Indemnity billing method.|

### Employee-Paid Coverage Fields
| Field | Description |
|---------|-------------|
| TS_EMPLOYEE_PAID_BL| Employee-paid Basic Life.|
| TS_EMPLOYEE_PAID_CI| Employee-paid Critical Illness.|
| TS_EMPLOYEE_PAID_STD| Employee-paid Short-Term Disability.|
| TS_EMPLOYEE_PAID_LTD| Employee-paid Long-Term Disability.|
| TS_EMPLOYEE_PAID_EAP| Employee-paid EAP coverage.|

### Employer-Paid Coverage Fields
| Field | Description |
|---------|-------------|
| TS_EMPLOYER_PAID_BL| Employer-paid Basic Life.|
| TS_EMPLOYER_PAID_CI| Employer-paid Critical Illness.|
| TS_EMPLOYER_PAID_STD| Employer-paid Short-Term Disability.|
| TS_EMPLOYER_PAID_LTD| Employer-paid Long-Term Disability.|
| TS_EMPLOYER_PAID_EAP| Employer-paid EAP coverage.|

### Tax Method Fields
| Field | Description |
|---------|-------------|
| TS_STD_ER_PD_TAX_METHOD| Employer-paid STD tax method.|
| TS_STD_EE_PD_TAX_METHOD| Employee-paid STD tax method.|
| TS_LTD_ER_PD_TAX_METHOD| Employer-paid LTD tax method.|
| TS_LTD_EE_PD_TAX_METHOD| Employee-paid LTD tax method.|

### Premium Holiday & Credits
| Field | Description |
|---------|-------------|
| TS_PREMIUM_HOLIDAY_GRANTED | Premium holiday indicator.|
| TS_AMOUNT_OF_PREMIUM_HOLIDAY | Premium holiday amount.|
| TS_CREDIT_TYPE | Credit type.|
| TS_CREDIT_AMOUNT | Credit amount.|
| TS_CREDIT_GIVEN | Credit issued indicator.|

### Audit & Tracking

| Field | Description |
|---------|-------------|
| TS_SUBMITDATE | Submission date.|
| TS_SUBMITTER | Submitted by.|
| TS_ACTIVEINACTIVE | Active/Inactive status. |
| TS_LASTMODIFIER | Last modified by.|
| TS_LASTMODIFIEDDATE | Last modification date.|
| TS_COMMENTS | Comments and notes.|

## Most Relevant Fields for Billing Reporting
- TS_ID
- TS_GROUP_NAME_BILLING_ENROLL
- TS_DATA_SOURCE
- TS_PREMIUMS_PAID
- TS_PREM_PAID_VIA
- TS_BILL_ADJUST_PERIOD
- TS_GRACE_PERIOD
- TS_SELF_BILL_DELIVERY
- TS_CI_BILL_METH
- TS_DI_BILL_METH
- TS_LIFEADD_BILL_METH
- TS_ACCIDENT_BILLING_METHOD
- TS_PAYROLL_PERIODS
- TS_PREMIUM_HOLIDAY_GRANTED
- TS_CREDIT_AMOUNT
- TS_ACTIVEINACTIVE
- TS_SUBMITDATE
- TS_LASTMODIFIEDDATE
