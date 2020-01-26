from API import BaseServerUrl
import requests


class Currencies(BaseServerUrl):
    """
    Instances of this class should be initialized with :param: "your api key" -> :type: string
    """

    def get_currencies_ticker(self, ids=None, interval=None, convert=None):
        """
        :param ids: (:type str): Comma separated list of Nomics Currency IDs to filter result rows. FOr example: "BCH"
        :param interval: (:type str): Comma separated time interval of the ticker(s). Default is '1d','7d','30d',
        '365d','ytd'
        :param convert: (:type str): Currency to quote ticker price, market cap, and volume values.
        May be a Fiat Currency or Cryptocurrency. Default is 'USD'.

        :return: data as JSON object.
        """
        url = self.base_url + "/currencies/ticker?key=" + self.api_key

        parameters = {
            "ids": ids,
            "interval": interval,
            "convert": convert,
        }

        response = requests.get(url, params=parameters)

        if int(response.status_code) == 200:
            return response
        else:
            raise Exception("Error: {} --> {}".format(response.status_code, response.text))

    def currencies_metadata(self):
        """
        The currencies endpoint returns all the currencies and their metadata that Nomics supports.
        :return:
        """
        pass
