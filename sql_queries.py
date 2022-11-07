# DROP TABLES

songplay_table_drop = "DROP table songlays"
user_table_drop = "DROP table users"
song_table_drop = "DROP table songs"
artist_table_drop = "DROP table artists"
time_table_drop = "DROP table time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXIST songplays (\
                        songplay_id serial PRIMARY_KEY,\
                        start_time int, \
                        user_id int NOT NULL, \
                        level int, \
                        song_id int NOT NULL, \
                        artis_id int NOT NULL, \
                        session_id int NOT NULL, \
                        location varchar, \
                        user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXIST users (\
                    user_id serial PRIMARY_KEY,\
                    first_name varchar NOT NULL,\
                    last_name varchar NOT NULL, \
                    gender varchar, \
                    level int);""")


song_table_create = ("""CREATE TABLE IF NOT EXIST songs (\
                    song_id serial PRIMARY KEY, \
                    title varchar NOT NULL,\
                    artist_id int NOT NULL, \
                    year int, \
                    duration timestamp NOT NULL);""")

artist_table_create = ("""CREATE TABLE IF NOT EXIST artists (\
                    artist_id serial PRIMARY KEY, \
                    name varchar NOT NULL,\
                    location varchar, \
                    year int, \
                    duration decimal NOT NULL, \
                    latitude decimal, \
                    longitude decimal);""")

time_table_create = ("""CREATE TABLE IF NT EXIST time (\
                    start_time time_stamp PRIMARY KEY, \
                    hour time_stamp NOT NULL,\
                    day int NOT NULL, \
                    week int NOT NULL, \
                    month int NOT NULL, \
                    year int NOT NULL, \
                    weekday varchar);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id,\
                                                    start_time,
                                                    used_id,
                                                    level,
                                                    song_id,
                                                    artist_id,
                                                    session_id,
                                                    location,
                                                    user_agent)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                ON CONFLICT (songplay_id)
                                DO NOTHINGF;""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (user_id)
                        DO NOTHING;""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)\
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (song_id)
                        DO NOTHING;""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude)\
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (artist_id)
                        DO NOTHING;""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)\
                        VALUES (%s, %s, %s, %s, %s, %s, %s)""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id
                FROM songs AS s JOIN artists AS a 
                    ON s.artist_id = a.artis_id""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, 
                        song_table_create, artist_table_create, 
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop,
                      artist_table_drop, time_table_drop]