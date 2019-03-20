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
    place_differ = []
    removed_strings = []
    added_strings = []
    if not diff_list:
        x = len(list1) - len(list2)
        # print(
        #     f"There are {x} changes, however strings have been moved around. Here is what has moved:"
        # )
        place_differ = [x for x, y in zip(list1, list2) if x != y]
        # print(*moved_strings, sep="\n")
        return place_differ, removed_strings, added_strings
    else:
        # obtain the strings that changed, and list them
        place_differ = [x for x, y in zip(list1, list2) if x != y]
        added_strings = [item for item in list2 if item not in list1]
        removed_strings = [item for item in list1 if item not in list2]

        # Print the resulting lists of changes
        print(
            "The lines in list1 that differ from files at the same space in list2, these can be assumed to be lines moved around"
        )
        print(*place_differ, sep="\n")
        print(
            "These list elements are diffrent from list1 compared to list2, including items moved around, added, or changed. These could be considerd to have been removed"
        )
        print(*removed_strings, sep="\n")
        print(
            "These list elements are diffrent from list2 compared to list1, including items moved around, added, or changed. These could be considerd to have been added"
        )
        print(*added_strings, sep="\n")

        # Return the lists of changes
        return place_differ, removed_strings, added_strings


def char_length_checker(
    place_differ, removed_strings, added_strings, char_check_length=3
):
    # if len(place_differ) + len(removed_strings) + len(added_strings) >= 3:
    #     return 1
    changed_charicters = 0
    for x in range(len(place_differ)):
        changed_charicters += len(place_differ[x])
    for x in range(len(removed_strings)):
        changed_charicters += len(removed_strings[x])
    for x in range(len(added_strings)):
        changed_charicters += len(added_strings[x])
    print(changed_charicters)
    if changed_charicters >= char_check_length:
        return 1
    else:
        return 0


list1 = ["abc", "123", "ddd", "bbb"]
list2 = ["123", "abc", "aaa", "eee", "hans get ze luger"]
list2 = ["abc", "123", "bbb", "ddd"]


place_differ, removed_strings, added_strings = list_diff(list1, list2)
if char_length_checker(place_differ, removed_strings, added_strings) == True:
    print("TRUE")
else:
    print("FALSE")
