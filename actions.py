# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import requests

class FormContact(FormAction):

    def name(self) -> Text:
        return "form_contact"
    
    @staticmethod
    def required_slots(tracker):
        return ["email","phone-number","PERSON"]


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionSelektor(Action):
    def name(self) -> Text:

        return "action_selektor"

    def run(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #  mydata ="hi how are you"
        response = requests.request("GET","http://thecreativeorchards.com/time.php")
        result = "" 
        json_data = response.json()
        result +="Hello >>"+ json_data["salutation"]
        dispatcher.utter_message(text=result)

        return []
