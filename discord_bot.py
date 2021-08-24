import discord
import os
import datetime
import requests

client = discord.Client()
    
@client.event
async def on_ready():
    print('We have logged in with {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!elden'):
        today = datetime.date.today()
        futdate = datetime.date(2022, 1, 21)
        now = datetime.datetime.now()
        mnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds = (mnight - now).seconds
        days = (futdate - today).days
        hms = str(datetime.timedelta(seconds=seconds))
        await message.channel.send(f"There's {days} days and {hms} hours left for the release of Elden Ring.")
        print("Release date for Elden Ring was looked at.")

    if message.content.startswith('!covidTotal'):
        url1 = 'https://covid19-api.vost.pt/Requests/get_full_dataset'
        result1 = requests.get(url1)

        if result1.status_code == 200:
            data_covid = result1.json()
            n1 = data_covid['data'].values()
            n2 = data_covid['confirmados_novos'].values()
            date_list = list(n1)
            new_conf_list = list(n2)
            print("OK")
            covid_message = f"For the date of {date_list[-1]} there where {new_conf_list[-1]} new confirmed cases in Portugal."
            await message.channel.send(covid_message)
            print("New cases checked.")
        else:
            print(f"Error fetching data {result1.status_code}")

client.run("INPUT YOUR TOKEN HERE")
