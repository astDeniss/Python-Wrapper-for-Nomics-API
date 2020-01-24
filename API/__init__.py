from configuration import NOMICS_API_KEY

class BaseServerUrl:
    def __init__(self):
        self.api_key = NOMICS_API_KEY
        self.base_url = "https://api.nomics.com/v1" #All requests should be prefixed by the server URL