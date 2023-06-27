import requests
from bs4 import BeautifulSoup



def dollars_rub():
    DOLLARS_rub = 'https://www.google.com/search?q=rehc+ljkkfhf+&sxsrf=AJOqlzWwB_70s_SAqla7Nzqpwpefjqaugg%3A1678539970528&ei=wnwMZJv2H5K7rgT8gppg&ved=0ahUKEwib37zV-NP9AhWSnYsKHXyBBgwQ4dUDCA8&uact=5&oq=rehc+ljkkfhf+&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQsQMQgwEQQzIHCAAQgAQQCjIECAAQQzIHCAAQsQMQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzINCAAQgAQQsQMQgwEQCjIECAAQQzIKCAAQgAQQsQMQCjIHCAAQgAQQCjoECCMQJzoOCC4QgAQQsQMQgwEQ1AI6CwgAEIAEELEDEIMBOggIABCABBCxAzoICC4QsQMQgwE6CwguELEDEMcBENEDOhEILhCABBCxAxCDARDHARDRAzoHCC4Q1AIQQzoKCC4QxwEQ0QMQQzoQCC4QsQMQgwEQxwEQ0QMQQzoJCAAQgAQQChABOgoILhCxAxDUAhBDOgQILhBDOg4ILhCABBCxAxDHARDRAzoJCAAQgAQQChAqOg4IABCABBAKECoQRhCCAkoECEEYAFAAWLUXYN4YaABwAXgAgAHEAogB4BCSAQc0LjYuMS4ymAEAoAEBwAEB&sclient=gws-wiz-serp'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    page = requests.get(DOLLARS_rub, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    convert = soup.findAll("span", {"class": "DFlfde", "class":"SwHCTb", "data-precision": 2})
    result_dollars = float((convert[0].text).replace(',','.'))
    return result_dollars






def euro_rub():
    EURO_rub = 'https://www.google.com/search?q=rehc+tdhj&sxsrf=AJOqlzVyfz2NN9MYL97chSM2b43XSOJ4WQ%3A1678539977840&ei=yXwMZPT3MuayrgS27Y-IDQ&ved=0ahUKEwi0gPvY-NP9AhVmmYsKHbb2A9EQ4dUDCA8&uact=5&oq=rehc+tdhj&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAFAAWOIPYMkRaABwAXgAgAEAiAEAkgEAmAEAoAEBwAEB&sclient=gws-wiz-serp'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    page = requests.get(EURO_rub, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    convert = soup.findAll("span", {"class": "DFlfde", "class":"SwHCTb", "data-precision": 2})
    result_euro = float((convert[0].text).replace(',','.'))
    return result_euro


dollars_rub()