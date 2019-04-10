from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from datetime import datetime
import requests
import json 

from typing import Dict, Text, Any, List, Union
from rasa_core_sdk import Action, Tracker
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk.events import SlotSet, AllSlotsReset, FollowupAction, Restarted
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

class CreateReportForm(FormAction):

    def name(self):
        return "create_report_form"

    @staticmethod
    def required_slots(tracker:Tracker) :
        return ["name"]

    def slot_mappings(self):
        return {"name": [self.from_entity(entity="name",intent=["enterdata"]),
                             self.from_text()]}


    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)


        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        name = tracker.get_slot('name')
        date = str(datetime.now().date())
        # sender_details = ''
        # sender_details = tracker.current_state()['sender_id']
        # sender_details = sender_details.replace('\'','\"')
        # sender = json.loads(sender_details)
        # user_id = sender['user_id']
        # comp_id = sender['comp_id']
        user_id = "9364"
        comp_id = "1403"
        print("Inside Create Report Form")
        
        r = requests.post('https://demo.sutiexpense.com/SutiExpense7.x/iphoneexpsave.do?navfrom=android&sutitest=true', data =  {"compid": f"{comp_id}","userid": f"{user_id}","delusr": "0","version": "8.4.0","copylines": "Slelect","mcurr": "","Department Name": "Dept1","Product Line Code": "gfg - Cghg","Client Code": "kkkkkk","Project Code": "fdfdf - fdfdf","expType": "report","expNm": f"{name}","expDt": f'{date}',"fdate": f'{date}',"tdate": f"{date}","expDesc": "","isencrypt":"No"})
        if r.status_code == 200:
            json_data = r.json()
            if json_data.get('status') == 'success':
                compexpid = json_data["exps"][0].get('compexpid')
                expid = json_data["exps"][0].get('expid')
                response = f'Created a report "{name}" with Company expense id as  {compexpid}'
                dispatcher.utter_message(response)
                return [SlotSet("compexpid", compexpid),SlotSet("expid", expid)]
            elif json_data.get('status') == 'fail':
                if json_data.get('errmsg'):
                    if json_data.get('errmsg') == 'Duplicate expense name':
                        msg = f"Name already exists: {name}"
                        response = "Name already Exists."
                        dispatcher.utter_message(response)
                        return [SlotSet("name", None),FollowupAction('create_report_form')]
                    else:
                        response = json_data.get('errmsg')
                else:
                    response = "Couldnt create the report at the moment."
            else:
                response = "Tried to create the report.Got an unexpected message"
        else:
            response = "Couldnt get the reports at this point of time."
        dispatcher.utter_message(response)
        # dispatcher.utter_message("Created the report")
        return []


class AddReceiptForm(FormAction):

    def name(self):
        return "add_receipt_form"

    @staticmethod
    def required_slots(tracker:Tracker) :
        return ["no_more_receipts"]

    def slot_mappings(self):
        return {"no_more_receipts": [self.from_entity(entity="no_more_receipts",intent=["choose"]),
                             self.from_text("choose")]}

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)


        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:               

        no_receipts = tracker.get_slot('no_more_receipts')
        print("Inside Add Receipt Form")
        if no_receipts ==  "camera":
            dispatcher.utter_message("openning Camera")
            dispatcher.utter_message("Added the receipt.")
# #      <------------------------ API call for camera----------------------------->
#             r = requests.post('http://192.168.0.243/SutiExpense/iphoneapp.do?callto=vcParse&navfrom=android', data =  {"compid": "1403","userid": "9364","delusr": "0","version": "8.4.0","vc": "open settings","screen": "camera","navigation": "navigation"})
#             if r.status_code == 200:
#             json_data = r.json()
#             if json_data.get('status') == 'success':
#                 print("Success Fully navigated to camera")
# #      <------------------------ API call end camera----------------------------->
            return [FollowupAction('utter_ask_receipt')]
        elif no_receipts == "attach":
            dispatcher.utter_message("attachment successfull.")
            dispatcher.utter_message("Added the receipt.")
            return [FollowupAction('utter_ask_receipt')]
        elif no_receipts == "No":
            expid = tracker.get_slot("expid")
            name = tracker.get_slot("name")
            compexpid = tracker.get_slot("compexpid")
            print(f"Inside No of Add Receipt Form.Slots are {expid},{name},{compexpid}")
            return [FollowupAction('utter_ask_submit_report')]

class PendingReport(Action):
    def name(self):
        return "pending_report"

    def run(self, dispatcher, tracker, domain):
        
        print("Inside Pending Reports")
        if 'user' in tracker.current_state()['sender_id']:
            sender_details = tracker.current_state()['sender_id']
            sender_details = sender_details.replace('\'','\"')
            sender = json.loads(sender_details)
            user_id = sender['user_id']
            comp_id = sender['comp_id']
            print(user_id)
            print(comp_id)
        response = ''
        user_id = "9364"
        comp_id = "1403"
# <------------------ API CALL BELOW ---------------->
        json_response = []
        r = requests.post('https://demo.sutiexpense.com/SutiExpense8.x/iphoneapp.do?callto=getExps&navfrom=android&sutitest=true', data = {"userid": f"{user_id}","compid": f"{comp_id}","delusr": "0","version": "8.4.0","isencrypt":"No"})
        if r.status_code == 200:
            json_data = r.json()
            if json_data.get('status') == 'success':
                if json_data['exps']:
                    for exp in json_data['exps']:
                        json_response.append({
                            'compexpid' : exp['compexpid'],
                            'expdt': exp['expdt'],
                            'nav_to':'drafts',
                            'text': f"{exp['expname']} with report id {exp['compexpid']}, generated on {exp['expdt']}"
                        }) 
                    response = json.dumps(json_response)
                else:
                    response("No pending reports available.")
            elif json_data.get('status') == 'fail':
                if json_data.get('errmsg'):
                    response = json_data.get('errmsg')
                else:
                    response = "Couldnt create the report at the moment."
            else:
                response = "Tried to create the report.Got an unexpected message"
        else:
            response = "Couldnt get the reports at this point of time."
# <------------------ API CALL ENDED ---------------->
        tracker.current_state()["sender_id"] = "Hello"
        elements = [
            {
                "images":[{
                    "nav":"nav123"
                }]
            },
        ]
        dispatcher.utter_message(response)
        return [Restarted()]


class NavToLineitems(Action):
    def name(self):
        return "nav_to_lineitems"

    def run(self, dispatcher, tracker, domain):

# <------------------ API CALL BELOW ---------------->

        # r = requests.post('https://demo.sutiexpense.com/SutiExpense8.x/iphoneapp.do?callto=getExps&navfrom=android&sutitest=true', data = {"userid": "9364","compid": "1403","delusr": "0","version": "8.4.0","isencrypt":"No", "screen": "create lineitem","navigation": "navigation"})
        # if r.status_code == 200:
        #     json_data = r.json()
        #     if json_data.get('status') == 'success':
        #         dispatcher.utter_template('utter_navlineitems',tracker)
        #     else:
        #         dispatcher.utter_message("Failed to navigate to 'Creation of line items'")
        # else:
        #     dispatcher.utter_message("Failed to make a request for navigating to 'Creation of line items'")
        # return []

# <------------------ API CALL ENDED ---------------->
        dispatcher.utter_template('utter_navlineitems',tracker)

class SubmitReport(Action):
    def name(self):
        return "action_submit_report"

    def run(self, dispatcher, tracker, domain):
        # sender_details = ''
        # sender_details = tracker.current_state()['sender_id']
        # sender_details = sender_details.replace('\'','\"')
        # sender = json.loads(sender_details)
        # user_id = sender['user_id']
        # comp_id = sender['comp_id']

        user_id = "9364"
        comp_id = "1403"
        compexpid = tracker.get_slot('compexpid')
        expid = tracker.get_slot('expid')
        name = tracker.get_slot('name')
        print("Inside Submit Report Action slots are {compexpid},{expid},{name}")
# <------------------ API CALL BELOW ---------------->

        r = requests.post('https://demo.sutiexpense.com/SutiExpense8.x/iphoneexpsubmit.do?navfrom=android&sutitest=true', data = {"userid": f"{user_id}","compid": f"{comp_id}","delusr": "0","version": "8.4.0","isencrypt":"No","expid":f'{expid}'})
        if r.status_code == 200:
            json_data = r.json()
            if json_data.get('status') == 'success':
                dispatcher.utter_message(f'Submited the report with expid {compexpid} successfully for approval')
            else:
                dispatcher.utter_message("Failed to add the recipt.Please try again later.'")
        else:
            dispatcher.utter_message("Failed to make a request for addition of receipt.'")
        return []

# <------------------ API CALL ENDED ---------------->
class ActionSlotReset(Action):
    def name(self):
        return "action_slot_reset"
    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]