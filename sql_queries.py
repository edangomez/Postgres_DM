# DROP TABLES

songplay_table_drop = "DROP table songlays"
user_table_drop = "DROP table users"
song_table_drop = "DROP table songs"
artist_table_drop = "DROP table artists"
time_table_drop = "DROP table time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXTIS songplays (songplay_id int,\
                        start_time int, user_id int, level int, song_id int, \
                        artis_id int, session_id int, location varchar, \
                        user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXTIS user (user_id int, first_name varchar,\
                        last_name varchar, gender varchar, level int);""")


song_table_create = ("""CREATE TABLE IF NOT EXTIS song (song_id int, title varchar,\
                    artist_id int, year int, duration );""")

artist_table_create = ("""
""")

time_table_create = ("""
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

create_table_queries = [songplay_table_create, user_table_create, 
                        song_table_create, artist_table_create, 
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop,
                      artist_table_drop, time_table_drop]