class BaseServerUrl:
    def __init__(self, nomics_api_key=None):
        """
        :param nomics_api_key: string
        """
        self.base_url = "https://api.nomics.com/v1" # All requests should be prefixed by the server URL
        if nomics_api_key:
            self.api_key = nomics_api_key

        else:
            raise AttributeError("Please provide your API_KEY as a porameter\n"
                                 "Example: Currencies('1287dskgsd39128ndkwG')")
