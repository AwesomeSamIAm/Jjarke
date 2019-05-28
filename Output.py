#By Ethan Wentworth & Jacob H.

import twilio
from twilio.rest import Client
def main(list1, list2, input_dict):
  Fpart = "This many characters have been changed, "
  Mpart = ". Key: + is added, - is removed. These were the characters that were added, or removed "

   #list1 is each character added

  #list2 is number total
  
  client = Client(input_dict["account_sid"], input_dict["auth_token"])

  message = client.messages \
                .create(
                     body= (Fpart+list2+Mpart+list1),
                     from_= input_dict["twinum"],
                     to= input_dict["num"]
                 )


#https://www.twilio.com/docs/sms/send-messages 
