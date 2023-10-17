# Import necessary modules and packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

# Initialize the Selenium WebDriver service
s = Service(r"C:/Users/1948NM/Documents/chromedriver.exe")

# Create an empty DataFrame to store the scraped data
df = pd.DataFrame(columns=['code'])

# List of URLs to scrape
urls = [
    # Add your list of URLs here
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intro%20to%20Python%20for%20Data%20Science/Instructions/Chapter1.md',
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Intro%20to%20Python%20for%20Data%20Science/Instructions/Chapter2.md',
    # Add more URLs as needed
]

# Loop through each URL in the list
for url in urls:
    # Initialize a new Chrome WebDriver instance
    driver = webdriver.Chrome(service=s)
    
    # Load the URL in the WebDriver
    driver.get(url)
    
    # Find all td elements on the page
    td_elements = driver.find_elements(By.TAG_NAME, value='td')
    
    # Iterate over every other p element starting from the second one
    for i in range(1, len(td_elements), 2):
        # Store the text content of the p element in the DataFrame
        df = df.append({'code': td_elements[i].text}, ignore_index=True)

    # Close the WebDriver instance
    driver.quit()

# Export the DataFrame to a CSV file
df.to_csv('Finale.csv', index=False)
