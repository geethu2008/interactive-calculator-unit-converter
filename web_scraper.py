import requests
from bs4 import BeautifulSoup
import json


def scrape_quotes():
    url = "https://quotes.toscrape.com/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = []

        for quote in soup.find_all("div", class_="quote"):
            text = quote.find("span", class_="text").get_text(strip=True)
            author = quote.find("small", class_="author").get_text(strip=True)

            quotes.append({
                "quote": text,
                "author": author
            })

        return quotes

    except requests.RequestException as e:
        print("Error while accessing website:", e)
        return []


def display_quotes(quotes):
    print("\n===== SCRAPED QUOTES =====")

    if not quotes:
        print("No quotes found.")
        return

    for index, quote in enumerate(quotes, start=1):
        print(f"\n{index}. {quote['quote']}")
        print(f"   Author: {quote['author']}")


def save_to_json(quotes):
    with open("quotes.json", "w", encoding="utf-8") as file:
        json.dump(quotes, file, indent=4, ensure_ascii=False)

    print("\nData saved to quotes.json")


def main():
    print("==============================")
    print("     WEB SCRAPER")
    print("==============================")

    quotes = scrape_quotes()

    display_quotes(quotes)

    if quotes:
        save_to_json(quotes)


main()