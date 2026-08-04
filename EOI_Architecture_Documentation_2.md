# EOI Process Validation — Architecture & Data Model Documentation

**Version:** 1.0  
**Date:** August 2026  
**Domain:** Insurance / Group Benefits — Evidence of Insurability (EOI)  

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Architecture Overview](#2-architecture-overview)
3. [System Components](#3-system-components)
4. [Entity Relationship Model](#4-entity-relationship-model)
5. [Field Descriptions](#5-field-descriptions)
6. [Process Flow](#6-process-flow)
7. [Validation Engine Design](#7-validation-engine-design)
8. [Integration Patterns](#8-integration-patterns)

---

## 1. Executive Summary

The **EOI (Evidence of Insurability) Process Validation System** is a rule-based automated underwriting platform designed to evaluate insurance coverage applications that exceed guaranteed issue limits. The system manages the complete lifecycle from application intake through validation, exception handling, underwriting decision, and audit compliance.

### Key Capabilities
- **Automated Rule Validation:** Configurable validation rules with priority and severity levels
- **Exception Management:** Intelligent routing of failed validations to underwriter queues
- **Workflow Orchestration:** State-machine driven application lifecycle tracking
- **Audit & Compliance:** Comprehensive change logging for regulatory requirements
- **Hierarchical Data Model:** Employer → Division → Class → Member → Coverage chain

---

## 2. Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EOI PROCESS VALIDATION ARCHITECTURE                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                  │
│  │   Channel    │    │    Member    │    │   Employer   │                  │
│  │   Layer      │    │    Portal    │    │    Admin     │                  │
│  │ (API/Web/    │    │  (Self-Serve)│    │   (Bulk Ops) │                  │
│  │  Paper/Bulk) │    │              │    │              │                  │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘                  │
│         │                   │                   │                           │
│         └───────────────────┼───────────────────┘                           │
│                             ▼                                               │
│  ┌──────────────────────────────────────────────────────────────┐          │
│  │                    INTAKE & ORCHESTRATION LAYER               │          │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │          │
│  │  │ Application │  │  Workflow   │  │   Document Mgmt     │  │          │
│  │  │  Service    │  │   Engine    │  │   (Attachments)     │  │          │
│  │  └──────┬──────┘  └──────┬──────┘  └─────────────────────┘  │          │
│  └─────────┼────────────────┼──────────────────────────────────┘          │
│            │                │                                               │
│            ▼                ▼                                               │
│  ┌──────────────────────────────────────────────────────────────┐          │
│  │                  VALIDATION ENGINE LAYER                      │          │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │          │
│  │  │   Rule      │  │  Execution  │  │    Result Store     │  │          │
│  │  │  Registry   │  │   Engine    │  │   (Pass/Fail/Msg)   │  │          │
│  │  │ (SQL/JSON)  │  │ (Async/Sync)│  │                     │  │          │
│  │  └──────┬──────┘  └──────┬──────┘  └─────────────────────┘  │          │
│  └─────────┼────────────────┼──────────────────────────────────┘          │
│            │                │                                               │
│            ▼                ▼                                               │
│  ┌──────────────────────────────────────────────────────────────┐          │
│  │                EXCEPTION & UNDERWRITING LAYER                 │          │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │          │
│  │  │  Exception  │  │ Underwriter │  │   Decision Engine   │  │          │
│  │  │    Queue    │  │  Workbench  │  │ (Approve/Decline/   │  │          │
│  │  │ (Priority)  │  │  (UI/Tasks) │  │  Request More Info) │  │          │
│  │  └──────┬──────┘  └──────┬──────┘  └─────────────────────┘  │          │
│  └─────────┼────────────────┼──────────────────────────────────┘          │
│            │                │                                               │
│            ▼                ▼                                               │
│  ┌──────────────────────────────────────────────────────────────┐          │
│  │              AUDIT, REPORTING & COMPLIANCE LAYER              │          │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │          │
│  │  │  Audit Log  │  │  Workflow   │  │   Compliance        │  │          │
│  │  │  (Immutable)│  │   History   │  │   Reports           │  │          │
│  │  └─────────────┘  └─────────────┘  └─────────────────────┘  │          │
│  └──────────────────────────────────────────────────────────────┘          │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────┐          │
│  │                    DATA PERSISTENCE LAYER                     │          │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐   │          │
│  │  │  Member  │ │  Plan &  │ │   EOI    │ │  Validation  │   │          │
│  │  │  Master  │ │ Coverage │ │  Application│ │   Engine     │   │          │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────────┘   │          │
│  └──────────────────────────────────────────────────────────────┘          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Architecture Principles

| Principle | Description |
|-----------|-------------|
| **Separation of Concerns** | Validation logic is decoupled from workflow and data persistence |
| **Configurability** | Rules are data-driven, not hard-coded, enabling business user control |
| **Auditability** | Every state change and data mutation is logged immutably |
| **Scalability** | Async validation execution supports high-volume batch processing |
| **Extensibility** | Plugin architecture allows new rule categories without schema changes |

---

## 3. System Components

### 3.1 Employer & Group Hierarchy
Manages the organizational structure: **Employer Group → Division → Class → Member**. This hierarchy determines eligibility, plan availability, and coverage rules.

### 3.2 Member Management
Central registry of insured members with demographic data, employment status, and linkage to group hierarchy. Tracks eligibility separately from enrollment.

### 3.3 Insurance Plan & Coverage
Defines available insurance products (Life, Disability, Critical Illness) with coverage parameters. Member_Coverage links members to active plans with specific amounts.

### 3.4 EOI Application
The core transaction entity representing a request for coverage above guaranteed issue limits. Tracks status through the entire lifecycle.

### 3.5 Validation Engine
**Rule Registry:** Stores configurable business rules with expressions, priority, and severity.  
**Execution Engine:** Runs rules against application data and produces pass/fail results.  
**Result Store:** Persists detailed validation outcomes for reporting and exception routing.

### 3.6 Exception & Underwriting
Failed validations create exceptions in a priority queue. Underwriters claim, review, and resolve exceptions through a dedicated workbench.

### 3.7 Workflow & Audit
State machine tracks application status transitions. Immutable audit logs capture all data changes for compliance (HIPAA, SOX, state insurance regulations).

---

## 4. Entity Relationship Model

### 4.1 Relationship Diagram (Textual)

```
Employer_Group (1) ───< (N) Group_Division
      │                          │
      │                     (1) ─┘
      │                          │
      │                     (N) Group_Class
      │                          │
      │                     (1) ─┘
      │                          │
      └─────────────────────> (N) Member <──── (N) Member_Eligibility
      │                          │
      │                          │ (N)
      │                          ▼
      │                    Member_Coverage (N) ──> (1) Insurance_Plan
      │                          │
      │                          │ (1)
      │                          ▼
      │                    EOI_Application (1) ──< (N) Validation_Execution
      │                          │                          │
      │                          │                     (1) ─┘
      │                          │                          │
      │                          │                     (N) Validation_Result
      │                          │                          ▲
      │                          │                     (1) ─┘
      │                          │                     Validation_Rule
      │                          │
      │                          ▼
      │                    Exception_Queue (N) ──> (1) Underwriter
      │                          │
      │                          │ (1)
      │                          ▼
      │                    Workflow_History (N)
      │
      └─────────────────────> Audit_Log (N)
```

### 4.2 Cardinality Summary

| Parent Entity | Child Entity | Cardinality | Relationship |
|---------------|-------------|-------------|--------------|
| Employer_Group | Group_Division | 1:N | One group has many divisions |
| Group_Division | Group_Class | 1:N | One division has many classes |
| Employer_Group | Member | 1:N | One group has many members |
| Group_Division | Member | 1:N | One division has many members (optional) |
| Group_Class | Member | 1:N | One class has many members (optional) |
| Member | Member_Eligibility | 1:N | One member has eligibility history |
| Member | Member_Coverage | 1:N | One member has multiple coverages |
| Insurance_Plan | Member_Coverage | 1:N | One plan covers many members |
| Member | EOI_Application | 1:N | One member submits many applications |
| Insurance_Plan | EOI_Application | 1:N | One plan has many applications |
| EOI_Application | Validation_Execution | 1:N | One app has many validation runs |
| Validation_Execution | Validation_Result | 1:N | One execution produces many results |
| Validation_Rule | Validation_Result | 1:N | One rule appears in many results |
| EOI_Application | Exception_Queue | 1:N | One app may have multiple exceptions |
| Underwriter | Exception_Queue | 1:N | One underwriter handles many exceptions |
| EOI_Application | Workflow_History | 1:N | One app has many status transitions |
| EOI_Application | Audit_Log | 1:N | One app generates many audit entries |

---

## 5. Field Descriptions

### 5.1 Employer_Group

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **group_id** | BIGINT | NO | Primary key. Unique identifier for the employer group. |
| **group_number** | VARCHAR(50) | NO | External reference number assigned by the carrier or administrator. Must be unique. |
| **group_name** | VARCHAR(255) | NO | Legal or trading name of the employer organization. |
| **employer_name** | VARCHAR(255) | NO | Name of the employing entity (may differ from group_name in trust arrangements). |
| **group_type** | VARCHAR(50) | NO | Classification: `Corporate`, `Small Business`, `Association`, `Union`, `Government`. |
| **market_segment** | VARCHAR(50) | YES | Market categorization: `Commercial`, `Individual`, `Government`, `Voluntary`. |
| **status** | VARCHAR(20) | NO | Lifecycle state: `ACTIVE`, `INACTIVE`, `PENDING`, `TERMINATED`. |
| **effective_date** | DATE | NO | Date when the group contract becomes effective. |
| **termination_date** | DATE | YES | Date when the group contract ends. NULL if ongoing. |
| **created_date** | TIMESTAMP | NO | Row creation timestamp. Auto-populated. |
| **updated_date** | TIMESTAMP | NO | Last modification timestamp. Auto-updated. |

---

### 5.2 Group_Division

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **division_id** | BIGINT | NO | Primary key. Unique identifier for the division. |
| **group_id** | BIGINT | NO | Foreign key to Employer_Group. Establishes ownership. |
| **division_code** | VARCHAR(50) | NO | Short code for the division (e.g., `DIV-001`, `EAST_REGION`). |
| **division_name** | VARCHAR(255) | NO | Descriptive name (e.g., "Northeast Sales Division"). |
| **effective_date** | DATE | NO | When this division becomes active under the group contract. |
| **status** | VARCHAR(20) | NO | `ACTIVE`, `INACTIVE`, or `TERMINATED`. |

---

### 5.3 Group_Class

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **class_id** | BIGINT | NO | Primary key. Unique identifier for the class. |
| **division_id** | BIGINT | NO | Foreign key to Group_Division. Classes belong to divisions. |
| **class_code** | VARCHAR(50) | NO | Short code (e.g., `CLS-A`, `EXECUTIVE`). |
| **class_name** | VARCHAR(255) | NO | Descriptive name (e.g., "Executive Officers", "Hourly Workers"). |
| **eligibility_rule** | TEXT | YES | JSON or expression defining who qualifies (e.g., minimum hours, job grade). |
| **status** | VARCHAR(20) | NO | `ACTIVE`, `INACTIVE`, or `TERMINATED`. |

---

### 5.4 Member

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **member_id** | BIGINT | NO | Primary key. System-generated unique member identifier. |
| **employee_number** | VARCHAR(50) | NO | Employer's internal employee ID or badge number. |
| **first_name** | VARCHAR(100) | NO | Member's legal first name. |
| **last_name** | VARCHAR(100) | NO | Member's legal last name. |
| **dob** | DATE | NO | Date of Birth. Used for age-based eligibility and rate calculations. |
| **gender** | CHAR(1) | YES | `M`=Male, `F`=Female, `O`=Other, `U`=Unknown. |
| **ssn** | VARCHAR(11) | YES | Social Security Number. Must be encrypted at rest (AES-256). |
| **email** | VARCHAR(255) | YES | Primary email for notifications and portal access. |
| **phone** | VARCHAR(20) | YES | Primary contact phone number. |
| **employment_status** | VARCHAR(30) | NO | `ACTIVE`, `TERMINATED`, `LEAVE`, `RETIRED`. Drives eligibility. |
| **hire_date** | DATE | NO | Original date of hire. Used for waiting period calculations. |
| **group_id** | BIGINT | NO | Foreign key to Employer_Group. Required association. |
| **division_id** | BIGINT | YES | Foreign key to Group_Division. Optional sub-organization. |
| **class_id** | BIGINT | YES | Foreign key to Group_Class. Optional benefit class. |
| **status** | VARCHAR(20) | NO | Member record status: `ACTIVE`, `INACTIVE`, `TERMINATED`. |

---

### 5.5 Member_Eligibility

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **eligibility_id** | BIGINT | NO | Primary key. Unique eligibility determination record. |
| **member_id** | BIGINT | NO | Foreign key to Member. Links to the subject. |
| **effective_date** | DATE | NO | Start date of this eligibility period. |
| **termination_date** | DATE | YES | End date of eligibility. NULL if currently eligible. |
| **eligibility_status** | VARCHAR(30) | NO | `ELIGIBLE`, `INELIGIBLE`, `PENDING`, `EXPIRED`. |
| **reason** | TEXT | YES | Human-readable explanation for the determination. |
| **verified_date** | TIMESTAMP | YES | When eligibility was last verified by a system or user. |
| **verified_by** | VARCHAR(100) | YES | User ID or system process that performed verification. |
| **created_date** | TIMESTAMP | NO | Record creation timestamp. |
| **updated_date** | TIMESTAMP | NO | Last update timestamp. |

---

### 5.6 Insurance_Plan

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **plan_id** | BIGINT | NO | Primary key. Unique plan identifier. |
| **plan_code** | VARCHAR(50) | NO | Carrier-specific plan code (e.g., `GL-2026-BASIC`). Unique. |
| **plan_name** | VARCHAR(255) | NO | Marketing or descriptive name (e.g., "Group Life Basic"). |
| **product_type** | VARCHAR(50) | NO | Insurance line: `Life`, `Disability`, `Critical Illness`, `Accident`. |
| **coverage_type** | VARCHAR(50) | NO | Tier: `Basic`, `Supplemental`, `Voluntary`, `Core`. |
| **guaranteed_issue** | BOOLEAN | YES | If TRUE, no EOI required up to the plan's GI limit. |
| **maximum_coverage** | DECIMAL(15,2) | YES | Absolute maximum coverage amount available under this plan. |
| **minimum_coverage** | DECIMAL(15,2) | YES | Minimum required enrollment amount. Default 0. |
| **status** | VARCHAR(20) | NO | `ACTIVE`, `INACTIVE`, `TERMINATED`. |

---

### 5.7 Member_Coverage

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **coverage_id** | BIGINT | NO | Primary key. Unique coverage enrollment record. |
| **member_id** | BIGINT | NO | Foreign key to Member. The insured individual. |
| **plan_id** | BIGINT | NO | Foreign key to Insurance_Plan. The enrolled product. |
| **coverage_amount** | DECIMAL(15,2) | NO | Dollar amount of coverage (e.g., $150,000.00). |
| **coverage_level** | VARCHAR(50) | YES | Tier: `Employee`, `Employee+Spouse`, `Employee+Child`, `Family`. |
| **coverage_status** | VARCHAR(20) | NO | `ACTIVE`, `PENDING`, `TERMINATED`, `SUSPENDED`. |
| **effective_date** | DATE | NO | When coverage becomes active. |
| **termination_date** | DATE | YES | When coverage ends. NULL if active. |

---

### 5.8 EOI_Application

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **application_id** | BIGINT | NO | Primary key. System-generated application ID. |
| **application_number** | VARCHAR(50) | NO | Business-facing reference number (e.g., `EOI-2026-0004521`). Unique. |
| **member_id** | BIGINT | NO | Foreign key to Member. Applicant. |
| **plan_id** | BIGINT | NO | Foreign key to Insurance_Plan. Target plan. |
| **requested_amount** | DECIMAL(15,2) | NO | Additional coverage amount requested above current/GI limit. |
| **application_date** | DATE | NO | Date the application was submitted. |
| **submission_channel** | VARCHAR(50) | NO | Origin: `PORTAL`, `PAPER`, `EMAIL`, `API`, `BULK_IMPORT`. |
| **application_status** | VARCHAR(30) | NO | Business outcome: `SUBMITTED`, `UNDER_REVIEW`, `APPROVED`, `DECLINED`, `PENDING_INFO`, `WITHDRAWN`. |
| **workflow_status** | VARCHAR(30) | NO | Process stage: `INTAKE`, `VALIDATION`, `UNDERWRITING`, `DECISION`, `CLOSED`, `EXCEPTION`. |
| **created_by** | VARCHAR(100) | YES | User ID or system that created the application. |
| **created_date** | TIMESTAMP | NO | Submission timestamp. |

---

### 5.9 Validation_Rule

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **rule_id** | BIGINT | NO | Primary key. Unique rule identifier. |
| **rule_name** | VARCHAR(255) | NO | Human-readable name (e.g., "Age Under 70 at Application"). Unique. |
| **rule_category** | VARCHAR(50) | NO | Functional area: `ELIGIBILITY`, `COVERAGE_LIMIT`, `DATA_QUALITY`, `COMPLIANCE`, `BUSINESS_RULE`. |
| **rule_expression** | TEXT | NO | The validation logic. Can be SQL, JSON Logic, or DSL reference. |
| **priority** | INT | NO | Execution order. Lower numbers run first (1 = highest). |
| **severity** | VARCHAR(20) | NO | Impact level: `INFO`, `WARNING`, `ERROR`, `CRITICAL`. |
| **enabled** | BOOLEAN | YES | If FALSE, rule is skipped during execution. |
| **created_date** | TIMESTAMP | NO | When the rule was defined. |

---

### 5.10 Validation_Execution

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **execution_id** | BIGINT | NO | Primary key. Unique validation run identifier. |
| **application_id** | BIGINT | NO | Foreign key to EOI_Application. The subject application. |
| **started_time** | TIMESTAMP | NO | When the validation run began. |
| **completed_time** | TIMESTAMP | YES | When the validation run finished. NULL if still running. |
| **execution_status** | VARCHAR(30) | NO | `RUNNING`, `COMPLETED`, `FAILED`, `TIMEOUT`. |
| **rule_engine_version** | VARCHAR(20) | YES | Semantic version of the validation engine (e.g., `2.4.1`). |

---

### 5.11 Validation_Result

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **result_id** | BIGINT | NO | Primary key. Unique result record. |
| **execution_id** | BIGINT | NO | Foreign key to Validation_Execution. Parent run. |
| **rule_id** | BIGINT | NO | Foreign key to Validation_Rule. The rule evaluated. |
| **passed** | BOOLEAN | NO | `TRUE` if the application satisfied the rule; `FALSE` if it failed. |
| **expected_value** | TEXT | YES | The value or condition the rule expected (for debugging). |
| **actual_value** | TEXT | YES | The actual value found in the application data. |
| **message** | TEXT | YES | Human-readable explanation of the result (success or failure). |
| **created_date** | TIMESTAMP | NO | When the result was recorded. |

---

### 5.12 Underwriter

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **underwriter_id** | BIGINT | NO | Primary key. Unique underwriter identifier. |
| **employee_id** | VARCHAR(50) | NO | HR system employee ID. Unique. |
| **name** | VARCHAR(255) | NO | Full name of the underwriter. |
| **email** | VARCHAR(255) | NO | Business email for notifications and SSO. |
| **role** | VARCHAR(50) | NO | Seniority: `JUNIOR`, `SENIOR`, `LEAD`, `MANAGER`. Determines authority limits. |
| **department** | VARCHAR(100) | YES | Organizational unit (e.g., "Group Life Underwriting"). |
| **status** | VARCHAR(20) | NO | `ACTIVE`, `INACTIVE`, `ON_LEAVE`. |

---

### 5.13 Exception_Queue

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **exception_id** | BIGINT | NO | Primary key. Unique exception record. |
| **application_id** | BIGINT | NO | Foreign key to EOI_Application. The problematic application. |
| **exception_type** | VARCHAR(50) | NO | Category: `VALIDATION_FAILURE`, `MANUAL_REVIEW`, `SYSTEM_ERROR`, `POLICY_EXCEPTION`. |
| **priority** | INT | NO | Triage level: `1`=Critical, `2`=High, `3`=Medium, `4`=Low. |
| **assigned_underwriter** | BIGINT | YES | Foreign key to Underwriter. NULL if unassigned. |
| **status** | VARCHAR(20) | NO | `OPEN`, `IN_PROGRESS`, `RESOLVED`, `ESCALATED`. |
| **created_date** | TIMESTAMP | NO | When the exception was generated. |
| **resolved_date** | TIMESTAMP | YES | When the exception was closed. NULL until resolved. |

---

### 5.14 Workflow_History

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **workflow_id** | BIGINT | NO | Primary key. Unique transition record. |
| **application_id** | BIGINT | NO | Foreign key to EOI_Application. The subject. |
| **previous_status** | VARCHAR(30) | NO | Status before the transition. |
| **current_status** | VARCHAR(30) | NO | Status after the transition. |
| **changed_by** | VARCHAR(100) | NO | User ID or `SYSTEM` that triggered the change. |
| **changed_date** | TIMESTAMP | NO | Exact timestamp of the transition. |
| **comments** | TEXT | YES | Free-text explanation for the status change. |

---

### 5.15 Audit_Log

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| **audit_id** | BIGINT | NO | Primary key. Immutable audit record identifier. |
| **application_id** | BIGINT | YES | Foreign key to EOI_Application. Optional if change is unrelated to a specific app. |
| **table_name** | VARCHAR(100) | NO | Database table that was modified. |
| **field_name** | VARCHAR(100) | NO | Specific column that changed. |
| **old_value** | TEXT | YES | Previous value (NULL for inserts). |
| **new_value** | TEXT | YES | New value (NULL for deletes). |
| **changed_by** | VARCHAR(100) | NO | Identity of the actor (user or system process). |
| **changed_date** | TIMESTAMP | NO | Timestamp of the change. Immutable. |

---

## 6. Process Flow

### 6.1 Standard EOI Application Lifecycle

```
┌──────────┐     ┌──────────┐     ┌────────────┐     ┌─────────────┐     ┌──────────┐
│  INTAKE  │────>│ VALIDATE │────>│  DECISION  │────>│ UNDERWRITE  │────>│  CLOSED  │
│ (Submit) │     │  (Rules) │     │ (Auto/Man) │     │  (If Req'd) │     │ (Final)  │
└──────────┘     └────┬─────┘     └─────┬──────┘     └─────────────┘     └──────────┘
                      │                 │
                      ▼                 ▼
               ┌──────────┐      ┌──────────┐
               │  PASS    │      │  FAIL    │
               │ (Proceed)│      │ (Exception│
               └──────────┘      │  Queue)  │
                                  └──────────┘
```

### 6.2 Detailed Process Steps

| Step | Stage | Actor | Action | Outcome |
|------|-------|-------|--------|---------|
| 1 | **Intake** | Member/Admin | Submit EOI application with requested amount | Record created; `workflow_status` = `INTAKE` |
| 2 | **Pre-Validation** | System | Check member eligibility and plan availability | If invalid, app declined immediately |
| 3 | **Rule Execution** | Validation Engine | Execute all enabled rules by priority | `Validation_Execution` + `Validation_Result` records created |
| 4 | **Result Analysis** | System | Aggregate results; check for ERROR/CRITICAL failures | If all pass → auto-approve or route to underwriting based on amount |
| 5 | **Exception Routing** | System | Create `Exception_Queue` entry for failed rules | Priority assigned based on severity and amount |
| 6 | **Underwriter Review** | Underwriter | Claim exception, review application, request info if needed | Status updated to `IN_PROGRESS` |
| 7 | **Decision** | Underwriter/System | Approve, decline, or pend for more information | `application_status` updated; `Workflow_History` record created |
| 8 | **Coverage Update** | System | If approved, update `Member_Coverage` with new amount | Member record synchronized |
| 9 | **Closure** | System | Archive application; send notification | `workflow_status` = `CLOSED` |

---

## 7. Validation Engine Design

### 7.1 Rule Categories

| Category | Purpose | Example Rules |
|----------|---------|---------------|
| **ELIGIBILITY** | Verify member qualifies for EOI | Member is ACTIVE; hire date > 90 days ago |
| **COVERAGE_LIMIT** | Ensure requested amount is within plan bounds | Requested <= Plan.maximum_coverage; Requested >= GI limit |
| **DATA_QUALITY** | Validate completeness and format | SSN is valid; Email is present; DOB is not future date |
| **COMPLIANCE** | Regulatory and policy checks | Age at application < 70; State allows product type |
| **BUSINESS_RULE** | Carrier-specific underwriting criteria | No prior declinations in 12 months; Coverage increase < 3x current |

### 7.2 Severity Levels

| Severity | Behavior | Example |
|----------|----------|---------|
| **INFO** | Logged only; no impact on routing | "Member has multiple active coverages" |
| **WARNING** | Logged; may trigger review if combined with other issues | "Requested amount is 90% of maximum" |
| **ERROR** | Fails validation; routes to exception queue | "Member is not currently eligible" |
| **CRITICAL** | Immediate decline; no underwriter review | "Fraud indicator detected" |

### 7.3 Execution Model

Rules are executed sequentially by **priority** (ascending). Execution stops early only for CRITICAL failures (hard stop). All other severities continue to collect full results for comprehensive reporting.

```
FOR each enabled_rule IN rules ORDER BY priority ASC:
    result = evaluate(rule.expression, application_context)
    save_result(result)
    IF rule.severity == 'CRITICAL' AND result.passed == FALSE:
        mark_immediate_decline()
        BREAK
```

---

## 8. Integration Patterns

### 8.1 Inbound Integrations

| Source | Pattern | Data |
|--------|---------|------|
| Member Portal | REST API | Application submission, document upload |
| Employer HR System | SFTP/Batch | Member demographics, eligibility files |
| Underwriter Workbench | Web UI + API | Decisions, exception resolution |
| Document Management | Event-driven | Medical records, attestation forms |

### 8.2 Outbound Integrations

| Target | Pattern | Data |
|--------|---------|------|
| Member Portal | Webhook/Push | Status updates, decision notifications |
| Email Service | SMTP/API | Approval/decline letters, information requests |
| Policy Admin System | REST/SOAP | Approved coverage enrollments |
| Data Warehouse | ETL/Batch | Analytics, regulatory reporting |
| SIEM/Monitoring | Event Stream | Security events, anomaly detection |

### 8.3 Event-Driven Architecture

Key domain events published to message bus:

- `EOI.ApplicationSubmitted`
- `EOI.ValidationStarted`
- `EOI.ValidationCompleted`
- `EOI.ExceptionCreated`
- `EOI.DecisionMade`
- `EOI.CoverageActivated`
- `EOI.WorkflowStatusChanged`

---

## Appendix A: Data Retention & Compliance

| Entity | Retention Period | Encryption | PII |
|--------|-----------------|------------|-----|
| Member | 7 years post-termination | AES-256 | Yes (SSN, DOB) |
| EOI_Application | 10 years | AES-256 | Yes |
| Audit_Log | 10 years (immutable) | AES-256 | Yes |
| Validation_Result | 7 years | AES-256 | No |
| Exception_Queue | 7 years | AES-256 | Yes |

---

## Appendix B: Glossary

| Term | Definition |
|------|------------|
| **EOI** | Evidence of Insurability — medical or financial proof required for coverage above standard limits |
| **Guaranteed Issue (GI)** | Coverage amount available without health questions or underwriting |
| **Underwriter** | Insurance professional who evaluates risk and makes coverage decisions |
| **Exception Queue** | Worklist of applications requiring manual review due to validation failures |
| **Rule Engine** | Software component that evaluates business rules against application data |
| **Workflow Status** | Technical process stage (Intake -> Validation -> Underwriting -> Decision -> Closed) |
| **Application Status** | Business outcome state (Submitted, Approved, Declined, etc.) |

---

*Document generated from EOI_Validation_Process entity data model.*
*For questions, contact the Architecture Team.*
