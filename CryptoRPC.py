print("Setting up program... this may take a while.")
import asyncio
import datetime
from distutils.command.build import build
from email import message
import functools
import io
import json
from msilib import datasizemask
import os
import random
import re
import signal
import rpc
from sqlite3 import Timestamp
import string
import sys
import urllib.parse
import urllib.request
import time
from urllib import parse, request
import hypixel
from itertools import cycle
from bs4 import BeautifulSoup as bs4
import aiohttp
import colorama
import discord
import numpy
import requests
from PIL import Image
from colorama import Fore
from discord import Permissions
from discord.ext import commands
from discord.utils import get
from gtts import gTTS
from time import mktime
import rpc
#hypixel.setKeys(['975eeeec-10ae-470a-9f2c-d52309e794bb'])
from os import system

class SELFBOT():
    __version__ = 0.3


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

tts_language = "en"

start_time = datetime.datetime.utcnow()
# Replacement for asyncio.get_event_loop()
loop = asyncio.get_event_loop()


languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def startprint():

    print(f'''{Fore.RESET}

                 ▄████▄  ██▀███  ▓██   ██▓ ██▓███  ▄▄▄█████▓ ▒█████   ██▀███   ██▓███   ▄████▄ 
                ▒██▀ ▀█ ▓██ ▒ ██▒ ▒██  ██▒▓██░  ██ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▓██░  ██ ▒██▀ ▀█ 
                ▒▓█    ▄▓██ ░▄█ ▒  ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒▓██░ ██▓▒▒▓█    ▄
                ▒▓▓▄ ▄██▒██▀▀█▄    ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ▒██▄█▓▒ ▒▒▓▓▄ ▄██
                ▒ ▓███▀ ░██▓ ▒██▒  ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒▒██▒ ░  ░▒ ▓███▀ 
                ░ ░▒ ▒  ░ ▒▓ ░▒▓░   ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒▓▒░ ░  ░░ ░▒ ▒  
                  ░  ▒    ░▒ ░ ▒  ▓██ ░▒░ ░▒ ░         ░      ░ ▒ ▒░   ░▒ ░ ▒░░▒ ░       ░  ▒  
                ░         ░░   ░  ▒ ▒ ░░  ░░         ░      ░ ░ ░ ▒     ░   ░ ░░       ░       
                ░ ░        ░      ░ ░                           ░ ░     ░              ░ ░     

                       {Fore.CYAN}CryptoRPC v{SELFBOT.__version__} | {Fore.GREEN}Logged in as: {lilith.user.name}#{lilith.user.discriminator} {Fore.CYAN}| ID: {Fore.GREEN}{lilith.user.id}   
                       {Fore.CYAN}Cached Users: {Fore.GREEN}{len(lilith.users)}
                       {Fore.CYAN}Guilds: {Fore.GREEN}{len(lilith.guilds)}
                       {Fore.CYAN}Prefix: {Fore.GREEN}{lilith.command_prefix}

                       {Fore.CYAN}By: {Fore.GREEN}Lilith❤#0001
    ''' + Fore.RESET)


def Clear():
    os.system('cls')

Clear()


def Init():
    token = config.get('token')
    try:
        lilith.run(token, bot=False, reconnect=True)
        system("title Lilith v{}".format(SELFBOT.__version__))
        startprint()
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer


@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


colorama.init()
lilith = discord.Client()
lilith = commands.Bot(description='CryptoRPC - By Lilith❤#0001', command_prefix=prefix, self_bot=True)
lilith.remove_command('help')

@lilith.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        await ctx.send(f'[ERROR]: {error_str}', delete_after=3)

@lilith.event
async def on_connect():
    Clear()
    startprint()

@lilith.command()
async def RPC(ctx, crypto_currency: str, fiat_currency: str):
    await ctx.message.delete()
    if crypto_currency is None:
        await ctx.send(f"`Please specify a cryptocurrency to track!`")
        return
    if fiat_currency is None:
        await ctx.send(f"`Please specify a fiat currency to track!`")
        return
    crypto_currency = crypto_currency.upper()
    if crypto_currency == ("BITCOIN"):
        crypto_currency = "BTC"
    elif crypto_currency == ("ETHEREUM"):
        crypto_currency = "ETH"
    elif crypto_currency == ("ETHERIUM"):
        crypto_currency = "ETH"
    elif crypto_currency == ("LITECOIN"):
        crypto_currency = "LTC"
    elif crypto_currency == ("RIPPLE"):
        crypto_currency = "XRP"
    elif crypto_currency == ("BITCOIN CASH"):
        crypto_currency = "BCH"
    elif crypto_currency == ("BITCOIN GOLD"):
        crypto_currency = "BTG"
    elif crypto_currency == ("BITCOIN SV"):
        crypto_currency = "BSV"
    elif crypto_currency == ("MONERO"):
        crypto_currency = "XMR"
    elif crypto_currency == ("ZCASH"):
        crypto_currency = "ZEC"
    elif crypto_currency == ("ETHEREUM CLASSIC"):
        crypto_currency = "ETC"
    elif crypto_currency == ("BINANCE"):
        crypto_currency = "BNB"
    elif crypto_currency == ("CARDANO"):
        crypto_currency = "ADA"
    elif crypto_currency == ("DOGECOIN"):
        crypto_currency = "DOGE"

    fiat_currency = fiat_currency.upper()
    if fiat_currency == ("USDOLLAR"):
        fiat_currency = "USD"
    elif fiat_currency == ("EURO"):
        fiat_currency = "EUR"
    elif fiat_currency == ("POUND"):
        fiat_currency = "GBP"
    elif fiat_currency == ("AUSTRALIANDOLLAR"):
        fiat_currency = "AUD"
    elif fiat_currency == ("CANADIANDOLLAR"):
        fiat_currency = "CAD"
    # Autocomplete for fiat currencies

    await ctx.send(f"`Tracking {crypto_currency} in {fiat_currency}, updating every Minute!`")
    last_result = "0.0"
    while True:
        try:
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={crypto_currency}&tsyms={fiat_currency}')
            responsexd = r.json()
            result = responsexd[f'{fiat_currency}']
            changed_up_down = ""
            if result > float(last_result):
                changed_up_down = "increase"
            elif result < float(last_result):
                changed_up_down = "decrease"
            build_price = f"{result} {fiat_currency}"
            if result == None:
                await ctx.send(f"`No valid currency found.`")
                return
            client_id = '991087075610734602'
            start_time = mktime(time.localtime())
            rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
            changed_up_down.lower()
            last_result = result
            activity = {
                "state": "Updating every Minute!",
                "details": (build_price),
                "timestamps": {
                "start": start_time
                    },
                "assets": {
                    "small_text": "Compared to the last minute!",
                    "small_image": (changed_up_down),
                    "large_text": "Made by Lilith❤#0001",
                    "large_image": (crypto_currency.lower())
                    }
                }
            rpc_obj.set_activity(activity)
            await asyncio.sleep(60)
        except Exception as e:
            print(e)
            await ctx.send(f"{ctx.author.mention} An error has occurred")
            return



@lilith.command()
async def track(ctx, crypto_currency = str, fiat_currency = str):
    await ctx.message.delete()
    if crypto_currency is None:
        await ctx.send(f"`Please specify a cryptocurrency to track`")
        return
    if fiat_currency is None:
        await ctx.send(f"`Please specify a fiat currency to track`")
        return
    crypto_currency = crypto_currency.upper()
    if crypto_currency == ("BITCOIN"):
        crypto_currency = "BTC"
    elif crypto_currency == ("ETHEREUM"):
        crypto_currency = "ETH"
    elif crypto_currency == ("ETHERIUM"):
        crypto_currency = "ETH"
    elif crypto_currency == ("LITECOIN"):
        crypto_currency = "LTC"
    elif crypto_currency == ("RIPPLE"):
        crypto_currency = "XRP"
    elif crypto_currency == ("BITCOIN CASH"):
        crypto_currency = "BCH"
    elif crypto_currency == ("BITCOIN GOLD"):
        crypto_currency = "BTG"
    elif crypto_currency == ("BITCOIN SV"):
        crypto_currency = "BSV"
    elif crypto_currency == ("MONERO"):
        crypto_currency = "XMR"
    elif crypto_currency == ("ZCASH"):
        crypto_currency = "ZEC"
    elif crypto_currency == ("ETHEREUM CLASSIC"):
        crypto_currency = "ETC"
    elif crypto_currency == ("BINANCE", "BINANCE COIN"):
        crypto_currency = "BNB"
    elif crypto_currency == ("CARDANO"):
        crypto_currency = "ADA"

    fiat_currency = fiat_currency.upper()
    if fiat_currency == ("US DOLLAR"):
        fiat_currency = "USD"
    elif fiat_currency == ("EURO"):
        fiat_currency = "EUR"
    elif fiat_currency == ("POUND"):
        fiat_currency = "GBP"
    elif fiat_currency == ("AUSTRALIAN DOLLAR"):
        fiat_currency = "AUD"
    elif fiat_currency == ("CANADIAN DOLLAR"):
        fiat_currency = "CAD"
    elif fiat_currency == ("SWISS FRANC"):
        fiat_currency = "CHF"
    await ctx.send(f"`Tracking {crypto_currency} in {fiat_currency}, updating every 10 seconds`")
    last_result = "0.0"
    while True:
        try:
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={crypto_currency}&tsyms={fiat_currency}')
            r = r.json()
            fiat_currency = r[f'{fiat_currency}']
            result = str(fiat_currency)
            changed_up_down = ""
            if result > float(last_result):
                changed_up_down = "📈"
            elif result < float(last_result):
                changed_up_down = "📉"
            build_price = ""
            if fiat_currency == "usd":
                build_price = f"{result} USD"
            elif fiat_currency == "eur":
                build_price = f"{result} EUR"
            elif fiat_currency == "gbp":
                build_price = f"{result} GBP"
            elif fiat_currency == "aud":
                build_price = f"{result} AUD"
            elif fiat_currency == "cad":
                build_price = f"{result} CAD"
            elif fiat_currency == "chf":
                build_price = f"{result} CHF"
            if result == None:
                await ctx.send(f"`An error has occurred`")
                return

            message = (f"{crypto_currency} | {build_price} | {changed_up_down}")
            await lilith.change_presence(
                activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=message
                ))
            await asyncio.sleep(10)
        except Exception as e:
            print(e)
            await ctx.send(f"{ctx.author.mention} An error has occurred")
            return

@lilith.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching", "stopactivity", "stopprocessing"])
async def stoptracking(ctx):
    await ctx.message.delete()
    await lilith.change_presence(activity=None)
    await ctx.send("`Stopped tracking!`")


if __name__ == '__main__':
    Init()
