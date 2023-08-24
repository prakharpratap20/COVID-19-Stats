from typing import NamedTuple

import requests
from lxml import html 

class CovidData(NamedTuple):
    cases: int 
    deaths: int 
    recovered: int 


def covid_stats(url: str = "https://www.worldometers.info/coronavirus/") -> CovidData:
    xpath_str = '//div[@class = "maincounter-number"]/span/text()'
    return CovidData(*html.fromstring(requests.get(url).content).xpath(xpath_str))

fmt = """Total COVID-19 cases in the world: {}
Total deaths due to COVID-19 in the world: {}
Total COVID-19 patients recovered in the world: {}"""
print(fmt.format(*covid_stats()))