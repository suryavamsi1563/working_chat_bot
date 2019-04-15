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
from rasa_core.actions.action import ACTION_LISTEN_NAME

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

# <------------------ APPROVAL ACTIONS START ---------------->

class Writing_approve(Action):
    def name(self):
        return "action_approve_report"

    def run(self, dispatcher, tracker, domain):
        response = "Showing 2 reports requiring your approval:@#$@#$"
        report_names = []
        buttons = [{'title': 'low', 'payload': 'low'}] 
        #<------------------ API CALL BELOW ---------------->
        json_response = []
        r = requests.post("https://demo.sutiexpense.com/SutiExpense8.x/iphoneapprove.do?callto=getExpAppRecords&navfrom=android&sutitest=yes",data={"userid": "9409","compid": "1403","version": "8.4.0"})
        if r.status_code == 200:
            json_data = r.json()
            if json_data.get('status') == 'success':
                if json_data['exps']:
                    no_of_reports = len(json_data['exps'])
                    dispatcher.utter_message(f"There are {no_of_reports} reports waiting for your approval as follows: ")
                    for exp in json_data['exps']:
                        json_response.append({
                            'expname': exp['expname'],
                            'amt': exp['amt'],
                            'crtuserid':exp['crtuserid'],
                            'compexpid' : exp['compexpid'],
                            'expid': exp['expid'],
                            'expdt': exp['expdt'],
                            'subby':exp['subby'],
                            'text': f"Report '{exp['expname']}' created by '{exp['subby']}' for an amount  ${exp['amt']} on {exp['expdt']}."
                        })
                    response = json.dumps(json_response)
                else:
                    response = "No reports for you to approve."
            elif json_data.get('status') == 'fail':
                if json_data.get('errmsg'):
                    response = json_data.get('errmsg')
                else:
                    response = "Couldnt create the report at the moment."
            else:
                response = "Tried to create the report.Got an unexpected message"
        else:
            response = "Couldnt get the reports at this point of time."

        dispatcher.utter_message(response)
        # report_data = {
        #     "John":["E000125","June 2018"],
        #     "Will":["ER0214256","Opera_2013"]
        # }
        # names = report_data.keys()
        # report_names = [x[1] for x in report_data.values()]
        # expids= [x[0] for x in report_data.values()]

        # for x,y,z in zip(names,report_names,expids):
        #     response += f'{y} created by {x} with  expense id {z}@#$'
        
        

        # return[SlotSet("name_list", report_names), SlotSet("expid_list", expids),SlotSet("report_data",report_data)]
        return []


# class Writing_approve(Action):
#     def name(self):
#         return "action_approve_report"

#     def run(self, dispatcher, tracker, domain):
#         response = "Showing 2 reports requiring your approval:@#$@#$"
#         report_names = []
#         #<------------------ API CALL BELOW ---------------->
#         report_data = {
#             "John":["E000125","June 2018"],
#             "Will":["ER0214256","Opera_2013"]
#         }
#         names = report_data.keys()
#         report_names = [x[1] for x in report_data.values()]
#         expids= [x[0] for x in report_data.values()]

#         for x,y,z in zip(names,report_names,expids):
#             response += f'{y} created by {x} with  expense id {z}@#$'
#         dispatcher.utter_message(response)
        
#         return[SlotSet("name_list", report_names), SlotSet("expid_list", expids),SlotSet("report_data",report_data)]


class Approvingreports(FormAction):
    def name(self):
        return "approve_report_form"
  
    @staticmethod
    def required_slots(tracker:Tracker) :
        return ["expid_or_name"]

    def slot_mappings(self):
        return {"expid_or_name": [self.from_entity(entity="expid_or_name",intent=["approvals"]), self.from_text()]}

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
    def submit(self,dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:               

        expid_or_name = tracker.get_slot('expid_or_name')
        names = tracker.get_slot('name_list')
        expids = tracker.get_slot('expid_list')
        report_data = tracker.get_slot("report_data")
        print(names)
        print(expids)
        print(type(names[0]))
        print(len(names[0]))
        print(expid_or_name)
        print(type(expid_or_name))
        print(len(expid_or_name))
        report_name = ""
        user_name = ""
        expid = ""
        for x in report_data:
            if expid_or_name in report_data[x]:
                user_name = x
                report_name = report_data[x][1]
                expid = report_data[x][0]
        print("Report Nme is: ",report_name)
        print("user Nme is: ",user_name)
        print("Expid is: ",expid)
        response = f"{report_name} created by {user_name} with expid {expid}.The report has 2 line items as follows: @#$@#$"
        if (expid_or_name in names) or (expid_or_name in expids) : 
            print("Entered name ", expid_or_name)
            response += "Requested for $100 for meals spent at Eastern Delight. Reciept available.@#$Requested for $25 for Hotel spent at Eastern Delight. Reciept available."
            dispatcher.utter_message(response)
            return[FollowupAction("utter_ask_approve")]
        else:
            dispatcher.utter_message("Please enter correct name or expid !!!")
            return [SlotSet("expid_or_name", None),FollowupAction('approve_report_form')]
        
class ApproveOrRejectAction(Action):
    def name(self):
        return "action_approve_or_reject"

    def run(self, dispatcher, tracker, domain):
        sender = {
            'user_id':9364,
            'comp_id':1403,
            'approver':"Yes"
        }
        appr_or_rej = tracker.get_slot('appr_or_rej')
        if appr_or_rej == 'Approve':
            dispatcher.utter_message("Approved the report.")
        elif appr_or_rej == "Reject":
            dispatcher.utter_message("Rejected the report.")
        
class CustomGreet(Action):
    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        # sender_details = tracker.current_state()['sender_id']
        # print(sender_details)
        # sender_details = sender_details.replace('\'','\"')
        # print(sender_details)
        # sender = json.loads(sender_details)
        # print(sender)
        sender = {
            'user_id':9364,
            'comp_id':1403,
            'approver':"Yes"
        }
        user_id = sender['user_id']
        comp_id = sender['comp_id']
        
        response = "Hey there, welcome to Suti!"
        dispatcher.utter_message(response)
        if 'approver' in sender:
            SlotSet("approver_or_not", True)
            return[FollowupAction('action_approve_report')]
        else:
            SlotSet("approver_or_not", False)
            dispatcher.utter_message("You r not an approver")
            return[FollowupAction(ACTION_LISTEN_NAME)]