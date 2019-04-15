## greet story
* greet
    - action_greet

## pending report with greet and bye
* greet
    - action_greet
* pendingreport
    - pending_report
* bye
    - utter_goodbye

## pending report with only greet
* greet
    - action_greet
* pendingreport
    - pending_report


## Generated Story 2686991663111706778
* greet
    - action_greet
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
    - action_greet
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
    - action_greet
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
    - action_greet
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
    - action_greet
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
    - action_greet
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
    - action_greet
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
    - action_greet
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
    - action_greet
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
    - action_greet
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

<!-- Approval Stories start -->
## Generated Story 4068002384361156032
* greet
    - action_greet
    - action_approve_report
    - slot{"name_list": ["john", "will"]}
    - slot{"expid_list": ["E000125", "ER0214256"]}
    - approve_report_form
    - form{"report_name": "approve_report_form"}
    - slot{"requested_slot": "expid_or_name"}
* form: approvals
    - form: approve_report_form
    - slot{"expid_or_name": "ER0214256"}
    - form{"report_name": null}
    - slot{"requested_slot": null}
* bye
    - utter_goodbye

## Generated Story -7379889380351166288
* greet
    - action_greet
    - action_approve_report
    - slot{"name_list": ["john", "will"]}
    - slot{"expid_list": ["E000125", "ER0214256"]}
    - approve_report_form
    - form{"report_name": "approve_report_form"}
    - slot{"requested_slot": "expid_or_name"}
* form: approvals
    - form: approve_report_form
    - slot{"expid_or_name": "E000125"}
    - form{"report_name": null}
    - slot{"requested_slot": null}
* bye
    - utter_goodbye

## Generated Story -435509751590996170
* greet
    - action_greet
    - action_approve_report
    - slot{"name_list": ["June 2018", "Opera_2013"]}
    - slot{"expid_list": ["E000125", "ER0214256"]}
    - approve_report_form
    - form{"report_name": "approve_report_form"}
    - slot{"requested_slot": "expid_or_name"}
* form: approvals
    - form: approve_report_form
    - slot{"expid_or_name": "June 2018"}
    - form{"report_name": null}
    - slot{"requested_slot": null}
* bye
    - utter_goodbye

## Generated Story 4312342529377818882
* greet
    - action_greet
    - action_approve_report
    - slot{"name_list": ["June 2018", "Opera_2013"]}
    - slot{"expid_list": ["E000125", "ER0214256"]}
    - approve_report_form
    - form{"report_name": "approve_report_form"}
    - slot{"requested_slot": "expid_or_name"}
* form: approvals
    - form: approve_report_form
    - slot{"expid_or_name": "may 2019"}
    - slot{"expid_or_name": null}
    - form: followup{"report_name": "approve_report_form"}
    - form{"report_name": null}
    - slot{"requested_slot": null}
    - approve_report_form
    - form{"report_name": "approve_report_form"}
    - slot{"requested_slot": "expid_or_name"}
* form: approvals
    - form: approve_report_form
    - slot{"expid_or_name": "Opera_2013"}
    - form{"report_name": null}
    - slot{"requested_slot": null}
    - utter_ask_approve
* affirm{"appr_or_rej": "Approve"}
    - slot{"appr_or_rej": "Approve"}
    - action_approve_or_reject
    - utter_okay
* bye
    - utter_goodbye

## Generated Story -6996739691440456252
* greet
    - action_greet
    - followup{"report_name": "action_approve_report"}
    - action_approve_report
    - slot{"name_list": ["June 2018", "Opera_2013"]}
    - slot{"expid_list": ["E000125", "ER0214256"]}
    - slot{"report_data": {"John": ["E000125", "June 2018"], "Will": ["ER0214256", "Opera_2013"]}}
    - approve_report_form
    - form{"report_name": "approve_report_form"}
    - slot{"requested_slot": "expid_or_name"}
* form: approvals
    - form: approve_report_form
    - slot{"expid_or_name": "Opera_2013"}
    - form: followup{"report_name": "utter_ask_approve"}
    - form{"report_name": null}
    - slot{"requested_slot": null}
    - utter_ask_approve
* affirm{"appr_or_rej": "Approve"}
    - slot{"appr_or_rej": "Approve"}
    - action_approve_or_reject
    - utter_okay
* bye
    - utter_goodbye

## Generated Story 9177491305532895313
* greet
    - action_greet
    - followup{"report_name": "action_approve_report"}
    - action_approve_report
    - slot{"name_list": ["June 2018", "Opera_2013"]}
    - slot{"expid_list": ["E000125", "ER0214256"]}
    - slot{"report_data": {"John": ["E000125", "June 2018"], "Will": ["ER0214256", "Opera_2013"]}}
    - approve_report_form
    - form{"report_name": "approve_report_form"}
    - slot{"requested_slot": "expid_or_name"}
* form: approvals
    - form: approve_report_form
    - slot{"expid_or_name": "June 2018"}
    - form: followup{"report_name": "utter_ask_approve"}
    - form{"report_name": null}
    - slot{"requested_slot": null}
    - utter_ask_approve
* deny{"appr_or_rej": "Reject"}
    - slot{"appr_or_rej": "Reject"}
    - action_approve_or_reject
    - utter_okay
* bye
    - utter_goodbye

<!-- Approval Stories End -->

## Generated Story 2161502644231060296
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"name_list": ["June 2018", "Opera_2013"]}
    - slot{"expid_list": ["E000125", "ER0214256"]}
    - slot{"report_data": {"John": ["E000125", "June 2018"], "Will": ["ER0214256", "Opera_2013"]}}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "expid_or_name"}
* form: approvals
    - form: approve_report_form
    - slot{"expid_or_name": "E000125"}
    - form: followup{"name": "utter_ask_approve"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_approve
* affirm{"appr_or_rej": "Approve"}
    - slot{"appr_or_rej": "Approve"}
    - action_approve_or_reject
    - utter_okay
* bye
    - utter_goodbye

