# Data modeling with postgres

This is the first project of Udacity Data Engineer Nanodegree program and consists of data modeling a star schema for a startup called Sparkify.

Sparkify is a data driven music stream service! That means that all its strategics decisions, in all levels of the company, are taken based on the data produced by its users, by the company itself and data from outside.

This data has to be set up in a form that sparkify analysts are able to perform good insights and work their magic around it. This is the task of the data engineer team, and this project tackles this. The objective is to create an etl pipeline to load user data and songs/artists data into a database.

The analysis of the used data was made in the notebook `etl.ipynb` and tests to see if data was loaded in `test.ipynb`

The database is modeled as a [star schema](https://en.wikipedia.org/wiki/Star_schema) and thats shown belown:

[image]

All the queries used in this project are on `sql_queries.py`


## How to run this project

Firstly: 
In your terminal: Run `python3 create_tables.py` 

Secondly:
In your terminal: Run `python3 etl.py` 

## How the DB could be used

Any data analyst of Sparkify could run these queries to retrieve some intesresting meaningful data that could answer some questions and bring forth some good insights.

---

#1 How many paid users vs free users we have??
```sql
SELECT Count(user_id),
       Trunc(Count(user_id) * 100.0 / Sum(Count(*)) OVER(), 3) AS percentage,
       level
FROM   songplays
GROUP  BY level; 
```
This gives good strategic data to estimate the company expense!
The result:

[QUERY 1]

---

#2 What is the gender proportion of users and their levels?
```sql
SELECT Count(gender),
       Trunc(Count(gender) * 100.0 / Sum(Count(*)) OVER(), 3) AS percentage,
       gender,
       level
FROM   users
GROUP  BY gender,
          level; 
```
This result is important to understand the demographics of sparkify users. 
The result:

[QUERY 2]

---

#3 What are the locations where users are using sparkify?

By region:
```sql
SELECT Count(Split_part(location, ',', 1)),
       Split_part(location, ',', 1) region,
       Split_part(location, ',', 2) state
FROM   songplays
GROUP  BY region,
          state
ORDER  BY count DESC;
```
By state:
``` sql
SELECT Count(Split_part(location, ',', 2)),
       Split_part(location, ',', 2) state
FROM   songplays
GROUP  BY state
ORDER  BY count DESC;
```
This can give some input on demographics based on geography. Many decisions can taken based on this result. For instance, if sparkify wants to launch a campaign on certain region to bring more users to the service and then see its effects.
The result:
[QUERY 3.1]
[QUERY 3.2]

---

#4 What time of the day does Sparkify have more active users?
```sql
SELECT t.hour,
       Count(*)
FROM   songplays s
       LEFT JOIN "time" t
              ON s.start_time = t.start_time
GROUP  BY t.hour
ORDER  BY t.hour; 
```
This is a good way to estimate demographics and also to know when advertise campaings can have more effect for exmaple.
[QUERY 4]
