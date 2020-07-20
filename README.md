# Learn How to build a chatbot

I have been building chatbots for past 3 years using existing platforms like Google's Dialogflow, Wit.ai, Recast.ai. Over the years I have fallen in love with open source frameworks and Rasa is one of the best to build chatbots.
In this tutorial we will build 3 simple chatbots thereby understanding the basics and what differentiates chatbots webapps


## Bots
1. Echo bot - A bot that repeats whatever you say
2. Google Search Bot - A bot that searches Google for you
3. wordbot - A bot that gives you meaning and opposites

Each bot has it's own folder with `Tutorial.md` file.

## How do we build it?

Any chatbot building consist of 3 parts

1. Training your bot
2. Writing your actions
3. Giving a chat interface

## Prerequistes

This repo assumes you know python, if you don't learn basics of python and ML and get back here.

1. python 3.7
2. pip
3. virtualenv

## Setup

I use `virtualenv` to create a virtualenv and create

`pip install -r requirements.txt`


## Creating bot from scratch

```
mkdir <botname>
cd <botname>
rasa init
```

## Using Existing bot

### 1. Echo bot

For a bot that repeats whatever a user says we don't need any NLP. But this will help us few concepts.

But before moving on let's do this without any NLP.

`cd echo_bot/`

`python bot_without_nlp.py`


### 2. Search bot

Again, a search bot does not need much of NLP. But this example is just to explain how chatbots make an API call to fetch you data.

`cd search_bot/`

`python bot_without_nlp.py`

### 3. Word bot

1. Train the bot
```
cd wordbot
rasa train
```

2. Run the command line UI

```
rasa shell
```

3. Run the actions server

```
rasa run actions
```



