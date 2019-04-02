from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals


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
                             self.from_text(intent="enterdata")],

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

        from datetime import datetime
        import parsedatetime
        from dateutil.parser import parse
        def date_formater(dt):
            try:
                dt = parse(dt)
                return f"{dt}"
            except ValueError:
                cal = parsedatetime.Calendar()
                time_struct, parse_status = cal.parse(dt)
                return f"{datetime(*time_struct[:6])}"

        name = tracker.get_slot('name')
        startdate = tracker.get_slot('startdate')
        enddate = tracker.get_slot('enddate')

        startdate = date_formater(startdate)[:10]

        enddate = date_formater(enddate)[:10]

        dispatcher.utter_message(f'Created a report {name} with start-date as {startdate} and end-date as {enddate}')
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


class PendingReport(Action):
    def name(self):
        return "pending_report"

    def run(self, dispatcher, tracker, domain):
        import requests
        response = ''
        r = requests.post('http://192.168.0.92/SutiExpense/iphoneapp.do?callto=getExps&navfrom=android&sutitest=true', data =  {"userid": "7624","compid": "552","delusr": "0","version": "8.4.0","isencrypt":"No"})
        if r.status_code == 200:
            json_data = r.json()
            if json_data['exps']:
                response += f"Total their are {len(json_data['exps'])} pending reports.The following reports are pending:"
                for exp in json_data['exps']:
                    response += f"{exp['expname']} with report id {exp['expid']}, generated on {exp['expdt']} \n"
            else:
                response("No pending reports available.")

        else:
            response = "Couldnt get the reports at this point of time."
        dispatcher.utter_message(response)
        return []