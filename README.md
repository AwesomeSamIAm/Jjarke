# Jjarke

## Web Scraper:
 This project is for people who want to use an easy way to get web data/- information from the world wide web and to see the changes after a certain time. The user has the possibilitiy to define the content he wants to get in order to only receive this part of the website.
 Before the use can receive the output he need to define the input. The input contains following variables:
weburl: To get the content from this website.
interv: The time interval - How many times it should update the content.
account_sid: User information. So it is able to connect to the user.
auth_token: variable so it is authorized to connect to the user.
twinum: The virtuel number of the user.
num: The destination number of the user so it can finally send the message.

After the input software process the data. It tries to connect to the web server. If it was successfull it scrapes the whole webcontent into two files. One file contains the old content, the other one the updated version. Finally it uses the defined content informatio so it is able to get specific data. Then it process the differences between the old and the new version. As it finishes it writes the information in a variable.

On the next process step it connect to twillio server to send the message to the user.
The user receives defined output with data about the changes, data and time.

## This project should be run in a virtual enviroment with the following libraries installed:

1. BeautifulSoup4
2. Requests
3. Twilio

## The project is formatted using black
