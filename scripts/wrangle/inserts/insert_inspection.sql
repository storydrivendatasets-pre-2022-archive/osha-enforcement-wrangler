-- bool ('X' vs BLANK): safety_manuf,safety_const,safety_marit
--                      ,health_const,health_marit,migrant
--  bool Y/N/NULL: adv_notice

INSERT INTO target_db.inspection(
    "activity_nr"
    , "reporting_id"
    , "estab_name"
    , "site_address"
    , "site_city"
    , "site_state"
    , "site_zip"
    , "owner_type"
    , "owner_code"
    , "adv_notice"
    , "safety_hlth"
    , "sic_code"
    , "naics_code"
    , "insp_type"
    , "insp_scope"
    , "why_no_insp"
    , "union_status"
    , "safety_manuf"
    , "safety_const"
    , "safety_marit"
    , "health_manuf"
    , "health_const"
    , "health_marit"
    , "migrant"
    , "mail_street"
    , "mail_city"
    , "mail_state"
    , "mail_zip"
    , "host_est_key"
    , "nr_in_estab"
    , "open_date"
    , "case_mod_date"
    , "close_conf_date"
    , "close_case_date"
    , "load_dt"
)
SELECT
    "activity_nr"
    , "reporting_id"
    , "estab_name"
    , "site_address"
    , "site_city"
    , "site_state"
    , "site_zip"
    , "owner_type"
    , "owner_code"
    , "adv_notice"
    , "safety_hlth"
    , "sic_code"
    , "naics_code"
    , "insp_type"
    , "insp_scope"
    , "why_no_insp"
    , "union_status"
    , CONVERT_XYN_BOOLEAN("safety_manuf")
    , CONVERT_XYN_BOOLEAN("safety_const")
    , CONVERT_XYN_BOOLEAN("safety_marit")
    , CONVERT_XYN_BOOLEAN("health_manuf")
    , CONVERT_XYN_BOOLEAN("health_const")
    , CONVERT_XYN_BOOLEAN("health_marit")
    , CONVERT_XYN_BOOLEAN("migrant")
    , "mail_street"
    , "mail_city"
    , "mail_state"
    , "mail_zip"
    , "host_est_key"
    , "nr_in_estab"
    , "open_date"
    , "case_mod_date"
    , "close_conf_date"
    , "close_case_date"
    , SUBSTR("ld_dt", 1, 10) AS "load_dt"

FROM src_db.inspection
;
