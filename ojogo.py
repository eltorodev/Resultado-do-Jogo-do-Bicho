from bs4 import BeautifulSoup
import requests

url = requests.get("https://www.ojogodobicho.com/deu_no_poste.htm").text

soup = BeautifulSoup(url, "lxml")

table = soup.find("table", {
    "class": "twelve"
})

caption = table.findAll("caption")[0].getText()

th = table.findAll("th")
td = table.findAll("td")
