
from bs4 import BeautifulSoup
import requests
import smtplib
import os

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"



header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}


response = requests.get(live_url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").get_text()

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
title = soup.find(id='productTitle').get_text().strip()

print(title)

if price_as_float>=95:
    message = f"{title} is on sale for {price}!"  
    print(message)  
    # with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
    #     connection.starttls()
    #     result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
    #     connection.sendmail(
    #         from_addr=os.environ["EMAIL_ADDRESS"],
    #         to_addrs=os.environ["EMAIL_ADDRESS"],
    #         msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
    #     )