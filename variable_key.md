# Variable Key

## MagicHappens.py

### get_html:

Function to return the html from a specified site, may change in future

- url: the url of the site to use
- elements: this takes any number of arguments, and stores them in a list called elements, these should be types of html tags. E.g. get_html("google.com", "h1", "h2", "h3", "p")

### list_diff

Function to return 3 lists of the changed strings

- list1: the original list to base comparisons off of
- list2: the changed list
- diff_list: this is a list of all the strings that are changed between list1 and list2.
- place_differ: a list of each string that has a diffrent position but the same characters between the two lists.
- removed_strings: strings that have been removed from list1, when looking at list2
- added_strings: strings that have been added to list2, compared to list1

## char_length_checker

Function that checks the amount of characters that changed based on the returns of list_diff

- place_differ: a list of each string that has a diffrent position but the same characters between the two lists.
- removed_strings: strings that have been removed from list1, when looking at list2
- added_strings: strings that have been added to list2, compared to list1
- char_check_length: this is the amount of characters required to have changed for it to return TRUE
- changed_characters: the number of characters that have changed between list1 and list2
