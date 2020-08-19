
## Process

- Given an accident and an event_date, find the summary_nr
- With summary_nr, lookup rel_insp_nr in accident_injury
- with rel_insp_nr, find inspection



### random process sql notes

Starting with:
https://www.osha.gov/pls/imis/accidentsearch.accident_detail?id=121039.015

```
SELECT *
FROM accident
where reporting_id = '0453730'
order by event_date DESC;

-- summary_nr: 221211246

-- select * from accident_abstract where summary_nr = '221210396';

select * from accident_injury where summary_nr = '221210396';
-- rel_insp_nr = 344372941

select * from inspection where activity_nr = '344372941'

select * from related_activity where activity_nr = '344372941'
```

`related_activity`

| activity_nr | rel_type | rel_act_nr | rel_safety | rel_health |
| ----------- | -------- | ---------- | ---------- | ---------- |
| 344372941   | R        | 001508134  | 1          | 0          |
| 344372941   | A        | 001511903  | 0          | 0          |


Now with `related_activity.rel_act_nr`...we find related inspections??










## Putting it together in SQL

- 1458614.015 inspection detail??
- 123478.015 accident detail id?

Find the inspection (how to find the activity_nr??)

```sh
SELECT *
FROM inspection 
where activity_nr = '344586144'
;
```


Find connected violation and violation_event

```sh
SELECT *
FROM violation 
where activity_nr = '344586144'
;


SELECT *
FROM violation_event 
where activity_nr = '344586144'
;
```


### Accident???


```sh
SELECT *
FROM accident_injury
WHERE rel_insp_nr like '344586144';
```

reveals `summary_nr` as : `221234784`


```sh
SELECT *
FROM accident
WHERE summary_nr like '221234784'
```
