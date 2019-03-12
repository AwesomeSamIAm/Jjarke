from bs4 import BeautifulSoup
import requests


def get_site_html(url):
    print(url)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    print(soup.prettify())
    return soup


def html_parser(html_2_parse, elements):
    for x in elements:
        print(x)
    return "in progress"


def main():
    site_html = get_site_html("https://kaimoritamcvey.me")
    elements = ["p", "h1", "h2", "h3"]
    print(html_parser(site_html, elements))


if __name__ == "__main__":
    main()
