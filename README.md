# Project: Data Modelling with Postgres

In this project we practice data modelling with Postgres. As context, a music streaming startup called Sparkify wants  to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Hence, the two tasks are expected from a data engineer:

- Create a database star schema
- Write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

This repository contains three ```.py``` files:
- ```create_tables.py``` that create the necesary tables for the star schema
- ```sql_queries.py``` is a file containing the SQL queries for the creation of the tables and the ETL process. This file is imported by the other to ```.py``` files in this repo.
- ```etl.py``` which contains the main commands for the ETL pipeline. 

## Datasets

Two datasets are used for the ETL pipeline: logs of user activity and metadata of the songs in their app, both in JSON files.
### Song dataset

Each JSON file of this dataset contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are file paths to two files in this dataset.

```
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

````
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud","song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
````

### Log dataset

The second dataset consists of files in JSON of logs from the music streaming app. The log files in the dataset are partitioned by year and month. For example, here are filepaths to two files in this dataset.

````
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
````
And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.

![image](https://video.udacity-data.com/topher/2019/February/5c6c15e9_log-data/log-data.png)