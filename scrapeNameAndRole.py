# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Start the webdriver
#driver = webdriver.Chrome("C:/Users/valerio/Desktop/Courses/LinkedinAuto/chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #starts the webdriver
# Open LinkedIn
driver.get("https://linkedin.com") #open a specific page


time.sleep(2)

# Locate the username and password fields and enter the credentials
username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")

username.send_keys("YOURUSERNAME@gmail.com")
password.send_keys("YOURPASSWORD") 

time.sleep(6)

# Click the submit button to login
submit = driver.find_element(By.XPATH,"//button[@type='submit']").click() #click on the submit button to login

time.sleep(4)


###### end of the login process ################################################

n_pages = 3 # number of pages you want to submit excluding the last one, range is not inclusive

# Loop through each page
for n in range(1,n_pages):
    # *** Add to the next line the page where you want to start to send messages, if you want to use recently added connection just remove +str(n)
    # and add https://www.linkedin.com/mynetwork/invite-connect/connections/
    driver.get("https://www.linkedin.com/search/results/people/?geoUrn=%5B%22104738515%22%5D&origin=FACETED_SEARCH&page=" + str(n))
    time.sleep(4)

       # Initialize an empty list for storing data
    data = []
    # Locate the elements and subtitles
    elements = driver.find_elements(By.CSS_SELECTOR, ".entity-result__title-text")
    subtitles = driver.find_elements(By.CSS_SELECTOR, ".entity-result__primary-subtitle")
    # Select 20 elements and subtitles
    selected_elements = elements[:]
    selected_subtitles = subtitles[:]
   
    # Loop through each element and subtitle
    for element, subtitle in zip(selected_elements, selected_subtitles):
        # Split the name into first and last name
        name_parts = element.text.split(" ")
        first_name = name_parts[0]
        last_name = name_parts[1]
        last_name = last_name.replace("View", "").strip()
        last_name = last_name.replace("'", "").strip()
        role = subtitle.text
        role = role.replace("Current:", "").strip()
        # Append the data to the list
        data.append([first_name, last_name, role])
    # Create a pandas dataframe from the data 
    
    df = pd.DataFrame(data, columns=["First Name", "Last Name", "Role"])
    def extract_company(role):
        separators = [" at ", " en ", " @ ", " presso ", " bij ", " | ", " bei ", " chez "]
        for separator in separators:
            if separator in role:
                return role.split(separator)[1]
        return ""   

  

    def extract_role(role):
        separators = [" at ", " en ", " @ ", " presso ", " bij ", " | ", " bei ", " chez "]
        for separator in separators:
            if separator in role:
                return role.split(separator)[0]
        return role
#extract the company name
    df['Company'] = df['Role'].apply(lambda x: extract_company(x))
    df['Company'] = df['Company'].apply(lambda x: x.split()[:4])
    df['Company'] = df['Company'].apply(lambda x: " ".join(x))
#extract the role
    df['Role'] = df['Role'].apply(lambda x: extract_role(x))
#extract the domain (the first word from Company name)
    df['Domain'] = df['Company'].apply(lambda x: x.split()[0:1])
    df['Domain'] = df['Domain'].apply(lambda x: " ".join(x))
#build the email using the combination of names and domain
    df['Email'] = (df['First Name'] + "." + df['Last Name'] + "@" + df['Domain'].str.replace("'", "") + ".com").str.lower()
    

# Read the existing file into a pandas dataframe
    try:
        existing_df = pd.read_excel("dataToExcel.xlsx")
        # Concatenate the existing data with the new data
        final_df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        # If the file doesn't exist, just write the new data to it
        final_df = df

    # Write the final data to the same excel file
    final_df.to_excel("dataToExcel.xlsx", index=False, sheet_name='Sheet1', engine='openpyxl')
