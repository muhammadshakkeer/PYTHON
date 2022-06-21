import requests
from bs4 import BeautifulSoup
website_url = "https://infopark.in/companies/job-search"


res = requests.get(website_url)
soup = BeautifulSoup(res.text, "lxml")
jobs = soup.find_all("div", {"class": "row company-list joblist"})
# print(jobs)

for job in jobs:
  title_details = job.find("a")
  job_title = title_details.text
  print(title_details)