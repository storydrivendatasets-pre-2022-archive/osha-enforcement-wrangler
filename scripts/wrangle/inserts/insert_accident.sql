INSERT INTO target_db.accident(
    "summary_nr"
    , "report_id"
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
    "summary_nr"
    , "report_id"
    , SUBSTR(event_date, 1, 16)
    , "event_desc"
    , "event_keyword"
    , "const_end_use"
    , "build_stories"
    , "nonbuild_ht"
    , "project_cost"
    , "project_type"
    , "sic_list"
    , "fatality"
    , SUBSTR(load_dt, 1, 10)
FROM src_db.accident
;
