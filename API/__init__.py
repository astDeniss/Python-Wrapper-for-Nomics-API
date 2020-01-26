class BaseServerUrl:
    def __init__(self, nomics_api_key):
        """

        :param nomics_api_key: string
        """
        self.api_key = nomics_api_key
        self.base_url = "https://api.nomics.com/v1" #All requests should be prefixed by the server URL