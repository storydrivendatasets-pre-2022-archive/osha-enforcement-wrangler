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
  LEFT_ZERO_PAD("activity_nr", 9) AS "activity_nr"
  , LEFT_ZERO_PAD("citation_id", 7) AS "citation_id"
  , "pen_fta"
  , "hist_event"
  , "hist_date"
  , "hist_penalty"
  , "hist_abate_date"
  , "hist_vtype"
  , LEFT_ZERO_PAD("hist_insp_nr", 9) AS "hist_insp_nr"
  , SUBSTR(load_dt, 1, 10)

FROM src_db.violation_event
;
