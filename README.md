QUERIES = 


---

#1 qtt of paid users vs free users and its proportion
```sql
SELECT Count(user_id),
       Trunc(Count(user_id) * 100.0 / Sum(Count(*)) OVER(), 3) AS percentage,
       level
FROM   songplays
GROUP  BY level; 
```

---

#2 gender proportion of users and their levels

```sql
SELECT Count(gender),
       Trunc(Count(gender) * 100.0 / Sum(Count(*)) OVER(), 3) AS percentage,
       gender,
       level
FROM   users
GROUP  BY gender,
          level; 
```

---

#3 region with more listening users 
region with less listening users

```sql
SELECT Count(Split_part(location, ',', 1)),
       Split_part(location, ',', 1) region,
       Split_part(location, ',', 2) state
FROM   songplays
GROUP  BY region,
          state
ORDER  BY count DESC;
```
``` sql
SELECT Count(Split_part(location, ',', 2)),
       Split_part(location, ',', 2) state
FROM   songplays
GROUP  BY state
ORDER  BY count DESC;
```
---

#4 time where are played more
```sql
SELECT t.hour,
       Count(*)
FROM   songplays s
       LEFT JOIN "time" t
              ON s.start_time = t.start_time
GROUP  BY t.hour
ORDER  BY t.hour; 
```

blabalbalba
