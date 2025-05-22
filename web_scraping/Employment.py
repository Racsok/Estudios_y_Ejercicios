import requests
import json 
from bs4 import BeautifulSoup as bs


#model class for job offers
class JobOffer():
    def __init__(self, job_id, name, url, company, salary, tags):
        self.job_id = job_id
        self.name = name
        self.url = url
        self.company = company
        self.salary = salary
        self.tags = tags
        
    def to_dict(self):
        return {
            "job_id": self.job_id,
            "name": self.name,
            "url": self.url,
            "company": self.company,
            "salary": self.salary,
            "tags": self.tags
        }
    
    
def processingOffers(listResult):
    save_offers = []
    for result in listResult:
        urlJob = result.div['data-url']
        data = json.loads(result.div['data-ga4-offerdata'])
        if data:
            offer = JobOffer(
            job_id = data.get("id"),
            name = data.get("title"),
            company = data.get("company"),
            url = urlJob,
            salary = data.get("salary"),
            tags = data.get("tags"))
            save_offers.append(offer)
        
    return save_offers

def scrappingOffers(url):
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')
    listResult = soup.find_all('div', class_="result-item")
    offers = processingOffers(listResult)
    return offers