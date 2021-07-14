import pandas as pd
import geojson
import pymysql
from .database_connection import db_host, db_user, db_password, database_name
import os


def data2geojson(id_list):
    df_list_result = []
    df_list_result = id_list

    if os.path.exists("data.geojson"):
        os.remove("data.geojson")
    else:
        print("The file does not exist")

    if len(df_list_result) != 0:

        df_list_result_raw = str(df_list_result).replace('[', '(')
        df_list_result_raw = str(df_list_result_raw).replace(']', ')')

        dbcon = pymysql.connect(host=db_host, user=db_user, password=db_password, database=database_name)
        try:
            SQL_Query = pd.read_sql_query(con=dbcon, sql="SELECT * FROM job_data WHERE id IN " + df_list_result_raw)
            df = pd.DataFrame(SQL_Query)
            # return print('The data type of df is: ', type(df))
            print(df.shape)
        except:
            print("Error: unable to convert the data")
        dbcon.close()

        def file_create(self):
            print("testttt")
            features = []
            insert_features = lambda X: features.append(
                geojson.Feature(geometry=geojson.Point((X["longitude"],
                                                        X["latitude"])),
                                properties=dict(name=X["job_title"],
                                                city=X["location"])))
            df.apply(insert_features, axis=1)
            with open('data.geojson', 'w', encoding='utf8') as fp:
                geojson.dump(geojson.FeatureCollection(features), fp, sort_keys=True, ensure_ascii=False)

            # col = ['lat','long','elev','name','description']
            # data = [[-29.9953,-70.5867,760,'A','Place ñ'],
            #         [-30.1217,-70.4933,1250,'B','Place b'],
            #         [-30.0953,-70.5008,1185,'C','Place c']]

            # df = pd.DataFrame(data, columns=col)

        file_create(df)
