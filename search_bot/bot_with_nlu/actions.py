# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from googlesearch import search


def search_bot(text):
    return "I have a link for you " + list(search(text, num=1, stop=1, pause=2))[0]


class ActionFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = search_bot(tracker.latest_message["text"])
        dispatcher.utter_message(response)
        return []


class SearchGoogle(Action):
    def name(self) -> Text:
        return "action_search_google"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            search_term = tracker.latest_message['entities'][0]["value"]
        except (KeyError, IndexError):
            search_term = tracker.latest_message["text"]
        response = search_bot(search_term)
        dispatcher.utter_message(response)

        return []

