

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms

def get_antonym(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return list(set(antonyms))



class ActionGetMeaning(Action):

    def name(self) -> Text:
        return "action_get_meaning"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        word = list(tracker.get_latest_entity_values("word"))[0]

        meaning = get_synonyms(word)
        dispatcher.utter_message(text=f"The meaning of word {word} is {meaning}")

        return []


class ActionGetOpposite(Action):

    def name(self) -> Text:
        return "action_get_opposite"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        word = list(tracker.get_latest_entity_values("word"))[0]
        opposite = get_antonym(word)
        dispatcher.utter_message(text=f"The meaning of word {word} is {opposite}")

        return []
