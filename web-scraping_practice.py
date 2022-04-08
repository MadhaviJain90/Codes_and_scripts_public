

import requests as req
URL = "https://realpython.github.io/fake-jobs/"
# page = req.get(URL)

# print(page.text)
from bs4 import BeautifulSoup
soup = BeautifulSoup(req.get(URL).content, "html.parser")
print(soup.text)
job_elements = soup.find_all("div", class_="card-content")



import csv
file = open("jobs.csv", "w", newline='')
writer = csv.writer(file)
# write title row
writer.writerow(['Job Title', 'Company', 'Location'])
# for i in range(len(job_elements)):
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title").text.strip()
    company_element = job_element.find("h3", class_="company").text.strip()
    location_element = job_element.find("p", class_="location").text.strip()
    writer.writerow([title_element,company_element, location_element])

file.close()

# import os

# # Get the current working directory
# cwd = os.getcwd()
# cwd

# for i in range(length): 
#         filewriter.writerow([dates[i].get_text(), cost[i].get_text()]) 
title_element
job_elements