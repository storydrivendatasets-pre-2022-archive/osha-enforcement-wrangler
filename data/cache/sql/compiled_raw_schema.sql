CREATE TABLE IF NOT EXISTS "accident" (
  "summary_nr" INTEGER NOT NULL,
  "report_id" INTEGER NOT NULL,
  "event_date" TEXT NOT NULL,
  "event_time" INTEGER,
  "event_desc" TEXT,
  "event_keyword" TEXT,
  "const_end_use" TEXT,
  "build_stories" INTEGER,
  "nonbuild_ht" INTEGER,
  "project_cost" TEXT,
  "project_type" TEXT,
  "sic_list" TEXT,
  "fatality" TEXT,
  "state_flag" INTEGER,
  "abstract_text" INTEGER,
  "load_dt" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "accident_abstract" (
  "summary_nr" INTEGER NOT NULL,
  "line_nr" INTEGER NOT NULL,
  "abstract_text" TEXT,
  "load_dt" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "accident_injury" (
  "summary_nr" INTEGER NOT NULL,
  "rel_insp_nr" INTEGER  NOT NULL,
  "age" INTEGER,
  "sex" TEXT,
  "nature_of_inj" INTEGER,
  "part_of_body" INTEGER,
  "src_of_injury" INTEGER,
  "event_type" INTEGER,
  "evn_factor" INTEGER,
  "hum_factor" INTEGER,
  "occ_code" INTEGER,
  "degree_of_inj" INTEGER,
  "task_assigned" INTEGER,
  "hazsub" TEXT,
  "const_op" INTEGER,
  "const_op_cause" INTEGER,
  "fat_cause" INTEGER,
  "fall_distance" INTEGER,
  "fall_ht" INTEGER,
  "injury_line_nr" INTEGER NOT NULL,
  "load_dt" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "accident_lookup2" (
  "accident_code" TEXT  NOT NULL,
  "accident_number" INTEGER,
  "accident_value" TEXT NOT NULL,
  "accident_letter" TEXT,
  "load_dt" TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS "inspection" (
"activity_nr" INTEGER NOT NULL,
  "reporting_id" INTEGER NOT NULL,
  "state_flag" INTEGER,
  "estab_name" TEXT,
  "site_address" TEXT,
  "site_city" TEXT,
  "site_state" TEXT,
  "site_zip" INTEGER,
  "owner_type" TEXT,
  "owner_code" INTEGER,
  "adv_notice" TEXT,
  "safety_hlth" TEXT,
  "sic_code" INTEGER,
  "naics_code" INTEGER,
  "insp_type" TEXT,
  "insp_scope" TEXT,
  "why_no_insp" TEXT,
  "union_status" TEXT,
  "safety_manuf" TEXT,
  "safety_const" TEXT,
  "safety_marit" TEXT,
  "health_manuf" TEXT,
  "health_const" TEXT,
  "health_marit" TEXT,
  "migrant" TEXT,
  "mail_street" TEXT,
  "mail_city" TEXT,
  "mail_state" TEXT,
  "mail_zip" INTEGER,
  "host_est_key" TEXT,
  "nr_in_estab" INTEGER,
  "open_date" TEXT NOT NULL,
  "case_mod_date" TEXT,
  "close_conf_date" TEXT,
  "close_case_date" TEXT,
  "load_dt" TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS "optional_info" (
"activity_nr" INTEGER NOT NULL,
  "opt_type" TEXT,
  "opt_id" INTEGER,
  "opt_value" TEXT,
  "opt_info_id" INTEGER,
  "load_dt" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "related_activity" (
"activity_nr" INTEGER NOT NULL,
  "rel_type" TEXT,
  "rel_act_nr" INTEGER,
  "rel_safety" TEXT,
  "rel_health" TEXT,
  "load_dt" TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS "strategic_codes" (
"activity_nr" INTEGER NOT NULL,
  "prog_type" TEXT NOT NULL,
  "prog_value" TEXT NOT NULL,
  "load_dt" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "violation" (
  "activity_nr" INTEGER NOT NULL,
  "citation_id" TEXT NOT NULL,
  "delete_flag" TEXT,
  "standard" TEXT,
  "viol_type" TEXT,
  "issuance_date" TEXT  NOT NULL,
  "abate_date" TEXT,
  "abate_complete" TEXT,
  "current_penalty" REAL,
  "initial_penalty" REAL,
  "contest_date" TEXT,
  "final_order_date" TEXT,
  "nr_instances" INTEGER,
  "nr_exposed" INTEGER,
  "rec" TEXT,
  "gravity" INTEGER,
  "emphasis" TEXT,
  "hazcat" TEXT,
  "fta_insp_nr" INTEGER,
  "fta_issuance_date" TEXT,
  "fta_penalty" REAL,
  "fta_contest_date" TEXT,
  "fta_final_order_date" TEXT,
  "hazsub1" TEXT,
  "hazsub2" TEXT,
  "hazsub3" TEXT,
  "hazsub4" TEXT,
  "hazsub5" TEXT,
  "load_dt" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "violation_event" (
  "activity_nr" INTEGER NOT NULL,
  "citation_id" TEXT NOT NULL,
  "pen_fta" TEXT,
  "hist_event" TEXT,
  "hist_date" TEXT,
  "hist_penalty" REAL,
  "hist_abate_date" TEXT,
  "hist_vtype" TEXT,
  "hist_insp_nr" INTEGER,
  "load_dt" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "violation_gen_duty_std" (
  "activity_nr" INTEGER NOT NULL,
  "citation_id" TEXT NOT NULL,
  "line_nr" INTEGER NOT NULL,
  "line_text" TEXT,
  "load_dt" TEXT NOT NULL
);
