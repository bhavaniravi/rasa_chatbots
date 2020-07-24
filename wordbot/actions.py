

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        synonyms.append(syn.definition())
    return synonyms

def get_antonym(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l)
    return list(set(antonyms))



class ActionGetMeaning(Action):

    def name(self) -> Text:
        return "action_get_meaning"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # bot cannot find entity
        try:
            print (tracker.latest_message["entities"])
            word = list(tracker.get_latest_entity_values("word"))[0]
        except:
            dispatcher.utter_message(text=f"Sorry I didn't get what you are saying")
            return []

        meaning = get_synonyms(word)

        # bot cannot find meaning
        if  meaning:
            meaning = meaning[0]
            dispatcher.utter_message(text=f"The meaning of word {word} is {meaning}")
        else: 
            dispatcher.utter_message(text=f"Couldn't find meaning for the {word}")
        return []


class ActionGetOpposite(Action):

    def name(self) -> Text:
        return "action_get_opposite"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # bot cannot find entity
        try:
            print (tracker.latest_message["entities"])
            word = list(tracker.get_latest_entity_values("word"))[0]
        except:
            dispatcher.utter_message(text=f"Sorry I didn't get what you are saying")
            return []
        
        opposite = get_antonym(word)
        if  opposite:
            opposite = opposite[0]
            dispatcher.utter_message(text=f"The meaning of word {word} is {opposite}")
        else: 
            dispatcher.utter_message(text=f"Couldn't find meaning for the {word}")
        return []
