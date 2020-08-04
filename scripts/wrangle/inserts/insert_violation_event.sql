INSERT INTO target_db.violation_event(
  "activity_nr"
  , "citation_id"
  , "pen_fta"
  , "hist_event"
  , "hist_date"
  , "hist_penalty"
  , "hist_abate_date"
  , "hist_vtype"
  , "hist_insp_nr"
  , "load_dt"
)
SELECT
      "activity_nr"
      , "citation_id"
      , "pen_fta"
      , "hist_event"
      , "hist_date"
      , "hist_penalty"
      , "hist_abate_date"
      , "hist_vtype"
      , "hist_insp_nr"
    , SUBSTR(load_dt, 1, 10)

FROM src_db.violation_event
;
