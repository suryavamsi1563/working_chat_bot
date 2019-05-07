## story 1
* init
    - action_first_message
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - action_open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay
    
## Generated Story -3585865023927045001

* greet
    - utter_greet
    - utter_do
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000177"}
    - slot{"expid": 56297}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "Very good work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - action_open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay
## Generated Story 1701616164937545232
* init
    - action_first_message
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* choose{"no_more_receipts": "camera"}
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "camera"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* choose{"no_more_receipts": "No"}
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "No"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay
<!-- ----- prasanth work------ -->
## Generated Story 8013699853458311246
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "nov 2016"}
    - slot{"compexpid": "E000194"}
    - slot{"expid": 56321}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - action_open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* choose{"no_more_receipts": "attach"}
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "attach"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay

## Generated Story -2313946811660095926
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* greet
    - utter_greet
    - utter_do

## Generated Story -8340467822388395327
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* bye
    - utter_goodbye

## Generated Story 1
* init
    - action_first_message
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000194", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56321, "expname": "nov 2016", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000193", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56319, "expname": "december 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000192", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56318, "expname": "xyz", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "nov 2016"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit{"adlt_or_sub": "submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots
## Generated Story 2942844647825540147
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000194", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56321, "expname": "nov 2016", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000193", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56319, "expname": "december 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000192", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56318, "expname": "xyz", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "december 2015"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* choose{"no_more_receipts": "camera"}
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "camera"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* choose{"no_more_receipts": "attach"}
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "attach"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay

## Generated Story 8641464499929981919
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addlineitem
    - action_addlineitem_to_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000194", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56321, "expname": "nov 2016", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000193", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56319, "expname": "december 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000192", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56318, "expname": "xyz", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "nov 2016"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* choose{"no_more_receipts": "camera"}
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "camera"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* choose{"no_more_receipts": "attach"}
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "attach"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay
## Generated Story -9083439832207100483
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* submit
    - action_submitpdr_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000194", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56321, "expname": "nov 2016", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000193", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56319, "expname": "december 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000192", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56318, "expname": "xyz", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "nov 2016"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset

## Generated Story 1810774146043363969
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "feb_mar-2019"}
    - slot{"compexpid": "E000195"}
    - slot{"expid": 56324}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - action_open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* attachreceipt
    - action_attach_receipt
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report

* deny
    - utter_okay
    - action_slot_reset
* submit
    - action_submitpdr_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000194", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56321, "expname": "nov 2016", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000193", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56319, "expname": "december 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000192", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56318, "expname": "xyz", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "nov 2016"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset
## Generated Story 449044272276413869
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000195", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56324, "expname": "feb_mar-2019", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000194", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56321, "expname": "nov 2016", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000193", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56319, "expname": "december 2015", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "nov 2016"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit{"adlt_or_sub": "submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no reasons"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - action_open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay   
* submit
    - action_submitpdr_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000194", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56321, "expname": "nov 2016", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000193", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56319, "expname": "december 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000192", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56318, "expname": "xyz", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "nov 2016"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset     
## Generated Story 4700216445743528784
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "test 1233"}
    - slot{"compexpid": "E000198"}
    - slot{"expid": 56329}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no reasons"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* submit
    - action_submitpdr_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000194", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56321, "expname": "nov 2016", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000193", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56319, "expname": "december 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000192", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56318, "expname": "xyz", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "nov 2016"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay   
    - action_slot_reset 
## Generated Story -3814962485315233730
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "hims meet"}
    - slot{"compexpid": "E000200"}
    - slot{"expid": 56331}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* choose{"no_more_receipts": "No"}
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "No"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - action_open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay
## Generated Story 2477778495865934915
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "russel-2015"}
    - slot{"compexpid": "E000203"}
    - slot{"expid": 56334}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - action_open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* enterdata
    - action_attach_receipt
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000203", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56334, "expname": "russel-2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000202", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56333, "expname": "nasa 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000201", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56332, "expname": "nasa 2018", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "nasa 2018"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem
    - utter_ask_receipt
* opencamera
    - action_open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000177"}
    - slot{"expid": 56297}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "Very good work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* addlineitem
    - action_addlineitem_to_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000194", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56321, "expname": "nov 2016", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000193", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56319, "expname": "december 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000192", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56318, "expname": "xyz", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "nov 2016"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* choose{"no_more_receipts": "camera"}
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "camera"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* choose{"no_more_receipts": "attach"}
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "attach"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay 
* submit
    - action_submitpdr_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000194", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56321, "expname": "nov 2016", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000193", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56319, "expname": "december 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000192", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56318, "expname": "xyz", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "nov 2016"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay  
    - action_slot_reset     
## Generated Story 2848295067655817418
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "good work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "trip_newyork"}
    - slot{"compexpid": "E000205"}
    - slot{"expid": 56336}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - action_open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* attachreceipt
    - action_attach_receipt
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000205", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56336, "expname": "trip_newyork", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000204", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56335, "expname": "xyz trip", "reportType": "report", "travType": "Expense"}, {"amt": "125.00", "compexpid": "E000203", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56334, "expname": "russel-2015", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "xyz trip"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit{"adlt_or_sub": "submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* reject
    - action_reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "fake details"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000205", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56336, "expname": "trip_newyork", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000204", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56335, "expname": "xyz trip", "reportType": "report", "travType": "Expense"}, {"amt": "245.00", "compexpid": "E000203", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56334, "expname": "russel-2015", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "xyz trip"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submitpdr_report
    - slot{"adlt_or_sub": "sumbit"}
    - action_submit_report
    - reset_slots
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no reasons"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
## Generated Story -1152944773577057022
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no reasons"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
## Generated Story 3
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "hims meet"}
    - slot{"compexpid": "E000200"}
    - slot{"expid": 56331}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* choose{"no_more_receipts": "No"}
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "No"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no reasons"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
## Generated Story -6135534706895138843
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no reasons"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000177"}
    - slot{"expid": 56297}
    - followup{"name": "action_listen"}
* reject
    - action_reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "please provide correct details"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "120.00", "compexpid": "E000206", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56337, "expname": "west2103", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000205", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56336, "expname": "trip_newyork", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000204", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56335, "expname": "xyz trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "trip_newyork"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submitpdr_report
    - slot{"adlt_or_sub": "sumbit"}
    - action_submit_report
    - reset_slots

## Generated Story -6
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no reasons"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000177"}
    - slot{"expid": 56297}
    - followup{"name": "action_listen"}
* reject
    - action_reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "please provide correct details"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "120.00", "compexpid": "E000206", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56337, "expname": "west2103", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000205", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56336, "expname": "trip_newyork", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000204", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56335, "expname": "xyz trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "trip_newyork"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submitpdr_report
    - slot{"adlt_or_sub": "sumbit"}
    - action_submit_report
    - reset_slots
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "hims meet"}
    - slot{"compexpid": "E000200"}
    - slot{"expid": 56331}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* choose{"no_more_receipts": "No"}
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "No"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset
## Generated Story 1136028023702880312
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* submit
    - action_submitpdr_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000212", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56343, "expname": "hyderAbad", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000211", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56342, "expname": "hyderbad_trip", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000210", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56341, "expname": "hdhdhj", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "hyderbad_trip"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit{"adlt_or_sub": "submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots
* addlineitem
    - action_addlineitem_to_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000212", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56343, "expname": "hyderAbad", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000211", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56342, "expname": "hyderbad_trip", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000210", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56341, "expname": "hdhdhj", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "hyderAbad"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit{"adlt_or_sub":"submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots

## Generated Story -7429253991622411002
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addlineitem
    - action_addlineitem_to_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000213", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56344, "expname": "fgsfgdggdggg", "reportType": "report", "travType": "Expense"}, {"amt": "225.00", "compexpid": "E000212", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56343, "expname": "hyderAbad", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000211", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56342, "expname": "hyderbad_trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"name": "fgsfgdggdggg"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit{"adlt_or_sub":"submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots

## Generated Story -2014172669696819818
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* submit
    - action_submitpdr_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000213", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56344, "expname": "fgsfgdggdggg", "reportType": "report", "travType": "Expense"}, {"amt": "225.00", "compexpid": "E000212", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56343, "expname": "hyderAbad", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000211", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56342, "expname": "hyderbad_trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit{"adlt_or_sub": "submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots

## Generated Story -7993262216048518006
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000213", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56344, "expname": "fgsfgdggdggg", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000211", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56342, "expname": "hyderbad_trip", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000210", "displayType": "Expense", "expdt": "Apr 23, 2019", "expid": 56341, "expname": "hdhdhj", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* choose{"no_more_receipts": "No"}
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "No"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay

## Generated Story -1299139777205908949
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit{"adlt_or_sub": "submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots

## Generated Story 7483536591405322101
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submitpdr_report
    - slot{"adlt_or_sub": "sumbit"}
    - action_submit_report
    - reset_slots

## Generated Story -6892342278877612769
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots

## Generated Story -6106599940083195364
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots

## Generated Story -7557906947663114339
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots

## Generated Story 5188960408398298158
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots

## Generated Story -8232179941413663026
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - followup{"name": "action_listen"}
* go_to_pendingreports
    - action_goto_pendingreports
    - reset_slots

## Generated Story -4581384462436713929
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - followup{"name": "action_listen"}
* go_to_pendingreports
    - action_goto_pendingreports
    - reset_slots

## Generated Story 4803286594066648310
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots

## Generated Story -4616818450458811404
* init
    - action_first_message
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - followup{"name": "action_listen"}
* go_to_pendingreports
    - action_goto_pendingreports
    - reset_slots

## Generated Story -3098775243866405528
* init
    - action_first_message
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000216", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56350, "expname": "gfgfdgfgfgddfgsrwetwt", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000215", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56349, "expname": "hyd_1245", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000214", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56348, "expname": "hyderabad_trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
* go_to_pendingreports
    - action_goto_pendingreports
    - reset_slots

## Generated Story 849844126166911991
* init
    - action_first_message
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000216", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56350, "expname": "gfgfdgfgfgddfgsrwetwt", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000215", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56349, "expname": "hyd_1245", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000214", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56348, "expname": "hyderabad_trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* attachreceipt
    - action_attach_receipt
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay

## Generated Story -8384750071389708136
* init
    - action_first_message
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000218", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56352, "expname": "summit 2000", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000217", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56351, "expname": "Belgium Trip", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000216", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56350, "expname": "gfgfdgfgfgddfgsrwetwt", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* greet
    - utter_greet
    - utter_do
* createreport{"name": "Begium Trip"}
    - slot{"name": "Begium Trip"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000219"}
    - slot{"expid": 56353}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* choose{"no_more_receipts": "No"}
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "No"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000219", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56353, "expname": "Begium Trip", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000218", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56352, "expname": "summit 2000", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000217", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56351, "expname": "Belgium Trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset

## Generated Story 302293593542108687
* init
    - action_first_message
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000219", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56353, "expname": "Begium Trip", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000218", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56352, "expname": "summit 2000", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000217", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56351, "expname": "Belgium Trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset
    - reset_slots
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000219", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56353, "expname": "Begium Trip", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000218", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56352, "expname": "summit 2000", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000217", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56351, "expname": "Belgium Trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem
    - utter_ask_receipt
* noreceipts
    - action_no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - reset_slots
    - utter_okay

## Generated Story 1473131247957466830
* init
    - action_first_message
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* submit
    - action_submitpdr_report
    - slot{"adlt_or_sub": "sumbit"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* submit
    - action_submitpdr_report
    - slot{"adlt_or_sub": "sumbit"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}

## Generated Story -1446976448454862857
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56297}
    - followup{"name": "action_listen"}
* reject{"appr_or_rej": "reject"}
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "bad work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 1683025201661693406
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56297}
    - followup{"name": "action_listen"}
* reject
    - action_reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "fake details"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 5048305882051480063
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56297}
    - followup{"name": "action_listen"}
* reject
    - action_reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "hjhdsajash"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -9023445722911124636
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56297}
    - followup{"name": "action_listen"}
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "good work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 7509165579018518049
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56297}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "good work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -8794375039170859815
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56297}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "hdshfashfasfh"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay



<!-- Import transactions stories -->


## Generated Story -127173379372017192
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"startdate": "jan 15th", "enddate": "jan 20th", "name": "trip to xzy"}
    - slot{"enddate": "jan 20th"}
    - slot{"name": "trip to xzy"}
    - slot{"startdate": "jan 15th"}
    - action_check_name
    - followup{"name": "import_tran_form"}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* bye
    - utter_goodbye

## Generated Story 8344576525336199802
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"cardname": "visa", "name": "kellogs summit"}
    - slot{"cardname": "visa"}
    - slot{"name": "kellogs summit"}
    - action_check_name
    - followup{"name": "import_tran_form"}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do

## Generated Story 280418395808632469
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"cardname": "amex"}
    - slot{"cardname": "amex"}
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "keras 2015"}
    - slot{"expid": 56357}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 7259234020314249073
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"startdate": "25th jan", "enddate": "13th feb", "name": "dec_2015"}
    - slot{"enddate": "13th feb"}
    - slot{"name": "dec_2015"}
    - slot{"startdate": "25th jan"}
    - action_check_name
    - followup{"name": "import_tran_form"}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do

## Generated Story 2025756804259586360
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "paris20156"}
    - slot{"expid": 56355}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - slot{"requested_slot": "line_category"}
* form: line_category
    - form: import_tran_form
    - slot{"line_category": "travel"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 4844683948083742181
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"cardname": "visa"}
    - slot{"cardname": "visa"}
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "keras_125"}
    - slot{"expid": 56356}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - slot{"requested_slot": "line_category"}
* form: line_category
    - form: import_tran_form
    - slot{"line_category": "entertainment"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay


## Generated Story 8498230392749684680
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"startmonth": "jan", "endmonth": "feb"}
    - slot{"endmonth": "feb"}
    - slot{"startmonth": "jan"}
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "keras_125"}
    - slot{"expid": 56356}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - slot{"requested_slot": "line_category"}
* form: line_category
    - form: import_tran_form
    - slot{"line_category": "travel"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay


## Generated Story 7896279625768852495
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"startmonth": "march"}
    - slot{"startmonth": "march"}
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "keras_125"}
    - slot{"expid": 56356}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - slot{"requested_slot": "line_category"}
* form: line_category
    - form: import_tran_form
    - slot{"line_category": "meals"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 2308209036213039520
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "keras_125"}
    - slot{"expid": 56356}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - slot{"requested_slot": "line_category"}
* form: line_category
    - form: import_tran_form
    - slot{"line_category": "meals"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -8066507123874709233
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"startdate": "25th jan", "endmonth": "feb", "cardname": "amex"}
    - slot{"cardname": "amex"}
    - slot{"endmonth": "feb"}
    - slot{"startdate": "25th jan"}
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "keras_125"}
    - slot{"expid": 56356}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - slot{"requested_slot": "line_category"}
* form: line_category
    - form: import_tran_form
    - slot{"line_category": "entertainment"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -1432530016390725505
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"endmonth": "dec"}
    - slot{"endmonth": "dec"}
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "paris20156"}
    - slot{"expid": 56355}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 433574392646596492
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"cardname": "amex"}
    - slot{"cardname": "amex"}
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "paris20156"}
    - slot{"expid": 56355}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 3873571994545477240
* addtransaction{"cardname": "amex"}
    - slot{"cardname": "amex"}
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "paris20156"}
    - slot{"expid": 56355}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -1187215393978970460
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "keras_125"}
    - slot{"expid": 56356}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - slot{"requested_slot": "line_category"}
* form: line_category
    - form: import_tran_form
    - slot{"line_category": "travel"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -7096556509328038462
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction{"line_category": "meals"}
    - slot{"line_category": "meals"}
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "keras_125"}
    - slot{"expid": 56356}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 835017215500358094
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* addtransaction
    - action_check_name
    - followup{"name": "action_display_tran_reports"}
    - action_display_tran_reports
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000223", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56357, "expname": "keras 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000222", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56356, "expname": "keras_125", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000221", "displayType": "Expense", "expdt": "Apr 24, 2019", "expid": 56355, "expname": "paris20156", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_for_tran
    - slot{"name": "keras_125"}
    - slot{"expid": 56356}
    - import_tran_form
    - form{"name": "import_tran_form"}
    - slot{"requested_slot": "line_category"}
* form: line_category
    - form: import_tran_form
    - slot{"line_category": "entertainment"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -4092027422496341499
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "10.00", "compexpid": "E000168", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56275, "expname": "june-2018 trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "10.00", "compexpid": "E000159", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56261, "expname": "hyderabad trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "10.00", "compexpid": "E000157", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56259, "expname": "CROOMS -Mastercard 6873 - 03.18.17-04.17.17", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56275}
    - slot{"name": "june-2018 trip"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000251", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56401, "expname": "Great report with the transactions", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000250", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56400, "expname": "trip", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000249", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56399, "expname": "trip to new york", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}

## Generated Story -3454354223103243737
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "10.00", "compexpid": "E000168", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56275, "expname": "june-2018 trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "10.00", "compexpid": "E000159", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56261, "expname": "hyderabad trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000252", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56402, "expname": "trip 2018", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000251", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56401, "expname": "Great report with the transactions", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000250", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56400, "expname": "trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "10.00", "compexpid": "E000168", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56275, "expname": "june-2018 trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "10.00", "compexpid": "E000159", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56261, "expname": "hyderabad trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56261}
    - slot{"name": "hyderabad trip"}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "correct information"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -3525331781891566609
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "10.00", "compexpid": "E000168", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56275, "expname": "june-2018 trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "417.72", "compexpid": "E000010", "crtuserid": "9364", "currency": "USD", "expdt": "Dec 4, 2018", "expid": 55611, "expname": "IMport", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000252", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56402, "expname": "trip 2018", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000251", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56401, "expname": "Great report with the transactions", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000250", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56400, "expname": "trip", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "10.00", "compexpid": "E000168", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56275, "expname": "june-2018 trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "417.72", "compexpid": "E000010", "crtuserid": "9364", "currency": "USD", "expdt": "Dec 4, 2018", "expid": 55611, "expname": "IMport", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56236}
    - slot{"name": "June 2018"}
    - followup{"name": "action_listen"}
* reject{"appr_or_rej": "reject"}
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "none"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 6747458824569356607
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "225.00", "compexpid": "E000254", "crtuserid": "9364", "currency": "USD", "expdt": "May 1, 2019", "expid": 56404, "expname": "testing123", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "10.00", "compexpid": "E000168", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56275, "expname": "june-2018 trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "nokia summit"}
    - slot{"compexpid": "E000255"}
    - slot{"expid": 56405}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* choose{"no_more_receipts": "No"}
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "No"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
    - action_slot_reset
    - reset_slots

## Generated Story -5018149357780859622
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "417.72", "compexpid": "E000010", "crtuserid": "9364", "currency": "USD", "expdt": "Dec 4, 2018", "expid": 55611, "expname": "IMport", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56447}
    - slot{"name": "demo"}
    - followup{"name": "action_listen"}
* reject
    - action_reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "looks good"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* deny
    - utter_goodbye

## Generated Story -8235333514365641704
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "417.72", "compexpid": "E000010", "crtuserid": "9364", "currency": "USD", "expdt": "Dec 4, 2018", "expid": 55611, "expname": "IMport", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56447}
    - slot{"name": "demo"}
    - followup{"name": "action_listen"}

## Generated Story -3987823865288393513
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "417.72", "compexpid": "E000010", "crtuserid": "9364", "currency": "USD", "expdt": "Dec 4, 2018", "expid": 55611, "expname": "IMport", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata{"name": "june 2018"}
    - slot{"name": "june 2018"}
    - action_select_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56236}
    - slot{"name": "June 2018"}
    - followup{"name": "action_listen"}

## Generated Story -3943902086216641594
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "417.72", "compexpid": "E000010", "crtuserid": "9364", "currency": "USD", "expdt": "Dec 4, 2018", "expid": 55611, "expname": "IMport", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* selectionreport
    - action_select_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56447}
    - slot{"name": "demo"}
    - followup{"name": "action_listen"}

## Generated Story -5868660409968155599
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "417.72", "compexpid": "E000010", "crtuserid": "9364", "currency": "USD", "expdt": "Dec 4, 2018", "expid": 55611, "expname": "IMport", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* selectionreport
    - action_select_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 55611}
    - slot{"name": "IMport"}
    - followup{"name": "action_listen"}
* reject
    - action_reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: affirm
    - form: approve_report_form
    - slot{"comments": "very bad"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

