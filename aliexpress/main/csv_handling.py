import pandas
import os
import numpy as np
from .db_handling import *
from django.core.mail import EmailMessage


class CSV_Handling(object):
    '''All functionality dealing with .csv file handling is addressed in this class'''

    @classmethod
    def boolean_convert(cls, get_request):
        '''Converts a GET request into a boolean value'''
        if get_request == "True":
            get_request = True
        else:
            get_request = False
        return get_request

    @classmethod
    def csv_file_limit(cls, recent_query):
        '''Limits the amount of csv files held in static to 5 files'''
        query = recent_query + ".csv"    #saves the most recent search
        filename = query.replace(" ", "_")  #in case there is whitespace in the query 
        csv_files = [name for name in os.listdir('C://Users/User/Desktop/Ali-Express-Web-Scraping-App/aliexpress/main/static/csv_files')]   #list of all csv file names in the directory
        if len(csv_files) > 5:  #maximum of 5
            for file in csv_files:
                if file != filename:
                    os.remove('C://Users/User/Desktop/Ali-Express-Web-Scraping-App/aliexpress/main/static/csv_files/{}'.format(file))   # deletes all files except for the most recent search

    @classmethod
    def convert_to_csv(cls, search, amount, checked, titles, nf_prices, rating, nf_sold, suppliers, nf_shipping):
        '''Converts all the list data into a .csv file, and if the checked parameter doesn't equal None,
        the .csv file will have an extra column for 'Free Shipping' information'''

        prices = [i.replace('US $', '') for i in nf_prices]     #these 3 list comprehensions will process the data from each 'not finished' list into correct format
        almost_sold = [i.replace(' Sold', '') for i in nf_sold]
        shipping = ["XXX" if i == "Free Shipping" else '-' for i in nf_shipping]
        print(len(titles), len(prices), len(rating), len(almost_sold), len(suppliers), len(shipping))
        ratings = CSV_Handling.missing_elements_fix(amount, rating)
        sold = CSV_Handling.missing_elements_fix(amount, almost_sold)

        if checked != None:     #pandas will convert these lists into a usable table
            df = pandas.DataFrame({'Product': titles, 'Price': prices, 'Rating':ratings, 'Sold':sold, 'Supplier':suppliers, 'Free_Shipping': shipping})
        else:
            df = pandas.DataFrame({'Product': titles, 'Price': prices, 'Rating':ratings, 'Sold':sold, 'Supplier':suppliers})     #if 'free shipping' is not checked, the data will not be included in the .csv
        df.index += 1
        df.to_csv('C://Users/User/Desktop/Ali-Express-Web-Scraping-App/aliexpress/main/static/csv_files/{}.csv'.format(search.replace(" ", "_")), index=True)     #THIS WILL PATH WILL CHANGE IN DEPLOYMENT

    @classmethod
    def missing_elements_fix(cls, amount, string_list):
        '''This will eentually be fixed if enough people use this app--if the ratings or amount sold list come up shorter
        than the specified product amount, then '-' will be added to the list until it list length reaches the
        specified amount'''
        if len(string_list) != amount:
            print('Beginning while loop')
            while len(string_list) != amount:
                string_list.append('-')
            corrected_list = string_list
            return corrected_list
        else:
            return string_list

    @classmethod
    def email_csv_file(cls, filename, user_email):
        '''Emails the most recent query to the user's email'''
        body = "From your '{}' product search".format(filename)     #body of the email
        message = EmailMessage("AliExpress Webscraper .csv", body ,"aliexpressscrapingapp@gmail.com",[user_email])  #title, body, exporter, user email
        message.attach_file('C://Users/User/desktop/ali-express-web-scraping-app/aliexpress/main/static/csv_files/{}.csv'.format(filename.replace(" ", "_")))     #attaches desired csv file to email
        message.send()

    @classmethod
    def csv_to_db(cls, filename, username, checked):
        '''Extracts all columns from the desired csv file and exports them as lists'''
        data = pandas.read_csv('C://Users/User/Desktop/Ali-Express-Web-Scraping-App/aliexpress/main/static/csv_files/{}.csv'.format(filename.replace(" ", "_")))
        prices = data.Price.tolist()    #price, ratings, suppliers, and free shipping lists can be extracted as is, no problem
        ratings = data.Rating.tolist()
        suppliers = data.Supplier.tolist()
        if checked == True:
            shipping = data.Free_Shipping.tolist()
        else:
            shipping = False

        integers = data.Sold.tolist()   #elements of this list need to be changed to string types
        sold = [str(x) for x in integers]   #usable for db save

        encoding_mess = data.Product.tolist()   #for some reason, the products list always has an encoding problem.
        bstrings = [x.encode('utf-8') for x in encoding_mess]   #changes these elements to b' strings
        unfinshed_str = [str(x) for x in bstrings]  #changes to normalstring types, but the b' is still attached to each element
        products = [x.replace("b", '').replace("'", '') for x in unfinshed_str]     #usable for db save

        DB_Handling.save_to_db(filename, username, products, prices, ratings, sold, suppliers, shipping)    #handles the real db saving

    @classmethod
    def history_to_csv(cls, username, id):
        '''Converts all the list data into a .csv file, and if the checked parameter doesn't equal None,
        the .csv file will have an extra column for 'Free Shipping' information'''
        csv_list = DB_Handling.db_to_csvlist(username, id)
        search = csv_list[0]
        products = eval(csv_list[1])    #im not exactly sure why eval(x) works, but is allows these lists to be usable for pandas. otherwise, an error is raised
        prices = eval(csv_list[2])
        ratings = eval(csv_list[3])
        sold = eval(csv_list[4])
        suppliers = eval(csv_list[5])
        df = pandas.DataFrame({'Product': products, 'Price': prices, 'Rating':ratings, 'Sold':sold, 'Supplier':suppliers})
        df.index += 1
        df.to_csv('C://Users/User/Desktop/Ali-Express-Web-Scraping-App/aliexpress/main/static/csv_files/{}.csv'.format(search.replace(" ", "_")), index=True)     #THIS WILL PATH WILL CHANGE IN DEPLOYMENT
