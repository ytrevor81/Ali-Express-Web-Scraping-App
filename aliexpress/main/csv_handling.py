import pandas
from django.core.mail import EmailMessage


class CSV_Handling(object):
    '''All functionality dealing with .csv file handling is addressed in this class'''

    @classmethod
    def boolean_convert(cls, get_request):
        if get_request == "True":
            get_request = True
        else:
            get_request = False
        return get_request

    @classmethod
    def convert_to_csv(cls, search, checked, titles, nf_prices, rating, nf_sold, suppliers, nf_shipping):
        '''Converts all the list data into a .csv file, and if the checked parameter doesn't equal None,
        the .csv file will have an extra column for 'Free Shipping' information'''

        prices = [i.replace('US $', '') for i in nf_prices]     #these 3 list comprehensions will process the data from each 'not finished' list into correct format
        sold = [i.replace(' Sold', '') for i in nf_sold]
        shipping = ["XXX" if i == "Free Shipping" else '-' for i in nf_shipping]
        print(len(titles), len(prices), len(rating), len(sold), len(suppliers), len(shipping))
        ratings = CSV_Handling.ratings_fix(rating)

        if checked != None:     #pandas will convert these lists into a usable table
            df = pandas.DataFrame({'Product': titles, 'Price': prices, 'Rating':ratings, 'Sold':sold, 'Supplier':suppliers, 'Free_Shipping': shipping})
        else:
            df = pandas.DataFrame({'Product': titles, 'Price': prices, 'Rating':ratings, 'Sold':sold, 'Supplier':suppliers})     #if 'free shipping' is not checked, the data will not be included in the .csv
        df.index += 1
        df.to_csv('C://Users/User/Desktop/Ali-Express-Web-Scraping-App/aliexpress/main/static/csv_files/{}.csv'.format(search), index=True)     #THIS WILL PATH WILL CHANGE IN DEPLOYMENT

    @classmethod
    def ratings_fix(cls, rating):
        '''TEMPORARY FIX -- Appends the ratings list until the length reaches 60 elements'''
        if len(rating) != 60:
            print('Beginning while loop')
            while len(rating) != 60:
                rating.append('-')
            ratings = rating
            return ratings
        else:
            return rating

    @classmethod
    def email_csv_file(cls, filename, user_email):
        body = "From your '{}' product search on (date)".format(filename)
        message = EmailMessage("AliExpress Webscraper Date .csv", body ,"aliexpressscrapingapp@gmail.com",["{}".format(user_email)])
        message.attach_file('C://Users/User/desktop/ali-express-web-scraping-app/aliexpress/main/static/csv_files/{}.csv'.format(filename))
        message.send()

    @classmethod
    def csv_to_db(cls, filename, username):
        data = pandas.read_csv('C://Users/User/Desktop/Ali-Express-Web-Scraping-App/aliexpress/main/static/csv_files/tobacco.csv')
        prices = data.Price.tolist()
        ratings = data.Rating.tolist()
        suppliers = data.Supplier.tolist()
        shipping = data.Free_Shipping.tolist() #catch error is not list

        integers = data.Sold.tolist()
        sold = [str(x) for x in integers]

        encoding_mess = data.Product.tolist()
        bstrings = [x.encode('utf-8') for x in encoding_mess]
        unfinshed_str = [str(x) for x in bstrings]
        products = [x.replace("b", '').replace("'", '') for x in unfinshed_str]

        DB_Handling.save_to_db(filename, username, products, prices, ratings, sold, suppliers, shipping)

    @classmethod
    def db_to_csv(cls):
        pass
