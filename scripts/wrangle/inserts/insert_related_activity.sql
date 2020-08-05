INSERT INTO target_db.related_activity(
  "activity_nr"
  , "rel_type"
  , "rel_act_nr"
  , "rel_safety"
  , "rel_health"
--  , "load_dt"
)
SELECT
  LEFT_ZERO_PAD("activity_nr", 9) AS "activity_nr"
  , "rel_type"
  , LEFT_ZERO_PAD("rel_act_nr", 9) AS "rel_act_nr"
  , CONVERT_XYN_BOOLEAN("rel_safety")
  , CONVERT_XYN_BOOLEAN("rel_health")
--  , SUBSTR(load_dt, 1, 10)

FROM src_db.related_activity
;
