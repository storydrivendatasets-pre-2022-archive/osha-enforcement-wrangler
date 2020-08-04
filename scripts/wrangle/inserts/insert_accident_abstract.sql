INSERT INTO target_db.accident_abstract(
     "summary_nr"
    , "line_count"
    , "abstract_text"
    , "load_dt"
)
WITH orderedtbl AS (
    SELECT *
    FROM src_db.accident_abstract
    ORDER BY
        summary_nr ASC
        , line_nr ASC
)
SELECT
    summary_nr
    , COUNT(1) as line_count
    , GROUP_CONCAT(abstract_text, '') AS abstract_text
    , SUBSTR(MAX(load_dt), 1, 10) AS load_dt
FROM orderedtbl
GROUP BY summary_nr
;

