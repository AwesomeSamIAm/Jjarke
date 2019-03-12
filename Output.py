#By Ethan Wentworth & Jacob H.

from twilio.rest import Client

#minecraft = 7

message = client.messages.create(
    to="+############", 
    from_="+###########",
    # body="Testing testing one two three four five six ",minecraft, "!"  
    body="This many characters have been changed, ", result, "These were the characters that were added, or removed", result, "." #1600 character limit
  
)

print(message.sid)

#What variables do we need for the output section? find_line_diff? d? result? list1 or 3?

#https://www.twilio.com/docs/sms/send-messages
