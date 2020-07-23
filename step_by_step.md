# Creating a bot from Scratch

## Prerequistes

This repo assumes you know python, if you don't learn basics of python and get back here.

1. python 3.7
2. pip
3. virtualenv

## Setup

I use `virtualenv` to create a virtualenv and create

`pip install -r requirements.txt`

## Checklist before starting

1. Type `python` in a terminal and see if Python is installed
2. Type `rasa` and ensure rasa is installed

## Create a Rasa Project

```
mkdir <botname>
cd <botname>
rasa init
```

## Creating Training data

1. open `data/nlu.md` and update the file with your intent data
```
## intent:<intent_name>
- sentence 1
- sentence 2
- sentence 3
```

2. Open `data/stories.md` update it with the conversation flow

```
## <story name>
* <intent_name>
  - <action_name>
* <intent_name>{"<entity_name>": "<entity_word>"}
  - <action_name>
```

3. Open `domain.yml` fill in all the `intents, entities, actions and responses`

## Train the bot

```
rasa train
```

## Running the bot

1. Open `endpoints.yml` and uncomment the following lines

```
action_endpoint:
 url: "http://localhost:5055/webhook"
```

2. Open a terminal and run `rasa shell` this is your UI
3. Open another terminal and run `rasa run actions` this is your actions server.

