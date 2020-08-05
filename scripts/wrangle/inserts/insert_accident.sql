INSERT INTO target_db.accident(
    "summary_nr"
    , "reporting_id"
    , "event_date"
    , "event_desc"
    , "event_keyword"
    , "const_end_use"
    , "build_stories"
    , "nonbuild_ht"
    , "project_cost"
    , "project_type"
    , "sic_list"
    , "fatality"
    , "load_dt"
)
SELECT
    LEFT_ZERO_PAD("summary_nr", 9) AS "summary_nr"
    , LEFT_ZERO_PAD("report_id", 7) AS "reporting_id"
    , SUBSTR(event_date, 1, 16)
    , NORMALIZE_TEXT("event_desc") AS "event_desc"
    , REPLACE("event_keyword", ' ,', ',') AS "event_keyword"    -- only trailing whitespace was found
    , "const_end_use"
    , "build_stories"
    , "nonbuild_ht"
    , "project_cost"
    , "project_type"
    , "sic_list"                -- no funny trailing/leading whitespace in comma-delimited list
    , CONVERT_XYN_BOOLEAN("fatality") AS "fatality"
    , SUBSTR(load_dt, 1, 10)
FROM src_db.accident
;
