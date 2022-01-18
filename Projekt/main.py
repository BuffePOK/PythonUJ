import discord
from discord.ext import commands
from discord.message import Message
from config import settings
import exchange_rate
from logging_bot import logging_bot
from time import ctime


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    logging_bot("Bot started")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/exchange'):
        currency = exchange_rate.Currency()
        course = currency.get_currency_price()
        print("Wywolana funkcja \'Exchange\'")
        message_list = [
        "Time: ", ctime(), 
        "\nUSD in PLN: ", course[0].replace(",", "."), 
        "\nPLN in USD: ", course[1].replace(",", "."), 
        "\nEUR in PLN: ", course[2].replace(",", "."), 
        "\nPLN in EUR: ", course[3].replace(",", ".")
        ]

        mess = ""
        for i in message_list:
            mess += str(i)

        await message.channel.send(mess)
        logging_bot("Wywolano Exchange. Success")

    if message.content.startswith('/exit'):
        logging_bot("Turns off")
        await message.channel.send("Bot turns off")
        quit(0)


if __name__ == "__main__":
    client.run(settings['token'])