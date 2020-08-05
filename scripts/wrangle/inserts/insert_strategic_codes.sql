INSERT INTO target_db.strategic_codes(
  "activity_nr"
  , "prog_type"
  , "prog_value"
--  , "load_dt"
)
SELECT
      LEFT_ZERO_PAD("activity_nr", 9) AS "activity_nr"
    , "prog_type"
    , "prog_value"
--    , SUBSTR(load_dt, 1, 10)

FROM src_db.strategic_codes
;
