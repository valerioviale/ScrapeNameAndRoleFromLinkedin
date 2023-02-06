#This program has been created for education pourpose since the different companies have different strategies and policies regarding scraping data
#If you are using for commercial porpouse better to check specifically if that practice is allowed.
Just to know that is a delicate matter be aware for example of this article:
https://www.forbes.com/sites/zacharysmith/2022/04/18/scraping-data-from-linkedin-profiles-is-legal-appeals-court-rules/?sh=61ec0c392a9c

# As you can see the program can be converted to scrape any webpage with the proper change in the syntax.
# ScrapeNameAndRoleFromLinkedin
A Selenium/Python program to scrape name, first name and role at company from a linkedin page and the following and append all in one excel sheet.

What to install? You need Python, Selenium, Webdriver, Pandas, Time. You can install them using pip:

pip install selenium webdriver_manager pandas time
pip install xlrd


This script logs into a LinkedIn account, navigates to a LinkedIn search results page, and retrieves the name, last name, and role of each of the people listed on the page, then progress to the following page.
It then appends the retrieved data to an excel file named "datoToExcel.xlsx". If the file does not exist, it creates it.
The excel file is created/stored in the same folder you save the python file.

The following libraries are imported:

    selenium: used to automate web browsing
    selenium.webdriver.common.keys: used to interact with form elements such as text fields
    selenium.webdriver.support.expected_conditions: used to wait for certain conditions to be met before proceeding with execution
    selenium.webdriver.common.by: used to specify the type of search method to locate an element
    selenium.webdriver.support.wait: used to wait for an element to appear on the page
    selenium.webdriver.chrome.service: used to manage the chromedriver service
    webdriver_manager.chrome: used to manage the chromedriver installation
    time: used to add delays between actions
    pandas: used to create and store data in dataframes

The script starts by creating an instance of the Chrome web driver and navigating to the LinkedIn homepage.
Next, the script logs into the LinkedIn account by locating the username and password text fields and sending the corresponding values.

After logging in, the script retrieves the name, last name, and role of each of the 10 first people listed on the LinkedIn search results page n_pages times.
Each iteration, the script retrieves the data, creates a new set of data scraped from a linkedin page a paste it in an excel file

If you start the program another time, it is going to append the new data in the same excel file.
