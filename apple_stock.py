import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/95.0.4638.54 Safari/537.36'}


def main(url):
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, features="lxml")

    table = soup.find('table', attrs={'class': 'W(100%) M(0)'})

    rows = table.find_all('tr', attrs={'class': 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})

    for row in rows:

        data = row.find_all('td')

        try:
            date = data[0].get_text()
            closing_price = data[4].get_text()

        except:
            continue

        print(f"Date: {date} | Closing Price: {closing_price}")


if __name__ == "__main__":
    main(url)
