# Option 1, does not account for multiple of the same differences in the files, no record of place of difference
# def compare():
#     with open("test_html/index1.html", "r") as file1:
#         with open("test_html/index2.html", "r") as file2:
#             same = set(file1).difference(file2)

#         same.discard("\n")

#         for line in same:
#             print(line)
#         # with open("some_output_file.txt", "w") as file_out:
#         #     for line in same:
#         #         file_out.write(line)


# compare()


# Option 2, uses a library to compare total changes, then if there are changes looks charicter by charicter
# import filecmp

# # returns true if the files are the
# if filecmp.cmp("test_html/index1.html", "test_html/index2.html"):

#     print("The files are the same")
# else:
#     print("The files are diffrent, finding different charicters")
#     # Goes to the compare_character def
#     compare_character()


# def compare_character():
#     pass

#################################################################################################################

# Option 3 is to use the difflib library to find differences between two lines of text read from the html page
from difflib import Differ
from obtain_html import get_site_html


# Set both text strings
def get_html(url_1, url_2, *elements):
    # text1 = "text"
    # text2 = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Tempore, ea, exercitationem magni doloremque aspernatur iste earum commodi, quibusdam tempora nulla alias iusto eaque! Cumque eaque quibusdam adipisci dicta in neque."
    get_site_html(url_1, url_2, elements)


# Function that takes two strings, compares them, then returns the number of changes and specific changes
def find_line_diff(str1, str2):
    # Initialize the Differ class as d
    d = Differ()

    # Create a list of the differences found by the compare method
    result = list(d.compare(str1, str2))

    # Print the number of changes (entries in the list), then the changes. The key is as follows:
    # '- ' 	line unique to sequence 1
    # '+ ' 	line unique to sequence 2
    # '  ' 	line common to both sequences
    # '? ' 	line not present in either input sequence
    return len(result), result


def send_changes():
    # Print the changes found between text1 and text2 returned by find_line_diff
    print(find_line_diff(text1, text2))

    list3, list1 = find_line_diff(text1, text2)

    for x in list1:
        if "+" in x:
            print(x)
        elif "-" in x:
            print("-" + x)
        else:
            pass


get_html()
