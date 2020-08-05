CREATE TABLE IF NOT EXISTS "accident" (
  "summary_nr" CHAR(9) PRIMARY KEY,              -- Identifies the accident OSHA-170 form
  "reporting_id" CHAR(7) NOT NULL,               -- Identifies the OSHA federal or state reporting jurisdiction|original name was "report_id"
  "event_date" DATETIME NOT NULL,
-- always NULL  "event_time" INTEGER,
  "event_desc" VARCHAR(100),                     -- Short description of event (60 is official max length)
  "event_keyword" VARCHAR(255),                  -- Contains comma separated keywords entered by ERG during the review process.
  "const_end_use" CHAR(1),                       -- Construction - end-use (code table ENDU)| enum letters A-Q
  "build_stories" INTEGER,                       -- Construction - nr of stories in building
  "nonbuild_ht" INTEGER,                         -- Construction - height in feet when not a building
  "project_cost" CHAR(1),                        -- Construction - project cost range (code table COST)| enum letters A-G
  "project_type" CHAR(1),                        -- Construction - project type (code table PTYP)| enum letters A-E
  "sic_list" VARCHAR(40),                               -- Comma separated 4-digit SICs associated with related inspections
  "fatality" BOOLEAN,
-- always NULL  "state_flag" INTEGER,
-- always NULL  "abstract_text" INTEGER,
  "load_dt" DATE NOT NULL
);;--


CREATE TABLE IF NOT EXISTS "accident_abstract" (
  "summary_nr" CHAR(9) NOT NULL,
-- obsolete  "line_nr" INTEGER NOT NULL,
  "line_count" INTEGER NOT NULL, -- result of group count
  "abstract_text" TEXT,
  "load_dt" DATE NOT NULL
);;--

CREATE TABLE IF NOT EXISTS "accident_injury" (
  "summary_nr" CHAR(9) NOT NULL,
  "rel_insp_nr" CHAR(9)  NOT NULL,
  "age" SMALLINT,
  "sex" CHAR(1),
  "nature_of_inj" SMALLINT,    -- Part of body code - code table BD| max length 2
  "part_of_body" SMALLINT,     -- Occupation code - code table OCC| max length 3
  "src_of_injury" SMALLINT,    -- Source of injury code - code table SO| max length 2
  "event_type" SMALLINT,       -- Event type code - code table FT| max length 2
  "evn_factor" INTEGER,       -- Environmental factor code - code table EN; max length 2
  "hum_factor" SMALLINT,       -- Human factor code - code table HU; max length 2
  "occ_code" SMALLINT,         -- Occupation code - code table OCC; max length 3
  "degree_of_inj" SMALLINT,    -- 1=Fatality. 2=Hospitalized injuries. 3=No Hospitalized injuries; ENUM
  "task_assigned" SMALLINT,    -- 1=Task regularly assigned. 2=Task not regularly assigned
  "hazsub" CHAR(4),             -- Hazardous substance code
  "const_op" SMALLINT,          -- Construction - operation code (code table OPER)| max length 2
  "const_op_cause" SMALLINT,    -- Construction - cause of injury (code table OPER)| max length 2
  "fat_cause" SMALLINT,          -- Construction - cause of fatality (code table CAUS)| max length 2
-- always NULL  fall_distance INTEGER,
  "fall_ht" SMALLINT             -- Construction - height of person when fell (feet); max length 4
-- unneeded  injury_line_nr INTEGER NOT NULL,
 -- "load_dt" DATE NOT NULL
);;--

CREATE TABLE IF NOT EXISTS "accident_lookup" (
  "accident_code" VARCHAR(4)  NOT NULL,
  "accident_number" INTEGER,              -- maxlength 4
  "accident_value"  VARCHAR NOT NULL,
  "accident_letter" CHAR(1)
--  "load_dt" DATE NOT NULL
);;--


CREATE TABLE IF NOT EXISTS "inspection" (
  "activity_nr" CHAR(9) NOT NULL,                     -- Unique identifier for the inspection
  "reporting_id" CHAR(7) NOT NULL,                    -- Identifies the OSHA federal or state reporting jurisdiction
-- always NULL  "state_flag" INTEGER,
  "estab_name" VARCHAR(200),                          -- Establishment being inspected
  "site_address" VARCHAR(200),
  "site_city" VARCHAR(200),
  "site_state" CHAR(3),                               -- includes non states like JQ, UK, CZ, MN, AS
  "site_zip" CHAR(5),
  "owner_type" CHAR(1),                               -- ENUM A=Private. B=LocalGovt. C=StateGovt. D=Federal
  "owner_code" CHAR(4),                               -- Used for owner=D only
  "adv_notice" BOOLEAN,                               -- Advance Notice Y/N/blank
  "safety_hlth" CHAR(1),                              -- ENUM Safety/Health indicator (S=Safety. H=Health)
  "sic_code" CHAR(4),
  "naics_code" CHAR(6),
  "insp_type" CHAR(1),                                --ENUM A=Accident. B=Complaint. C=Referral. D=Monitoring. E=Variance. F=FollowUp. G=Unprog Rel. H=Planned. I=Prog Related. J=Unprog Other. K=Prog Other. L=Other-L. M=Fat/Cat
  "insp_scope" CHAR(1),                                --ENUM A=Complete.B=Partial.C=Records.D=NoInspection
  "why_no_insp" CHAR(1),                                -- ENUM A=No Insp/Not Found.B=No Insp/Out of Business.C=No Insp/Process Inactive.D=No Insp/10 or Fewer Empe.E=No Insp/Denied Entry.F=No Insp/SIC not on PG.G=No Insp/Exempt Voluntary.H=No Insp/NonExempt Consult.I=No Insp/Other.J=No Insp/Employer Exempted By Appropriation Act
  "union_status" CHAR(1),                             -- ENUM Indicates union representation during inspection (Yes=Y/U/A. No=N/B/blank)
  "safety_manuf" BOOLEAN,
  "safety_const" BOOLEAN,
  "safety_marit" BOOLEAN,
  "health_manuf" BOOLEAN,
  "health_const" BOOLEAN,
  "health_marit" BOOLEAN,
  "migrant" BOOLEAN,
  "mail_street" VARCHAR(200),
  "mail_city" VARCHAR(200),
  "mail_state" CHAR(3),
  "mail_zip" CHAR(5),
  "host_est_key" VARCHAR(20),                                -- Internal establishment key
  "nr_in_estab" INTEGER,                              -- Number of employees in establishment
  "open_date" DATE NOT NULL,
  "case_mod_date" DATE,
  "close_conf_date" DATE,
  "close_case_date" DATE,
  "load_dt" DATE NOT NULL
);;--


CREATE TABLE IF NOT EXISTS "optional_info" (
  "activity_nr" CHAR(9) NOT NULL,
  -- ALWAYS N "opt_type" TEXT,
  "opt_id" INTEGER,                                     -- Optional Information ID| max length of 2
  "opt_value" VARCHAR(50)                               -- Identifies the optional information type (only N type included)
  -- ALWAYS NULL"opt_info_id" INTEGER,
--  "load_dt" DATE NOT NULL
);;--

CREATE TABLE IF NOT EXISTS "related_activity" (
  "activity_nr" CHAR(9) NOT NULL,                           -- Identifies the parent inspection
  "rel_type" CHAR(1),                                    -- C=Complaint.I=Inspection.R=Referral.A=Accident
  "rel_act_nr" CHAR(9),
  "rel_safety" BOOLEAN,
  "rel_health" BOOLEAN
--  "load_dt" DATE NOT NULL
);;--


CREATE TABLE IF NOT EXISTS "strategic_codes" (
  "activity_nr" CHAR(9) NOT NULL,                 -- Identifies the parent inspection
  "prog_type" CHAR(1) NOT NULL,                   -- N=NEP (National Emphasis Program).L=LEP (Local Emphasis Program).S=Strategic Plan Code
  "prog_value" CHAR(30) NOT NULL                      -- Code value
--  "load_dt" DATE NOT NULL
);;--

CREATE TABLE IF NOT EXISTS "violation" (
  "activity_nr" CHAR(9) NOT NULL,
  "citation_id" CHAR(7) NOT NULL,
  "delete_flag" BOOLEAN,
  "standard" CHAR(25),                                  -- The OSHA standard violated
  "viol_type" CHAR(1),                                  -- S=Serious.W=Willful.R=Repeat.O=Other| has additional undocument fields like U,F,P,H
  "issuance_date" DATE  NOT NULL,
  "abate_date" DATE,
  "abate_complete" CHAR(1),                             -- Q=Quick Fix.X=Abatement Completed.I=Corrected During Inspection.E=Not Completed - Employer out of business.W=Not Changed - Worksite changed.S=Not Completed - Solicitor advised.A=Not Completed - AD discretion
  "current_penalty" DECIMAL(16, 2),
  "initial_penalty" DECIMAL(16, 2),
  "contest_date" DATE,
  "final_order_date" DATE,
  "nr_instances" INTEGER,
  "nr_exposed" INTEGER,
  "rec" CHAR(1),                                         -- A=Accident.C=Complaint.I=Imminent Danger.R=Referral.V=Variance
  "gravity" INTEGER,
  "emphasis" BOOLEAN,
  "hazcat" VARCHAR(10),                                         -- General industry standard hazard category
  "fta_insp_nr" INTEGER,
  "fta_issuance_date" DATE,
  "fta_penalty" DECIMAL(16, 2),
  "fta_contest_date" DATE,
  "fta_final_order_date" DATE,
  "hazsub1" CHAR(4),
  "hazsub2" CHAR(4),
  "hazsub3" CHAR(4),
  "hazsub4" CHAR(4),
  "hazsub5" CHAR(4),
  "load_dt" DATE NOT NULL
);;--

CREATE TABLE IF NOT EXISTS "violation_event" (
  "activity_nr" CHAR(9) NOT NULL,
  "citation_id" CHAR(7) NOT NULL,                     -- Identifies the citation number. item number. and item group of the associated citation.
  "pen_fta" CHAR(1),                                  -- P=Penalty. F=FTA
  "hist_event" CHAR(1),
  "hist_date" DATE,
  "hist_penalty" DECIMAL(16, 2),
  "hist_abate_date" DATE,                            -- Abatement date (yyyymmdd) - when pen-fta=P
  "hist_vtype" CHAR(1),
  "hist_insp_nr" CHAR(9),                            -- FTA inspection nr -when pen-fta=F
  "load_dt" DATE NOT NULL
);;--

CREATE TABLE IF NOT EXISTS "violation_gen_duty_std" (
  "activity_nr" CHAR(9) NOT NULL,
  "citation_id" CHAR(7) NOT NULL,
  -- obsoleted by group count "line_nr" INTEGER NOT NULL,
  "line_text" TEXT,
  "line_count" SMALLINT NOT NULL, -- derived from group count
  "start_line_nr" SMALLINT NOT NULL,
  "end_line_nr" SMALLINT NOT NULL,
  "load_dt" DATE NOT NULL
);;--
