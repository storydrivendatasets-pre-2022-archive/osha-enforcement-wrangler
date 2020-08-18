### The data attributes of Inspection 1458614.015

As derived from the [inspection detail page #1458614.015](https://www.osha.gov/pls/imis/establishment.inspection_detail?id=1458614.015)

|  Web attribute  |    Value    |
|-----------------|-------------|
| activity_nr     | 1458614.015 |
| report_id       | 0418200     |
| open_date       | 2020-01-29  |
| Union Status    | NonUnion    |
| inspection_type | Referral    |
|                 |             |


As derived from the `inspection` table, though:

```sql
SELECT * FROM inspection WHERE site_address like "1661 Whittle%"
```

| fieldname       | value                           |
| --------------- | ------------------------------- |
| activity_nr     | 344586144                       |
| reporting_id    | 0418200                         |
| estab_name      | GROUP 1 AUTOMOTIVE, INC.        |
| site_address    | 1661 WHITTLESEY RD.             |
| site_city       | COLUMBUS                        |
| site_state      | GA                              |
| site_zip        | 31904                           |
| owner_type      | A                               |
| owner_code      |                                 |
| adv_notice      | 0                               |
| safety_hlth     | S                               |
| sic_code        |                                 |
| naics_code      | 441110                          |
| insp_type       | C                               |
| insp_scope      | B                               |
| why_no_insp     | I                               |
| union_status    | B                               |
| safety_manuf    | 0                               |
| safety_const    | 0                               |
| safety_marit    | 0                               |
| health_manuf    | 0                               |
| health_const    | 0                               |
| health_marit    | 0                               |
| migrant         | 0                               |
| mail_street     | 5800 PEACHTREE INDUSTRIAL BLVD. |
| mail_city       | ATLANTA                         |
| mail_state      | GA                              |
| mail_zip        | 30341                           |
| host_est_key    | HOST_EST_KEY_VALUE              |
| nr_in_estab     | 63                              |
| open_date       | 2020-01-29                      |
| case_mod_date   | 2020-08-09                      |
| close_conf_date | 2020-01-29                      |
| close_case_date |                                 |
| load_dt         | 2020-08-10                      |






### The data attributes of Accident #123478.015


#### Accident data table

As derived from the [accident detail page](https://www.osha.gov/pls/imis/accidentsearch.accident_detail?id=123478.015)



| Web attribute |                        Value                        |
|---------------|-----------------------------------------------------|
| summary_nr    | 123478.015                                          |
| report_id     | 0418200                                             |
| event_date    | 2020-01-22 15:30                                    |
| keywords      | pelvis, fracture, lost balance, finger, ankle, fall |
| event_desc    | Employee Falls From Automotive Lift And Sustains... |
|               |                                                     |


Unfortunately, nothing on the web view of the accident detail corresponds to the `summary_nr` of the record in the `accident` table:

| header        | value                                                        |
| ------------- | ------------------------------------------------------------ |
| summary_nr    | 221234784                                                    |
| reporting_id  | 0418200                                                      |
| event_date    | 2020-01-22 03:01                                             |
| event_desc    | EMPLOYEE FALLS FROM AUTOMOTIVE LIFT AND SUSTAINS MULTIPLE FR |
| event_keyword | PELVIS,LOST BALANCE,FRACTURE,ANKLE,FALL,FINGER               |
| const_end_use |                                                              |
| build_stories |                                                              |
| nonbuild_ht   |                                                              |
| project_cost  |                                                              |
| project_type  |                                                              |
| sic_list      |                                                              |
| fatality      | 0                                                            |
| load_dt       | 2020-08-10                                                   |


From the `accident_injury` table:

```sql
SELECT * FROM accident_injury WHERE summary_nr = '221234784'
```

| fieldname      | value     |
| -------------- | --------- |
| summary_nr     | 221234784 |
| rel_insp_nr    | 344586144 |
| age            | 0         |
| sex            |           |
| nature_of_inj  | 3         |
| part_of_body   | 14        |
| src_of_injury  | 43        |
| event_type     | 5         |
| evn_factor     | 13        |
| hum_factor     | 6         |
| occ_code       | 889       |
| degree_of_inj  | 2         |
| task_assigned  | 2         |
| hazsub         |           |
| const_op       |           |
| const_op_cause |           |
| fat_cause      |           |
| fall_ht        |           |


From `related_activity`

```sql
SELECT * FROM related_activity WHERE activity_nr = '344586144'
```

| fieldname   | value     |
| ----------- | --------- |
| activity_nr | 344586144 |
| rel_type    | R         |
| rel_act_nr  | 001536836 |
| rel_safety  | 1         |
| rel_health  | 0         |



### The data attributes of violation #1458614.015 and 1458614.015 01001



 
