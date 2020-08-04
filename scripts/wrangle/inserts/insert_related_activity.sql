INSERT INTO target_db.related_activity(
  "activity_nr"
  , "rel_type"
  , "rel_act_nr"
  , "rel_safety"
  , "rel_health"
--  , "load_dt"
)
SELECT
"activity_nr"
  , "rel_type"
  , "rel_act_nr"
  , CONVERT_XYN_BOOLEAN("rel_safety")
  , CONVERT_XYN_BOOLEAN("rel_health")
--  , SUBSTR(load_dt, 1, 10)

FROM src_db.related_activity
;
