from twilio.rest import Client

TWILIO_SID = 'AC72a1bf6946523b370d71ff66099cff04'
TWILIO_AUTH_TOKEN = 'c041efa4f95af11bc06ed6dad06576ff'
TWILIO_VIRTUAL_NUMBER = '+16185906409'
TWILIO_VERIFIED_NUMBER = '+918310854483'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
