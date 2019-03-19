from difflib import Differ
from bs4 import BeautifulSoup
import requests
import time


# Set both text strings
def get_html(url, *elements):
    def get_site_html():
        # print(url)
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "html.parser")
        # print(soup.prettify())
        return soup

    def html_parser():
        element_list = []
        for x in elements:
            # print(x)
            element_list += html_soup.find_all(x)
        return element_list

    html_soup = get_site_html()
    parsed_html = html_parser()
    return parsed_html


def list_diff(list1, list2):
    diff_list = list(set(list1).symmetric_difference(set(list2)))
    if not diff_list:
        x = len(list1) - len(list2)
        print(
            f"There are {x} changes, however strings have been moved around. Here is what has moved:"
        )
        print(*[x for x, y in zip(list1, list2) if x != y], sep="\n")
    else:
        print(
            "The lines in list1 that differ from files at the same space in list2, these can be assumed to be lines moved around"
        )
        print(*[x for x, y in zip(list1, list2) if x != y], sep="\n")
        print(
            "These list elements are diffrent from listx compared to listy, including items moved around, added, or changed. These could be considerd to have been removed"
        )
        print(*[item for item in list1 if item not in list2], sep="\n")
        print(
            "These list elements are diffrent from listy compared to listx, including items moved around, added, or changed. These could be considerd to have been added"
        )
        print(*[item for item in list2 if item not in list1], sep="\n")

