## greet story
* greet
    - utter_greet

## pending report with greet and bye
* greet
    - utter_greet
* pendingreport
    - pending_report
* bye
    - utter_goodbye

## pending report with only greet
* greet
    - utter_greet
* pendingreport
    - pending_report


## Generated Story 2686991663111706778
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "West - April 2015 2nd Report-1"}
    - form{"name": null}
    - slot{"requested_slot": null}
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
    - action_slot_reset
    - utter_okay
    

## Generated Story 2564268866482652283
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Jennison - April 2015"}
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

## Generated Story 55085010115142509
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Cthearle - May 2015 Expenses-1"}
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

## Generated Story 1002004506990139782
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Lewis - May 2015"}
    - form{"name": null}
    - slot{"requested_slot": null}
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
    - action_slot_reset
    - utter_okay

## Generated Story -1288192080090115682
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Routine Expenses Tyler Smith through Jan 30 2019"}
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
    - action_slot_reset
    - utter_okay

## Generated Story 7807415952395738139
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Blakey - May 2015-1"}
    - form{"name": null}
    - slot{"requested_slot": null}
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
    - action_slot_reset
    - utter_okay
* bye
    - utter_goodbye

## Generated Story -5235559010194957009
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "JC 1-8-19"}
    - slot{"compexpid": "E102221"}
    - form{"name": null}
    - slot{"requested_slot": null}
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
    - action_slot_reset
    - reset_slots
    - utter_okay
* bye
    - utter_goodbye

## Generated Story -5696692326278751666
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "week of 2/5/18"}
    - slot{"compexpid": "E102221"}
    - form{"name": null}
    - slot{"requested_slot": null}
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
* choose{"no_more_receipts": "attach"}
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - slot{"no_more_receipts": "attach"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
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
    - action_slot_reset
    - reset_slots
    - utter_okay
* bye
    - utter_goodbye

## Generated Story -252555865541267198
* createreport{"name": "Dec 17 Cell"}
    - slot{"name": "Dec 17 Cell"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E102221"}
    - form{"name": null}
    - slot{"requested_slot": null}
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
* bye
    - utter_goodbye

## Generated Story -395339882576267122
* greet
    - utter_greet
* createreport{"name": "hyderabad_trip"}
    - slot{"name": "hyderabad_trip"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000114"}
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
* bye
    - utter_goodbye

## Generated Story 8773553794715781915
* greet
    - utter_greet
* createreport{"name": "dec 17 cell"}
    - slot{"name": "dec 17 cell"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000115"}
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
    - action_slot_reset
    - reset_slots
    - utter_okay
* bye
    - utter_goodbye

## Generated Story 787668454841770196
* createreport{"name": "Rasky - October 2014"}
    - slot{"name": "Rasky - October 2014"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000116"}
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
    - action_slot_reset
    - reset_slots
    - utter_okay
* bye
    - utter_goodbye

## Generated Story 4804152964659728738
* greet
    - utter_greet
* createreport{"name": "Grzandziel - November 2014"}
    - slot{"name": "Grzandziel - November 2014"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000117"}
    - form{"name": null}
    - slot{"requested_slot": null}
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
    - action_slot_reset
    - reset_slots
    - utter_okay
* bye
    - utter_goodbye

## Generated Story -8083090070214785419
* createreport{"name": "hanschen - october 2014"}
    - slot{"name": "hanschen - october 2014"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000130"}
    - slot{"expid": 56215}
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
    - action_slot_reset
    - reset_slots
    - utter_okay
* bye
    - utter_goodbye

## Generated Story 159757378610241439
* greet
    - utter_greet
* createreport{"name": "wolfe - november 2014 - 1"}
    - slot{"name": "wolfe - november 2014 - 1"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000131"}
    - slot{"expid": 56216}
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
    - action_slot_reset
    - reset_slots
    - utter_okay
* bye
    - utter_goodbye

