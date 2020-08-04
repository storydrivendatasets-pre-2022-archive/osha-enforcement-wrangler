

## Notes on Trimming the compiled raw data and converting to wrangled db

Each subhed notes things that have to be changed for the `wrangled_schema.sql`

### accident

- always null: abstract_text, event_time, state_flag
- event_date trim seconds value

### accident_abstract
- connects to accident via summary_nr

### accident_injury
- always null: fall_distance
- not needed?: line_nr – since we concat all the lines in accident_abstract

### accident_lookup2
- load_dt: load_date
- rename table to accident_lookup

### inspection
- always null: state_flag
- bool ('X' vs BLANK): safety_manuf,safety_const,safety_marit,safety_manuf,health_const,health_marit,migrant
- bool Y/N/NULL: adv_notice
- load_dt: ld_dt

### optional_info
opt_info_id: all blanks
opt_type:    always 'N'

### related_activity
- bool: rel_safety, rel_health

### strategic codes

### violation
- bool: emphasis,delete_flag

### violation_event

### violation_gen_duty_std



## Future work


### Can we remove load_dt from most tables?

Figure out how much of space savings this is:

Are any load_dt's between related reports out of sync?

The following returns 4045 non-synced records for 762 summary_nr



```sql
CREATE INDEX IF NOT EXISTS accident_idx_sumdate ON accident(summary_nr, load_dt );
CREATE INDEX IF NOT EXISTS accident_injury_idx_sumdate ON accident_injury(summary_nr, load_dt);
CREATE INDEX IF NOT EXISTS accident_abstract_idx_sumdate ON accident_abstract(summary_nr, load_dt);

WITH nonsyncs AS (
    SELECT 
        tx.summary_nr AS summary_nr
        , tx.load_dt
        , ty.load_dt AS abstract_dt
        , tz.load_dt AS injury_dt 
    FROM
        accident AS tx
    LEFT JOIN
        accident_abstract AS ty
        ON tx.summary_nr = ty.summary_nr
            AND SUBSTR(tx.load_dt, 1, 10) != SUBSTR(ty.load_dt, 1, 10)
    LEFT JOIN
        accident_injury AS tz
        ON tx.summary_nr = tz.summary_nr
            AND SUBSTR(tx.load_dt, 1, 10) != SUBSTR(tz.load_dt, 1, 10)

    WHERE    
        (ty.summary_nr IS NOT NULL 
            OR tz.summary_nr IS NOT NULL)
        AND NOT (ty.summary_nr IS NULL AND tz.summary_nr IS NULL)
    ORDER BY
        tx.summary_nr, tx.load_dt, ty.load_dt
)
SELECT COUNT(1)
FROM nonsyncs
GROUP BY summary_nr
;
```
