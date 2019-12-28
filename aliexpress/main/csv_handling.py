from django.http import HttpResponse
from pandas import DataFrame
from django.views.static import serve


class CSV_Handling(object):
    '''All functionality dealing with .csv file handling is addressed in this class'''

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
            df = DataFrame({'Product': titles, 'Price': prices, 'Rating':ratings, '# Sold':sold, 'Supplier':suppliers, 'Free Shipping': shipping})
        else:
            df = DataFrame({'Product': titles, 'Price': prices, 'Rating':ratings, '# Sold':sold, 'Supplier':suppliers})     #if 'free shipping' is not checked, the data will not be included in the .csv
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
