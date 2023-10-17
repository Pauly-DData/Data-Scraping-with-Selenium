# Data-Scraping-with-Selenium

## Web Scraping for Data Collection

This project is a part of a master's thesis which aims to collect data on standard questions available on websites like Datacamp. The main tools used for this task are the **Selenium** and **Pandas** libraries.

## Overview

- **Selenium WebDriver**: A tool that automates web browsers, simulating user interactions with a website.
- **Pandas**: A powerful data manipulation and analysis library.

## Modules and Packages

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
```

# Workflow

## URL Collection:

As a part of my master's thesis project, I needed to collect data on standard questions available on websites like Datacamp. For this assignment, I used the Selenium and Pandas libraries to complete the task.

The URLs are stored in a list called `urls`. The script imports the necessary modules and packages such as `webdriver`, `Service`, `By`, and `pandas`.

The Selenium WebDriver is a tool that automates web browsers and allows us to simulate user interactions with a website. The `webdriver` module is used to create a WebDriver instance for a specific browser. In this case, we are using Chrome, which is why we also import the `Service` module.

The `By` module is used to locate elements on a webpage using various methods like ID, class, tag name, etc.

The `pandas` module is used to manipulate and analyze data that has been scraped from the webpages.

The `urls` list contains a list of URLs to scrape. These URLs are all from the same GitHub repository, and each URL points to a specific Markdown file containing instructions for a different chapter of a Python data science course.

## Data Extraction:

For each URL in the `urls` list, the script uses the WebDriver to load the page and extract specific data. The extracted data is then stored in a pandas DataFrame.

## Data Export:

Finally, the data stored in the DataFrame is exported to a CSV file named 'Finale.csv'.



