import pymysql
import haversine as hs
import pandas as pd
from geopy.geocoders import Nominatim
import datetime
from .database_connection import db_host, db_user, db_password, database_name

def job_search(title_input, special_input, loc_input, date_posted_input):
    nom = Nominatim(user_agent="cas_ron@yahoo.com")
    country_code = ""
    loc_latitude = ""
    loc_longitude = ""
    date_value = ""

    if loc_input != "":
        try:
            location = nom.geocode(loc_input)
            loc_latitude = location.latitude
            loc_longitude = location.longitude
        except:
            country_code = "error"

        if country_code != "error":
            location = nom.geocode(loc_input)
            lat_long = str(location.latitude) + ", " + str(location.longitude)
            loc_latitude = location.latitude
            loc_longitude = location.longitude
            location_reverse = nom.reverse(lat_long)
            country_code = location_reverse.raw['address']['country_code']

    if (country_code == "ph") or (loc_input == ""):
        input_sql_query = ''
        location_search = False
        special_search = False

        if (title_input == "") and (special_input == "") and (loc_input == ""):
            input_sql_query = "SELECT * FROM job_data"
            print('empty search')
        elif (title_input != "") and (special_input == "") and (loc_input == ""):
            input_sql_query = "SELECT * FROM job_data WHERE job_title LIKE '%" + title_input + "%'"
            print('job title search')
        elif (title_input == "") and (special_input != "") and (loc_input == ""):
            input_sql_query = "SELECT * FROM job_data WHERE special LIKE '%" + special_input + "%'"
            special_search = True
            print('job specialization search')
        elif (title_input == "") and (special_input == "") and (loc_input != ""):
            input_sql_query = "SELECT * FROM job_data"
            location_search = True
            print('location search')
        elif (title_input != "") and (special_input != "") and (loc_input == ""):
            input_sql_query = "SELECT * FROM job_data WHERE job_title LIKE '%" + title_input + "%' AND special LIKE '%" + special_input + "%'"
            special_search = True
            print('title and special search')
        elif (title_input == "") and (special_input != "") and (loc_input != ""):
            input_sql_query = "SELECT * FROM job_data WHERE special LIKE '%" + special_input + "%'"
            special_search = True
            location_search = True
            print('special and location search')
        elif (title_input != "") and (special_input == "") and (loc_input != ""):
            input_sql_query = "SELECT * FROM job_data WHERE job_title LIKE '%" + title_input + "%'"
            location_search = True
            print('title and location search')
        elif (title_input != None) and (special_input != None) and (loc_input != None):
            input_sql_query = "SELECT * FROM job_data WHERE job_title LIKE '%" + title_input + "%' AND special LIKE '%" + special_input + "%'"
            special_search = True
            location_search = True
            print('all search')

        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        start_date = datetime.datetime.strptime(current_date, '%Y-%m-%d %H:%M:%S')
        end_date = ''


        if date_posted_input != "default" and date_posted_input != "":

            if input_sql_query == "SELECT * FROM job_data":
                input_sql_query = input_sql_query + " WHERE "
            else:
                input_sql_query = input_sql_query + " AND "

            # if date_posted_input == 'default':
            #     print('anytime')
            #     end_date = start_date - datetime.timedelta(days=1)
            #     # end_date = datetime.datetime.strptime(end_date, '%m/%d/%y %H:%M:%S')
            #     input_sql_query = input_sql_query + "date_posted < '" + str(
            #         current_date) + "' AND date_posted > '" + str(end_date) + "' ORDER BY `date_posted`"
            #     print(input_sql_query)
            if date_posted_input == '1day':
                print('1day')
                end_date = start_date - datetime.timedelta(days=1)
                # end_date = datetime.datetime.strptime(end_date, '%m/%d/%y %H:%M:%S')
                input_sql_query = input_sql_query + "date_posted < '" + str(
                    current_date) + "' AND date_posted > '" + str(end_date) + "' ORDER BY `date_posted`"
            elif date_posted_input == '3day':
                print('3day')
                end_date = start_date - datetime.timedelta(days=3)
                input_sql_query = input_sql_query + "date_posted < '" + str(
                    current_date) + "' AND date_posted > '" + str(end_date) + "' ORDER BY `date_posted`"
            elif date_posted_input == '1week':
                print('1week')
                end_date = start_date - datetime.timedelta(days=7)
                input_sql_query = input_sql_query + "date_posted < '" + str(
                    current_date) + "' AND date_posted > '" + str(end_date) + "' ORDER BY `date_posted`"
            elif date_posted_input == '2week':
                print('2week')
                end_date = start_date - datetime.timedelta(days=14)
                input_sql_query = input_sql_query + "date_posted < '" + str(
                    current_date) + "' AND date_posted > '" + str(end_date) + "' ORDER BY `date_posted`"
            elif date_posted_input == '1month':
                print('1month')
                end_date = start_date - datetime.timedelta(days=30)
                input_sql_query = input_sql_query + "date_posted < '" + str(
                    current_date) + "' AND date_posted > '" + str(end_date) + "' ORDER BY `date_posted`"


        dbcon = pymysql.connect(host=db_host, user=db_user, password=db_password, database=database_name)

        try:
            SQL_Query = pd.read_sql_query(con=dbcon, sql=input_sql_query)
            df = pd.DataFrame(SQL_Query)
            # return print('The data type of df is: ', type(df))
        except:
            print("Error: unable to convert the data")
            print(input_sql_query)
        dbcon.close()

        filtered_job = []

        if df.empty:
            print('DataFrame is empty!')
            filtered_job = ''
        else:
            for index, item in df.iterrows():
                filtered_job.append(item['id'])


        if location_search is True:
            filtered_job_location = []

            filtered_job.clear()

            for index, row in df.iterrows():
                loc1=(loc_latitude, loc_longitude)
                loc2= (row['latitude'], row['longitude'])
                total_dis = hs.haversine(loc1, loc2)

                if total_dis <= 10:
                    #print(str(total_dis), row['location'])
                    filtered_job.append(row['id'])

            #print(str(hs.haversine(loc1, loc2)) + " " + row['location'])
            #print(row['latitude'], row['longitude'])

        return filtered_job
    else:
        # print('location searched is not within the Philippines!')
        filtered_job = "loc_not_ph"
        return filtered_job
