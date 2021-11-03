import requests
from bs4 import BeautifulSoup

url = "http://www.footballlocks.com/nfl_point_spreads.shtml"


def main(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, features="lxml")

    table = soup.find_all('table', attrs={'cols': '4'})

    rows = table[0].find_all('tr')

    for row in rows:
        favorite = row.find_all('td')[1].get_text().strip()
        underdog = row.find_all('td')[3].get_text().strip()
        spread = row.find_all('td')[2].get_text().strip()

        print(f"{favorite: <15} | {underdog: <20} | {spread}")


if __name__ == "__main__":
    main(url)
