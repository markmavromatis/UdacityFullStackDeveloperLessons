from twilio.rest import TwilioRestClient

account_sid = "AC99b1e7b342d58eb6b14e611573aeebcb" # Your Account SID from www.twilio.com/console
auth_token  = "a4b4bddd0f8a243cea8b9187fa28ea4c"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+14159678404",    # Replace with your phone number
    from_="+12056390319") # Replace with your Twilio number

print(message.sid)
