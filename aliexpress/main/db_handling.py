from .models import *

class DB_Handling(object):
    '''All functionality directly related to the database is located here'''

    @classmethod
    def save_to_db(cls, filename, username, products, prices, ratings, sold, suppliers, shipping):
        '''Takes in the lists of csv columns from CSV_Handling and submits the data to the database'''
        if shipping == False:
            submission = AliSubmission(User=username, Products=products, Prices=prices, Ratings=ratings, Sold=sold, Suppliers=suppliers, Search=filename)
        else:
            submission = AliSubmission(User=username, Products=products, Prices=prices, Ratings=ratings, Sold=sold, Suppliers=suppliers, Shipping=shipping, Search=filename)
        submission.save()

    @classmethod
    def db_to_csvlist(cls, username, id):
        '''This returns a list of lists, made from extracting specific queries from
        the database'''
        query = AliSubmission.objects.filter(User=username, id=id)
        for prop in query:
            search = prop.Search    #each of these are lists
            products = prop.Products
            prices = prop.Prices
            ratings = prop.Ratings
            sold = prop.Sold
            suppliers = prop.Suppliers
        return [search, products, prices, ratings, sold, suppliers]     #list of lists to be converted to a csv file

    @classmethod
    def delete_from_db(cls, username, id):
        '''Deletes a selected past query for the user'''
        query = AliSubmission.objects.filter(User=username, id=id)  #id is probably good enough, but I wanted to include username to ensure accuracy
        query.delete()
        print('Deleted')
