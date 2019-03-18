#By Ethan Wentworth & Jacob H.

from twilio.rest import Client
Fpart = "This many characters have been changed, "
Mpart = "Key: + is added, - is removed. These were the characters that were added, or removed"

#list1 is each character added
#list2 is number total

message = client.messages.create(
    to="+############", 
    from_="+###########",  
    body=""
   )

print(Fpart+list2+Mpart+list1)


#https://www.twilio.com/docs/sms/send-messages 
