# Variable Key

## MagicHappens.py

### get_html:

function to return the html from a specified site, may change in future

- url: the url of the site to use
- elements: this takes any number of arguments, and stores them in a list called elements, these should be types of html tags. E.g. get_html("google.com", "h1", "h2", "h3", "p")

### find_line_diff:

function to return the charecter by charecter difference of two strings.

- str1: the first string, the "original" one
- str2: the second string, will be compared against str1
- d: Initializes the Differ class as d
- result: a list of the differences, the key to how the list is displayed is in the comments

### send_changes:

this parses the result list given by find_line_diff.

- text1: is the first string of text, will be sent to find_line_diff as str1
- text2: is the second string of text to compare, will be sent to find_line_diff as str2
- list2: is the amound of differences,
- list1: is the list of actual differences
- x: used in the for list to

---

## obatain_html.py

### get_site_html:

gets the html of the url given and returns it

- url: the url of the site to use, E.g. "google.com"
- req: this initializes the requests.get function and stores the html it recieves in "req"
- soup: this is the BeautifulSoup object, it stores the BeautifulSoup parsed html in soup for later use
  - req.content: returns the html stored in "req"
  - html.parser: this specifies which parser for BeautifulSoup to use, this is the default one
- soup.prettify: returns the html after "soup" parses it, and also makes it nice to read by removeing excess whitespace and other stuff

### html_parser:

_should_ parse the html and return only the html elements specified

- html_2_parse: the html that should be parsed, string form
- elements: a list of the elements that need to be parsed, e.g. ["h1", "h2", "h3", "p"]
- x: the x'th element in the list,

### main:

AF
