import requests
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"


def main(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, features="lxml")

    rows = soup.find_all('tr', attrs={'class': 'TableBase-bodyTr'})

    count = 0

    for row in rows:
        name = row.find('span', attrs={'class': 'CellPlayerName--long'}).find('a').get_text()
        position = row.find('span', attrs={'class': 'CellPlayerName-position'}).get_text().strip()
        team = row.find('span', attrs={'class': 'CellPlayerName-team'}).get_text().strip()
        tds = row.find_all('td')
        touchdowns = tds[8].get_text().strip()

        print(f"{count + 1}: {name} | {position} | {team} | {touchdowns} touchdowns")

        count += 1
        if count > 19:
            break


if __name__ == "__main__":
    main(url)
