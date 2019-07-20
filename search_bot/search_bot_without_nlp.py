from base import bot_runner
from googlesearch import search


def search_bot(text):
    return "I have a link for you " + list(search(text, num=1, stop=1, pause=2))[0]


bot_runner(search_bot)
