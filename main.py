import requests
from bs4 import BeautifulSoup
import csv
import os

# Define the URL of the webpage you want to scrape
url = "https://institute.careerguide.com/8-career-steps-to-become-an-engineer-after-class-10th/"  # Replace with the URL of your choice

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the data you need from the parsed HTML
    # For example, let's extract data from <p> tags
    paragraphs = soup.find_all('p')
    
    # Extract text from <p> tags and remove any leading/trailing whitespace
    data = [p.get_text().strip() for p in paragraphs]
    
    # Define the CSV file name
    csv_file_name = "data.csv"
    
    # Check if the CSV file exists, if not, create it with a header row
    if not os.path.exists(csv_file_name):
        with open(csv_file_name, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Data"])  # Header row
    
    # Open the CSV file in append mode and add new data
    with open(csv_file_name, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item])
    
    print(f"Data from {url} has been scraped and appended to {csv_file_name}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
