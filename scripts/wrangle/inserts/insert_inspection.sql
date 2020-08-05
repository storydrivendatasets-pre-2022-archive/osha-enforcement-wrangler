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
      LEFT_ZERO_PAD("activity_nr", 9) AS "activity_nr"
    , LEFT_ZERO_PAD("reporting_id", 7) AS "reporting_id"
    , NORMALIZE_TEXT("estab_name")
    , NORMALIZE_TEXT("site_address")
    , NORMALIZE_TEXT("site_city")
    , "site_state"
    , LEFT_ZERO_PAD("site_zip", 5) AS "site_zip"
    , "owner_type"
    , LEFT_ZERO_PAD("owner_code", 4)
    , CONVERT_XYN_BOOLEAN("adv_notice") AS "adv_notice"
    , "safety_hlth"
    , LEFT_ZERO_PAD("sic_code", 4)
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
    , NORMALIZE_TEXT("mail_street") AS "mail_street"
    , NORMALIZE_TEXT("mail_city") AS "mail_city"
    , "mail_state"
    , LEFT_ZERO_PAD("mail_zip", 5) AS "mail_zip"
    , "host_est_key"
    , "nr_in_estab"
    , "open_date"
    , "case_mod_date"
    , "close_conf_date"
    , "close_case_date"
    , SUBSTR("ld_dt", 1, 10) AS "load_dt"

FROM src_db.inspection
;
