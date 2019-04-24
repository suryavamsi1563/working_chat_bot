from __future__ import absolute_import, division, unicode_literals

import json
from datetime import datetime
from typing import Any, Dict, List, Text, Union

import requests
from rasa_core_sdk import Action, ActionExecutionRejection, Tracker
from rasa_core_sdk.events import (AllSlotsReset, FollowupAction,SlotSet)
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import REQUESTED_SLOT, FormAction


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
        # if 'user' in tracker.current_state()['sender_id']:
        #     sender_details = tracker.current_state()['sender_id']
        #     sender_details = sender_details.replace('\'','\"')
        #     sender = json.loads(sender_details)
        #     user_id = sender['user_id']
        #     comp_id = sender['comp_id']
        #     print(user_id)
        #     print(comp_id)
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
                    # for exp in json_data['exps']:
                    #     json_response.append({
                    #         'compexpid' : exp['compexpid'],
                    #         'expdt': exp['expdt'],
                    #         'nav_to':'drafts',
                    #         'text': f"{exp['expname']} with report id {exp['compexpid']}, generated on {exp['expdt']}"
                    #     }) 
                    # response = json.dumps(json_response)
                    no_of_reports = len(json_data['exps'])
                    # Custom code for setting reports to 1
                    no_of_reports = 1
                    if no_of_reports == 1:
                        # dispatcher.utter_message(f"There is one pending report you have ")
                        compexpid = ""
                        expid=""
                        for exp in json_data['exps']:
                            json_response.append({
                            'compexpid' : exp['compexpid'],
                            'expdt': exp['expdt'],
                            'nav_to':'drafts',
                            'text': f"{exp['expname']} with report id {exp['compexpid']}, generated on {exp['expdt']}"
                                                }) 
                            break
                        response = json.dumps(json_response)    
                        dispatcher.utter_message(response)
                        # dispatcher.utter_template("utter_ask_receipt")
                        return [FollowupAction("utter_ask_addline_or_submit")]
                    elif no_of_reports > 1 and no_of_reports <= 3:
                        number_word = {
                            2:"two",
                            3:"three"
                        }
                        # dispatcher.utter_message(f"There are {number_word[no_of_reports]} pending reports you have. ")
                        
                        for exp in json_data['exps'][:no_of_reports]:
                            json_response.append({
                                'compexpid' : exp['compexpid'],
                                'expdt': exp['expdt'],
                                'nav_to':'drafts',
                                'text':f"{exp['expname']} with report id {exp['compexpid']}, generated on {exp['expdt']}"
                            })
                        response = json.dumps(json_response)
                        dispatcher.utter_message(response)
                        dispatcher.utter_message("Select a report to see summary :")
                        return [ SlotSet('pending_report_list',json_data['exps'][:no_of_reports]), FollowupAction('action_listen')]
                    elif no_of_reports > 3:
                        buttons = [
                                    {
                                        "title": "Go to pendingreports", 
                                        "payload": "/go_to_pendingreports"
                                    }]
                        dispatcher.utter_button_message(f"There are {no_of_reports} pending reports you have",buttons)
                        return [FollowupAction('action_listen')]

                    else:
                        dispatcher.utter_message("You have no pending reports .")
                        dispatcher.utter_message("Do you need anything else ? ")
                        return [FollowupAction('action_listen')]
                else:
                    response=("No pending reports available.")

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
        dispatcher.utter_message(response)
        return []


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

        # r = requests.post('https://demo.sutiexpense.com/SutiExpense8.x/iphoneexpsubmit.do?navfrom=android&sutitest=true', data = {"userid": f"{user_id}","compid": f"{comp_id}","delusr": "0","version": "8.4.0","isencrypt":"No","expid":f'{expid}'})
        # if r.status_code == 200:
        #     json_data = r.json()
        #     if json_data.get('status') == 'success':
        #         dispatcher.utter_message(f'Submited the report with expid {compexpid} successfully for approval')
        #     else:
        #         dispatcher.utter_message("Failed to add the recipt.Please try again later.'")
        # else:
        #     dispatcher.utter_message("Failed to make a request for addition of receipt.'")
        dispatcher.utter_message("Submited the report")
        return [AllSlotsReset()]

# <------------------ API CALL ENDED ---------------->
class ActionSlotReset(Action):
    def name(self):
        return "action_slot_reset"
    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class Writing_approve(Action):
    def name(self):
        return "action_approve_report"

    def run(self, dispatcher, tracker, domain):
        response = "Showing 2 reports requiring your approval:@#$@#$"
        report_names = []
        #<------------------ API CALL BELOW ---------------->
        json_response = []
        r = requests.post("https://demo.sutiexpense.com/SutiExpense8.x/iphoneapprove.do?callto=getExpAppRecords&navfrom=android&sutitest=yes",data={"userid": "9409","compid": "1403","version": "8.4.0"})
        if r.status_code == 200:
            json_data = r.json()
            if json_data.get('status') == 'success':
                print(json_data['exps'])
                if json_data['exps']:
                    no_of_reports = len(json_data['exps'])
                    # Custom code for setting reports to 1
                    no_of_reports = 3
                    if no_of_reports == 1:
                        dispatcher.utter_message(f"There is one report waiting for your approval. ")
                        dispatcher.utter_message(f'Report summary is: ')
                        compexpid = ""
                        expid=""
                        for exp in json_data['exps']:
                            response = f"Report '{exp['expname']}' created by '{exp['subby']}' for an amount  ${exp['amt']} on {exp['expdt']}.Comp expid is {exp['compexpid']}"
                            compexpid = exp['compexpid']
                            expid = exp['expid']
                            # Custom code for setting reports to 1
                            break
                        dispatcher.utter_message(response)
                        dispatcher.utter_template("utter_ask_approve",tracker)
                        return [SlotSet('compexpid',compexpid),SlotSet('expid',expid),FollowupAction("action_listen")]
                    elif no_of_reports > 1 and no_of_reports <= 3:
                        number_word = {
                            2:"two",
                            3:"three"
                        }
                        dispatcher.utter_message(f"There are {number_word[no_of_reports]} reports waiting for your approval. ")
                        
                        for exp in json_data['exps'][:no_of_reports]:
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
                        dispatcher.utter_message(response)
                        dispatcher.utter_message("Select a report for summary:")
                        return [ SlotSet('appr_report_list',json_data['exps'][:no_of_reports]), FollowupAction('action_listen')]
                    elif no_of_reports > 3:
                        buttons = [
                                    {
                                        "title": "Go to approvals", 
                                        "payload": "/go_to_approvals"
                                    }]
                        dispatcher.utter_button_message(f"There are {no_of_reports} reports waiting for your approval. ",buttons)
                        return [FollowupAction('action_listen')]

                    else:
                        dispatcher.utter_message("You have no reports to approve.")
                        dispatcher.utter_message("Do you need anything else ? ")
                        return [FollowupAction('action_listen')]

class Approvingreports(FormAction):
    def name(self):
        return "approve_report_form"
  
    @staticmethod
    def required_slots(tracker:Tracker) :
        return ["comments"]

    def slot_mappings(self):
        return {"comments": [self.from_entity(entity="comments",intent=["enter_data"]), self.from_text()]}

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
        appr_or_rej = tracker.get_slot('appr_or_rej')
        compexpid = tracker.get_slot('compexpid')
        expid = tracker.get_slot('expid')
        comments = tracker.get_slot("comments")
        
        if appr_or_rej == "approve":
            #------------------ API CALL ------------
            # r = requests.post("https://demo.sutiexpense.com/SutiExpense8.x/iphoneapprove.do?callto=approve&navfrom=android&sutitest=yes",data={"userid": "9409","compid": "1403","version": "8.4.0","expid":f"{expid}","comments":f"{comments}"})
            # if r.status_code == 200:
            #     json_data = r.json()
            #     if json_data.get('status') == 'approved':
            #         response = f"Approved the report"
            #         # dispatcher.utter_message(f'{comments}')
            #     else:
            #         response = "Failed to Approve .Please try again later."
            # else:
            #     response = "Couldnt get the reports at this point of time."

            # dispatcher.utter_message(response)
            dispatcher.utter_message(f"Approved the report ")
            # dispatcher.utter_message(f'{comments}')
        elif appr_or_rej == "reject":
              #------------------ API CALL ------------
            # r = requests.post("https://demo.sutiexpense.com/SutiExpense8.x/iphoneapprove.do?callto=reject&navfrom=android&sutitest=yes",data={"userid": "9409","compid": "1403","version": "8.4.0","rejresn":"1062","expid":f"{expid}","comments":f"{comments}"})
            # if r.status_code == 200:
            #     json_data = r.json()
            #     if json_data.get('status') == 'rejected':
            #         response = f"Rejected the report"
            #         # dispatcher.utter_message(f'{comments}')
            #     else:
            #         response = "Failed to Reject .Please try again later."
            # else:
            #     response = "Couldnt get the reports at this point of time."

            # dispatcher.utter_message(response)
            dispatcher.utter_message(f"Rejected the report")
            # dispatcher.utter_message(f'{comments}')
      
        return [AllSlotsReset()]
        
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
        if appr_or_rej == 'approve':
            dispatcher.utter_message("Approved the report.")
        elif appr_or_rej == "reject":
            dispatcher.utter_message("Rejected the report.")
        
class First_message(Action):
    def name(self):
        return "action_first_message"

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
            'approver':'yes'
        }
        
        dispatcher.utter_message("Hey there, welcome to Suti!")
        
        if 'approver' in sender:
            SlotSet("approver_or_not", True)
            return[FollowupAction('action_approve_report')]
        else:
            SlotSet("approver_or_not", False)
            return[FollowupAction("pending_report")]


class go_to_approvals(Action):
    def name(self):
        return "action_goto_approvals"
    
    def run(self,dispatcher,tracker,domain):
        sender = {
            'user_id':9364,
            'comp_id':1403
            # 'approver':'yes'
  
        } 
        if 'approver' in sender:
            dispatcher.utter_message("Navigating to Approvals")
        else:
            
            dispatcher.utter_message("you are not an approver")
        
        return [AllSlotsReset()]

class go_to_pendingrports(Action):
    def name(self):
        return "action_goto_pendingreports"
    
    def run(self,dispatcher,tracker,domain):
        dispatcher.utter_message("Navigating to penidng reports")
        return [AllSlotsReset()]


class select_report(Action):
    def name(self):
        return "action_select_report"

    def run(self,dispatcher,tracker,domain):
        print(tracker.latest_message['text'])
        selection_message = tracker.latest_message['text'].lower()
        appr_report_list = tracker.get_slot("appr_report_list")
        print(appr_report_list)
        print()
        if 'second' in selection_message or '2' in selection_message or 'two' in selection_message:
            exp = appr_report_list[1]
        elif 'third' in selection_message or '3' in selection_message or 'three' in selection_message or 'last' in selection_message:
            exp = appr_report_list[2]
        elif 'first' in selection_message or '1' in selection_message or 'one' in selection_message or 'latest' in selection_message:
            exp = appr_report_list[0]
        else:
            dispatcher.utter_message("Please select a report: ")
            return [FollowupAction("action_listen")]
        response = f"Report '{exp['expname']}' created by '{exp['subby']}' for an amount  ${exp['amt']} on {exp['expdt']}.Comp expid is {exp['compexpid']}"
        dispatcher.utter_message(response)
        dispatcher.utter_template("utter_ask_approve",tracker)
        return [SlotSet('compexpid',exp['compexpid']),SlotSet('expid',exp['expid']),FollowupAction("action_listen")]

class select_pendingreport(Action):
    def name(self):
        return "action_select_penidngreport"

    def run(self,dispatcher,tracker,domain):
        print(tracker.latest_message['text'])
        selection_message = tracker.latest_message['text'].lower()
        pending_report_list = tracker.get_slot("pending_report_list")
        print(pending_report_list)
        print()
        if 'second' in selection_message or '2' in selection_message or 'two' in selection_message:
            exp = pending_report_list[1]
        elif 'third' in selection_message or '3' in selection_message or 'three' in selection_message or 'last' in selection_message:
            exp = pending_report_list[2]
        elif 'first' in selection_message or '1' in selection_message or 'one' in selection_message or 'latest' in selection_message:
            exp = pending_report_list[0]
        else:
            dispatcher.utter_message("Please select a report: ")
            return [FollowupAction("action_listen")]    
        response = f"{exp['expname']} with report id {exp['compexpid']}, generated on {exp['expdt']}"
        dispatcher.utter_message(response)
        # dispatcher.utter_template("utter_ask_approve",tracker)
        # return [SlotSet('compexpid',exp['compexpid']),SlotSet('expid',exp['expid']),FollowupAction("action_listen")]
        return [SlotSet("name",exp['expname']),FollowupAction("utter_ask_addline_or_submit")]        

class approve_report(Action):
    def name(self):
        return "approve_report"
    def run(self,dispatcher,tracker,domain):
        return[SlotSet("appr_or_rej","approve")]

class reject_report(Action):
    def name(self):
        return "reject_report"
    def run(self,dispatcher,tracker,domain):
        return[SlotSet("appr_or_rej","reject")]

class addlineitem_to_report(Action):
    def name(self):
        return "action_addlineitem_to_report"
    def run(self,dispatcher,tracker,domain):
        return[SlotSet("adlt_or_sub","addlineitem")]

class submit_report(Action):
    def name(self):
        return "action_submitpdr_report"
    def run(self,dispatcher,tracker,domain):
        return[SlotSet("adlt_or_sub","sumbit")]

class open_camera(Action):
    def name(self):
        return "open_camera"
    def run(self,dispatcher,tracker,domain):
        return [SlotSet("no_more_receipts","camera")]    

class attach_receipt(Action):
    def name(self):
        return "attach_receipt"
    def run(self,dispatcher,tracker,domain):
        return [SlotSet("no_more_receipts","attach")]   

class no_receipt(Action):
    def name(self):
        return "no_receipt"
    def run(self,dispatcher,tracker,domain):
        return [SlotSet("no_more_receipts","No")]      
