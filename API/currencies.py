from API import BaseServerUrl
import requests


class Currencies(BaseServerUrl):
    """
    Instances of this Class have methods to retain data like:Price, volume, market cap, and rank
    for all currencies across 1 hour, 1 day, 7 day, 30 day, 365 day, and year
    to date intervals. Current prices are updated every 10 seconds.
    """

    def get_currencies_ticker(self, ids=None, interval=None, convert=None):
        """
        :param ids: (:type str): Comma separated list of Nomics Currency IDs to filter result rows. FOr example: "BCH"
        :param interval: (:type str): Comma separated time interval of the ticker(s). Default is '1d','7d','30d',
        '365d','ytd'
        :param convert: (:type str): Currency to quote ticker price, market cap, and volume values.
        May be a Fiat Currency or Cryptocurrency. Default is 'USD'.

        :return:
        """
        url = self.base_url + "/currencies/ticker?key=" + self.api_key

        parameters = {
            "ids": ids,
            "interval": interval,
            "convert": convert,
        }

        response = requests.get(url, params=parameters)

        if int(response.status_code) == 200:
            data = response.json()
            return data
        else:
            return "{} --> {}".format(response.status_code, response.text)
