INSERT INTO target_db.optional_info(
  "activity_nr"
  , "opt_id"
  , "opt_value"
--  ,"load_dt"
)
SELECT
  "activity_nr"
  , "opt_id"
  , "opt_value"
--  , SUBSTR(load_dt, 1, 10)

FROM src_db.optional_info
;


