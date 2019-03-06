#By Ethan Wentworth & Jacob H.

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+############", 
    from_="+###########",
    body="Testing testing one two three four five six ",minecraft, "!"  
)

print(message.sid)
