from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from datetime import datetime
import parsedatetime
from dateutil.parser import parse
import requests

from typing import Dict, Text, Any, List, Union
from rasa_core_sdk import Action, Tracker
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk.events import SlotSet, AllSlotsReset
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class CreateReportForm(FormAction):

    def name(self):
        return "create_report_form"

    @staticmethod
    def required_slots(tracker:Tracker) :
        return ["name", "startdate", "enddate"]

    def slot_mappings(self):
        return {"name": [self.from_entity(entity="name",intent=["enterdata"]),
                             self.from_text()],

                "startdate":[self.from_entity(entity="startdate",  intent=["enterdata"]),
                             self.from_text(intent="enterdata")],

                "enddate":[self.from_entity(entity="enddate", intent=["enterdata"]),
                             self.from_text(intent="enterdata")]}


    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)


        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            # print(slot_values)
            # if not slot_values:
            #     raise ActionExecutionRejection(self.name(),
            #                                    "Failed to validate slot {0}"
            #                                    "with action {1}"
            #                                    "".format(slot_to_fill,
            #                                              self.name()))

        

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]


    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        
        def date_formater(dt):
                try:
                    dt = parse(dt)
                    # currentMonth = datetime.now().month
                    # currentYear = datetime.now().year
                    # if currentMonth < dt.month:
                    #     if currentYear <= dt.year:
                    #         return f"{(dt.year)-1}-{dt.month}-{dt.day}"
                    #     else:
                    #         return f"{dt}"
                    # else:
                    #     return f"{dt}"
                    return f"{dt}"   
                except ValueError:
                    cal = parsedatetime.Calendar()
                    time_struct, parse_status = cal.parse(dt)
                    return f"{datetime(*time_struct[:6])} "
                    

        name = tracker.get_slot('name')
        startdate = tracker.get_slot('startdate')
        enddate = tracker.get_slot('enddate')

        startdate = date_formater(startdate)[:10]

        enddate = date_formater(enddate)[:10]
        r = requests.post('https://demo.sutiexpense.com/SutiExpense7.x/iphoneexpsave.do?navfrom=android&sutitest=true', data =  {"compid": "1403","userid": "1552","delusr": "0","version": "8.4.0","copylines": "Slelect","mcurr": "","Department Name": "Dept1","Product Line Code": "gfg - Cghg","Client Code": "kkkkkk","Project Code": "fdfdf - fdfdf","expType": "report","expNm": f"{name}","expDt": f'{startdate}',"fdate": f'{enddate}',"tdate": f"{startdate}","expDesc": "","isencrypt":"No"})
        if r.status_code == 200:
            json_data = r.json()
            if json_data.get('status') == 'success':
                expid = json_data.get('expid')
                response = f'Created a report "{name}" with start-date as {startdate} and end-date as {enddate}.Expense id of the created report is {expid}'
                # all slots reset
                # tracker._reset_slots()
                dispatcher.utter_message(response)
                return [AllSlotsReset()]
            elif json_data.get('status') == 'fail':
                print("status failed")
                print(name)
                print(startdate)
                print(enddate)
                if json_data.get('errmsg'):
                    if json_data.get('errmsg') == 'Duplicate expense name':
                        msg = f".Name already exists: {name}"
                        response = json_data.get('errmsg') + msg
                        print("got into fail and name error")
                        dispatcher.utter_message(response)
                        return [SlotSet("name", None)]
                    else:
                        response = json_data.get('errmsg')
                    # reset slot name
                else:
                    response = "Couldnt create the report at the moment."
            else:
                response = "Tried to create the report.Got an unexpected message"
        else:
            response = "Couldnt get the reports at this point of time."
        dispatcher.utter_message(response)
        # dispactcher.utter_template("utter_ask_lineitem",tracker)
        # dispatcher.utter_message(f'Created a report {name} with start-date as {startdate} and end-date as {enddate}')
        return []

class ActionSlotReset(Action):
    def name(self):
        return "action_slot_reset"
    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


# class CreateReport(Action):
#     def name(self):
#         return "create_report"

#     def run(self, dispatcher, tracker, domain):
#         name = tracker.get_slot('name')
#         startdate = tracker.get_slot('startdate')
#         enddate = tracker.get_slot('enddate')
        
#         if name and startdate and enddate:
#             with open(name + ".txt",w) as file:
#                 file.write(startdate + '\n')
#                 file.write(enddate + '\n')
#             dispatcher.utter_template('utter_created_report', tracker)
#             return []
#         else:
#             if not name:
#                 dispatcher.utter_template('utter_name', tracker)
#             elif not startdate:
#                 dispatcher.utter_template('utter_startdate', tracker)
#             elif not enddate:
#                 dispatcher.utter_template('utter_enddate', tracker)
#             else:
#                 return []

# class SendForApprove(Action):
#     def name(self):
#         return "send_for_approve"

#     def run(self, dispatcher, tracker,domain):
#         expid = tracker.get_slot('expid')
#         if not expid:
#             dispatcher.utter_template("utter_ask_expid", tracker)
#             expid = tracker.latest_message.get('text')
#         if expid.isdigit():
#             dispatcher.utter_message(f"Sent the report with expid: {expid}, for approval.")


class PendingReport(Action):
    def name(self):
        return "pending_report"

    def run(self, dispatcher, tracker, domain):
        print(tracker.__dir__())
        response = ''
        r = requests.post('https://demo.sutiexpense.com/SutiExpense8.x/iphoneapp.do?callto=getExps&navfrom=android&sutitest=true', data = {"userid": "9364","compid": "1403","delusr": "0","version": "8.4.0","isencrypt":"No"})
        if r.status_code == 200:
            json_data = r.json()
            if json_data.get('status') == 'success':
                if json_data['exps']:
                    response += f"Total their are {len(json_data['exps'])} pending reports as follows: @#$"
                    for exp in json_data['exps']:
                        response += f"{exp['expname']} with report id {exp['expid']}, generated on {exp['expdt']}.@#$"
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