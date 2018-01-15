"""
This class sends SMS alerts to selected phone numbers when CRITIC warnings are identified. These are errors that need to
be immediately addressed, as they either stop system functionality or are credible threats to data integrity.

Note: SMS messages should only be used in important circumstances, as these pose a small but actual cost per use.
"""


class SMS_alerts:

    def __init__(self):
        pass

    def prepare_sms(self, message_text):
        # Python library import
        from twilio.rest import Client
        # local file imports
        import _keys_and_secrets as keys

        client = Client(keys.twilio_account_sid, keys.twilio_auth_token)

        client.messages.create(to=keys.personal_cell_phone,
                               from_=keys.twilio_outbound_phone,
                               body=message_text)

    def critic_sms(self, failure_message):
        """
        Used whenever there is a critical failure in the script that requires immediate attention.
        :param failure_message: str
            The string can be passed from wherever the method is called to provide more information about where the
            failure occured
        :return: None
        """

        if failure_message:
            pass
        else:
            failure_message = ''

        # the following is a standard message passed regardless of the nature of error
        message_text = 'GRID critical failure\n' \
                       '---------------------\n' \
                       'An error has occurred.\n' \
                       '%s' % failure_message

        self.prepare_sms(message_text)

# sms = SMS_alerts()
# alert = sms.critic_sms('a test message')
