import csv
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
user_agent = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    )
}

wiki_page = requests.get(URL, headers=user_agent, timeout=60)
content = BeautifulSoup(wiki_page.text, "html.parser")
table = content.find("table", {"id" : "mwPw"}) 
rows = table.find_all("tr")

with open("data/country_populations.csv", "w", newline="") as file_csv:
    writer = csv.writer(file_csv)
    writer.writerow(["country", "population", "perc_of_world", "date", "source"])
    for row in rows:
        columns = row.find_all("td")
        try:
            country_data.append(columns[0].get_text().strip())
            country_data.append(columns[1].get_text().strip())
            country_data.append(columns[2].get_text().strip())
            country_data.append(columns[3].get_text().strip())
            country_data.append((columns[4].get_text().strip()).split("[")[0])
            writer.writerow(country_data)
        except Exception as e:
            print(f"Error occured: {e}!")
        finally:
            country_data = []

