"""
This class contains code that will be called in the case of errors in other scripts
"""


class Error:

    def if_error(self, e, full_e, method_name, failure_type, sms=False):
        """
        This method takes in errors from other methods and prints them to console and sends them as text to a specified
        phone number.
        :param e: Exception
        the exception that is raised by the error
        :param full_e: str
        this the is full stack trace for the error
        :param method_name: str
        the name of the method where the exception has occurred
        :param failure_type: str
        the specific type of error designed to be caught by the try/except block
        :param sms: bool
        this specifies whether SMS alerts should be sent when this method is trigger: SHOULD BE USED SPARINGLY!
        :return:
        """
        # Python library imports
        import datetime
        import time
        # local file imports
        import control
        import dissemination.sms_alerts.alerts as alerts

        # acquires the current time
        current_time_int = int(time.time())
        current_time_struct = time.gmtime(current_time_int)
        current_time = str(datetime.datetime.fromtimestamp(time.mktime(current_time_struct)))

        # instantiates SMS alerts class
        sms_alert = alerts.SMS_alerts()

        # creates multi-purpose error message
        message = ("error in: %s\n"
                   "error type: %s\n"
                   "exception: %s\n\n"
                   % (method_name, failure_type, str(e)))

        if control.debug is True:
            print(message)

        with open('error_log.txt', 'a') as f:
            f.write('=============================================================================================\n'
                    'error at %s UTC\n'
                    '=============================================================================================\n'
                    % current_time)
            f.write(message + '\n')
            f.write(full_e + '\n\n\n\n')
        if sms is True:
            sms_alert.critic_sms(message)
