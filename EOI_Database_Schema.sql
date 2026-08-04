-- ============================================================
-- EOI (Evidence of Insurability) Process Validation Database Schema
-- Version: 1.0
-- Description: Complete DDL for EOI Application Processing,
--              Validation Engine, and Workflow Management
-- ============================================================

-- ============================================================
-- 1. EMPLOYER & GROUP HIERARCHY
-- ============================================================

CREATE TABLE Employer_Group (
    group_id            BIGINT PRIMARY KEY AUTO_INCREMENT,
    group_number        VARCHAR(50) NOT NULL UNIQUE,
    group_name          VARCHAR(255) NOT NULL,
    employer_name       VARCHAR(255) NOT NULL,
    group_type          VARCHAR(50) NOT NULL COMMENT 'e.g., Corporate, Small Business, Association',
    market_segment      VARCHAR(50) COMMENT 'e.g., Commercial, Individual, Government',
    status              VARCHAR(20) NOT NULL DEFAULT 'ACTIVE' COMMENT 'ACTIVE, INACTIVE, PENDING, TERMINATED',
    effective_date      DATE NOT NULL,
    termination_date    DATE,
    created_date        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_date        TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT chk_employer_group_status CHECK (status IN ('ACTIVE', 'INACTIVE', 'PENDING', 'TERMINATED'))
);

CREATE TABLE Group_Division (
    division_id         BIGINT PRIMARY KEY AUTO_INCREMENT,
    group_id            BIGINT NOT NULL,
    division_code       VARCHAR(50) NOT NULL,
    division_name       VARCHAR(255) NOT NULL,
    effective_date      DATE NOT NULL,
    status              VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',

    FOREIGN KEY (group_id) REFERENCES Employer_Group(group_id),
    CONSTRAINT chk_division_status CHECK (status IN ('ACTIVE', 'INACTIVE', 'TERMINATED'))
);

CREATE TABLE Group_Class (
    class_id            BIGINT PRIMARY KEY AUTO_INCREMENT,
    division_id         BIGINT NOT NULL,
    class_code          VARCHAR(50) NOT NULL,
    class_name          VARCHAR(255) NOT NULL,
    eligibility_rule    TEXT COMMENT 'JSON or expression defining eligibility criteria',
    status              VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',

    FOREIGN KEY (division_id) REFERENCES Group_Division(division_id),
    CONSTRAINT chk_class_status CHECK (status IN ('ACTIVE', 'INACTIVE', 'TERMINATED'))
);

-- ============================================================
-- 2. MEMBER MANAGEMENT
-- ============================================================

CREATE TABLE Member (
    member_id           BIGINT PRIMARY KEY AUTO_INCREMENT,
    employee_number     VARCHAR(50) NOT NULL,
    first_name          VARCHAR(100) NOT NULL,
    last_name           VARCHAR(100) NOT NULL,
    dob                 DATE NOT NULL COMMENT 'Date of Birth',
    gender              CHAR(1) COMMENT 'M=Male, F=Female, O=Other, U=Unknown',
    ssn                 VARCHAR(11) COMMENT 'Social Security Number (encrypted at rest)',
    email               VARCHAR(255),
    phone               VARCHAR(20),
    employment_status   VARCHAR(30) NOT NULL DEFAULT 'ACTIVE' COMMENT 'ACTIVE, TERMINATED, LEAVE, RETIRED',
    hire_date           DATE NOT NULL,
    group_id            BIGINT NOT NULL,
    division_id         BIGINT,
    class_id            BIGINT,
    status              VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',

    FOREIGN KEY (group_id) REFERENCES Employer_Group(group_id),
    FOREIGN KEY (division_id) REFERENCES Group_Division(division_id),
    FOREIGN KEY (class_id) REFERENCES Group_Class(class_id),
    CONSTRAINT chk_member_gender CHECK (gender IN ('M', 'F', 'O', 'U')),
    CONSTRAINT chk_member_emp_status CHECK (employment_status IN ('ACTIVE', 'TERMINATED', 'LEAVE', 'RETIRED')),
    CONSTRAINT chk_member_status CHECK (status IN ('ACTIVE', 'INACTIVE', 'TERMINATED'))
);

CREATE TABLE Member_Eligibility (
    eligibility_id      BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id           BIGINT NOT NULL,
    effective_date      DATE NOT NULL,
    termination_date    DATE,
    eligibility_status  VARCHAR(30) NOT NULL DEFAULT 'PENDING' COMMENT 'ELIGIBLE, INELIGIBLE, PENDING, EXPIRED',
    reason              TEXT COMMENT 'Explanation for eligibility determination',
    verified_date       TIMESTAMP,
    verified_by         VARCHAR(100),
    created_date        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_date        TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (member_id) REFERENCES Member(member_id),
    CONSTRAINT chk_eligibility_status CHECK (eligibility_status IN ('ELIGIBLE', 'INELIGIBLE', 'PENDING', 'EXPIRED'))
);

-- ============================================================
-- 3. INSURANCE PLAN & COVERAGE
-- ============================================================

CREATE TABLE Insurance_Plan (
    plan_id             BIGINT PRIMARY KEY AUTO_INCREMENT,
    plan_code           VARCHAR(50) NOT NULL UNIQUE,
    plan_name           VARCHAR(255) NOT NULL,
    product_type        VARCHAR(50) NOT NULL COMMENT 'e.g., Life, Disability, Critical Illness',
    coverage_type       VARCHAR(50) NOT NULL COMMENT 'e.g., Basic, Supplemental, Voluntary',
    guaranteed_issue    BOOLEAN DEFAULT FALSE COMMENT 'True if no EOI required up to certain limit',
    maximum_coverage    DECIMAL(15, 2) COMMENT 'Maximum allowable coverage amount',
    minimum_coverage    DECIMAL(15, 2) DEFAULT 0 COMMENT 'Minimum required coverage amount',
    status              VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',

    CONSTRAINT chk_plan_status CHECK (status IN ('ACTIVE', 'INACTIVE', 'TERMINATED'))
);

CREATE TABLE Member_Coverage (
    coverage_id         BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id           BIGINT NOT NULL,
    plan_id             BIGINT NOT NULL,
    coverage_amount     DECIMAL(15, 2) NOT NULL,
    coverage_level      VARCHAR(50) COMMENT 'e.g., Employee, Employee+Spouse, Family',
    coverage_status     VARCHAR(20) NOT NULL DEFAULT 'ACTIVE' COMMENT 'ACTIVE, PENDING, TERMINATED, SUSPENDED',
    effective_date      DATE NOT NULL,
    termination_date    DATE,

    FOREIGN KEY (member_id) REFERENCES Member(member_id),
    FOREIGN KEY (plan_id) REFERENCES Insurance_Plan(plan_id),
    CONSTRAINT chk_coverage_status CHECK (coverage_status IN ('ACTIVE', 'PENDING', 'TERMINATED', 'SUSPENDED'))
);

-- ============================================================
-- 4. EOI APPLICATION
-- ============================================================

CREATE TABLE EOI_Application (
    application_id      BIGINT PRIMARY KEY AUTO_INCREMENT,
    application_number  VARCHAR(50) NOT NULL UNIQUE,
    member_id           BIGINT NOT NULL,
    plan_id             BIGINT NOT NULL,
    requested_amount    DECIMAL(15, 2) NOT NULL COMMENT 'Coverage amount requested via EOI',
    application_date    DATE NOT NULL,
    submission_channel  VARCHAR(50) NOT NULL COMMENT 'PORTAL, PAPER, EMAIL, API, BULK',
    application_status  VARCHAR(30) NOT NULL DEFAULT 'SUBMITTED' COMMENT 'SUBMITTED, UNDER_REVIEW, APPROVED, DECLINED, PENDING_INFO',
    workflow_status     VARCHAR(30) NOT NULL DEFAULT 'INTAKE' COMMENT 'INTAKE, VALIDATION, UNDERWRITING, DECISION, CLOSED',
    created_by          VARCHAR(100),
    created_date        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (member_id) REFERENCES Member(member_id),
    FOREIGN KEY (plan_id) REFERENCES Insurance_Plan(plan_id),
    CONSTRAINT chk_app_status CHECK (application_status IN ('SUBMITTED', 'UNDER_REVIEW', 'APPROVED', 'DECLINED', 'PENDING_INFO', 'WITHDRAWN')),
    CONSTRAINT chk_workflow_status CHECK (workflow_status IN ('INTAKE', 'VALIDATION', 'UNDERWRITING', 'DECISION', 'CLOSED', 'EXCEPTION'))
);

-- ============================================================
-- 5. VALIDATION ENGINE
-- ============================================================

CREATE TABLE Validation_Rule (
    rule_id             BIGINT PRIMARY KEY AUTO_INCREMENT,
    rule_name           VARCHAR(255) NOT NULL UNIQUE,
    rule_category       VARCHAR(50) NOT NULL COMMENT 'ELIGIBILITY, COVERAGE_LIMIT, DATA_QUALITY, COMPLIANCE, BUSINESS_RULE',
    rule_expression     TEXT NOT NULL COMMENT 'SQL expression, JSON logic, or script reference',
    priority            INT NOT NULL DEFAULT 100 COMMENT 'Lower number = higher priority (1-999)',
    severity            VARCHAR(20) NOT NULL DEFAULT 'ERROR' COMMENT 'INFO, WARNING, ERROR, CRITICAL',
    enabled             BOOLEAN DEFAULT TRUE,
    created_date        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_rule_severity CHECK (severity IN ('INFO', 'WARNING', 'ERROR', 'CRITICAL'))
);

CREATE TABLE Validation_Execution (
    execution_id        BIGINT PRIMARY KEY AUTO_INCREMENT,
    application_id      BIGINT NOT NULL,
    started_time        TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    completed_time      TIMESTAMP,
    execution_status    VARCHAR(30) NOT NULL DEFAULT 'RUNNING' COMMENT 'RUNNING, COMPLETED, FAILED, TIMEOUT',
    rule_engine_version VARCHAR(20) COMMENT 'Version of validation engine used',

    FOREIGN KEY (application_id) REFERENCES EOI_Application(application_id),
    CONSTRAINT chk_exec_status CHECK (execution_status IN ('RUNNING', 'COMPLETED', 'FAILED', 'TIMEOUT'))
);

CREATE TABLE Validation_Result (
    result_id           BIGINT PRIMARY KEY AUTO_INCREMENT,
    execution_id        BIGINT NOT NULL,
    rule_id             BIGINT NOT NULL,
    passed              BOOLEAN NOT NULL COMMENT 'True if rule validation succeeded',
    expected_value      TEXT COMMENT 'Expected result per rule definition',
    actual_value        TEXT COMMENT 'Actual value found during validation',
    message             TEXT COMMENT 'Human-readable validation message',
    created_date        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (execution_id) REFERENCES Validation_Execution(execution_id),
    FOREIGN KEY (rule_id) REFERENCES Validation_Rule(rule_id)
);

-- ============================================================
-- 6. EXCEPTION & UNDERWRITING
-- ============================================================

CREATE TABLE Underwriter (
    underwriter_id      BIGINT PRIMARY KEY AUTO_INCREMENT,
    employee_id         VARCHAR(50) NOT NULL UNIQUE,
    name                VARCHAR(255) NOT NULL,
    email               VARCHAR(255) NOT NULL,
    role                VARCHAR(50) NOT NULL COMMENT 'JUNIOR, SENIOR, LEAD, MANAGER',
    department          VARCHAR(100),
    status              VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',

    CONSTRAINT chk_underwriter_status CHECK (status IN ('ACTIVE', 'INACTIVE', 'ON_LEAVE'))
);

CREATE TABLE Exception_Queue (
    exception_id        BIGINT PRIMARY KEY AUTO_INCREMENT,
    application_id      BIGINT NOT NULL,
    exception_type      VARCHAR(50) NOT NULL COMMENT 'VALIDATION_FAILURE, MANUAL_REVIEW, SYSTEM_ERROR, POLICY_EXCEPTION',
    priority            INT NOT NULL DEFAULT 3 COMMENT '1=Critical, 2=High, 3=Medium, 4=Low',
    assigned_underwriter BIGINT,
    status              VARCHAR(20) NOT NULL DEFAULT 'OPEN' COMMENT 'OPEN, IN_PROGRESS, RESOLVED, ESCALATED',
    created_date        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_date       TIMESTAMP,

    FOREIGN KEY (application_id) REFERENCES EOI_Application(application_id),
    FOREIGN KEY (assigned_underwriter) REFERENCES Underwriter(underwriter_id),
    CONSTRAINT chk_exception_status CHECK (status IN ('OPEN', 'IN_PROGRESS', 'RESOLVED', 'ESCALATED'))
);

-- ============================================================
-- 7. WORKFLOW & AUDIT
-- ============================================================

CREATE TABLE Workflow_History (
    workflow_id         BIGINT PRIMARY KEY AUTO_INCREMENT,
    application_id      BIGINT NOT NULL,
    previous_status     VARCHAR(30) NOT NULL,
    current_status      VARCHAR(30) NOT NULL,
    changed_by          VARCHAR(100) NOT NULL COMMENT 'User ID or SYSTEM',
    changed_date        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    comments            TEXT,

    FOREIGN KEY (application_id) REFERENCES EOI_Application(application_id)
);

CREATE TABLE Audit_Log (
    audit_id            BIGINT PRIMARY KEY AUTO_INCREMENT,
    application_id      BIGINT,
    table_name          VARCHAR(100) NOT NULL,
    field_name          VARCHAR(100) NOT NULL,
    old_value           TEXT,
    new_value           TEXT,
    changed_by          VARCHAR(100) NOT NULL,
    changed_date        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (application_id) REFERENCES EOI_Application(application_id)
);

-- ============================================================
-- INDEXES FOR PERFORMANCE
-- ============================================================

CREATE INDEX idx_member_group ON Member(group_id);
CREATE INDEX idx_member_division ON Member(division_id);
CREATE INDEX idx_member_class ON Member(class_id);
CREATE INDEX idx_member_emp_status ON Member(employment_status);
CREATE INDEX idx_coverage_member ON Member_Coverage(member_id);
CREATE INDEX idx_coverage_plan ON Member_Coverage(plan_id);
CREATE INDEX idx_eligibility_member ON Member_Eligibility(member_id);
CREATE INDEX idx_app_member ON EOI_Application(member_id);
CREATE INDEX idx_app_plan ON EOI_Application(plan_id);
CREATE INDEX idx_app_status ON EOI_Application(application_status);
CREATE INDEX idx_app_workflow ON EOI_Application(workflow_status);
CREATE INDEX idx_exec_app ON Validation_Execution(application_id);
CREATE INDEX idx_result_execution ON Validation_Result(execution_id);
CREATE INDEX idx_result_rule ON Validation_Result(rule_id);
CREATE INDEX idx_exception_app ON Exception_Queue(application_id);
CREATE INDEX idx_exception_underwriter ON Exception_Queue(assigned_underwriter);
CREATE INDEX idx_exception_status ON Exception_Queue(status);
CREATE INDEX idx_workflow_app ON Workflow_History(application_id);
CREATE INDEX idx_audit_app ON Audit_Log(application_id);
CREATE INDEX idx_audit_table ON Audit_Log(table_name, changed_date);

-- ============================================================
-- END OF SCHEMA
-- ============================================================
