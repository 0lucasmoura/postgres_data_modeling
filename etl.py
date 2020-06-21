import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

# supress pandas futurewarning messages
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def process_song_file(cur, filepath):
    """
        Process a file with songs in it and puts them on a database.
        
        params:
        cur: A cursor to execute queries into the database
        filepath: the absolute path of the file
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = [value if type(value).__name__ in dir(__builtins__) else value.item() 
                 for value in df.loc[0, ['song_id', 'title', 'artist_id', 'year', 'duration']].values]
    song_data = [value if value == value else None for value in song_data]
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_data = [value if type(value).__name__ in dir(__builtins__) else value.item() 
                  for value in df.loc[0, ['artist_id', 'artist_name', 'artist_location', 'latitude', 'artist_longitude']].values]
    artist_data = [value if value == value else None for value in artist_data] 
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
        Process a file with logs of users in it and puts them on a database.
        
        params:
        cur: A cursor to execute queries into the database
        filepath: the absolute path of the file
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df = df[df.page == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df.ts, unit='ms')
    
    # insert time data records
    time_data = (t.values, t.dt.hour.values, t.dt.day.values, t.dt.weekofyear.values, t.dt.month.values, t.dt.year.values, t.dt.weekday.values)
    column_labels = ('timestamp', 'hour', 'day', 'week_of_year', 'month', 'year', 'weekday') 
    time_df = time_df = pd.DataFrame(list(map(list, zip(*time_data))), columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = user_df = df.loc[:, ['userId', 'firstName', 'lastName', 'gender', 'level']]
    user_df = user_df.where(pd.notna(user_df), None)

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data =  (pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
        An entry function to process all the data from users log and songs.
        
        params:
        cur: A cursor to execute queries into the database
        conn: A conneciton object with the database to commit the queries of data inserts
        filepath: the filepath from the parent file with data 
        func: a function to process the files.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
       This script connects to the sparkifydb database, process the logs and songs files and insert all the data into the DB.
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
