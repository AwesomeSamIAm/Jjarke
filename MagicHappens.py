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


# This is for testing with a local file
def get_html_test(url, *elements):
    def get_site_html():
        with open(url, "r", encoding="ascii", errors="surrogateescape") as f:
            req = f.read()
        soup = BeautifulSoup(req, "html.parser")
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

    # Check to see if the only change is moving the order
    if not diff_list:
        x = len(list1) - len(list2)
        place_differ = [x for x, y in zip(list1, list2) if x != y]
        return place_differ, removed_strings, added_strings

    else:
        # obtain the strings that changed, and list them
        place_differ = [x for x, y in zip(list1, list2) if x != y]
        added_strings = [item for item in list2 if item not in list1]
        removed_strings = [item for item in list1 if item not in list2]
        return place_differ, removed_strings, added_strings


# Find number of characters that changed
# TODO add suport to ignore line place changes
def char_length_checker(
    place_differ, removed_strings, added_strings, char_check_length=3
):
    # Store total character changes in a variable
    changed_characters = 0
    for x in range(len(place_differ)):
        changed_characters += len(place_differ[x])
    for x in range(len(removed_strings)):
        changed_characters += len(removed_strings[x])
    for x in range(len(added_strings)):
        changed_characters += len(added_strings[x])
    print(changed_characters)

    # If total character changes are equal or equal to amount specified return TRUE
    if changed_characters >= char_check_length:
        return 1
    else:
        return 0


# TODO add wait functionality, fix variable names to match input


# # This is for testing, will not make master
# list1 = ["abc", "123", "ddd", "bbb"]
# list2 = ["123", "abc", "aaa", "eee", "hans get ze luger"]
# # list2 = ["abc", "123", "bbb", "ddd"]

# place_differ, removed_strings, added_strings = list_diff(list1, list2)
# if char_length_checker(place_differ, removed_strings, added_strings) == True:
#     print("TRUE")
# else:
#     print("FALSE")
def main():
    print(time.ctime())
    list1 = get_html_test("test_html/index1.html", "p")
    print(time.ctime())
    time.sleep(10)
    list2 = get_html_test("test_html/index2.html", "p")
    print(time.ctime())

    place_differ, removed_strings, added_strings = list_diff(list1, list2)
    if char_length_checker(place_differ, removed_strings, added_strings) == True:
        print("TRUE")
    else:
        print("FALSE")
    print(time.ctime())
    # print(list_diff(list1, list2))


if __name__ == "__main__":
    x = 0
    while True:
        print(x)
        main()
        x += 1
