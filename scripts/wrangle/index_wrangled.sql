
------------------------------------------------------------------
-- accident

CREATE INDEX IF NOT EXISTS "accident-idx-summary_nr"
    ON accident(summary_nr);


CREATE INDEX IF NOT EXISTS "accident-idx-reporting_id"
    ON accident(reporting_id);

CREATE INDEX IF NOT EXISTS "accident-idx-event_date"
    ON accident(event_date);



------------------------------------------------------------------
-- accident_abstract
CREATE INDEX IF NOT EXISTS "accident_abstract-idx-summary_nr"
    ON accident_abstract(summary_nr);




------------------------------------------------------------------
-- inspection
CREATE INDEX IF NOT EXISTS "inspection-idx-activity_nr"
    ON inspection(activity_nr);


CREATE INDEX IF NOT EXISTS "inspection-idx-reporting_id"
    ON inspection(reporting_id);

CREATE INDEX IF NOT EXISTS "inspection-idx-open_date"
    ON inspection(open_date);

CREATE INDEX IF NOT EXISTS "inspection-idx-sic_code"
    ON inspection(sic_code);

CREATE INDEX IF NOT EXISTS "inspection-idx-naics_code"
    ON inspection(naics_code);

-- related_activity
CREATE INDEX IF NOT EXISTS "related_activity-idx-activity_nr"
    ON related_activity(activity_nr);

CREATE INDEX IF NOT EXISTS "related_activity-idx-rel_act_nr"
    ON related_activity(rel_act_nr);

-- violation_gen_duty_std
CREATE INDEX IF NOT EXISTS "violation_gen_duty_std-idx-activity_nr_citation_id"
    ON violation_gen_duty_std(activity_nr, citation_id);





/*
CREATE INDEX IF NOT EXISTS "TABLE_NAME-idx-IDX_NAME"
    ON TABLE_NAME(FIELDNAME);
*/
