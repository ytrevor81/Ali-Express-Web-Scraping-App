from .models import *


class DB_Handling(object):
    '''All functionality directly related to the database is located here'''

    @classmethod
    def save_to_db(cls, filename, username, products, prices, ratings, sold, suppliers, shipping):
        '''Takes in the lists of csv columns from CSV_Handling and submits the data to the database'''
        if shipping == None:
            submission = AliSubmission(User=username, Products=products, Prices=prices, Ratings=ratings, Sold=sold, Suppliers=suppliers, Search=filename)
        else:
            submission = AliSubmission(User=username, Products=products, Prices=prices, Ratings=ratings, Sold=sold, Suppliers=suppliers, Shipping=shipping, Search=filename)
        submission.save()

    @classmethod
    def history_queries(cls, username):
        pass

    @classmethod
    def csv_download_query(cls, username):
        pass
