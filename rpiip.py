import requests
import datetime
import pytz
import json

SERVICE_URL = 'http://ifconfig.me/ip'

class RPIIP(object):

    def __init__(self, *args, **kwargs):
        super(RPIIP, self).__init__(*args, **kwargs)
        try:
            self.set_ip()
        except:
            self.ip = None

        self.created = datetime.datetime.now(pytz.utc)
        return

    def set_ip(self):
        response = requests.get(SERVICE_URL)
        self.ip = str(response.text.strip())

    @property
    def timestamp(self):
            return self.created.isoformat(' ')

    @property
    def elements(self):
        return {'ip': self.ip,
         'timestamp': self.timestamp}
    
    @property
    def json(self):
        return json.dumps(self.elements)

