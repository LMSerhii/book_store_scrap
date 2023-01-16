import requests
import time
from bs4 import BeautifulSoup

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}


def collect_data():
    url = "https://starylev.com.ua/bookstore/category--paperovi-knyzhky"
    with requests.Session() as session:
        response = session.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        pagination = int(soup.find("ul", class_="ant-pagination").find_all("li")[-3].text)

        for page in range(1, pagination + 1)[:1]:
            page_url = f"https://starylev.com.ua/bookstore/category--paperovi-knyzhky/page--{page}"
            response = session.get(url=page_url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            cards = soup.find_all("div", class_="ant-card-body")
            for card in cards[:2]:
                link_to_card = f"https://starylev.com.ua{card.find('a').get('href', None)}"
                # print(link_to_card)
                response = session.get(url=link_to_card, headers=headers)
                soup = BeautifulSoup(response.text, "lxml")
                book_title = soup.find("div", class_="product-page__info").find("h1")
                author = book_title.previous_sibling.text.strip()
                book_title = book_title.text.strip()
                # print(author, book_title)
                book_type = soup.find("div", class_="product-page__variants")
                if book_type is not None:
                    book_type = book_type.text
                else:
                    book_type = ''
                # print(book_type)
                stock = soup.find("div", class_="product-page__status status-13 ")
                print(stock)
            time.sleep(3)


def main():
    collect_data()


if __name__ == '__main__':
    main()
