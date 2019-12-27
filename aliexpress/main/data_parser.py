from pandas import DataFrame
from bs4 import BeautifulSoup
from .webscrape import *


class PageSourceParsing(object):
    '''Using BeautifulSoup, this will use take in the search input from views.py and call
    the BrowserControl methods to prepare the page source, process the page source and
    parse the necessary data from the html, and close the browser'''

    @classmethod
    def convert_to_csv(cls, search, checked, titles, nf_prices, ratings, nf_sold, suppliers, nf_shipping):
        '''Converts all the list data into a .csv file, and if the checked parameter doesn't equal None,
        the .csv file will have an extra column for 'Free Shipping' information'''

        prices = [i.replace('US $', '') for i in nf_prices]     #these 3 list comprehensions will process the data from each 'not finished' list into correct format
        sold = [i.replace(' Sold', '') for i in nf_sold]
        shipping = ["XXX" if i == "Free Shipping" else '-' for i in nf_shipping]

        if checked != None:
            df = DataFrame({'Product': titles, 'Price': prices, 'Rating':ratings, '# Sold':sold, 'Supplier':supplier, 'Free Shipping': shipping})
        else:
            df = DataFrame({'Product': titles, 'Price': prices, 'Rating':ratings, '# Sold':sold, 'Supplier':supplier})
        df.index += 1
        df.to_csv('{}.csv'.format(search), index=True)


    @classmethod
    def page_source(cls, search, checked):
        '''This will perform the BeautifulSoup data parsing, close the robot-controlled browser, and be called in views.py'''

        driver = BrowserControl.prepare_page_source(search)     #will begin the webscraping process by opening up the robot-controlled browser to the correct page

        html = driver.page_source   #extracts the page source of the page
        soup = BeautifulSoup(html, 'lxml')  #processes the webpage and creates a useable object
        BrowserControl.close_browser(driver)    #close the robot-controlled browser

        htmlsupplier = soup.find_all('a', {'class': "store-name"})      #selects all elemtents in the page_source that match the given tag and class
        hmtlshipping = soup.find_all('span', {'class': "shipping-value"})
        htmltitles = soup.find_all('a', {'class':"item-title"})
        htmlprices = soup.find_all('span', {'class':"price-current"})
        htmlratings = soup.find_all('span', {'class':"rating-value"})
        htmlsold = soup.find_all('a', {'class':"sale-value-link"})

        titles = [x.get_text() for x in htmltitles]     #extracts the text within each element
        nf_prices = [x.get_text() for x in htmlprices]      #'nf' for 'not finshed'. These 'nf' lists will be processed in the convert_to_csv function below
        ratings = [x.get_text() for x in htmlratings]
        nf_sold = [x.get_text() for x in htmlsold]
        suppliers = [x.get_text() for x in htmlsupplier]
        nf_shipping = [x.get_text() for x in htmlshipping]

        self.convert_to_csv(checked, titles, nf_prices, ratings, nf_sold, suppliers, nf_shipping) #will convert data into a .csv file
