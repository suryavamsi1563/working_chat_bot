import requests
import json
from datetime import datetime
import parsedatetime
from dateutil.parser import parse


def card_names():
    response = ''
    user_id = "9364"
    comp_id = "1403"
# <-------------- API CALL BELOW ---------------->
    json_response = []
    r = requests.post('http://192.168.0.213/SutiExpense/iphonecc.do?callto=ccTabInfo&navfrom=iPhone',data={"compid": 469,"delusr": 0,"pgno" : 1,"userid":3452})
    if r.status_code == 200:
        json_data = r.json()
        if json_data.get('status') == 'success': 
            if json_data['cardnum']:
                print(json_data['cardnum'])
                for exp in json_data['cardnum'][:-1]:
                    json_response.append(exp)
                return json_response    
            else:
                return None       
        else:
            return None   
    else:
        return None

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



def adding_transactions(**kwargs):
    print(kwargs)
    cardname=kwargs['çardname']
    cardnum=kwargs['çardname']
    startdate=date_formater(kwargs['startdate'])
    enddate=date_formater(kwargs['enddate'])
    card=[]
    CARD=[]
    cards=card_names()
    
                     

    if cards!="None":
        # if cardnum!="None":
        #     for ccno in card:
        #         if cardnum in ccno:
        #             card.append(ccno)
        if cardname=="None" and cardnum=="None":
            for ccno in cards:
                json_response = []
                # <--------------add all transcation api----------->
                # r = requests.post('http://192.168.0.213/SutiExpense/iphonecc.do?callto=getTransactions&navfrom=iPhone',data={"ccno":f"{ccno}","compid": 469,"delusr": 0,"pgno" : 1,"userid":3452,"fdate":f"{startdate}","tdate":f"{enddate}"})
                # if r.status_code == 200:
                #     json_data = r.json()
                #     if json_data.get('status') == 'success': 
                #         if json_data['txs']:
                #             print(json_data['txs'])
                #             print(len(json_data['txs']))
                #             for txns in json_data['txs']:
                #                 json_response.append({
                #                             'date':txns['date'],
                #                             'amount':txns['amount'],
                #                             'txid':txns['txid']                                            
                #                         })
                #                 count+=1
                #<---------------add transactions api------------->
                #             response = json.dumps(json_response)

        elif cardname != "None" or cardnum!="None":
            for ccno in cards:
                if cardname in ccno:
                    card.append(ccno)
                    if cardnum =="None":
                        for ccno in cards:
                            if  cardnum in ccno:
                                CARD.append(ccno)

                   
# for  ccno in card:
#     json_response = []
#     r = requests.post('http://192.168.0.213/SutiExpense/iphonecc.do?callto=getTransactions&navfrom=iPhone',data={"ccno":f"{ccno}","compid": 469,"delusr": 0,"pgno" : 1,"userid":3452,"fdate":f"{startdate}","tdate":f"{enddate}"})
#     if r.status_code == 200:
#         json_data = r.json()
#         if json_data.get('status') == 'success': 
#             if json_data['txs']:
#                 print(json_data['txs'])
#                 for txns in json_data['txs']:
#                     json_response.append({
#                                 'date':txns['date'],
#                                 'amount':txns['amount'],
#                                 'txid':txns['txid']                                            
#                             })
#                     count+=1        
#                 response = json.dumps(json_response)

            
    