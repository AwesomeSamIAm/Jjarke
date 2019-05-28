def cli_input():
    print(
        "Welcome to our webscraping project! Please enter the URL \n of the website you would like to check, the length of \n time between checks, and your twilio info!\n"
    )
    weburl = input("Website URL: ")
    interv = input("Time Interval: ")
    account_sid = input("Account Sid: ")
    auth_token = input("Authorization Token: ")
    twinum = input("Twilio Number: ")
    num = input("Destination Number: ")
    input_dict = {
        "weburl": weburl,
        "interv": interv,
        "account_sid": account_sid,
        "auth_token": auth_token,
        "twinum": twinum,
        "destnum": num,
    }
    return input_dict

