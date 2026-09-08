## Draft Entity Model

![Data Model](/Entity%20Model.png)


# EOI Intake Process — Entity Model Normalization

## Overview
This document defines the normalized entity-relationship data model for the Evidence of Insurability (EOI) Intake Process. The model is designed in **Third Normal Form (3NF)** to eliminate redundancy while maintaining referential integrity across the Financial Protection (FP) workflow.

---
## Entity Relationship Diagram (High-Level)
```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   EMPLOYER      │◄────┤  EOI_APPLICATION │────►│    MEMBER       │
│   (Group)       │ 1:M │                  │ M:1 │   (Employee)    │
└─────────────────┘     └────────┬─────────┘     └─────────────────┘
                                 │
                    ┌────────────┼────────────┐
                    │            │            │
                    ▼            ▼            ▼
           ┌─────────────┐ ┌────────────┐ ┌─────────────────────┐
           │EOI DOCUMENT │ │EOI PRODUCT │ │HEALTH QUESTIONNAIRE │
           │  (Intake)   │ │  _LINE   │ │ │  (Responses)        │
           └─────────────┘ └────────────┘ └─────────────────────┘
                    │            │            │
                    ▼            ▼            ▼
           ┌─────────────┐ ┌──────────┐ ┌─────────────────┐
           │INDEXING LOG │ │FP PRODUCT│ │UNDERWRITING     │
           │             │ │ (Lookup) │ │    REVIEW       │
           └─────────────┘ └──────────┘ └─────────────────┘
                                              │
                                              ▼
                                     ┌─────────────────┐
                                     │UNDERWRITING     │
                                     │   DECISION      │
                                     └─────────────────┘
```

---

## 1. EMPLOYER (Group/Plan Sponsor)

**Description**: Commercial employers who contract with UHC to offer FP products to their employees.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| employer_id | UUID | PK | Unique identifier for the employer |
| group_number | VARCHAR(50) | UNIQUE, NOT NULL | UHC-assigned group/plan number |
| employer_name | VARCHAR(255) | NOT NULL | Legal name of the employer |
| tax_id | VARCHAR(20) | UNIQUE | Employer Tax ID (EIN) |
| industry_code | VARCHAR(10) | FK | SIC/NAICS industry classification |
| group_size | INT | | Number of enrolled employees |
| effective_date | DATE | NOT NULL | Plan effective date |
| termination_date | DATE | | Plan termination date (nullable) |
| is_active | BOOLEAN | DEFAULT TRUE | Whether the group plan is active |
| fp_products_offered | VARCHAR(500) | | Comma-separated or JSON array of FP product codes offered |
| address_line_1 | VARCHAR(255) | | Employer mailing address |
| address_line_2 | VARCHAR(255) | | |
| city | VARCHAR(100) | | |
| state | CHAR(2) | | US state code |
| zip_code | VARCHAR(10) | | |
| country | CHAR(2) | DEFAULT 'US' | ISO country code |
| contact_name | VARCHAR(255) | | HR/Benefits contact person |
| contact_email | VARCHAR(255) | | |
| contact_phone | VARCHAR(20) | | |
| created_at | TIMESTAMP | DEFAULT NOW() | Record creation timestamp |
| updated_at | TIMESTAMP | DEFAULT NOW() | Last update timestamp |

**Normalization**: Employer data is separated from applications because one employer has many applications over time. Storing employer details here avoids repetition in every EOI record.

---

## 2. MEMBER (Employee/Applicant)

**Description**: Individual employees or dependents applying for FP coverage. Separated from application to support multiple EOI submissions over time.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| member_id | UUID | PK | Unique member identifier |
| ssn | VARCHAR(11) | UNIQUE, NOT NULL | Social Security Number (encrypted at rest) |
| first_name | VARCHAR(100) | NOT NULL | Legal first name |
| middle_name | VARCHAR(100) | | Middle name/initial |
| last_name | VARCHAR(100) | NOT NULL | Legal last name |
| date_of_birth | DATE | NOT NULL | DOB (MM/DD/YYYY) |
| gender | CHAR(1) | | 'M', 'F', 'N', 'U' |
| height_inches | INT | | Height in inches |
| weight_lbs | INT | | Weight in pounds |
| marital_status | VARCHAR(20) | | Single, Married, Domestic Partner, etc. |
| email | VARCHAR(255) | | Personal email address |
| phone | VARCHAR(20) | | Primary phone number |
| address_line_1 | VARCHAR(255) | | Residential address |
| address_line_2 | VARCHAR(255) | | |
| city | VARCHAR(100) | | |
| state | CHAR(2) | | |
| zip_code | VARCHAR(10) | | |
| country | CHAR(2) | DEFAULT 'US' | |
| tobacco_use | BOOLEAN | | Tobacco usage status |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

**Normalization**: Member demographics are stored once and referenced by multiple EOI applications. This prevents storing the same SSN, DOB, and address repeatedly for every application.

---

## 3. FP_PRODUCT (Lookup/Master Data)

**Description**: Master reference table for all Financial Protection products offered by UHC.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| product_code | VARCHAR(20) | PK | Unique product code (e.g., 'SUPP_LIFE', 'STD', 'LTD', 'CRIT_ILL') |
| product_name | VARCHAR(100) | NOT NULL | Human-readable product name |
| product_category | VARCHAR(50) | NOT NULL | 'Life', 'Disability', 'Supplemental Health' |
| requires_eoi | BOOLEAN | DEFAULT TRUE | Whether EOI is required for this product |
| guaranteed_issue_amount | DECIMAL(12,2) | | Max coverage without EOI (e.g., 200000.00) |
| min_coverage_amount | DECIMAL(12,2) | | Minimum electable amount |
| max_coverage_amount | DECIMAL(12,2) | | Maximum electable amount |
| is_active | BOOLEAN | DEFAULT TRUE | Whether product is currently offered |
| created_at | TIMESTAMP | DEFAULT NOW() | |

**Products**:
| product_code | product_name | category | requires_eoi |
|--------------|--------------|----------|--------------|
| BASIC_LIFE | Basic Life Insurance | Life | FALSE |
| SUPP_LIFE | Supplemental Life Insurance | Life | TRUE |
| AD&D | Accidental Death & Dismemberment | Life | FALSE |
| STD | Short-Term Disability | Disability | TRUE |
| LTD | Long-Term Disability | Disability | TRUE |
| CRIT_ILL | Critical Illness | Supplemental Health | TRUE |
| ACCIDENT | Accident Insurance | Supplemental Health | FALSE |
| HOSP_INDEM | Hospital Indemnity | Supplemental Health | FALSE |

**Normalization**: Product definitions are centralized. If guaranteed issue amounts change, update one row instead of every historical record.

---

## 4. EOI_APPLICATION (Core Intake Record)

**Description**: The central entity representing a single EOI submission. Links employer, member, and intake metadata.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| application_id | UUID | PK | Unique application identifier |
| application_number | VARCHAR(50) | UNIQUE, NOT NULL | Business-facing application number (e.g., EOI-2026-00012345) |
| employer_id | UUID | FK → EMPLOYER | Group/plan sponsor reference |
| member_id | UUID | FK → MEMBER | Applicant reference |
| application_date | DATE | NOT NULL | Date the application was submitted |
| enrollment_type | VARCHAR(30) | NOT NULL | 'Initial', 'Open Enrollment', 'Late Entrant', 'Life Event', 'Increase' |
| intake_channel | VARCHAR(30) | NOT NULL | 'Paper', 'Portal_Adobe', 'Email', 'Fax', 'Census' |
| application_status | VARCHAR(30) | DEFAULT 'Received' | 'Received', 'Indexing', 'Under Review', 'Pending Info', 'Approved', 'Denied', 'Withdrawn' |
| is_census | BOOLEAN | DEFAULT FALSE | Whether part of a batch census submission |
| census_batch_id | UUID | FK → CENSUS_BATCH | Nullable reference to batch (future) |
| requested_effective_date | DATE | | When coverage should begin |
| submitted_by | VARCHAR(100) | | Name of person who submitted (if not member) |
| submitted_by_relationship | VARCHAR(50) | | 'Self', 'HR', 'Broker', 'Spouse' |
| adobe_agreement_id | VARCHAR(100) | | Adobe Sign agreement ID (if portal submission) |
| is_signature_valid | BOOLEAN | | Whether signature passed validation |
| signature_date | TIMESTAMP | | Date/time of signature |
| signature_type | VARCHAR(20) | | 'Wet', 'Digital', 'E-Sign' |
| indexing_completed_at | TIMESTAMP | | When indexing was finished |
| indexing_completed_by | VARCHAR(100) | | User ID of indexer or 'SYSTEM' if automated |
| underwriting_assigned_at | TIMESTAMP | | When assigned to underwriter |
| underwriter_id | VARCHAR(50) | | ID of assigned underwriter |
| review_started_at | TIMESTAMP | | When underwriter began review |
| review_completed_at | TIMESTAMP | | When decision was rendered |
| turnaround_days | INT | | Calculated: review_completed - application_date |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

**Normalization**: Application is the fact table. It contains only foreign keys to employer and member, plus intake-specific attributes. No repeating groups.

---

## 5. EOI_PRODUCT_LINE (Junction: Application × Products)

**Description**: Many-to-many junction between applications and products. One EOI application can request multiple FP products.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| product_line_id | UUID | PK | Unique line item ID |
| application_id | UUID | FK → EOI_APPLICATION | Parent application |
| product_code | VARCHAR(20) | FK → FP_PRODUCT | Product being applied for |
| requested_coverage_amount | DECIMAL(12,2) | NOT NULL | Amount requested (e.g., 50000.00) |
| current_coverage_amount | DECIMAL(12,2) | | Existing coverage amount (for increases) |
| approved_coverage_amount | DECIMAL(12,2) | | Final approved amount |
| premium_amount | DECIMAL(10,2) | | Calculated premium |
| product_status | VARCHAR(30) | DEFAULT 'Pending' | 'Pending', 'Approved', 'Denied', 'Approved with Exclusion' |
| exclusion_details | TEXT | | Specific exclusions if applicable |
| rating_class | VARCHAR(20) | | 'Standard', 'Rated', 'Declined' |
| is_guaranteed_issue | BOOLEAN | | Whether this line qualified for GI |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

**Normalization**: Separates product-specific details from the main application. Prevents storing variable number of products as columns in EOI_APPLICATION.

---

## 6. EOI_DOCUMENT (Document Management)

**Description**: Tracks all physical and digital documents associated with an EOI application.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| document_id | UUID | PK | Unique document identifier |
| application_id | UUID | FK → EOI_APPLICATION | Parent application |
| document_type | VARCHAR(50) | NOT NULL | 'EOI_Form', 'Questionnaire', 'Medical_Record', 'ID_Proof', 'Census_Sheet' |
| document_subtype | VARCHAR(50) | | 'Life_EOI', 'Disability_EOI', 'Cancer_Q', 'Cardiac_Q', 'Attending_Physician_Statement' |
| source_channel | VARCHAR(30) | NOT NULL | 'Mail', 'Fax', 'Email_Attachment', 'Portal_Upload', 'Adobe_Sign' |
| file_name | VARCHAR(255) | | Original file name |
| file_format | VARCHAR(10) | | 'PDF', 'TIFF', 'PNG', 'JPG', 'DOCX' |
| file_size_bytes | BIGINT | | Size in bytes |
| storage_path | VARCHAR(500) | | OnBase document handle or file path |
| onbase_doc_id | VARCHAR(100) | | OnBase document ID if integrated |
| received_date | TIMESTAMP | NOT NULL | When document was received |
| processed_date | TIMESTAMP | | When document was processed/indexed |
| ocr_confidence_score | DECIMAL(3,2) | | OCR accuracy score (0.00 - 1.00) |
| is_indexed | BOOLEAN | DEFAULT FALSE | Whether document has been indexed |
| indexed_by | VARCHAR(100) | | 'SYSTEM_AUTO' or user ID |
| checksum_hash | VARCHAR(64) | | SHA-256 hash for integrity verification |
| retention_expiry_date | DATE | | Date when document can be purged per retention policy |
| created_at | TIMESTAMP | DEFAULT NOW() | |

**Normalization**: Documents are separate from applications to support multiple documents per application (initial form + questionnaires + medical records). Document metadata is separated from binary content (stored in OnBase/file system).

---

## 7. INDEXING_LOG (Audit Trail for Intake)

**Description**: Detailed audit trail of the indexing process, capturing both manual and automated indexing events.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| log_id | UUID | PK | Unique log entry |
| document_id | UUID | FK → EOI_DOCUMENT | Document being indexed |
| application_id | UUID | FK → EOI_APPLICATION | Related application |
| indexing_type | VARCHAR(20) | NOT NULL | 'Manual', 'Automated_OCR', 'Automated_Barcode', 'API_Import' |
| started_at | TIMESTAMP | NOT NULL | When indexing began |
| completed_at | TIMESTAMP | | When indexing completed |
| indexer_user_id | VARCHAR(100) | | User ID (null for automated) |
| indexer_name | VARCHAR(255) | | Display name of indexer |
| fields_extracted | JSONB | | Key-value pairs of extracted fields: {"ssn": "xxx", "name": "John Doe", ...} |
| fields_corrected | JSONB | | Fields manually corrected during QA |
| correction_reason | TEXT | | Why corrections were needed |
| ocr_engine_version | VARCHAR(50) | | Version of OCR software used |
| validation_errors | JSONB | | Array of validation failures |
| status | VARCHAR(20) | NOT NULL | 'Success', 'Partial', 'Failed', 'Pending_QA' |
| created_at | TIMESTAMP | DEFAULT NOW() | |

**Normalization**: Audit data is separated from the document itself. JSONB fields allow flexible schema for extracted data without altering table structure when new form versions are introduced.

---

## 8. HEALTH_QUESTIONNAIRE (Medical History)

**Description**: Stores responses to the core Medical History Statement (MHS) and any follow-up condition-specific questionnaires.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| questionnaire_id | UUID | PK | Unique questionnaire instance |
| application_id | UUID | FK → EOI_APPLICATION | Parent application |
| document_id | UUID | FK → EOI_DOCUMENT | Link to the actual form document |
| questionnaire_type | VARCHAR(50) | NOT NULL | 'Initial_MHS', 'Cancer', 'Cardiac', 'Diabetes', 'Mental_Health', 'Musculoskeletal', 'Respiratory' |
| questionnaire_version | VARCHAR(10) | | Form version number |
| condition_category | VARCHAR(50) | | Broad condition category |
| condition_specific | VARCHAR(100) | | Specific condition name |
| diagnosis_date | DATE | | When condition was diagnosed |
| treatment_status | VARCHAR(30) | | 'Ongoing', 'Completed', 'In_Remission', 'Resolved' |
| medications | TEXT | | List of current medications |
| physician_name | VARCHAR(255) | | Treating physician name |
| physician_npi | VARCHAR(10) | | National Provider Identifier |
| physician_phone | VARCHAR(20) | | |
| physician_fax | VARCHAR(20) | | |
| hospital_name | VARCHAR(255) | | Hospital/facility name |
| hospital_address | TEXT | | |
| is_prescription_pending | BOOLEAN | | Whether surgery/treatment is pending |
| pending_procedure_date | DATE | | Scheduled date if applicable |
| additional_notes | TEXT | | Free-text medical details |
| is_complete | BOOLEAN | DEFAULT FALSE | Whether all required fields are filled |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

**Normalization**: Medical history is separated from the main application because:
- One application can trigger multiple condition-specific questionnaires
- Medical data has different access controls (HIPAA)
- Questionnaires can be added asynchronously after initial intake

---

## 9. UNDERWRITING_REVIEW

**Description**: Tracks the underwriter's review process and case management.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| review_id | UUID | PK | Unique review record |
| application_id | UUID | FK → EOI_APPLICATION | Parent application |
| underwriter_id | VARCHAR(50) | NOT NULL | Underwriter employee ID |
| underwriter_name | VARCHAR(255) | | Underwriter display name |
| review_queue | VARCHAR(50) | | 'Standard', 'Expedited', 'Complex', 'Senior_Review' |
| assigned_date | TIMESTAMP | NOT NULL | When case was assigned |
| started_date | TIMESTAMP | | When underwriter opened the case |
| complexity_score | INT | | 1-10 calculated complexity rating |
| risk_factors | JSONB | | Array of identified risk factors |
| required_medical_records | BOOLEAN | DEFAULT FALSE | Whether APS/medical records were requested |
| paramedical_required | BOOLEAN | DEFAULT FALSE | Whether paramed exam is needed |
| paramedical_vendor | VARCHAR(100) | | Vendor name (e.g., ExamOne, APPS) |
| paramedical_scheduled_date | DATE | | |
| paramedical_completed_date | DATE | | |
| review_notes | TEXT | | Underwriter's case notes |
| internal_referral_reason | VARCHAR(100) | | Reason if escalated to medical director |
| referred_to_medical_director | BOOLEAN | DEFAULT FALSE | |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

**Normalization**: Review data is separated from the application because one application may have multiple review cycles (if pended for additional info and re-submitted).

---

## 10. UNDERWRITING_DECISION

**Description**: Final underwriting decisions and communication tracking.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| decision_id | UUID | PK | Unique decision record |
| application_id | UUID | FK → EOI_APPLICATION | Parent application |
| review_id | UUID | FK → UNDERWRITING_REVIEW | Related review |
| decision_type | VARCHAR(30) | NOT NULL | 'Approved', 'Approved_Rated', 'Approved_Exclusion', 'Denied', 'Withdrawn', 'Pending' |
| decision_category | VARCHAR(30) | | 'Standard', 'Substandard', 'Declined', 'Postponed' |
| decision_reason_code | VARCHAR(20) | | Standardized reason code |
| decision_reason_description | TEXT | | Detailed explanation |
| approved_amount | DECIMAL(12,2) | | Final approved coverage amount |
| approved_premium_rate | DECIMAL(8,4) | | Premium rate per $1,000 |
| exclusion_codes | JSONB | | Array of exclusion condition codes |
| exclusion_rider_text | TEXT | | Legal exclusion language |
| effective_date | DATE | | When approved coverage becomes effective |
| decision_date | TIMESTAMP | NOT NULL | When decision was made |
| communicated_date | TIMESTAMP | | When decision was sent to applicant |
| communication_method | VARCHAR(20) | | 'Mail', 'Email', 'Portal', 'Phone' |
| employer_notified_date | TIMESTAMP | | When employer was notified |
| appeal_deadline_date | DATE | | Deadline for applicant to appeal |
| created_at | TIMESTAMP | DEFAULT NOW() | |

**Normalization**: Decision is separate from review to support appeals (new decision on same application) and to maintain historical decision records if decisions are amended.

---

## 11. MEDICAL_RECORD_REQUEST

**Description**: Tracks requests for Attending Physician Statements (APS) and other medical records.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| request_id | UUID | PK | Unique request ID |
| application_id | UUID | FK → EOI_APPLICATION | Parent application |
| review_id | UUID | FK → UNDERWRITING_REVIEW | Related review |
| provider_name | VARCHAR(255) | NOT NULL | Physician/facility name |
| provider_npi | VARCHAR(10) | | |
| provider_address | TEXT | | |
| provider_phone | VARCHAR(20) | | |
| provider_fax | VARCHAR(20) | | |
| request_type | VARCHAR(50) | | 'APS', 'Lab_Results', 'Hospital_Records', 'Specialist_Consult' |
| request_date | DATE | NOT NULL | When request was sent |
| follow_up_date | DATE | | Scheduled follow-up |
| received_date | DATE | | When records were received |
| document_id | UUID | FK → EOI_DOCUMENT | Link to received document |
| status | VARCHAR(20) | DEFAULT 'Pending' | 'Pending', 'Sent', 'Follow_Up', 'Received', 'Not_Available' |
| notes | TEXT | | |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| updated_at | TIMESTAMP | DEFAULT NOW() | |

**Normalization**: Medical record requests are a separate entity because multiple providers can be contacted for one application, each with independent timelines.

---

## 12. CENSUS_BATCH (Future Scope)

**Description**: Batch enrollment submissions from employers (census/non-census). Tabled for future implementation.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| batch_id | UUID | PK | Unique batch identifier |
| employer_id | UUID | FK → EMPLOYER | Submitting employer |
| batch_number | VARCHAR(50) | UNIQUE | Business-facing batch number |
| batch_type | VARCHAR(20) | | 'Census', 'Non_Census', 'Open_Enrollment' |
| submission_date | DATE | NOT NULL | |
| total_records | INT | | Number of employees in batch |
| processed_records | INT | DEFAULT 0 | |
| failed_records | INT | DEFAULT 0 | |
| file_name | VARCHAR(255) | | Original upload file |
| file_format | VARCHAR(10) | | 'CSV', 'XLSX', 'XML', 'EDI' |
| validation_status | VARCHAR(20) | | 'Pending', 'Validating', 'Validated', 'Failed' |
| processing_status | VARCHAR(20) | DEFAULT 'Pending' | 'Pending', 'Processing', 'Completed', 'Partial' |
| submitted_by | VARCHAR(255) | | HR contact |
| created_at | TIMESTAMP | DEFAULT NOW() | |
| completed_at | TIMESTAMP | | |

---

## 13. AUDIT_TRAIL (System-Wide)

**Description**: Comprehensive change tracking for compliance and debugging.

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| audit_id | UUID | PK | Unique audit record |
| table_name | VARCHAR(50) | NOT NULL | Table being modified |
| record_id | UUID | NOT NULL | PK of affected record |
| action | VARCHAR(10) | NOT NULL | 'INSERT', 'UPDATE', 'DELETE' |
| old_values | JSONB | | Previous state |
| new_values | JSONB | | New state |
| changed_by | VARCHAR(100) | | User ID or 'SYSTEM' |
| changed_at | TIMESTAMP | DEFAULT NOW() | |
| session_id | VARCHAR(100) | | Application session |
| ip_address | VARCHAR(45) | | Source IP |

---

## Normalization Summary

| Normal Form | Compliance |
|-------------|------------|
| **1NF** | ✅ All columns atomic. No repeating groups. Array data stored in junction tables or JSONB only for truly variable attributes (extracted fields). |
| **2NF** | ✅ All non-key attributes fully dependent on the entire PK. No partial dependencies. |
| **3NF** | ✅ No transitive dependencies. Employer details in EMPLOYER, member details in MEMBER, product definitions in FP_PRODUCT. |
| **Referential Integrity** | ✅ Foreign keys enforce relationships. Cascading rules defined for soft deletes. |

---

## Key Relationships

```sql
-- Primary Relationships
EMPLOYER (1) ───────< (M) EOI_APPLICATION
MEMBER (1) ─────────< (M) EOI_APPLICATION
EOI_APPLICATION (1) ─< (M) EOI_PRODUCT_LINE
FP_PRODUCT (1) ──────< (M) EOI_PRODUCT_LINE
EOI_APPLICATION (1) ─< (M) EOI_DOCUMENT
EOI_APPLICATION (1) ─< (M) HEALTH_QUESTIONNAIRE
EOI_APPLICATION (1) ─< (M) UNDERWRITING_REVIEW
UNDERWRITING_REVIEW (1) ─< (M) UNDERWRITING_DECISION
EOI_APPLICATION (1) ─< (M) MEDICAL_RECORD_REQUEST
CENSUS_BATCH (1) ────< (M) EOI_APPLICATION
EOI_DOCUMENT (1) ────< (M) INDEXING_LOG
```

---

## Indexing Strategy

| Table | Index Columns | Purpose |
|-------|--------------|---------|
| EOI_APPLICATION | (application_number) | Unique lookup |
| EOI_APPLICATION | (employer_id, application_date) | Employer reporting |
| EOI_APPLICATION | (member_id, application_date) | Member history |
| EOI_APPLICATION | (application_status, intake_channel) | Workflow queue |
| EOI_APPLICATION | (adobe_agreement_id) | Adobe Sign reconciliation |
| MEMBER | (ssn) | Encrypted, but indexed for lookup |
| MEMBER | (last_name, first_name, date_of_birth) | Name search |
| EOI_DOCUMENT | (application_id, document_type) | Document retrieval |
| EOI_DOCUMENT | (onbase_doc_id) | OnBase cross-reference |
| INDEXING_LOG | (document_id, status) | Processing queue |
| HEALTH_QUESTIONNAIRE | (application_id, questionnaire_type) | Medical review |
| UNDERWRITING_REVIEW | (underwriter_id, assigned_date) | Workload management |
| UNDERWRITING_DECISION | (application_id, decision_date) | Decision history |

---

## Data Retention & Compliance Notes

1. **PHI/PII**: SSN and medical history encrypted at rest (AES-256). Field-level encryption recommended for SSN.
2. **HIPAA**: HEALTH_QUESTIONNAIRE and UNDERWRITING_REVIEW access logged in AUDIT_TRAIL.
3. **Retention**: EOI documents retained per state regulations (typically 7 years). Retention expiry tracked in EOI_DOCUMENT.
4. **Audit**: All status changes on EOI_APPLICATION logged in AUDIT_TRAIL.
5. **Adobe e-sign**: Agreement IDs preserved for legal non-repudiation.

---

