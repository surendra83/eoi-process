## EOI – SBM Integration API Design 

## 1. Objective 

Provide an API that allows OnBase to retrieve Group, Division, Contact, and Plan information from SBM and display it within the EOI application without requiring underwriters to access SBM. 

## 2. Current Process 

EOI stored in OnBase → Underwriter opens EOI → Underwriter logs into SBM → Searches Group, Division, Contact and Plan information → Processes EOI. 

## 3. Proposed Process 

EOI stored in OnBase → Underwriter opens EOI → OnBase calls SBM API → API retrieves data from SBM → API returns JSON → OnBase displays consolidated information. 

## 4. API Trigger 

When an EOI application is opened in OnBase, OnBase automatically invokes the SBM API. 

## 6. Request Payload

OnBase sends identifiers available in the EOI record so the API can locate the correct SBM record. 

```
{
  "groupNumber": "306455",
  "groupName": "Centerfield Media Holding Company"
}

```

## 7. Information Retrieved from SBM 

Group Information: Group Number, Group Name, Situs State, Policy ID, Policy Effective Date, Policy Anniversary Date, Policy Renewal Date, Policy Termination Date. 

Division Information: Division Number, Division Name, Division Status, Subgroup Number, Subgroup Description. Product Information 

Contact Information: EOI Contact Name, EOI Contact Email, Contact Details. 

Plan Information: Product Type, Benefit Description, Plan Maximum, Guaranteed Issue Amount, Coverage Increment Rules, Participation Requirement, Enrollment Rules, Effective Date, Termination Date. 

## 8. Response body 

```
{
  "group_information": {
    "group_name": "Centerfield Media Holding Company",
    "group_policy_number": "306455",
    "plan_anniversary_date": "09/01",
    "group_effective_date": "09/01/2019",
    "group_termination_date": null,
    "situs_state": "CA"
  },
  "contact_information": [
    {
      "division_information": {
        "division_number": "2001",
        "division_name": "Centerfield Media Holding Company",
        "effective_date": "05/01/2021",
        "termination_date": null
      },
      "primary_contact": {
        "contact_type": "Billing",
        "contact_name": "Alex Horton",
        "contact_title": "Controller",
        "contact_email": "ahorton@centerfield.com",
        "contact_address": "12130 Millennium Dr, Suite 600",
        "contact_city_state_zip": "Los Angeles, CA 90094",
        "contact_phone": "3103414377",
        "contact_fax": null
      },
      "secondary_contact": {
        "contact_type": "Certificates,Claims,Eligibility,EOI,Executive (5500),Main/Plan Admin",
        "contact_name": "Gabbie Grzeskiewicz",
        "contact_title": "Controller",
        "contact_email": "ggrzeskiewicz@centerfield.com",
        "contact_address": null,
        "contact_city_state_zip": null,
        "contact_phone": "(310)3414377",
        "contact_fax": null
      },
      "comments_subgroup": "back up contact Gena Romano VP of Human Resources gromano@centerfield.com 3103318203"
    },
    {
      "division_information": {
        "division_number": "2002",
        "division_name": "Valpak",
        "effective_date": "05/01/2021",
        "termination_date": null
      },
      "primary_contact": {
        "contact_type": "",
        "contact_name": null,
        "contact_title": null,
        "contact_email": null,
        "contact_address": null,
        "contact_city_state_zip": null,
        "contact_phone": null,
        "contact_fax": null
      },
      "secondary_contact": {
        "contact_type": "",
        "contact_name": null,
        "contact_title": null,
        "contact_email": null,
        "contact_address": null,
        "contact_city_state_zip": null,
        "contact_phone": null,
        "contact_fax": null
      },
      "comments_subgroup": null
    },
    {
      "division_information": {
        "division_number": "2003",
        "division_name": "Datalot",
        "effective_date": "09/01/2022",
        "termination_date": null
      },
      "primary_contact": {
        "contact_type": "",
        "contact_name": null,
        "contact_title": null,
        "contact_email": null,
        "contact_address": null,
        "contact_city_state_zip": null,
        "contact_phone": null,
        "contact_fax": null
      },
      "secondary_contact": {
        "contact_type": "",
        "contact_name": null,
        "contact_title": null,
        "contact_email": null,
        "contact_address": null,
        "contact_city_state_zip": null,
        "contact_phone": null,
        "contact_fax": null
      },
      "comments_subgroup": null
    },
    {
      "division_information": {
        "division_number": "2004",
        "division_name": "Quotemanage",
        "effective_date": "09/01/2022",
        "termination_date": null
      },
      "primary_contact": {
        "contact_type": "",
        "contact_name": null,
        "contact_title": null,
        "contact_email": null,
        "contact_address": null,
        "contact_city_state_zip": null,
        "contact_phone": null,
        "contact_fax": null
      },
      "secondary_contact": {
        "contact_type": "",
        "contact_name": null,
        "contact_title": null,
        "contact_email": null,
        "contact_address": null,
        "contact_city_state_zip": null,
        "contact_phone": null,
        "contact_fax": null
      },
      "comments_subgroup": null
    }
  ],
  "product_information": {
    "short_term_dependent_std": {
      "benefit_percentage_std": "60% (standard)",
      "comments_std": null,
      "effective_date_std": "09/01/2019",
      "termination_date_std": null,
      "std_minimum_participation_std": "100% (Standard if Non-Contributory)",
      "std_guaranteed_issue_benefit_std": "Same as Maximum Weekly Benefit",
      "elimination_period_for_injury_std": "7 days (standard)",
      "elimination_period_for_sickness_std": "7 days (standard)",
      "expected_maximum_weekly_benefit_std": "$2,500",
      "maximum_weekly_benefit_std": "Other",
      "buy_up_option_std": "No",
      "maximum_benefit_period_weeks_std_buyup": null,
      "minimum_participation_std_buyup": null
    },
    "supplemental_dependent_life": {
      "effective_date_sdl": "09/01/2019",
      "termination_date_sdl": null,
      "current_employee_increase_am-ount_sd": "Yes - Explain limit in Comments",
      "current_employee_no_bl_sdl": "Yes - Explain limit in Comments",
      "must_employee_covered_for_sdl": "Yes",
      "na_takeover_for_employee_sdls": "No",
      "participation_requirement_sdl": "Yes",
      "comments_sdl": "True Open Enrollment for September 1, 2019: A one-time exception has been made to allow an Actively at Work employee, including an employee not currently enrolled for Supplemental Life coverage, to elect an amount of Supplemental Life coverage with no proof of good health as follows:\r\nFor employees insured under the Supplemental Life plan on August 31, 2019:\r\n- Employees insured under the Supplemental Life plan are eligible to increase their Supplemental Life coverage with no proof of good health, not to exceed the Guaranteed Issue limit. All requests must be received by September 30, 2019\r\nFor employees who are not insured under the Supplemental Life plan on August 31, 2019:\r\n- Employees not insured under the Supplemental Life plan are eligible to enroll for coverage with no proof of good health not to exceed the Guaranteed Issue limit. All requests must be received by September 30, 2019\r\nNote: These amounts are prior to any age reduction being taken.\r\nIn addition to the one-time exception allowing an employee to increase his/her Supplemental Life coverage, the employee may also elect to increase the Supplemental Spouse Life coverage, not to exceed the Spouse Life Guarantee Issue limit with no proof of good health.\r\nAnnual Enrollment: During the employer's scheduled Annual Enrollment Period, an employee who is insured for Supplemental Life may increase coverage by one incremental level with no proof of good health up to the Guaranteed Issue Level as long as:\r\n- Coverage had not been increased in the prior year due to a Family Status Change.\r\nAn employee who is not insured for Supplemental Life is considered a late applicant and satisfactory proof of good health is required for any amount.\r\nAn employee must submit satisfactory proof of good health for any increase in coverage over the Guarantee Issue Amount.\r\nNote: If an employee is already over the Guarantee Issue limit, an increase in coverage that is due solely to an increase in earnings will not require proof of good health unless the increased coverage is greater than a cumulative increase of $50,000 over the prior approved amount of Supplemental Life coverage.\r\nDuring the employer’s scheduled Annual Enrollment Period, a Spouse who is insured for Supplemental Dependent Life may increase coverage by one incremental level with no proof of good health, not to exceed the Guaranteed Issue limit. A Spouse over the Guarantee Issue limit must submit satisfactory proof of good health for any increase. A Spouse not insured for Supplemental Life is considered a late applicant and satisfactory proof of good health is required for any amount."
    },
    "supplemental_life": {
      "benefit_earnings_sl": "Base salary and wages only",
      "effective_date_sl": "09/01/2019",
      "termination_date_sl": null,
      "guaranteed_issue_amount_sl": "$150,000",
      "additional_comment_sl": "True Open Enrollment for September 1, 2019: A one-time exception has been made to allow an Actively at Work employee, including an employee not currently enrolled for Supplemental Life coverage, to elect an amount of Supplemental Life coverage with no proof of good health as follows:\r\nFor employees insured under the Supplemental Life plan on August 31, 2019:\r\n- Employees insured under the Supplemental Life plan are eligible to increase their Supplemental Life coverage with no proof of good health, not to exceed the Guaranteed Issue limit. All requests must be received by September 30, 2019\r\nFor employees who are not insured under the Supplemental Life plan on August 31, 2019:\r\n- Employees not insured under the Supplemental Life plan are eligible to enroll for coverage with no proof of good health not to exceed the Guaranteed Issue limit. All requests must be received by September 30, 2019\r\nNote: These amounts are prior to any age reduction being taken.\r\nIn addition to the one-time exception allowing an employee to increase his/her Supplemental Life coverage, the employee may also elect to increase the Supplemental Spouse Life coverage, not to exceed the Spouse Life Guarantee Issue limit with no proof of good health.\r\nAnnual Enrollment: During the employer's scheduled Annual Enrollment Period, an employee who is insured for Supplemental Life may increase coverage by one incremental level with no proof of good health up to the Guaranteed Issue Level as long as:\r\n- Coverage had not been increased in the prior year due to a Family Status Change.\r\nAn employee who is not insured for Supplemental Life is considered a late applicant and satisfactory proof of good health is required for any amount.\r\nAn employee must submit satisfactory proof of good health for any increase in coverage over the Guarantee Issue Amount.\r\nNote: If an employee is already over the Guarantee Issue limit, an increase in coverage that is due solely to an increase in earnings will not require proof of good health unless the increased coverage is greater than a cumulative increase of $50,000 over the prior approved amount of Supplemental Life coverage.\r\nDuring the employer’s scheduled Annual Enrollment Period, a Spouse who is insured for Supplemental Dependent Life may increase coverage by one incremental level with no proof of good health, not to exceed the Guaranteed Issue limit. A Spouse over the Guarantee Issue limit must submit satisfactory proof of good health for any increase. A Spouse not insured for Supplemental Life is considered a late applicant and satisfactory proof of good health is required for any amount.",
      "benifit_reduction_schedule_sl": null,
      "exp_rounding_sl": null,
      "virgin_line_coverage_sl": "No"
    },
    "long_term_dependent_ltd": {
      "benefit_percentage_ltd_buyup": null,
      "maximum_month_benefit_ltd": "Other ",
      "ltd_buyup_option": "No",
      "maximum_month_buyup_option_ltd": null,
      "open_enrollment_offered_ltd_buyup": null,
      "open_enrollment_termination_date_ltd_buyup": null,
      "guaranteed_issue_onetime_open_enrollment_ltd_buyup": null,
      "comments_ltd_buyup": null,
      "comments_ltd": "50/50 reinsurance\r\nThere is no earnings test in CA"
    }
  },
  "eligibility": [
    {
      "full_time_employees_effective_on": "Waiting Period:\r\nSalaried EE's- All salaried and hourly employees excluding hourly MA employees, The first day of the month following the date the Employee begins continuous employment with the Policyholder\r\n\r\nAll MA hourly employees The first day of the month following the date the Employee completes 60 days of continuous employment with the Policyholder\r\n\r\nValPak  -  The first day of the month following the date the Employee begins continuous employment with the Policyholder.\r\n\r\nBusiness.com EE's-  The first day of the month following the date the Employee begins continuous employment with the Policyholder.",
      "non_standard_detail": ",,",
      "waiting_period_design": null,
      "waiting_period_prefix": null
    }
  ],
  "sold_class_benefits_rates_information": [
    {
      "product_type": "Basic AD&D",
      "class_code": "1",
      "full_benefit_description": "$25,000",
      "insurance_class_of_ee": "All Active Full Time Employees",
      "comments": null
    },
    {
      "product_type": "Basic Life",
      "class_code": "1",
      "full_benefit_description": "$25,000",
      "insurance_class_of_ee": "All Active Full Time Employees",
      "comments": null
    },
    {
      "product_type": "Supp Life",
      "class_code": "1",
      "full_benefit_description": "Increments of $10,000 to $500,000, not to exceed 5 times BAE",
      "insurance_class_of_ee": "All Active Full Time Employees",
      "comments": null
    },
    {
      "product_type": "Supp AD&D",
      "class_code": "1",
      "full_benefit_description": "Increments of $10,000 to $500,000, not to exceed 5 times BAE",
      "insurance_class_of_ee": "All Active Full Time Employees",
      "comments": null
    },
    {
      "product_type": "Supp Dep Life",
      "class_code": "1",
      "full_benefit_description": "ncrements of $5,000 to $250,000 not to exceed 50.0% of Employee amount",
      "insurance_class_of_ee": "All Active Full Time Employees",
      "comments": null
    },
    {
      "product_type": "Supp Dep AD&D",
      "class_code": "1",
      "full_benefit_description": "Increments of $5,000 to $250,000, not to exceed 50.0% of the Employee amount",
      "insurance_class_of_ee": "All Active Full Time Employees",
      "comments": null
    },
    {
      "product_type": "STD",
      "class_code": "1",
      "full_benefit_description": null,
      "insurance_class_of_ee": "All Active Full Time Employees",
      "comments": null
    },
    {
      "product_type": "LTD",
      "class_code": "1",
      "full_benefit_description": null,
      "insurance_class_of_ee": "All active full time employees",
      "comments": null
    }
  ],
  "evidence_of_insurability": {
    "eoi_coverage_within_31_days_sdls": "Yes",
    "eoi_one_benefit_level_sdls": null,
    "eoi_for_increase_coverage_amount_sdls": "Yes",
    "eoi_new_hire_over_guaranteed_issue_sdls": "Yes",
    "eoi_required_if_elected_coverage_open_enrollment_sdls": "Yes",
    "eoi_required_for_newly_eligible_employees_sdls": "Yes - For Benefit Amounts Above the GI",
    "eoi_other_eoi_rules_sdls": null
  },
  "guaranteed_issue": {
    "one_benefit_level_equals_sdls": null,
    "guaranteed_issue_coverage_limits_n": null,
    "guaranteed_issue_amount_basic_life": "$25,000",
    "one_time_open_enrollment_ltd_buyup": null,
    "guaranteed_issue_annual_open_enrollment_ltd_buyup": null
  },
  "accidental_death_and_dismemberment": {
    "comments_basic_life_add_coverage": null,
    "comments_dependent_life_add_coverage": null,
    "comments_supplemental_life_add_coverage": null,
    "comments_supplemental_dependent_life_add_coverage": null
  },
  "life_insurance": {
    "comments_basic_life": null,
    "comments_dependent_life": null,
    "comments_guaranteed_issue": null,
    "supplemental_spouse_dependent_life_amount_limit": "Yes - 50% (Standard)"
  }
}

```

## 9. API Processing Flow 

OnBase → SBM API → SBM Database → Retrieve Group/Division/Contact/Plan Data → Build JSON Response → Return to OnBase → Display on OnBase Screen. 

## 10. Scope 

Included: API , JSON Schema, SBM Data Retrieval, REST API Development, OnBase Integration Support. 

## 11. Executive Summary 

OnBase will send EOI identifiers (Group ID, Group Name, Product Type) to the SBM API. The API will retrieve Group, Division, Contact, and Plan information from SBM and return a consolidated JSON response for display inside OnBase. 