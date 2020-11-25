# Ali Express Web Scraping App

A Django web app that extracts and parses the HTML of an AliExpress.com product query page. The user receives a CSV file of all product info from the page and can save their data in a PostgreSQL database.

# Technologies:
Django | Beautiful Soup (BS4) | PostgreSQL | Selenium | Bootstrap CSS | JQuery | HTML

# Notable Features:
- All functionality dealing with web scraping, using Beaufitul Soup (for retrieving the page's html) and Selenium (via Google Chrome webdriver), is located in webscrape.py
- Parsing the page's html using Beautiful Soup (BS4) is located in data_parser.py
- Functionality converting the parsed data into a CSV file is located in csv_handling.py 
- All PostgreSQL database handling is located in db_handling.py
- Authenticated users have the option to save their data in a PostgreSQL database and can email their CSV file to themselves.

![aliexpress](https://user-images.githubusercontent.com/46886041/77186894-2e5c5400-6b06-11ea-83f0-3faf1137867b.JPG)

# How the App Works:
1. <i>Without user authentication</i>, any user can type a product name in the search bar, choose on the slider how many products from the query page they want included in the CSV file, and check the option of having Free Shipping information available in the CSV file.

2. Clicking the "Collect Data" button will web scrape an aliexpress.com query page, using the user's query from the search bar. 

3. Once the HTML of the aliexpress.com page is successfully parsed, a CSV file can be downloaded by the user by clicking the "Download CSV" button.

4. <i>With user authentication</i>, the user has the option to email their CSV file to themselves by clicking the "Email CSV" button. 

5. The authenticated user can also save thier CSV data in a PostgreSQL database and access their data at a later time, utilizing the "History" section.

# Due to AliExpress.com recently strengthening protections against web scraping, this app no longer works as is. I have decided to focus my time and attention on other projects. This is why there is no active link available for this project.
