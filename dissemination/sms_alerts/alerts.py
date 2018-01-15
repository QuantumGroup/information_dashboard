"""
This class sends SMS alerts to selected phone numbers when CRITIC warnings are identified. These are errors that need to
be immediately addressed, as they either stop system functionality or are credible threats to data integrity.

Note: SMS messages should only be used in important circumstances, as these pose a small but actual cost per use.
"""


class SMS_alerts:

    def send_sms(self, message):
        # Python library import
        from twilio.rest import Client
        # local file imports
        import _keys_and_secrets as keys

        client = Client(keys.twilio_account_sid, keys.twilio_auth_token)

        message = client.messages.create(
            to=keys.personal_cell_phone,
            from_=keys.twilio_outbound_phone,
            body=message)

        print(message.sid)

message = 'another test message'

alerts = SMS_alerts()

alerts.send_sms(message)
