import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

# Crawl NAV & Net Assets
url = "https://etf.dws.com/en-us/XAIX-artificial-intelligence-and-big-data-etf/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")
page_text = soup.get_text(" ", strip=True)

nav_pattern = re.compile(r"NAV.*?\$([0-9]+\.[0-9]+)")
net_assets_pattern = re.compile(r"Net assets.*?\$([0-9,.]+)")

nav_value = nav_pattern.search(page_text).group(1)
net_assets_value = net_assets_pattern.search(page_text).group(1)

today = datetime.today().strftime("%Y-%m-%d")

# Email content
msg = MIMEText(f"Date: {today}\nNAV Value: ${nav_value}\nNet Assets: ${net_assets_value}")
msg["Subject"] = "XAIX ETF Daily Report"
msg["From"] = "your_email@gmail.com"
msg["To"] = "Naveen.5304@gmail.com"

# Send email (using Gmail SMTP)
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("your_email@gmail.com", "your_app_password")
    server.send_message(msg)
