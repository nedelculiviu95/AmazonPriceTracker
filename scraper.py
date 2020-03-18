import requests
from bs4 import BeautifulSoup
import smtplib

def check():
    URL = 'https://www.amazon.co.uk/Lavazza-Crema-Gusto-Ground-Coffee/dp/B01KLIGDEM/ref=sr_1_8?crid=39Z9Q2LFLOOU5&keywords=lavazza+ground&qid=1584526852&sprefix=lavazza+grou%2Caps%2C161&sr=8-8'

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:])

    if (converted_price < 28.76):
        print('Price Low')
        send_mail1()
    elif (converted_price > 28.76):
        print('Price Up')
        send_mail2()
    else:
        print('Same Price')

    print(title.strip())
    print(converted_price)


def send_mail1():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('liviuu808@gmail.com', 'wkronnnatmbkbili')

    subject = 'Price fell down'
    body = 'Check amazon link: https://www.amazon.co.uk/Lavazza-Crema-Gusto-Ground-Coffee/dp/B01KLIGDEM/ref=sr_1_8?crid=39Z9Q2LFLOOU5&keywords=lavazza+ground&qid=1584526852&sprefix=lavazza+grou%2Caps%2C161&sr=8-8'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'liviuu808@gmail.com',
        'lnede001@gold.ac.uk',
        msg
    )

    print('Email has been sent')
    server.quit()

def send_mail2():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('liviuu808@gmail.com', 'wkronnnatmbkbili')

    subject = 'Price went up'
    body = 'Check amazon link: https://www.amazon.co.uk/Lavazza-Crema-Gusto-Ground-Coffee/dp/B01KLIGDEM/ref=sr_1_8?crid=39Z9Q2LFLOOU5&keywords=lavazza+ground&qid=1584526852&sprefix=lavazza+grou%2Caps%2C161&sr=8-8'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'liviuu808@gmail.com',
        'lnede001@gold.ac.uk',
        msg
    )

    print('Email has been sent')
    server.quit()

check()