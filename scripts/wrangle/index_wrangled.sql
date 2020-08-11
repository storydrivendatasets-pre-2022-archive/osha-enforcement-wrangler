
------------------------------------------------------------------
-- accident

-- ALREADY PRIMARY KEY:
-- CREATE INDEX IF NOT EXISTS "accident-idx-summary_nr"
--     ON accident(summary_nr);


CREATE INDEX IF NOT EXISTS "accident-idx-reporting_id"
    ON accident(reporting_id);

CREATE INDEX IF NOT EXISTS "accident-idx-event_date"
    ON accident(event_date);



------------------------------------------------------------------
-- accident_abstract
-- ALREADY PRIMARY KEY:
-- CREATE INDEX IF NOT EXISTS "accident_abstract-idx-summary_nr"
--     ON accident_abstract(summary_nr);


------------------------------------------------------------------
-- accident_injury
CREATE INDEX IF NOT EXISTS "accident_injury-idx-summary_nr-rel_insp_nr"
    ON accident_injury(summary_nr, rel_insp_nr);


------------------------------------------------------------------
-- accident_lookup
CREATE INDEX IF NOT EXISTS "accident_lookup-idx-accident_code-accident_number"
    ON accident_lookup(accident_code, accident_number);


------------------------------------------------------------------
-- inspection

-- ALREADY PRIMARY KEY:
-- CREATE INDEX IF NOT EXISTS "inspection-idx-activity_nr"
--     ON inspection(activity_nr);


CREATE INDEX IF NOT EXISTS "inspection-idx-reporting_id"
    ON inspection(reporting_id);

CREATE INDEX IF NOT EXISTS "inspection-idx-open_date"
    ON inspection(open_date);

CREATE INDEX IF NOT EXISTS "inspection-idx-close_case_date"
    ON inspection(close_case_date);


CREATE INDEX IF NOT EXISTS "inspection-idx-sic_code"
    ON inspection(sic_code);

CREATE INDEX IF NOT EXISTS "inspection-idx-naics_code"
    ON inspection(naics_code);


-----------------------------------
-- optional_info
CREATE INDEX IF NOT EXISTS "optional_info-idx-activity_nr"
    ON optional_info(activity_nr);



-----------------------------------
-- related_activity
CREATE INDEX IF NOT EXISTS "related_activity-idx-activity_nr"
    ON related_activity(activity_nr);

CREATE INDEX IF NOT EXISTS "related_activity-idx-rel_act_nr"
    ON related_activity(rel_act_nr);

CREATE INDEX IF NOT EXISTS "related_activity-idx-activity_nr-rel_act_nr"
    ON related_activity(activity_nr, rel_act_nr);



-----------------------------------
-- strategic_codes
-----------------------------------
CREATE INDEX IF NOT EXISTS "strategic_codes-idx-activity_nr"
    ON strategic_codes(activity_nr);


-----------------------------------
-- violation
-----------------------------------

-- ALREADY PRIMARY KEY:
-- CREATE INDEX IF NOT EXISTS "violation-idx-activity_nr-citation_id"
--     ON violation(activity_nr, citation_id);



CREATE INDEX IF NOT EXISTS "violation-idx-issuance_date"
    ON violation(issuance_date);

CREATE INDEX IF NOT EXISTS "violation-idx-abate_date"
    ON violation(abate_date);


CREATE INDEX IF NOT EXISTS "violation-idx-standard"
    ON violation(standard);


-----------------------------------
-- violation_event
-----------------------------------
CREATE INDEX IF NOT EXISTS "violation_event-idx-activity_nr-citation_id"
    ON violation_event(activity_nr, citation_id);

CREATE INDEX IF NOT EXISTS "violation_event-idx-hist_date"
    ON violation_event(hist_date);

CREATE INDEX IF NOT EXISTS "violation_event-idx-hist_abate_date"
    ON violation_event(hist_abate_date);



----------------------------------------------------------------------
-- violation_gen_duty_std
----------------------------------------------------------------------

-- ALREADY PRIMARY KEY:
-- CREATE INDEX IF NOT EXISTS "violation_gen_duty_std-idx-activity_nr_citation_id"
--     ON violation_gen_duty_std(activity_nr, citation_id);





/*
-----------------------------------
-- TABLE_NAME
-----------------------------------
CREATE INDEX IF NOT EXISTS "TABLE_NAME-idx-IDX_NAME"
    ON TABLE_NAME(FIELDNAME);
*/
