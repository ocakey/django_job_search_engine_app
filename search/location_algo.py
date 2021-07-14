import haversine as hs
import pymysql
import pandas as pd


def location_algo(title_input, special_input, loc_input, list_output):

    dbcon = pymysql.connect(host='localhost', user='root', password='', database='iseek_web')

    try:
        input_sql_query = "SELECT * FROM job_data WHERE job_title LIKE '%" + "audit" + "%'"
        SQL_Query = pd.read_sql_query(con=dbcon, sql=input_sql_query)
        df = pd.DataFrame(SQL_Query)
        # return print('The data type of df is: ', type(df))
    except:
        print("Error: unable to convert the data")
        print(input_sql_query)
    dbcon.close()

    filtered_job_location = []

    for index, row in df.iterrows():
        loc1=(14.594714550386486, 121.04014520925527)
        loc2= (row['latitude'], row['longitude'])
        total_dis = hs.haversine(loc1, loc2)

        if total_dis <= 10:
            #print(str(total_dis), row['location'])
            filtered_job_location.append(row['id'])

    return filtered_job_location
    #print(str(hs.haversine(loc1, loc2)) + " " + row['location'])
    #print(row['latitude'], row['longitude'])