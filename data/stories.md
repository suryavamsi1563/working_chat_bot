## story 1
* init
    - action_first_message
## appr+pending+nav camera
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "417.72", "compexpid": "E000010", "crtuserid": "9364", "currency": "USD", "expdt": "Dec 4, 2018", "expid": 55611, "expname": "IMport", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "displayType": "Expense", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "travType": "Expense"}]}
    - slot{"name": "fdf"}
    - slot{"expid": 56453}
    - slot{"compexpid": "E000299"}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem{"navto": "camera"}
    - slot{"navto": "camera"}
    - action_navigate
    - reset_slots

## appr+crt rpt +add litm +nav camera
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "417.72", "compexpid": "E000010", "crtuserid": "9364", "currency": "USD", "expdt": "Dec 4, 2018", "expid": 55611, "expname": "IMport", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* form: enterdata
    - form: create_report_form
    - slot{"crt_name": "david-jan-1"}
    - slot{"compexpid": "E000303"}
    - slot{"expid": 56458}
    - slot{"name": "david-jan-1"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* addlineitem{"navto": "camera"}
    - slot{"navto": "camera"}
    - action_navigate
    - reset_slots

## apprr+nav drafts
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "417.72", "compexpid": "E000010", "crtuserid": "9364", "currency": "USD", "expdt": "Dec 4, 2018", "expid": 55611, "expname": "IMport", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* navigation{"navto": "drafts"}
    - slot{"navto": "drafts"}
    - action_navigate
    - slot{"navto": null}

## appr+nav appr
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - followup{"name": "action_listen"}
* go_to_approvals{"navto": "approvals"}
    - slot{"navto": "approvals"}
    - action_navigate
    - slot{"navto": null}

## appr+pending+nav drft
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - followup{"name": "action_listen"}
* go_to_pendingreports{"navto": "drafts"}
    - slot{"navto": "drafts"}
    - action_navigate
    - slot{"navto": null}

## appr+crrt rpt+ add litm nav camera+ appr+approve 
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* form: enterdata
    - form: create_report_form
    - slot{"crt_name": "david-jan-1"}
    - slot{"compexpid": "E000303"}
    - slot{"expid": 56458}
    - slot{"name": "david-jan-1"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
    - utter_ask_addline
* addlineitem{"navto": "camera"}
    - slot{"navto": "camera"}
    - action_navigate
    - reset_slots
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "looks goood"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do

## appr+apprve
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "fine details"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do

## appr+crrt rpt+addlitm nav rec+pending+sel rpt+nav rec+appr+apprve
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: enterdata
    - form: create_report_form
    - slot{"crt_name": "david-jan-1"}
    - slot{"compexpid": "E000303"}
    - slot{"expid": 56458}
    - slot{"name": "david-jan-1"}
    - form: followup{"name": "utter_ask_addline"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* addlineitem{"navto": "receipt"}
    - slot{"navto": "receipt"}
    - action_navigate
    - reset_slots
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000303", "displayType": "Expense", "expdt": "May 3, 2019", "expid": 56458, "expname": "david-jan-1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000302", "displayType": "Expense", "expdt": "May 3, 2019", "expid": 56457, "expname": "dec_mar2564", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000301", "displayType": "Expense", "expdt": "May 3, 2019", "expid": 56456, "expname": "my birthday", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* selectionreport
    - action_select_report
    - slot{"expid": 56458}
    - slot{"name": "david-jan-1"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem{"navto": "receipt"}
    - slot{"navto": "receipt"}
    - action_navigate
    - reset_slots
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "looks good"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do

## init+crt rpt+deactivate
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: deactivate_report
    - form: create_report_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do


## crt rpt+deactivate
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: deactivate_report
    - form: create_report_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do

## appr+is bot+whts possible
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* ask_isbot
    - utter_ask_whoisit
* ask_whatspossible
    - utter_ask_whatspossible

## appr+is bot+whts possible
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* ask_isbot
    - utter_ask_whoisit
* ask_whatspossible
    - utter_ask_whatspossible

## FAQ STORIES
* ask_contactsupport
    - utter_contact_support
* ask_Re-asinging_credit_card 
    - utter_reassign_cc_tran
* ask_view_transactions
    - utter_view_tran
* ask_local_vs_Travel
    - utter_local_vs_travel
* ask_billable_vs_reimbursable
    - utter_reimbursable_or_billable
* ask_delete_corporate_card_tran
    - utter_delete_corporate_card_tran
* Exporting_Expense_Reports
    - utter_Exporting_Expense_Reports
* reimbersebment_to_employees 
    - utter_reimbersebment_to_employees
* automatic_email_ACH
    - utter_automatic_email_ACH
* copy_line_items
    - utter_copy_line_items
* notif_fin_users
    - utter_notif_fin_users
* notif_new_users
    - utter_notif_new_users
* email_notif
    - utter_email_noifs
## appr+ affirm to apprv +crt rpt+add litm+nav rec+ pending+nav trans

* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* affirm
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "great work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: enterdata
    - form: create_report_form
    - slot{"crt_name": "france meet 2019"}
    - slot{"compexpid": "E000304"}
    - slot{"expid": 56459}
    - slot{"name": "france meet 2019"}
    - form: followup{"name": "utter_ask_addline"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* addlineitem{"navto": "receipt"}
    - slot{"navto": "receipt"}
    - action_navigate
    - reset_slots
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000304", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56459, "expname": "france meet 2019", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000303", "displayType": "Expense", "expdt": "May 3, 2019", "expid": 56458, "expname": "david-jan-1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000302", "displayType": "Expense", "expdt": "May 3, 2019", "expid": 56457, "expname": "dec_mar2564", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56459}
    - slot{"name": "france meet 2019"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem{"navto": "transaction"}
    - slot{"navto": "transaction"}
    - action_navigate
    - reset_slots

## appr+pending+slct rpt+add litm nav trasc
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000305", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56460, "expname": "france 20156", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000304", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56459, "expname": "france meet 2019", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000303", "displayType": "Expense", "expdt": "May 3, 2019", "expid": 56458, "expname": "david-jan-1", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* selectionreport
    - action_select_report
    - slot{"expid": 56458}
    - slot{"name": "david-jan-1"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem{"navto": "transaction"}
    - slot{"navto": "transaction"}
    - action_navigate
    - reset_slots

## appr+
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* deactivate_report
    - utter_do
* ask_isbot
    - utter_ask_whoisit
* ask_whatspossible
    - utter_ask_whatspossible
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000305", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56460, "expname": "france 20156", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000304", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56459, "expname": "france meet 2019", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000303", "displayType": "Expense", "expdt": "May 3, 2019", "expid": 56458, "expname": "david-jan-1", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* deny
    - utter_do
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* reject
    - action_reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no reasons"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* navigation{"navto": "transactions"}
    - slot{"navto": "transactions"}
    - action_navigate
    - slot{"navto": null}

## Generated Story 7611420521860877996
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "great work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* createreport{"crt_name": "david - jan 2015"}
    - slot{"crt_name": "david - jan 2015"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000317"}
    - slot{"expid": 56472}
    - slot{"name": "david - jan 2015"}
    - form: followup{"name": "utter_ask_addline"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* addlineitem{"navto": "camera"}
    - slot{"navto": "camera"}
    - action_navigate
    - reset_slots
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000317", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56472, "expname": "david - jan 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000316", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56471, "expname": "dravid - dec 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000315", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56470, "expname": "edvgvg", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* selectionreport
    - action_select_report
    - slot{"expid": 56470}
    - slot{"name": "edvgvg"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem{"navto": "camera"}
    - slot{"navto": "camera"}
    - action_navigate
    - reset_slots
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no comments"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* bye
    - utter_goodbye

## appr 

* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no comments"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000317", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56472, "expname": "david - jan 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000316", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56471, "expname": "dravid - dec 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000315", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56470, "expname": "edvgvg", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* selectionreport
    - action_select_report
    - slot{"expid": 56470}
    - slot{"name": "edvgvg"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem{"navto": "receipts"}
    - slot{"navto": "receipts"}
    - action_navigate
    - reset_slots    
## Generated Story -271892755880691866
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "nice work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
## appr full
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "nice work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do    
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000317", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56472, "expname": "david - jan 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000316", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56471, "expname": "dravid - dec 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000315", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56470, "expname": "edvgvg", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* selectionreport
    - action_select_report
    - slot{"expid": 56470}
    - slot{"name": "edvgvg"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem{"navto": "camera"}
    - slot{"navto": "camera"}
    - action_navigate
    - reset_slots 
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "nice work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* createreport{"crt_name": "david - jan 20156"}
    - slot{"crt_name": "david - jan 2015"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000317"}
    - slot{"expid": 56472}
    - slot{"name": "david - jan 2015"}
    - form: followup{"name": "utter_ask_addline"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* addlineitem{"navto": "camera"}
    - slot{"navto": "camera"}
    - action_navigate
    - reset_slots 
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000317", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56472, "expname": "david - jan 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000316", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56471, "expname": "dravid - dec 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000315", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56470, "expname": "edvgvg", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* selectionreport
    - action_select_report
    - slot{"expid": 56470}
    - slot{"name": "edvgvg"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem{"navto": "receipts"}
    - slot{"navto": "receipts"}
    - action_navigate
    - reset_slots  
## Generated Story 2136666136834785677
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000317", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56472, "expname": "david - jan 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000316", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56471, "expname": "dravid - dec 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000315", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56470, "expname": "edvgvg", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56471}
    - slot{"name": "dravid - dec 2015"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* addlineitem{"navto": "camera"}
    - slot{"navto": "camera"}
    - action_navigate
    - reset_slots

## Generated Story -6541730143017437818
* createreport{"crt_name": "dhoni - mar 569"}
    - slot{"crt_name": "dhoni - mar 569"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000318"}
    - slot{"expid": 56473}
    - slot{"name": "dhoni - mar 569"}
    - form: followup{"name": "utter_ask_addline"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* addlineitem{"navto": "transactions"}
    - slot{"navto": "transactions"}
    - action_navigate
    - reset_slots

## Generated Story 1603887209364330886
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* reject
    - action_reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "not impressed"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do

## Generated Story 6965292365299225091
* createreport{"crt_name": "lasya - trip 1"}
    - slot{"crt_name": "lasya - trip 1"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000320"}
    - slot{"expid": 56475}
    - slot{"name": "lasya - trip 1"}
    - form: followup{"name": "utter_ask_addline"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* navigation{"navto": "receipts"}
    - slot{"navto": "receipts"}
    - action_navigate
    - reset_slots

## Generated Story -7665890323544739568
* addlineitem
    - action_addlineitem_to_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000322", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56477, "expname": "hyd-usa", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000321", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56476, "expname": "dev - jan 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000320", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56475, "expname": "lasya - trip 1", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56477}
    - slot{"name": "hyd-usa"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* navigation{"navto": "receipts"}
    - slot{"navto": "receipts"}
    - action_navigate
    - reset_slots
## direct addlineitm
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* addlineitem
    - action_addlineitem_to_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000322", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56477, "expname": "hyd-usa", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000321", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56476, "expname": "dev - jan 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000320", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56475, "expname": "lasya - trip 1", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56477}
    - slot{"name": "hyd-usa"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* navigation{"navto": "receipts"}
    - slot{"navto": "receipts"}
    - action_navigate
    - reset_slots
## appr+addlinitem direct
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "nice work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do    
* addlineitem
    - action_addlineitem_to_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000322", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56477, "expname": "hyd-usa", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000321", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56476, "expname": "dev - jan 2015", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000320", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56475, "expname": "lasya - trip 1", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56477}
    - slot{"name": "hyd-usa"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* navigation{"navto": "receipts"}
    - slot{"navto": "receipts"}
    - action_navigate
    - reset_slots   
## Generated Story -36184388130007689456

* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "displayType": "Expense", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "travType": "Expense"}, {"amt": "148.73", "compexpid": "E000296", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56449, "expname": "demo - 94", "reportType": "report", "travType": "Expense"}, {"amt": "10.00", "compexpid": "E000295", "displayType": "Expense", "expdt": "May 2, 2019", "expid": 56448, "expname": "trip to belgium", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56453}
    - slot{"name": "fdf"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit{"adlt_or_sub": "submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots
    - utter_do

## Generated Story -3618438813000768949
* init
    - action_first_message
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
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "looks good"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "displayType": "Expense", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "travType": "Expense"}, {"amt": "148.73", "compexpid": "E000296", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56449, "expname": "demo - 94", "reportType": "report", "travType": "Expense"}, {"amt": "10.00", "compexpid": "E000295", "displayType": "Expense", "expdt": "May 2, 2019", "expid": 56448, "expname": "trip to belgium", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56453}
    - slot{"name": "fdf"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit{"adlt_or_sub": "submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots
    - utter_do

## Generated Story 5593426817140986571
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000324", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56479, "expname": "create report", "reportType": "report", "travType": "Expense"}, {"amt": "148.73", "compexpid": "E000296", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56449, "expname": "demo - 94", "reportType": "report", "travType": "Expense"}, {"amt": "10.00", "compexpid": "E000295", "displayType": "Expense", "expdt": "May 2, 2019", "expid": 56448, "expname": "trip to belgium", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56448}
    - slot{"name": "trip to belgium"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submitpdr_report
    - followup{"name": "action_submit_report"}
    - action_submit_report
    - reset_slots
    - utter_do
## only pending report    
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000324", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56479, "expname": "create report", "reportType": "report", "travType": "Expense"}, {"amt": "148.73", "compexpid": "E000296", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56449, "expname": "demo - 94", "reportType": "report", "travType": "Expense"}, {"amt": "10.00", "compexpid": "E000295", "displayType": "Expense", "expdt": "May 2, 2019", "expid": 56448, "expname": "trip to belgium", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56448}
    - slot{"name": "trip to belgium"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submitpdr_report
    - followup{"name": "action_submit_report"}
    - action_submit_report
    - reset_slots

## only submit report
* submit
    - action_submitpdr_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000324", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56479, "expname": "create report", "reportType": "report", "travType": "Expense"}, {"amt": "148.73", "compexpid": "E000296", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56449, "expname": "demo - 94", "reportType": "report", "travType": "Expense"}, {"amt": "10.00", "compexpid": "E000295", "displayType": "Expense", "expdt": "May 2, 2019", "expid": 56448, "expname": "trip to belgium", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56479}
    - slot{"name": "create report"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* submit
    - action_submitpdr_report
    - followup{"name": "action_submit_report"}
    - action_submit_report
    - reset_slots
## appr+sub
* init
    - action_first_message
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
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "looks good"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* submit
    - action_submitpdr_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000324", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56479, "expname": "create report", "reportType": "report", "travType": "Expense"}, {"amt": "148.73", "compexpid": "E000296", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56449, "expname": "demo - 94", "reportType": "report", "travType": "Expense"}, {"amt": "10.00", "compexpid": "E000295", "displayType": "Expense", "expdt": "May 2, 2019", "expid": 56448, "expname": "trip to belgium", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56479}
    - slot{"name": "create report"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* submit
    - action_submitpdr_report
    - followup{"name": "action_submit_report"}
    - action_submit_report
    - reset_slots
    - utter_do
## Generated Story 8156501687698676135
* init
    - action_first_message
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
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "looks good"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do

## Generated Story 6907662549035477484
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000324", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56479, "expname": "create report", "reportType": "report", "travType": "Expense"}, {"amt": "148.73", "compexpid": "E000296", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56449, "expname": "demo - 94", "reportType": "report", "travType": "Expense"}, {"amt": "10.00", "compexpid": "E000295", "displayType": "Expense", "expdt": "May 2, 2019", "expid": 56448, "expname": "trip to belgium", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56448}
    - slot{"name": "trip to belgium"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000324", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56479, "expname": "create report", "reportType": "report", "travType": "Expense"}, {"amt": "148.73", "compexpid": "E000296", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56449, "expname": "demo - 94", "reportType": "report", "travType": "Expense"}, {"amt": "10.00", "compexpid": "E000295", "displayType": "Expense", "expdt": "May 2, 2019", "expid": 56448, "expname": "trip to belgium", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* showapprvls
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - slot{"name": "demo"}
    - slot{"expid": 56447}
    - followup{"name": "action_listen"}
* reject
    - action_reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "not impressed"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do  
## pend+pend      
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000324", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56479, "expname": "create report", "reportType": "report", "travType": "Expense"}, {"amt": "148.73", "compexpid": "E000296", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56449, "expname": "demo - 94", "reportType": "report", "travType": "Expense"}, {"amt": "10.00", "compexpid": "E000295", "displayType": "Expense", "expdt": "May 2, 2019", "expid": 56448, "expname": "trip to belgium", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56448}
    - slot{"name": "trip to belgium"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000324", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56479, "expname": "create report", "reportType": "report", "travType": "Expense"}, {"amt": "148.73", "compexpid": "E000296", "displayType": "Expense", "expdt": "May 1, 2019", "expid": 56449, "expname": "demo - 94", "reportType": "report", "travType": "Expense"}, {"amt": "10.00", "compexpid": "E000295", "displayType": "Expense", "expdt": "May 2, 2019", "expid": 56448, "expname": "trip to belgium", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
## Generated Story -8817791663014818223
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport{"crt_name": "feb"}
    - slot{"crt_name": "feb"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"crt_name": null}
    - form: followup{"name": "create_report_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: enterdata
    - form: create_report_form
    - slot{"crt_name": "march"}
    - slot{"compexpid": "E000330"}
    - slot{"expid": 56485}
    - slot{"name": "march"}
    - slot{"crt_name": null}
    - form: followup{"name": "utter_ask_addline"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: enterdata
    - form: create_report_form
    - slot{"crt_name": "march 13th"}
    - slot{"compexpid": "E000332"}
    - slot{"expid": 56487}
    - slot{"name": "march 13th"}
    - slot{"crt_name": null}
    - form: followup{"name": "utter_ask_addline"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* navigation{"navto": "receipts"}
    - slot{"navto": "receipts"}
    - action_navigate
    - reset_slots

## Generated Story 6430766980111527535
* submittedreport
    - action_submited_report
    - slot{"appr_report_list": [{"amt": "1783.78", "appby": "Harry Wilson", "compexpid": "E000031", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 27, 2019", "expid": 55906, "expname": "Trip  to SFO", "reportType": "report", "status": "Approved", "travType": "Expense"}, {"amt": "2788.05", "appby": "Approver Two", "compexpid": "E000031-3", "convert": "N", "dspmsg": "Rejected", "expdt": "Feb 27, 2019", "expid": 55917, "expname": "Trip  to SFO-3", "reportType": "report", "status": "Rejected", "travType": "Expense"}, {"amt": "156.00", "appby": "Harry Wilson", "compexpid": "E000029", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 25, 2019", "expid": 55904, "expname": "Trip to Mumbai", "reportType": "report", "status": "Approved", "travType": "Expense"}]}
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}


## Generated Story 2519388338953488581
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* submittedreport
    - action_submited_report
    - slot{"appr_report_list": [{"amt": "1783.78", "appby": "Harry Wilson", "compexpid": "E000031", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 27, 2019", "expid": 55906, "expname": "Trip  to SFO", "reportType": "report", "status": "Approved", "travType": "Expense"}, {"amt": "2788.05", "appby": "Approver Two", "compexpid": "E000031-3", "convert": "N", "dspmsg": "Rejected", "expdt": "Feb 27, 2019", "expid": 55917, "expname": "Trip  to SFO-3", "reportType": "report", "status": "Rejected", "travType": "Expense"}, {"amt": "156.00", "appby": "Harry Wilson", "compexpid": "E000029", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 25, 2019", "expid": 55904, "expname": "Trip to Mumbai", "reportType": "report", "status": "Approved", "travType": "Expense"}]}
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: enterdata
    - form: create_report_form
    - slot{"crt_name": "travel to china"}
    - slot{"compexpid": "E000339"}
    - slot{"expid": 56494}
    - slot{"name": "travel to china"}
    - slot{"crt_name": null}
    - form: followup{"name": "utter_ask_addline"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* addlineitem{"navto": "transaction"}
    - slot{"navto": "transaction"}
    - action_navigate
    - reset_slots
## sub+ bye
* submittedreport
    - action_submited_report
    - slot{"appr_report_list": [{"amt": "1783.78", "appby": "Harry Wilson", "compexpid": "E000031", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 27, 2019", "expid": 55906, "expname": "Trip  to SFO", "reportType": "report", "status": "Approved", "travType": "Expense"}, {"amt": "2788.05", "appby": "Approver Two", "compexpid": "E000031-3", "convert": "N", "dspmsg": "Rejected", "expdt": "Feb 27, 2019", "expid": 55917, "expname": "Trip  to SFO-3", "reportType": "report", "status": "Rejected", "travType": "Expense"}, {"amt": "156.00", "appby": "Harry Wilson", "compexpid": "E000029", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 25, 2019", "expid": 55904, "expname": "Trip to Mumbai", "reportType": "report", "status": "Approved", "travType": "Expense"}]}
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}
* bye
    - utter_goodbye    
## Generated Story -3130274903860487901
* navigation{"navto": "submitted"}
    - slot{"navto": "submitted"}
    - action_navigate
    - slot{"navto": null}

## Generated Story -5193097595894736089
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000348", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56503, "expname": "create new report with the name czsertg", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000347", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56502, "expname": "create a new report with the name fvxzsdfnm", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000346", "displayType": "Expense", "expdt": "May 6, 2019", "expid": 56501, "expname": "i changed my mind", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56503}
    - slot{"name": "create new report with the name czsertg"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* submit
    - action_submitpdr_report
    - followup{"name": "action_submit_report"}
    - action_submit_report
    - reset_slots
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: deactivate_report
    - form: create_report_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* submittedreport
    - action_submited_report
    - slot{"appr_report_list": [{"amt": "1783.78", "appby": "Harry Wilson", "compexpid": "E000031", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 27, 2019", "expid": 55906, "expname": "Trip  to SFO", "reportType": "report", "status": "Approved", "travType": "Expense"}, {"amt": "2788.05", "appby": "Approver Two", "compexpid": "E000031-3", "convert": "N", "dspmsg": "Rejected", "expdt": "Feb 27, 2019", "expid": 55917, "expname": "Trip  to SFO-3", "reportType": "report", "status": "Rejected", "travType": "Expense"}, {"amt": "156.00", "appby": "Harry Wilson", "compexpid": "E000029", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 25, 2019", "expid": 55904, "expname": "Trip to Mumbai", "reportType": "report", "status": "Approved", "travType": "Expense"}]}
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}

## Generated Story -1690422908205675008
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: deactivate_report
    - form: create_report_form
    - reset_slots
    - slot{"requested_slot": "crt_name"}
    - utter_do
## Generated Story 6898451368154344173
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: pendingreport
    - form: create_report_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - reset_slots
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000351", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56508, "expname": "vbjkgds", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000350", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56507, "expname": "tesdddd", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000349", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56506, "expname": "holi trip 2018", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}

## Generated Story 7342883999771693173
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: pendingreport
    - form: create_report_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - reset_slots
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000351", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56508, "expname": "vbjkgds", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000350", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56507, "expname": "tesdddd", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000349", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56506, "expname": "holi trip 2018", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}

## Generated Story -6871196488810122248
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: greet
    - form: create_report_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - reset_slots
    - followup{"name": "utter_greet"}
    - utter_greet
    - utter_do

## Generated Story -8036963733749944680
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* ask_isbot
    - utter_ask_whoisit
* submit
    - action_submitpdr_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000352", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56510, "expname": "holi 2", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000351", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56508, "expname": "vbjkgds", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000350", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56507, "expname": "tesdddd", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}

## Generated Story 141740951319225164
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: deactivate_report
    - form: create_report_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - reset_slots
    - followup{"name": "utter_do"}
    - utter_do
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000352", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56510, "expname": "holi 2", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000351", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56508, "expname": "vbjkgds", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000350", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56507, "expname": "tesdddd", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56510}
    - slot{"name": "holi 2"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* navigation{"navto": "transactions"}
    - slot{"navto": "transactions"}
    - action_navigate
    - reset_slots
* createreport{"crt_name": "repo 245"}
    - slot{"crt_name": "repo 245"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000353"}
    - slot{"expid": 56512}
    - slot{"name": "repo 245"}
    - slot{"crt_name": null}
    - form: followup{"name": "utter_ask_addline"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_addline
* deactivate_report
    - utter_do
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000353", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56512, "expname": "repo 245", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000352", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56510, "expname": "holi 2", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000351", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56508, "expname": "vbjkgds", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* showapprvls
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
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "looks fine"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* showapprvls
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
* approve{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: submittedreport
    - form: approve_report_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - reset_slots
    - followup{"name": "action_submited_report"}
    - action_submited_report
    - slot{"appr_report_list": [{"amt": "1783.78", "appby": "Harry Wilson", "compexpid": "E000031", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 27, 2019", "expid": 55906, "expname": "Trip  to SFO", "reportType": "report", "status": "Approved", "travType": "Expense"}, {"amt": "2788.05", "appby": "Approver Two", "compexpid": "E000031-3", "convert": "N", "dspmsg": "Rejected", "expdt": "Feb 27, 2019", "expid": 55917, "expname": "Trip  to SFO-3", "reportType": "report", "status": "Rejected", "travType": "Expense"}, {"amt": "156.00", "appby": "Harry Wilson", "compexpid": "E000029", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 25, 2019", "expid": 55904, "expname": "Trip to Mumbai", "reportType": "report", "status": "Approved", "travType": "Expense"}]}
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}
* bye
    - utter_goodbye

## Generated Story 1572186986822833651
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* deactivate_report
    - utter_do
* addlineitem
    - action_addlineitem_to_report
    - followup{"name": "action_pending_report"}
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000355", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56514, "expname": "june", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000354", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56513, "expname": "france trip 45667653", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000353", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56512, "expname": "repo 245", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"expid": 56512}
    - slot{"name": "repo 245"}
    - followup{"name": "utter_ask_addline"}
    - utter_ask_addline
* navigation{"navto": "camera"}
    - slot{"navto": "camera"}
    - action_navigate
    - reset_slots
* greet
    - utter_greet
    - utter_do

## Generated Story -6898061343903005116
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
* form: navigation{"navto": "camera"}
    - slot{"navto": "camera"}
    - form: create_report_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - followup{"name": "action_navigate"}
    - action_navigate
    - slot{"navto": null}

## Generated Story 6258393031449843133
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
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
    - slot{"expid": 56236}
    - slot{"name": "June 2018"}
    - followup{"name": "action_listen"}
* approve
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "great work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do

## Generated Story 3131831893104994301
* init
    - action_first_message
    - followup{"name": "action_display_appr_report"}
    - action_display_appr_report
    - slot{"appr_report_list": [{"amt": "4.00", "compexpid": "E000299", "crtuserid": "9364", "currency": "USD", "expdt": "May 3, 2019", "expid": 56453, "expname": "fdf", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "136.73", "compexpid": "E000294", "crtuserid": "9364", "currency": "USD", "expdt": "May 2, 2019", "expid": 56447, "expname": "demo", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "20.00", "compexpid": "E000141", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 12, 2019", "expid": 56236, "expname": "June 2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - slot{"appr_or_pend": "appr"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - followup{"name": "action_listen"}
* selectionreport
    - action_select_report
    - slot{"appr_or_pend": "appr"}
    - slot{"expid": 56453}
    - slot{"name": "fdf"}
    - followup{"name": "action_listen"}
* affirm
    - action_approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "nice work"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_do
* submittedreport
    - action_submited_report
    - slot{"appr_report_list": [{"amt": "1783.78", "appby": "Harry Wilson", "compexpid": "E000031", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 27, 2019", "expid": 55906, "expname": "Trip  to SFO", "reportType": "report", "status": "Approved", "travType": "Expense"}, {"amt": "2788.05", "appby": "Approver Two", "compexpid": "E000031-3", "convert": "N", "dspmsg": "Rejected", "expdt": "Feb 27, 2019", "expid": 55917, "expname": "Trip  to SFO-3", "reportType": "report", "status": "Rejected", "travType": "Expense"}, {"amt": "156.00", "appby": "Harry Wilson", "compexpid": "E000029", "convert": "N", "dspmsg": "Approved", "expdt": "Feb 25, 2019", "expid": 55904, "expname": "Trip to Mumbai", "reportType": "report", "status": "Approved", "travType": "Expense"}]}
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"appr_or_pend": "sub"}
    - followup{"name": "action_listen"}
* greet
    - utter_greet
    - utter_do
* ask_whatspossible
    - utter_ask_whatspossible
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "crt_name"}
* form: deactivate_report
    - form: create_report_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - reset_slots
    - followup{"name": "utter_do"}
    - utter_do
* pendingreport
    - action_pending_report
    - slot{"appr_report_list": [{"amt": "0.00", "compexpid": "E000359", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56518, "expname": "create new report with name pras", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000358", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56517, "expname": "jdjdkflg", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000357", "displayType": "Expense", "expdt": "May 7, 2019", "expid": 56516, "expname": "ghbcx", "reportType": "report", "travType": "Expense"}]}
    - slot{"appr_or_pend": "pend"}
    - followup{"name": "action_listen"}

