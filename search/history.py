import pymysql
from .database_connection import db_host, db_user, db_password, database_name
import datetime
import pandas as pd


def recent_search(job_title, job_special, location, ip_add, user_agent):
    start_date = datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S')
    current_date = datetime.datetime.strptime(start_date, '%m/%d/%y %H:%M:%S')
    end_date = current_date + datetime.timedelta(days=1)

    exp_date = end_date

    # print(job_title)
    # print(job_special)
    # print(location)
    # print(ip_add)
    # print(user_agent)
    # print(exp_date)

    try:
        dbcon = pymysql.connect(host=db_host, user=db_user, password=db_password, database=database_name)
        cur = dbcon.cursor()
        # dbcon.open
        cur.execute(
            "INSERT INTO user_history (job_title, special, location, ip_address, user_agent, exp_date) VALUES (%s, %s, %s, %s, %s, %s)",
            (job_title, job_special, location, ip_add, user_agent, exp_date))
        dbcon.commit()
        print("Data Inserted: history.py / recent_search")
        dbcon.close()
        # df = pd.DataFrame(SQL_Query)
        # return print('The data type of df is: ', type(df))
    except pymysql.Error as e:
        print(e.args)
        print("Error: unable to insert the data: history.py / recent_search")
        print(e.args)


def existing_search(ip_add, user_agent):
    filtered_search = []
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        dbcon = pymysql.connect(host=db_host, user=db_user, password=db_password, database=database_name)
        input_sql_query = "SELECT * FROM user_history WHERE ip_address = '" + ip_add + "' AND user_agent = '" + user_agent + "' AND exp_date >= '" + current_date + "' ORDER BY exp_date DESC"
        #input_sql_query = "SELECT * FROM user_history"
        sql_query = pd.read_sql_query(con=dbcon, sql=input_sql_query)
        df = pd.DataFrame(sql_query)
        for index, item in df.iterrows():
            filtered_search.append(item['id'])
        # print(filtered_search)
        # # return print('The data type of df is: ', type(df))
        dbcon.close()
    except Exception as e:
        print("Error: unable to insert the data: history.py / existing_search")
        print(e.args)

    return filtered_search

