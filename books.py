import requests
import time
import json

from bs4 import BeautifulSoup

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}


def collect_data():

    all_data = []
    url = "https://starylev.com.ua/bookstore/category--paperovi-knyzhky"
    with requests.Session() as session:
        response = session.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        pagination = int(soup.find("ul", class_="ant-pagination").find_all("li")[-3].text)

        for page in range(1, pagination + 1):
            page_url = f"https://starylev.com.ua/bookstore/category--paperovi-knyzhky/page--{page}"
            response = session.get(url=page_url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            cards = soup.find_all("div", class_="ant-card-body")
            for card in cards:
                link_to_card = f"https://starylev.com.ua{card.find('a').get('href', None)}"
                # print(link_to_card)
                response = session.get(url=link_to_card, headers=headers)
                soup = BeautifulSoup(response.text, "lxml")

                book_title = soup.find("div", class_="product-page__info").find("h1")
                author = book_title.previous_sibling.text.strip()
                book_title = book_title.text.strip()

                book_type = soup.find("div", class_="product-page__variants")
                if book_type is not None:
                    book_type = book_type.text
                else:
                    book_type = ""

                stock = soup.find("div", class_="product-page__status status-13")
                if stock is not None:
                    stock = stock.text.strip()
                else: 
                    stock = ""

                cost = soup.find("div", class_="product-page__info").\
                    find("span", class_="undefined product-price").find("span").text
                price = float(cost.split(" ")[0])

                sign = cost.split(" ")[1]

                # print(f"{type(price)}:{price:.2f} - {sign}:{type(sign)}")

                product_details_tables = soup.find("div", class_="ant-collapse-content ant-collapse-content-active").\
                    find_all("table")

                product_details = {}
                for table in product_details_tables:
                    trs = table.find_all("tr")
                    for tr in trs:
                        tds = tr.find_all("td")
                        product_details[tds[0].text] = tds[1].text
                        # print(f"{tds[0].text}: {tds[1].text}")

                data = {
                    "book_title": book_title,
                    "author": author,
                    "book_type": book_type,
                    "stock": stock,
                    "price": price,
                    "currency": sign,
                    "product_details": product_details
                }
                all_data.append(data)
            print(f"Page: {page}/{pagination}")
            time.sleep(3)

    with open("data/data.json", "w") as file:
        json.dump(all_data, file, indent=4, ensure_ascii=False)


def main():
    collect_data()


if __name__ == '__main__':
    main()
