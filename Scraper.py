from bs4 import BeautifulSoup
import requests
import json
webpage = "https://summerofcode.withgoogle.com/api/program/current/project/?page=1&page_size=20https://summerofcode.withgoogle.com/projects/"
f = open("gsoc2021.csv","w")
f.write("Name,Project,Organization")
while(webpage):
    page = requests.get(webpage)
    soup = BeautifulSoup(page.content, 'html.parser')
    site_json = json.loads(soup.text)
    results = site_json['results']
    for i in results:
        f.write(i["student"]["display_name"]+",\""+i["title"].replace('"', '""')+"\",\""+i["organization"]["name"]+"\"\n")
    webpage = site_json['next']
f.close

