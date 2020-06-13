# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id int NOT NULL, 
                                                                 start_time int NOT NULL, 
                                                                 user_id int NOT NULL, 
                                                                 level varchar NOT NULL, 
                                                                 song_id int NOT NULL, 
                                                                 artist_id int NOT NULL, 
                                                                 session_id int NOT NULL, 
                                                                 location varchar NOT NULL, 
                                                                 user_agent varchar NOT NULL);
                        """)

user_table_create = ("""
                     CREATE TABLE IF NOT EXISTS users (user_id int NOT NULL, 
                                                      first_name varchar NOT NULL, 
                                                      last_name varchar NOT NULL, 
                                                      gender varchar NOT NULL, 
                                                      level varchar NOT NULL);
                    """)

song_table_create = ("""
                    CREATE TABLE IF NOT EXISTS songs (song_id int NOT NULL, 
                                                     title varchar NOT NULL, 
                                                     artist_id int NOT NULL, 
                                                     year int NOT NULL, 
                                                     duration int NOT NULL);
                    """)

artist_table_create = ("""
                       CREATE TABLE IF NOT EXISTS artists (artist_id int NOT NULL, 
                                                           name varchar NOT NULL, 
                                                           location varchar NOT NULL, 
                                                           latitude int, 
                                                           longitude int);
                      """)

time_table_create = ("""
                     CREATE TABLE IF NOT EXISTS time (start_time int NOT NULL,
                                                     hour int NOT NULL, 
                                                     day int NOT NULL, 
                                                     week int NOT NULL, 
                                                     month int NOT NULL,
                                                     year int NOT NULL,
                                                     weekday varchar NOT NULL);
                    """)

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]