## Generated Story 554961401350704084
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* deactivate_report
    - utter_do
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: submittedreport
    - form: create_report_form
    - reset_slots
    - followup{"name": "action_submited_report"}
    - slot{"requested_slot": "crt_name"}
    - action_submited_report
    - slot{"appr_report_list": [{"amt": "1783.78", "appby": "Harry Wilson", "compexpid": "E000031", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 27, 2019", "expid": 55906, "expname": "Trip  to SFO", "reportType": "report", "status": "Approved", "travType": "Expense"}, {"amt": "2788.05", "appby": "Approver Two", "compexpid": "E000031-3", "convert": "N", "dspmsg": "Rejected", "expdt": "Feb 27, 2019", "expid": 55917, "expname": "Trip  to SFO-3", "reportType": "report", "status": "Rejected", "travType": "Expense"}, {"amt": "156.00", "appby": "Harry Wilson", "compexpid": "E000029", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 25, 2019", "expid": 55904, "expname": "Trip to Mumbai", "reportType": "report", "status": "Approved", "travType": "Expense"}]}
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56447}
    - slot{"name": "demo"}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - action_listen
    - slot{"requested_slot": "comments"}
* form: enterdata
    - approve_report_form
    - slot{"comments": "looks good"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000351", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56508, "expname": "vbjkgds", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000350", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56507, "expname": "tesdddd", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000349", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56506, "expname": "holi trip 2018", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56507}
    - slot{"name": "tesdddd"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* navigation{"navto": "camera"}
    - slot{"navto": "camera"}
    - action_navigate
    - reset_slots