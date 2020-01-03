from pandas import DataFrame
from bs4 import BeautifulSoup
from .webscrape import *
from .csv_handling import *


class PageSourceParsing(object):
    '''Using BeautifulSoup, this will use take in the search input from views.py and call
    the BrowserControl methods to prepare the page source, process the page source and
    parse the necessary data from the html, and close the browser'''

    @classmethod
    def page_source(cls, search, amount, checked):
        '''This will perform the BeautifulSoup data parsing, close the robot-controlled browser, and be called in views.py'''

        driver = BrowserControl.prepare_page_source(search)     #will begin the webscraping process by opening up the robot-controlled browser to the correct page

        html = driver.page_source   #extracts the page source of the page
        soup = BeautifulSoup(html, 'lxml')  #processes the webpage and creates a useable object
        BrowserControl.close_browser(driver)    #close the robot-controlled browser

        htmlsupplier = soup.find_all('a', {'class': "store-name"})      #selects all elemtents in the page_source that match the given tag and class
        htmlshipping = soup.find_all('span', {'class': "shipping-value"})
        htmltitles = soup.find_all('a', {'class':"item-title"})
        htmlprices = soup.find_all('span', {'class':"price-current"})
        htmlratings = soup.find_all('span', {'class':"rating-value"})
        htmlsold = soup.find_all('a', {'class':"sale-value-link"})

        titles = [x.get_text() for x in htmltitles][:amount]     #extracts the text within each element
        nf_prices = [x.get_text() for x in htmlprices][:amount]       #'nf' for 'not finshed'. These 'nf' lists will be processed in the convert_to_csv function below
        ratings = [x.get_text() for x in htmlratings][:amount]
        nf_sold = [x.get_text() for x in htmlsold][:amount]
        suppliers = [x.get_text() for x in htmlsupplier][:amount]
        nf_shipping = [x.get_text() for x in htmlshipping][:amount]

        CSV_Handling.convert_to_csv(search, amount, checked, titles, nf_prices, ratings, nf_sold, suppliers, nf_shipping) #will convert data into a .csv file

    @classmethod
    def list_refresh(cls, specific_list, element):
        '''This will be used to refresh the lists in views.py'''
        specific_list.clear()
        specific_list.append(element)
