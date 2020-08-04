CREATE INDEX IF NOT EXISTS accident_abstract_idx_NR
    ON accident_abstract(summary_nr, line_nr);


CREATE INDEX IF NOT EXISTS violation_gen_duty_std_idx_NR
    ON violation_gen_duty_std(activity_nr, citation_id, line_nr);

