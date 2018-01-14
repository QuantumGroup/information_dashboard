"""
This class sends SMS alerts to selected phone numbers when CRITIC warnings are identified. These are errors that need to
be immediately addressed, as they either stop system functionality or are credible threats to data integrity.

Note: SMS messages should only be used in important circumstances, as these pose a small but actual cost per use.
"""

import twilio