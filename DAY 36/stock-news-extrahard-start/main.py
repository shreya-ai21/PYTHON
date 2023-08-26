import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = 'B0CK7D76N5QFP87K'
NEWS_API_KEY = 'c9a120d6000f4d83b874e6f2eefb4171'

TWILIO_SID = 'AC72a1bf6946523b370d71ff66099cff04'
TWILIO_AUTH_TOKEN = '9f40d66cb786cb037a3c0f37781c1863'

# STEP 1: Use https://www.alphavantage.co
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
response = requests.get(url='https://www.alphavantage.co/query', params=params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday = data_list[0]
yest_close = yesterday['4. close']


day_bef_yesterday = data_list[1]
day_bef_yest_close = day_bef_yesterday['4. close']

difference = float(yest_close)-float(day_bef_yest_close)
if difference>0:
    up_down='🔺'
else:
    up_down='🔻'

diff_percent = round(difference/float(yest_close)*100,2)

if abs(diff_percent) > 2:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    news = requests.get(
        url='https://newsapi.org/v2/everything?', params=news_params)
    articles = news.json()['articles']
    three_articles = articles[:3]

    articles_list = [
        f"{COMPANY_NAME}:{up_down}{diff_percent}% Headline: {article['title']} Brief:{article['description']}" for article in three_articles]
    print(articles_list)

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in articles_list:
        message = client.messages.create(
            body=article,
            from_='+16185906409',
            to='+918310854483'
        )


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
