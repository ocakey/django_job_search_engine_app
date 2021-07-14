import pandas as pd
import pymysql
import numpy as np
import geopandas as gpd

import matplotlib.pyplot as plt
import seaborn as sns

import folium

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from datetime import datetime, timedelta
from .database_connection import db_host, db_user, db_password, database_name

# # Store the data
# # df = pd.read_csv('totaldata.csv')
# # Show the first 3 rows of data
# # df.head(10)
# # print(df.shape)
#
# dbcon = pymysql.connect(host=db_host, user=db_user, password=db_password, database=database_name)
# try:
#     SQL_Query = pd.read_sql_query(con=dbcon, sql="SELECT * FROM job_data WHERE special='unavailable'")
#     df = pd.DataFrame(SQL_Query)
#     # return print('The data type of df is: ', type(df))
#     print(df.shape)
# except:
#     print("Error: unable to convert the data")
# dbcon.close()
# date_scraped = "16d ago"
#
# num_extract = ""
# num_show = ""
# for c in date_scraped:
#     if c.isdigit():
#         num_extract = num_extract + c
# # print("Extracted numbers from the list : " + num)
#
# # print(str.find('h'))
#
# if date_scraped.find('s') != -1:
#     print("Extracted numbers from the list : " + num_extract)
#     print("s only")
#     last_hour_date_time = datetime.now() - timedelta(seconds=int(num_extract))
# elif date_scraped.find('m') != -1:
#     print("Extracted numbers from the list : " + num_extract)
#     print("s only")
#     last_hour_date_time = datetime.now() - timedelta(minutes=int(num_extract))
# elif date_scraped.find('h') != -1:
#     print("Extracted numbers from the list : " + num_extract)
#     print("hour only")
#     last_hour_date_time = datetime.now() - timedelta(hours=int(num_extract))
# else:
#     print("Extracted numbers from the list : " + num_extract)
#     print("day only")
#     last_hour_date_time = datetime.now() - timedelta(days=int(num_extract))

# dbcon = pymysql.connect(host=db_host, user=db_user, password=db_password, database=database_name)
# try:
#     SQL_Query = pd.read_sql_query(con=dbcon, sql="SELECT * FROM job_data")
#     df = pd.DataFrame(SQL_Query)
#     # return print('The data type of df is: ', type(df))
#     print(df.shape)
# except:
#     print("Error: unable to convert the data")
# dbcon.close()

def time_changed(data_results):
    time_converted = []
    df_list_result = []
    df_list_result = data_results

    df_list_result_raw = str(df_list_result).replace('[', '(')
    df_list_result_raw = str(df_list_result_raw).replace(']', ')')
    # print(df_list_result_raw)



    dbcon = pymysql.connect(host=db_host, user=db_user, password=db_password, database=database_name)
    try:
        df = []
        SQL_Query = pd.read_sql_query(con=dbcon, sql="SELECT * FROM job_data WHERE id IN " + df_list_result_raw)
        df = pd.DataFrame(SQL_Query)
        # return print('The data type of df is: ', type(df))
        print("data converted")
    except:
        print("Error: unable to convert the data")
    dbcon.close()

    if len(df) != 0:
        for index, item in df.iterrows():
            # last_hour_date_time = datetime.now() - timedelta(hours=1)
            # data_date_raw = last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S')
            # print(item)
            # data_date_raw = '2021-07-10 15:58:07'



            data_date_raw = str(item['date_posted']).replace('T', ' ')
            job_date_raw = []
            job_date_raw = str(data_date_raw).split('.')
            # data_date_raw = job_date_raw[0]
            current_date_raw = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            data_date = []
            current_date = []
            data_date = data_date_raw.split(' ')
            current_date = current_date_raw.split(' ')

            # tdelta = datetime.strptime(current_date[1], "%H:%M:%S") - datetime.strptime(data_date[1],"%H:%M:%S")
            tdelta = datetime.strptime(current_date_raw, '%Y-%m-%d %H:%M:%S') - datetime.strptime(job_date_raw[0],
                                                                                                  '%Y-%m-%d %H:%M:%S')
            # print(tdelta)
            tdelta = str(tdelta)
            # print(tdelta)
            time_show = []
            time_interval = ""
            if tdelta.find('-') != -1:
                print("advance date")
            else:
                if tdelta.find(',') != -1:
                    time_show = tdelta.split(',')
                    # print("day and time " + time_show[0])
                    num_show = ''
                    for c in time_show[0]:
                        if c.isdigit():
                            num_show = num_show + c
                    time_interval = num_show + "d ago"
                else:
                    time_show = tdelta.split(':')
                    if time_show[0] != "0":
                        print("hour only")
                        time_interval = time_show[0] + 'h ago'
                    elif time_show[0] == "0" and time_show[1] != "00":
                        print("minute only")
                        time_interval = time_show[1] + 'm ago'
                    elif time_show[0] == "0" and time_show[1] == "00":
                        print("second only")
                        time_interval = time_show[2] + 's ago'
            # print(time_interval)
            time_converted.append([item['id'], time_interval])
        # return time_converted
        # print(time_converted)
        char = '1'
        # [item[0] for item in time_converted]
        # for item in time_converted:
        #     if char == str(item[0]):
        #         print(str(item[1]))
        return time_converted
    else:
        return time_converted
    # return df_list_result
