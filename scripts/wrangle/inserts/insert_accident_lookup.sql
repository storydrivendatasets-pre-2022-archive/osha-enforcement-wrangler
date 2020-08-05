INSERT INTO target_db.accident_lookup(
    "accident_code"
    , "accident_number"
    , "accident_value"
    , "accident_letter"
--    , "load_dt"
)
SELECT
    "accident_code"
    , "accident_number"
    , NORMALIZE_TEXT("accident_value") as "accident_value"
    , "accident_letter"
--    , SUBSTR(load_date, 1, 10)

FROM src_db.accident_lookup2
;
