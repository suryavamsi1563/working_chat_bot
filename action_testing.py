from __future__ import absolute_import, division, unicode_literals

import json
from datetime import datetime
from typing import Any, Dict, List, Text, Union
import re
from datetime import datetime
import parsedatetime
from dateutil.parser import parse
import requests
from rasa_core_sdk import Action, ActionExecutionRejection, Tracker
from rasa_core_sdk.events import (AllSlotsReset, FollowupAction,SlotSet)
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import REQUESTED_SLOT, FormAction


# ---------------------FUNCTIONS USED IN ACTIONS---------------------------

def report_summary(expid,appr_or_draft,user_id,comp_id):
    r = requests.post('https://demo.sutiexpense.com/SutiExpense7.x/iphoneapp.do?callto=getsubexps', data =  {"userid": user_id,"compid": comp_id,"expid" : expid,"reqfrm" : appr_or_draft,"version": "8.4.0"})
    line_item_summary = []
    total_amount = 0
    no_of_lineitems = 0
    if r.status_code == 200:
        json_data = r.json()
        if json_data.get('status') == 'success':
            if len(json_data['subexps']) == 1 and json_data['subexps'][0]['subexpid'] == 0 :
                print("No line items for the report")
                return {
                    "Line_items_cnt":0,
                    "expid":expid
                }
            else:
                for line_item in json_data['subexps']:
                    line_item_summary.append(f"Expenditure on {line_item['subexptype']} at {line_item['merchant'] } for an amount of ${line_item['amount']}")
                    no_of_lineitems += 1
                Expenses_Subtotal = json_data['amountsTable'][0]['v']
                Grand_Total = json_data['amountsTable'][1]['v']
                Amount_Owed = json_data['amountsTable'][2]['v']
                return {
                    "Line_items_cnt":no_of_lineitems,
                    "Line_items_summary":line_item_summary,
                    "Expenses_Subtotal":Expenses_Subtotal,
                    "Grand_Total":Grand_Total,
                    "Amount_Owed":Amount_Owed
                }
        else:
            return "Status Failed"
    else:
        return "Status Code is non 200"


# Function to get card transactions which accepts the card numbers as parameter
def get_card_transactions(startdate,enddate,card):
    card_trans = []
    if startdate and enddate:
        r = requests.post('http://192.168.0.213/SutiExpense/iphonecc.do?callto=getTransactions&navfrom=iPhone',data={"ccno":f"{card}","compid": 469,"delusr": 0,"pgno" : 1,"userid":3452,"fdate":f"{startdate}","tdate":f"{enddate}"})
    elif startdate and not enddate:
        r = requests.post('http://192.168.0.213/SutiExpense/iphonecc.do?callto=getTransactions&navfrom=iPhone',data={"ccno":f"{card}","compid": 469,"delusr": 0,"pgno" : 1,"userid":3452,"fdate":f"{startdate}"})
    elif  not startdate and enddate:
        r = requests.post('http://192.168.0.213/SutiExpense/iphonecc.do?callto=getTransactions&navfrom=iPhone',data={"ccno":f"{card}","compid": 469,"delusr": 0,"pgno" : 1,"userid":3452,"tdate":f"{enddate}"})
    else:
        r = requests.post('http://192.168.0.213/SutiExpense/iphonecc.do?callto=getTransactions&navfrom=iPhone',data={"ccno":f"{card}","compid": 469,"delusr": 0,"pgno" : 1,"userid":3452})
    if r.status_code == 200:
        json_data = r.json()
        if json_data.get('status') == 'success': 
            if json_data['txs']:
                for txn in json_data['txs']:
                    card_trans.append({
                        'date':txn['date'],
                        'amount':txn['amount'],
                        'txid':txn['txid']                                            
                    })
            return card_trans

# Code to get the perfect startdate and enddate
def date_formater(dt):
    try:
        dt = parse(dt)
        if datetime.today().strftime("%m")>dt.strftime("%m"):
            return dt.strftime("%b %d, %Y")
        else:
            return dt.strftime("%b %d,"),int(dt.strftime("%Y"))-1  
    except ValueError:
        cal = parsedatetime.Calendar()
        time_struct, parse_status = cal.parse(dt)
        date=datetime(*time_struct[:6])
        if datetime.today().strftime("%m")>date.strftime("%m"):
            return date.strftime("%b %d, %Y")
        else:
            return date.strftime("%b %d,"),int(date.strftime("%Y"))-1

def adding_transactions(name,expid,startdate,enddate,startmonth,endmonth,cardnum,cardname):
    user_id = "9364"
    comp_id = "1403"
    
    # Getting all the cardnumbers of the user through API
    cards_list = []
    trans_list = []
    selected_card = ""
    selected_cards = []
    
    # getting cards that the user has
    r = requests.post('http://192.168.0.213/SutiExpense/iphonecc.do?callto=ccTabInfo&navfrom=iPhone',data={"compid": 469,"delusr": 0,"pgno" : 1,"userid":3452})
    if r.status_code == 200:
        json_data = r.json()
        if json_data.get('status') == 'success': 
            if json_data['cardnum']:
                for exp in json_data['cardnum'][:-1]:
                    cards_list.append(exp)
            else:
                cards_list = []
        else:
            return {
                    "message":"Got status failed at the card retrieval api"
                }
    else:
        return {
                "message":"Got an error at the Card retreival api."
            }

# Below code for getting perfect date for card api

    month_dict = {
        "jan":{
            "last_day":"31",
            "end_note":"st"
        },
        "feb":{
            "last_day":"28",
            "end_note":"th"
        },
        "mar":{
            "last_day":"31",
            "end_note":"st"
        },
        "apr":{
            "last_day":"30",
            "end_note":"th"
        },
        "may":{
            "last_day":"31",
            "end_note":"st"
        },
        "jun":{
            "last_day":"30",
            "end_note":"th"
        },
        "july":{
            "last_day":"31",
            "end_note":"st"
        },
        "aug":{
            "last_day":"31",
            "end_note":"st"
        },
        "sep":{
            "last_day":"30",
            "end_note":"th"
        },
        "oct":{
            "last_day":"31",
            "end_note":"st"
        },
        "nov":{
            "last_day":"30",
            "end_note":"th"
        },
        "dec":{
            "last_day":"31",
            "end_note":"st"
        }
    }


# Only startdate
    if startdate and not enddate  and not startmonth and not endmonth:
        startdate = date_formater(startdate)
# Only enddate
    elif not startdate and enddate  and not startmonth and not endmonth:
        enddate = date_formater(enddate)
# Only startdate and enddate
    elif startdate and enddate and not startmonth and endmonth:
        startdate = date_formater(startdate)
        enddate = date_formater(enddate)
#only Startmonth and enddate
    elif startmonth and endmonth and not startdate and not enddate:
        for month in month_dict:
            if month in startmonth:
                start_month_date = "1st" + " " + month
                startdate = date_formater(start_month_date)
        for month in month_dict:
            if month in endmonth:
                if month == "feb":
                    end_month_date = "1st" + " " + month
                    end = date_formater(end_month_date)
                    year=int(end[8:])
                    if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
                        enddate="feb"+" "+"29,"+year
                    else:
                        enddate="feb"+" "+"28,"+year
                else:
                    end_month_date=str(month_dict[month]['last_day'])+" "+month
                    enddate = date_formater(end_month_date)
# Only startmonth 
    elif startmonth and not endmonth and not startdate and not enddate:
        for month in month_dict:
            if month in startmonth:
                if month == "feb":
                    start_month_date = "1st" + " " + month
                    startdate = date_formater(start_month_date)
                    year=int(startdate[8:])
                    if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
                        enddate="feb"+" "+"29,"+year
                    else:
                        enddate="feb"+" "+"28,"+year
                else:
                    start_month_date = "1st" + " " + month
                    startdate=date_formater(start_month_date)
                    end_month_date=str(month_dict[month]['last_day'])+" "+month
                    enddate = date_formater(end_month_date)
# Only Endmonth
    elif endmonth and not startdate and not startmonth and not enddate:
        for month in month_dict:
            if month in endmonth:
                if month == "feb":
                    end_month_date = "1st" + " " + month
                    end = date_formater(end_month_date)
                    year=int(end[8:])
                    if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
                        enddate="feb"+" "+"29,"+year
                    else:
                        enddate="feb"+" "+"28,"+year
                else:
                    end_month_date=str(month_dict[month]['last_day'])+" "+month
                    enddate = date_formater(end_month_date)
# Only startdate and endmonth
    elif startdate and endmonth and not enddate and not startmonth:
        startdate = date_formater(startdate)
        for month in month_dict:
            if month in endmonth:
                if month == "feb":
                    end_month_date = "1st" + " " + month
                    end = date_formater(end_month_date)
                    year=int(end[8:])
                    if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
                        enddate="feb"+" "+"29,"+year
                    else:
                        enddate="feb"+" "+"28,"+year
                else:
                    end_month_date=str(month_dict[month]['last_day'])+" "+month
                    enddate = date_formater(end_month_date)
# Only startmonth and enddate
    elif startmonth and enddate and not startdate and not endmonth:
        enddate = date_formater(enddate)
        for month in month_dict:
            if month in startmonth:
                if month == "feb":
                    start_month_date = "1st" + " " + month
                    startdate = date_formater(start_month_date)
                    year=int(startdate[8:])
                    if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
                        enddate="feb"+" "+"29,"+year
                    else:
                        enddate="feb"+" "+"28,"+year
                else:
                    start_month_date = "1st" + " " + month
                    startdate=date_formater(start_month_date)
                    end_month_date=str(month_dict[month]['last_day'])+" "+month
                    enddate = date_formater(end_month_date)
    
# Perfect code ends for startdate and endate

# Getting card transactions code below

    if cards_list:
        # User has cards
        if cardname and cardnum:
            # getting all the transactions from that specific card
            for card in cards_list:
                if cardnum in card and cardname in card:
                    selected_card = card
                    break
            trans_list = get_card_transactions(startdate,enddate,selected_card)
            return {
                "trans_list":trans_list,
                "trans_count":len(trans_list),
                "message":"success",
                "cards_cnt":1,
                "selected_card":selected_card
                }
        elif cardname:
            # getting all the cards with cardname
            for card in cards_list:
                if cardname in card:
                    selected_cards.append(card)
            for card in selected_cards:
                # <--------------All Cards transcations  api----------->
                for tran in  get_card_transactions(startdate,enddate,card):
                    trans_list.append(tran)
            return {
                "trans_list":trans_list,
                "trans_count":len(trans_list),
                "message":"success",
                "cards_cnt":len(selected_cards),
                "cardname":cardname
                }
        elif cardnum:
            # getting the card with card number
            for card in cards_list:
                if cardnum in card:
                    selected_card = card
                    break
            trans_list = get_card_transactions(startdate,enddate,selected_card)
            return {
                "trans_list":trans_list,
                "trans_count":len(trans_list),
                "message":"success",
                "cards_cnt":1,
                "selected_card":selected_card
                }
        elif not cardnum and not cardname:
            # getting all the transactions for all the cards
            for card in cards_list:
                # <--------------All Cards transcations  api----------->
                for tran in  get_card_transactions(startdate,enddate,card):
                    trans_list.append(tran)
            return {
                "trans_list":trans_list,
                "trans_count":len(trans_list),
                "message":"success",
                "cards_cnt":len(cards_list),
                "cardname": "all"
                }
    else:
        return {
            "message":"Failed"
        }

def get_expid(name):
    pass

# ------------------------------------------FUNCTIONS END--------------------------


# -------------------------------------------ACTION FORMS START----------------------------
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
        userid,compid,approver = get_user_details(tracker.current_state()['sender_id'])
        
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
        if no_receipts ==  "camera":
            dispatcher.utter_message("openning Camera")
            dispatcher.utter_message("Added the receipt.")
            return [FollowupAction('utter_ask_receipt')]
        elif no_receipts == "attach":
            dispatcher.utter_message("attachment successfull.")
            dispatcher.utter_message("Added the receipt.")
            return [FollowupAction('utter_ask_receipt')]
        elif no_receipts == "import":
            dispatcher.utter_message("Redirecting to import transactions...")
            dispatcher.utter_message("Transactions added")
            return [FollowupAction('utter_ask_submit_report')]
        elif no_receipts == "No":
            expid = tracker.get_slot("expid")
            name = tracker.get_slot("name")
            compexpid = tracker.get_slot("compexpid")
            print(f"Inside No of Add Receipt Form.Slots are {expid},{name},{compexpid}")
            return [FollowupAction('utter_ask_submit_report')]

class ImportTranForm(FormAction):

    def name(self):
        return "import_tran_form"

    @staticmethod
    def required_slots(tracker:Tracker) :
        return ["name","line_category"]

    def slot_mappings(self):
        return {"name": [self.from_entity(entity="name",intent=["enterdata"]),
                             self.from_text("")],
                "line_category": [self.from_entity(entity="line_category",intent=["line_category"]),
                             self.from_text("line_category")]}

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
        userid,compid,approver = get_user_details(tracker.current_state()['sender_id'])
        name = tracker.get_slot('name')
        expid = tracker.get_slot('expid')
        startdate = tracker.get_slot('startdate')
        enddate = tracker.get_slot('enddate')
        startmonth = tracker.get_slot('startmonth')
        endmonth = tracker.get_slot('endmonth')
        cardnum = tracker.get_slot('cardnum')
        cardname = tracker.get_slot('cardname')
        # line_category = tracker.get_slot('line_category')
        print("name slot:",name)
        print("expid slot:",expid)
        print("startdate slot:",startdate)
        print("enddate slot:",enddate)
        print("startmonth slot:",startmonth)
        print("endmonth slot:",endmonth)
        print("cardnum slot:",cardnum)
        print("cardname slot:",cardname)

        cardname = cardname.upper() if cardname else cardname

        out_message = adding_transactions(name=name,
                                        expid=expid,
                                        startdate=startdate,
                                        enddate=enddate,
                                        startmonth=startmonth,
                                        endmonth=endmonth,
                                        cardname=cardname,
                                        cardnum=cardnum,
                                        userid=userid,
                                        compid=compid)

        if out_message['message'] == "success":
            count = out_message['trans_count']
            if out_message["cards_cnt"] == 1:
                selected_card = out_message["selected_card"]
                startdate = out_message["startdate"]
                enddate = out_message["enddate"]
                json_response = [
                    {
                    "selected_card":selected_card,
                    "startdate":startdate,
                    "enddate":enddate,
                    "type":"menu",
                    "status":"success",
                    "report_name":name,
                    "expid":expid
                    }
                ]
                dispatcher.utter_message(json.dumps(json_response))
                # dispatcher.utter_message(f"Added {count} transactions to the report '{name}' with line category as {line_category} from {selected_card}.")
            elif out_message["cards_cnt"] > 1:
                cardname = out_message["cardname"]
                startdate = out_message["startdate"]
                enddate = out_message["enddate"]
                json_response = [
                    {
                    "selected_card":cardname,
                    "startdate":startdate,
                    "enddate":enddate,
                    "type":"menu",
                    "status":"success",
                    "report_name":name,
                    "expid":expid
                    }
                ]
                dispatcher.utter_message(json.dumps(json_response))
                # dispatcher.utter_message(f"Added {count} transactions to the report '{name}' with line category as {line_category} from {cardname} cards.")
        else:
            dispatcher.utter_message("You dont have any cards assigned.")
        
        return [AllSlotsReset()]

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
            # ------------------ API CALL ------------
            # r = requests.post("https://demo.sutiexpense.com/SutiExpense8.x/iphoneapprove.do?callto=approve&navfrom=android&sutitest=yes",data={"userid": "9366","compid": "1403","version": "8.4.0","expid":f"{expid}","comments":f"{comments}"})
            # if r.status_code == 200:
            #     json_data = r.json()
            #     if json_data.get('status') == 'approved':
            #         response = "Approved the report"
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
            # r = requests.post("https://demo.sutiexpense.com/SutiExpense8.x/iphoneapprove.do?callto=reject&navfrom=android&sutitest=yes",data={"userid": "9366","compid": "1403","version": "8.4.0","rejresn":"1062","expid":f"{expid}","comments":f"{comments}"})
            # if r.status_code == 200:
            #     json_data = r.json()
            #     if json_data.get('status') == 'rejected':
            #         response = "Rejected the report"
            #         # dispatcher.utter_message(f'{comments}')
            #     else:
            #         response = "Failed to Reject .Please try again later."
            # else:
            #     response = "Couldnt get the reports at this point of time."

            # dispatcher.utter_message(response)
            dispatcher.utter_message(f"Rejected the report")
            # dispatcher.utter_message(f'{comments}')
      
        return [AllSlotsReset()]

# ---------------------------------------------ACTION FORMS END--------------------------------------------

# -----------------------------------------------ACTIONS START-----------------------------------------------

class PendingReport(Action):
    def name(self):
        return "action_pending_report"

    def run(self, dispatcher, tracker, domain):
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
                    print(json_data['exps'])
                    no_of_reports = len(json_data['exps'])
                    # Custom code for setting reports to 1
                    no_of_reports = 1
                    if no_of_reports == 1:
                        dispatcher.utter_message("You have one pending report as follows :")
                        compexpid = ""
                        expid=""
                        expname = ""
                        expdt = ""
#<-------------------- API call for showing the pending report full data ------------->
#<-------------------- with line items summary---------------------------------------->
                        for exp in json_data['exps']:
                            expid = exp['expid']
                            compexpid = exp['compexpid']
                            expname = exp['expname']
                            expdt = exp['expdt']
                            break
#<-------------------------- Calling report SUMMARY API ------------------------------>
                        out_summary = report_summary(expid,'drafts',user_id,comp_id)
                        print(out_summary)
                        if 'Line_items_cnt' in out_summary:
                            if out_summary.get('Line_items_cnt') == 0:
                                response = f"Report '{expname} with report id {compexpid}, created on {expdt}'.@#$@#$The report has no line items"
                                dispatcher.utter_message(response)
                                return [SlotSet('appr_report_list',json_data['exps'][:no_of_reports]),SlotSet("name",expname),SlotSet("expid",expid),SlotSet("compexpid",compexpid),SlotSet('appr_or_pend','pend'),FollowupAction("utter_ask_addline")]
                            elif out_summary.get('Line_items_cnt') > 0:
                                response += f"Report '{expname} with report id {compexpid}, created on {expdt}'.@#$@#$The report has {out_summary.get('Line_items_cnt')} line items as follows@#$@#$"
                                response += '@#$'.join(out_summary["Line_items_summary"])
                                response += f"@#$Expenses Subtotal {out_summary['Expenses_Subtotal']}"
                                response += f"@#$Grand Total : {out_summary['Grand_Total']}"
                                response += f"@#$Amount Owed : {out_summary['Amount_Owed']}"
                                dispatcher.utter_message(response)
                                return [SlotSet('appr_report_list',json_data['exps'][:no_of_reports]),SlotSet("name",expname),SlotSet("expid",expid),SlotSet("compexpid",compexpid),SlotSet('appr_or_pend','pend'),FollowupAction("utter_ask_addline_or_submit")]
                        else:
                            dispatcher.utter_message("Pending report API not working.")
#<-------------------------- Report SUMMARY API END------------------------------>
                    elif no_of_reports > 1 and no_of_reports <= 3:
                        number_word = {
                            2:"two",
                            3:"three"
                        }
                        dispatcher.utter_message(f"There are {number_word[no_of_reports]} pending reports you have. ")
                        for exp in json_data['exps'][:no_of_reports]:
                            json_response.append({
                                'compexpid' : exp['compexpid'],
                                'expdt': exp['expdt'],
                                'nav_to':{
                                    "goto":"drafts",
                                    "type":"menu",
                                    "status":"success"
                                },
                                'text':f"{exp['expname']} with report id {exp['compexpid']}, generated on {exp['expdt']}"
                            })
                        response = json.dumps(json_response)
                        dispatcher.utter_message(response)
                        # dispatcher.utter_message("Select a report to see summary :")
                        return [ SlotSet('appr_report_list',json_data['exps'][:no_of_reports]),SlotSet('appr_or_pend','pend'),FollowupAction('action_listen')]
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

#<------------IMPORT TRANSACTION ACTIONS------------------>
class CheckNameSlot(Action):
    def name(self):
        return "action_check_name"
    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot('name')
        if name:
            return [FollowupAction('import_tran_form')]
        else:
            return [FollowupAction('action_display_tran_reports')]


class DisplayTranReports(Action):
    def name(self):
        return "action_display_tran_reports"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("You have not selected a report yet")
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
                    no_of_reports = len(json_data['exps'])
                    if no_of_reports > 0:
                        no_of_reports = 3
                    # Custom code for setting reports to 1
                        for exp in json_data['exps'][:no_of_reports]:
                            json_response.append({
                                'compexpid' : exp['compexpid'],
                                'expdt': exp['expdt'],
                                'nav_to':'drafts',
                                'text':f"{exp['expname']} with report id {exp['compexpid']}, generated on {exp['expdt']}"
                            })
                        response = json.dumps(json_response)
                        dispatcher.utter_message(response)
                        dispatcher.utter_message("Select a report for adding transactions to it :")
                        return [ SlotSet('appr_report_list',json_data['exps'][:no_of_reports]),SlotSet('appr_or_pend','pend'),FollowupAction('action_listen')]
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


class SelectForTran(Action):
    def name(self):
        return "action_select_for_tran"

    def run(self, dispatcher, tracker, domain):
        sender = {
            'user_id':9364,
            'comp_id':1403,
            'approver':'yes'
        }
        user_id = 9364
        comp_id = 1403
        selection_message = tracker.latest_message['text'].lower()
        appr_report_list = tracker.get_slot("appr_report_list")
        if 'second' in selection_message or '2' in selection_message or 'two' in selection_message:
            exp = appr_report_list[1]
        elif 'third' in selection_message or '3' in selection_message or 'three' in selection_message or 'last' in selection_message:
            exp = appr_report_list[2]
        elif 'first' in selection_message or '1' in selection_message or 'one' in selection_message or 'latest' in selection_message:
            exp = appr_report_list[0]
        else:
            dispatcher.utter_message("Please Click on a report :")
            return [FollowupAction("action_display_tran_reports")]
        
        print(exp)
        return [SlotSet('name',exp['expname']),SlotSet('expid',exp['expid'],FollowupAction("import_tran_form"))]

class NavToLineitems(Action):
    def name(self):
        return "action_navigate"

    def run(self, dispatcher, tracker, domain):
        navto = tracker.get_slot("navto")
        print(navto)
        if "receipt" in navto:
            navto = "my receipts"
        elif "transaction" in navto:
            navto = "my transactions"
        elif "setting" in navto:
            navto = "settings"
        elif "submit" in navto:
            navto = "submitted"
        elif "appr" in navto:
            navto = "approvals"
        json_response = { "goto":navto,
                        "type":"menu",
                        "status":"success"
                        }
        dispatcher.utter_message(json.dumps(json_response))

        return [SlotSet("navto",None)]

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
                dispatcher.utter_message(f"Submited the report '{name}' successfully for approval")
            else:
                dispatcher.utter_message("Failed to submit the report.Status Failed")
        else:
            dispatcher.utter_message("Failed at the submit api call.'")
        # dispatcher.utter_message("Submited the report")
        return [AllSlotsReset()]

# <------------------ API CALL ENDED ---------------->
class ActionSlotReset(Action):
    def name(self):
        return "action_slot_reset"
    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]

class Display_Approval(Action):
    def name(self):
        return "action_display_appr_report"

    def run(self, dispatcher, tracker, domain):
            #<------------------ API CALL BELOW ---------------->
        json_response = []
        r = requests.post("https://demo.sutiexpense.com/SutiExpense8.x/iphoneapprove.do?callto=getExpAppRecords&navfrom=android&sutitest=yes",data={"userid": "9366","compid": "1403","version": "8.4.0"})
        
        if r.status_code == 200:
            json_data = r.json()
            if json_data.get('status') == 'success':
                if json_data['exps']:
                    no_of_reports = len(json_data['exps'])
                    no_of_reports = 3 # Custom code for setting reports to 1
        #<------------- Code for no of reports equal to 1-------------------->
                    if no_of_reports == 1:
                        dispatcher.utter_message(f"There is one report waiting for your approval.")
                        dispatcher.utter_message(f'Report summary is as follows: ')
                        compexpid = ""
                        expid=""
                        expname = ""
                        expdt = ""
#<-------------------- API call for showing the approval report full data ------------->
#<-------------------- with line items summary---------------------------------------->
                        for exp in json_data['exps']:
                            expid = exp['expid']
                            expsubby = exp['subby']
                            expamt = exp['amt']
                            compexpid = exp['compexpid']
                            expname = exp['expname']
                            expdt = exp['expdt']
                            break
#<-------------------------- Calling report SUMMARY API ------------------------------>
                        user_id = "9409"
                        comp_id = "1403"
                        out_summary = report_summary(expid,'approvals',user_id,comp_id)
                        response = ""
                        print(out_summary)
                        if 'Line_items_cnt' in out_summary:
                            if out_summary.get('Line_items_cnt') == 0:
                                response = f"Report '{expname}' created by '{expsubby}' for an amount  ${expamt} on {expdt}.Comp expid is {compexpid}"
                                dispatcher.utter_message(response)
                                dispatcher.utter_template("utter_ask_approve",tracker)
                                return [SlotSet('appr_report_list',json_data['exps'][:no_of_reports]),SlotSet('appr_or_pend','appr'),SlotSet("name",expname),SlotSet('expid',expid),FollowupAction("action_listen")]
                            elif out_summary.get('Line_items_cnt') > 0:
                                response += f"Report '{expname}' created by '{expsubby}' for an amount  ${expamt} on {expdt}.Comp expid is {compexpid}.@#$@#$The report has {out_summary.get('Line_items_cnt')} line items as follows@#$@#$"
                                response += '@#$'.join(out_summary["Line_items_summary"])
                                response += f"@#$Expenses Subtotal {out_summary['Expenses_Subtotal']}"
                                response += f"@#$Grand Total : {out_summary['Grand_Total']}"
                                response += f"@#$Amount Owed : {out_summary['Amount_Owed']}"
                                dispatcher.utter_message(response)
                                dispatcher.utter_template("utter_ask_approve",tracker)
                                return [SlotSet('appr_report_list',json_data['exps'][:no_of_reports]),SlotSet('appr_or_pend','appr'),SlotSet("name",expname),SlotSet('expid',expid),FollowupAction("action_listen")]
                        else:
                            dispatcher.utter_message("Report Summary API not working.")
#<-------------------------- Report SUMMARY API END------------------------------->
        #<------------- Code for no of reports equal to 1 END---------------------->

        #<------------- Code for no of reports between 2 and 3 -------------------->
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
                        # dispatcher.utter_message("Select a report for summary:")
                        return [ SlotSet('appr_report_list',json_data['exps'][:no_of_reports]),SlotSet('appr_or_pend','appr'),FollowupAction('action_listen')]
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
    
class ApproveOrRejectAction(Action):
    def name(self):
        return "action_approve_or_reject"

    def run(self, dispatcher, tracker, domain):
        sender = {
            'user_id':9364,
            'comp_id':1403
            # 'approver':"yes"
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
            return[FollowupAction('action_display_appr_report')]
        else:
            SlotSet("approver_or_not", False)
            return[FollowupAction("action_pending_report")]


class go_to_approvals(Action):
    def name(self):
        return "action_goto_approvals"
    
    def run(self,dispatcher,tracker,domain):
        sender = {
            'user_id':9364,
            'comp_id':1403,
            'approver':'yes'
  
        } 
        if 'approver' in sender:
            return [SlotSet("navto","approvals"),FollowupAction("action_navigate")]
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
        sender = {
            'user_id':9364,
            'comp_id':1403,
            'approver':'yes'
  
        }
        user_id = 9364
        comp_id = 1403
        selection_message = tracker.latest_message['text'].lower()
        appr_report_list = tracker.get_slot("appr_report_list")
        appr_or_pend = tracker.get_slot("appr_or_pend")
        if not appr_report_list and appr_or_pend == "appr":
            dispatcher.utter_message("No reports to select for approving")
            return [FollowupAction("utter_okay")]
        if not appr_report_list and appr_or_pend == "pend":
            dispatcher.utter_message("No reports to select from drafts")
            return [FollowupAction("utter_okay")]

        if 'second' in selection_message or '2' in selection_message or 'two' in selection_message:
            exp = appr_report_list[1]
        elif 'third' in selection_message or '3' in selection_message or 'three' in selection_message or 'last' in selection_message:
            exp = appr_report_list[2]
        elif 'first' in selection_message or '1' in selection_message or 'one' in selection_message or 'latest' in selection_message:
            exp = appr_report_list[0]
        else:
            dispatcher.utter_message("Please Click on a report: ")
            return [FollowupAction("action_listen")]
        print(exp)
        expid = exp['expid']
        compexpid = exp['compexpid']
        expname = exp['expname']
        expdt = exp['expdt']
        response = ""
#<-------------------------- Calling report SUMMARY API for approval report ------------------------------>        
        if appr_or_pend == 'appr':
            expsubby = exp['subby']
            expamt = exp['amt']
            user_id = "9409"
            comp_id = "1403"
            out_summary = report_summary(expid,'approvals',user_id,comp_id)
            response = ""
            print(out_summary)
            if 'Line_items_cnt' in out_summary:
                if out_summary.get('Line_items_cnt') == 0:
                    response = f"Report '{expname}' created by '{expsubby}' for an amount  ${expamt} on {expdt}.Comp expid is {compexpid}"
                    dispatcher.utter_message(response)
                    dispatcher.utter_template("utter_ask_approve",tracker)
                    return [SlotSet('appr_or_pend','appr'),SlotSet('expid',expid),SlotSet('name',expname),FollowupAction("action_listen")]
                elif out_summary.get('Line_items_cnt') > 0:
                    response += f"Report '{expname}' created by '{expsubby}' for an amount  ${expamt} on {expdt}.Comp expid is {compexpid}.@#$@#$The report has {out_summary.get('Line_items_cnt')} line items as follows@#$@#$"
                    response += '@#$@#$'.join(out_summary["Line_items_summary"])
                    response += f"@#$Expenses Subtotal {out_summary['Expenses_Subtotal']}"
                    response += f"@#$Grand Total : {out_summary['Grand_Total']}"
                    response += f"@#$Amount Owed : {out_summary['Amount_Owed']}"
                    dispatcher.utter_message(response)
                    dispatcher.utter_template("utter_ask_approve",tracker)
                    return [SlotSet('appr_or_pend','appr'),SlotSet('expid',expid),SlotSet('name',expname),FollowupAction("action_listen")]
            else:
                dispatcher.utter_message("Report Summary API not working.")
        else:
#<-------------------------- Calling report SUMMARY API for pending report ------------------------------>
            out_summary = report_summary(expid,'drafts',user_id,comp_id)
            
            print(out_summary)
            if 'Line_items_cnt' in out_summary:
                if out_summary.get('Line_items_cnt') == 0:
                    response = f"Report '{expname} with report id {compexpid}, created on {expdt}'.@#$@#$The report has no line items"
                    dispatcher.utter_message(response)
                    return [SlotSet('expid',expid),SlotSet('name',expname),FollowupAction("utter_ask_addline")]
                elif out_summary.get('Line_items_cnt') > 0:
                    response += f"Report '{expname} with report id {compexpid}, created on {expdt}'.@#$@#$The report has {out_summary.get('Line_items_cnt')} line items as follows@#$@#$"
                    response += '@#$'.join(out_summary["Line_items_summary"])
                    dispatcher.utter_message(response)
                    return [SlotSet('expid',expid),SlotSet('name',expname),FollowupAction("utter_ask_addline_or_submit")]
            else:
                dispatcher.utter_message("Pending report API not working.")

class approve_report(Action):
    def name(self):
        return "action_approve_report"
    def run(self,dispatcher,tracker,domain):
        appr_report_list = tracker.get_slot("appr_report_list")
        appr_or_pend = tracker.get_slot("appr_or_pend")
        name = tracker.get_slot("name")
        if appr_report_list and appr_or_pend == 'appr' and name:
            return[SlotSet("appr_or_rej","approve")]
        else:
            # if not appr_report_list or not name:
            dispatcher.utter_message("No report Selected to approve")
            return [FollowupAction('action_display_appr_report')]

class reject_report(Action):
    def name(self):
        return "action_reject_report"
    def run(self,dispatcher,tracker,domain):
        appr_report_list = tracker.get_slot("appr_report_list")
        appr_or_pend = tracker.get_slot("appr_or_pend")
        name = tracker.get_slot("name")
        if appr_report_list and appr_or_pend == 'appr' and name:
            return[SlotSet("appr_or_rej","reject")]
        else:
            # if not appr_report_list:
            dispatcher.utter_message("No report Selected to reject")
            return [FollowupAction('action_display_appr_report')]

class addlineitem_to_report(Action):
    def name(self):
        return "action_addlineitem_to_report"
    def run(self,dispatcher,tracker,domain):
        appr_report_list = tracker.get_slot("appr_report_list")
        appr_or_pend = tracker.get_slot("appr_or_pend")
        if appr_report_list and appr_or_pend == 'pend' :
            return[SlotSet("adlt_or_sub","addlineitem")]
        else :
            return [FollowupAction('action_pending_report')]

class submit_report(Action):
    def name(self):
        return "action_submitpdr_report"
    def run(self,dispatcher,tracker,domain):
        appr_report_list = tracker.get_slot("appr_report_list")
        appr_or_pend = tracker.get_slot("appr_or_pend")
        if appr_report_list and appr_or_pend == 'pend' :
            return[SlotSet("adlt_or_sub","sumbit")]
        else :
            return [FollowupAction('action_pending_report')]

class open_camera(Action):
    def name(self):
        return "action_open_camera"
    def run(self,dispatcher,tracker,domain):

        name = tracker.get_slot("name")
        expid = tracker.get_slot("expid")
        compexpid = tracker.get_slot("compexpid")

        if name and expid and compexpid:
            return [SlotSet("no_more_receipts","camera")] 
        else:
            json_response = [
            {
                "goto":"camera",
                "type":"menu",
                "status":"success"
                }
            ]
            dispatcher.utter_message(json.dumps(json_response))
            return [FollowupAction("action_listen")]

class attach_receipt(Action):
    def name(self):
        return "action_attach_receipt"
    def run(self,dispatcher,tracker,domain):
        return [SlotSet("no_more_receipts","attach")]   

class no_receipt(Action):
    def name(self):
        return "action_no_receipt"
    def run(self,dispatcher,tracker,domain):
        return [SlotSet("no_more_receipts","No")]      
