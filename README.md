# ScrapeNameAndRoleFromLinkedin
Un Selenium/Python program to scrape name from a linkedin page and the following and append all in one excel sheet


This script logs into a LinkedIn account, navigates to a LinkedIn search results page, and retrieves the name, last name, and role of each of the 20 first people listed on the page.
It then appends the retrieved data to an excel file named "datoToExcel.xlsx". If the file does not exist, it creates it.
The excel file is stored in the same sheet named 'Sheet1'.

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
    random: used to generate random numbers

The script starts by creating an instance of the Chrome web driver and navigating to the LinkedIn homepage.
Next, the script logs into the LinkedIn account by locating the username and password text fields and sending the corresponding values.

After logging in, the script retrieves the name, last name, and role of each of the 20 first people listed on the LinkedIn search results page n_pages times.
Each iteration, the script retrieves the data, creates a new set of data scraped from a linkedin page
