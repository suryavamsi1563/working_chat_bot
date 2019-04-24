## greet story
* greet
    - action_greet


* init
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

## Generated Story 6615228156551201391
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots

## Generated Story 3687589573089308105
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots



## Generated Story -1125353825545435735
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "Approve"}
    - slot{"appr_or_rej": "Approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "Approved the report because its valid."}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 4152731965264351058
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - followup{"name": "action_listen"}
* deny{"appr_or_rej": "Reject"}
    - slot{"appr_or_rej": "Reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "Rejected because of high risk value."}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -6448817463876892830
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "133.00", "compexpid": "E000145", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56244, "expname": "W/E 9/8/2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000145"}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "Approve"}
    - slot{"appr_or_rej": "Approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "Accepted becoz evrything looks good"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -7182168689551324045
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "133.00", "compexpid": "E000145", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56244, "expname": "W/E 9/8/2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000146"}
    - followup{"name": "action_listen"}
* deny{"appr_or_rej": "Reject"}
    - slot{"appr_or_rej": "Reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "3"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 8803504140135374925
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "133.00", "compexpid": "E000145", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56244, "expname": "W/E 9/8/2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000146"}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "good"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay


## Generated Story 809068275684738002
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "133.00", "compexpid": "E000145", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56244, "expname": "W/E 9/8/2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000145"}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "amount limit is over"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -205416194542648069
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "WE012564"}
    - slot{"compexpid": "E000155"}
    - slot{"expid": 56256}
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

## Generated Story -766260666706737690
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "50.00", "compexpid": "E000155", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 16, 2019", "expid": 56256, "expname": "WE012564", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "133.00", "compexpid": "E000145", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56244, "expname": "W/E 9/8/2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000145"}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "good"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -8668719674421155233
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "50.00", "compexpid": "E000155", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 16, 2019", "expid": 56256, "expname": "WE012564", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "133.00", "compexpid": "E000145", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56244, "expname": "W/E 9/8/2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000145"}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "good"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay


## Generated Story -7206613712242564752
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "50.00", "compexpid": "E000155", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 16, 2019", "expid": 56256, "expname": "WE012564", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "133.00", "compexpid": "E000145", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56244, "expname": "W/E 9/8/2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000145"}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "fine information"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* showapprvls
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "50.00", "compexpid": "E000155", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 16, 2019", "expid": 56256, "expname": "WE012564", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "133.00", "compexpid": "E000145", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56244, "expname": "W/E 9/8/2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000155"}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "everything fine"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -4263595736310604095
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "50.00", "compexpid": "E000155", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 16, 2019", "expid": 56256, "expname": "WE012564", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000155"}
    - slot{"expid": 56256}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "everything  fine"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
<!-- 17-04-2019 -->
## Generated Story 2648734465814660424
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "50.00", "compexpid": "E000155", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 16, 2019", "expid": 56256, "expname": "WE012564", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "133.00", "compexpid": "E000145", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56244, "expname": "W/E 9/8/2018", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000155"}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "everything correct"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -7188431337656056202
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots

## Generated Story 680958707035228041
* showapprvls
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
* go_to_approvals
    - action_goto_approvals
    - reset_slots


## Generated Story 4397846605150214123
* approvals
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"compexpid": "E000156"}
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots

## Generated Story 2479153569843494257
* pendingreport
    - pending_report
    - reset_slots
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "CROOMS -Mastercard 6873 - 03.18.17-04.17.17"}
    - slot{"compexpid": "E000157"}
    - slot{"expid": 56259}
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
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "gas card 9192 2/17 3/17"}
    - slot{"compexpid": "E000158"}
    - slot{"expid": 56260}
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
* showapprvls
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"compexpid": "E000156"}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "everything correct"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* pendingreport
    - pending_report
    - reset_slots

## Generated Story -1629772166863241311
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "50.00", "compexpid": "E000155", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 16, 2019", "expid": 56256, "expname": "WE012564", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000155"}
    - followup{"name": "action_listen"}
* deny{"appr_or_rej": "reject"}
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
    - utter_okay
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "hyderabad trip"}
    - slot{"compexpid": "E000159"}
    - slot{"expid": 56261}
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
* pendingreport
    - pending_report
    - reset_slots
* bye
    - utter_goodbye

## Generated Story -8658122136386921209
* createreport{"name": "burns - july 2016"}
    - slot{"name": "burns - july 2016"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000160"}
    - slot{"expid": 56262}
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
* pendingreport
    - pending_report
    - reset_slots
* showapprvls
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots
* bye
    - utter_goodbye

<!-- 18-04-2019 -->
## Generated Story 5431602277006287334
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000156"}
    - slot{"expid": 56258}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
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
## Generated Story -4260399207202248399
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000146"}
    - slot{"expid": 56245}
    - followup{"name": "action_listen"}
* affirm
    - approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "every thing is fine"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -6632535511995018724
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000146"}
    - slot{"expid": 56245}
    - followup{"name": "action_listen"}
* affirm
    - approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "everything is fine"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* showapprvls
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000156"}
    - slot{"expid": 56258}
    - followup{"name": "action_listen"}
* deny
    - reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "provide correct details"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 6208839985680870204
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000146"}
    - slot{"expid": 56245}
    - followup{"name": "action_listen"}
* approve
    - approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "everything good"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 659670364639364001
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000156"}
    - slot{"expid": 56258}
    - followup{"name": "action_listen"}
* reject
    - reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "provide correct details"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 7607885115049200859
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000146"}
    - slot{"expid": 56245}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "everything is fine"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* showapprvls
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "565.10", "compexpid": "E000146", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 13, 2019", "expid": 56245, "expname": "Iradimed expense report", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000156"}
    - slot{"expid": 56258}
    - followup{"name": "action_listen"}
* approve
    - approve_report
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
    - utter_okay

## Generated Story 6458194422603042363
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - followup{"name": "action_listen"}
* go_to_approvals
    - action_goto_approvals
    - reset_slots

## Generated Story -3493341593475363702
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "July 2017 Expense Log"}
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* attachreceipt
    - attach_receipt
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - action_slot_reset
    - reset_slots
    - utter_okay

## Generated Story -1404457202416559123
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "june-2018 trip"}
    - slot{"compexpid": "E000168"}
    - slot{"expid": 56275}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - action_slot_reset
    - reset_slots
    - utter_okay

## Generated Story -4406311657714027904
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Stoehr January 2015"}
    - slot{"compexpid": "E000169"}
    - slot{"expid": 56276}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - action_slot_reset
    - reset_slots
    - utter_okay

## Generated Story 1
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Stoehr January 2015"}
    - slot{"compexpid": "E000169"}
    - slot{"expid": 56276}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* attachreceipt
    - attach_receipt
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt  
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt      
* noreceipts
    - no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - action_slot_reset
    - reset_slots
    - utter_okay
## Generated Story-2
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "june-2018 trip"}
    - slot{"compexpid": "E000168"}
    - slot{"expid": 56275}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* attachreceipt
    - attach_receipt
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt     
* noreceipts
    - no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - action_slot_reset
    - reset_slots
    - utter_okay
## Generated Story -52773353946907766
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "april_trip"}
    - slot{"compexpid": "E000170"}
    - slot{"expid": 56277}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - open_camera
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
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - action_slot_reset
    - reset_slots
    - utter_okay

## Generated Story -5884791831356322933
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - followup{"name": "action_listen"}
* approve
    - approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "everything good"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* showapprvls
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - followup{"name": "action_listen"}
* affirm
    - approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "ya its fine"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -4598849865021807902
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - followup{"name": "action_listen"}
* affirm
    - approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "fine information"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -3352444474310269608
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - followup{"name": "action_listen"}
* reject
    - reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "i think its fake data"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 8483380246048262850
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - followup{"name": "action_listen"}
* affirm{"appr_or_rej": "approve"}
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "correct details"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 2067131121580916873
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - followup{"name": "action_listen"}
* approve
    - approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "nooo reason"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 4
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - followup{"name": "action_listen"}
* reject
    - reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "i think its fake data"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
## Generated Story 6527459851031057943
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "143.00", "compexpid": "E000166", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56273, "expname": "July 2017 Expense Log", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - followup{"name": "action_listen"}
* approve
    - approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "noo reason for this report"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story -2071390936349936242
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "143.00", "compexpid": "E000166", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56273, "expname": "July 2017 Expense Log", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - followup{"name": "action_listen"}
* approve
    - approve_report
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
* pendingreport
    - pending_report
    - reset_slots
* showapprvls
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "143.00", "compexpid": "E000166", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56273, "expname": "July 2017 Expense Log", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "100.00", "compexpid": "E000156", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 17, 2019", "expid": 56258, "expname": "5/29/17 Dawn Expenses", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000156"}
    - slot{"expid": 56258}
    - followup{"name": "action_listen"}
* deny{"appr_or_rej": "reject"}
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "i think its fake information, please provide correct information"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* pendingreport
    - pending_report
    - reset_slots
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Levenson August 2015"}
    - slot{"compexpid": "E000172"}
    - slot{"expid": 56279}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - open_camera
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
    - no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - action_slot_reset
    - reset_slots
    - utter_okay
* pendingreport
    - pending_report
    - reset_slots
* bye
    - utter_goodbye

## Generated Story 6245577011800584671
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "231.00", "compexpid": "E000172", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56279, "expname": "Levenson August 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "143.00", "compexpid": "E000166", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56273, "expname": "July 2017 Expense Log", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000173"}
    - slot{"expid": 56280}
    - followup{"name": "action_listen"}
* affirm
    - approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no reasons for this report"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* createreport{"name": "Bey July 2016"}
    - slot{"name": "Bey July 2016"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000175"}
    - slot{"expid": 56282}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
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
    - pending_report
    - reset_slots
* bye
    - utter_goodbye

## Generated Story 928472436981389527
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "231.00", "compexpid": "E000172", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56279, "expname": "Levenson August 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "143.00", "compexpid": "E000166", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56273, "expname": "July 2017 Expense Log", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000166"}
    - slot{"expid": 56273}
    - followup{"name": "action_listen"}
* approve
    - approve_report
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
* showapprvls
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "231.00", "compexpid": "E000172", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56279, "expname": "Levenson August 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "143.00", "compexpid": "E000166", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56273, "expname": "July 2017 Expense Log", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000173"}
    - slot{"expid": 56280}
    - followup{"name": "action_listen"}
* reject
    - reject_report
    - slot{"appr_or_rej": "reject"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "crossed your expense limit"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay
* pendingreport
    - pending_report
    - reset_slots
<!-- complete pending reports 22-04-2019 -->
## Generated Story 4950641221715869874
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"pending_report_list": [{"amt": "0.00", "compexpid": "E000180", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56300, "expname": "kxcvk", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000179", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56299, "expname": "Winchester parade 1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000178", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56298, "expname": "dec 2018 summit", "reportType": "report", "travType": "Expense"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_penidngreport
    - slot{"name": "Winchester parade 1"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* affirm{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
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

## Generated Story -8279135100951804713
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"pending_report_list": [{"amt": "0.00", "compexpid": "E000180", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56300, "expname": "kxcvk", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000179", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56299, "expname": "Winchester parade 1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000178", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56298, "expname": "dec 2018 summit", "reportType": "report", "travType": "Expense"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_penidngreport
    - slot{"name": "dec 2018 summit"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* noreceipts
    - no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* affirm
    - action_submit_report
    - action_slot_reset
    - reset_slots
    - utter_okay

## Generated Story 7346984542526238545
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"pending_report_list": [{"amt": "0.00", "compexpid": "E000180", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56300, "expname": "kxcvk", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000179", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56299, "expname": "Winchester parade 1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000178", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56298, "expname": "dec 2018 summit", "reportType": "report", "travType": "Expense"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_penidngreport
    - slot{"name": "Winchester parade 1"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* deny{"adlt_or_sub": "submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots
    - utter_okay


## Generated Story -1984325422377695556
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"pending_report_list": [{"amt": "0.00", "compexpid": "E000180", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56300, "expname": "kxcvk", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000179", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56299, "expname": "Winchester parade 1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000178", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56298, "expname": "dec 2018 summit", "reportType": "report", "travType": "Expense"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_penidngreport
    - slot{"name": "kxcvk"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submit_report
    - reset_slots
    - utter_okay

## Generated Story 2524821452849285883
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"pending_report_list": [{"amt": "0.00", "compexpid": "E000180", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56300, "expname": "kxcvk", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000179", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56299, "expname": "Winchester parade 1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000178", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56298, "expname": "dec 2018 summit", "reportType": "report", "travType": "Expense"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_penidngreport
    - slot{"name": "kxcvk"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submit_report
    - reset_slots
    - utter_okay

## Generated Story -2480999792537275609
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"pending_report_list": [{"amt": "0.00", "compexpid": "E000180", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56300, "expname": "kxcvk", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000179", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56299, "expname": "Winchester parade 1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000178", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56298, "expname": "dec 2018 summit", "reportType": "report", "travType": "Expense"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_penidngreport
    - slot{"name": "kxcvk"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submit_report
    - reset_slots
    - utter_okay
* enterdata
    - pending_report
    - slot{"pending_report_list": [{"amt": "0.00", "compexpid": "E000180", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56300, "expname": "kxcvk", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000179", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56299, "expname": "Winchester parade 1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000178", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56298, "expname": "dec 2018 summit", "reportType": "report", "travType": "Expense"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_penidngreport
    - slot{"name": "kxcvk"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* attachreceipt
    - attach_receipt
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
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

## Generated Story 7842445332802807284
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"pending_report_list": [{"amt": "0.00", "compexpid": "E000180", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56300, "expname": "kxcvk", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000179", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56299, "expname": "Winchester parade 1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000178", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56298, "expname": "dec 2018 summit", "reportType": "report", "travType": "Expense"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_penidngreport
    - slot{"name": "dec 2018 summit"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* attachreceipt
    - attach_receipt
    - slot{"no_more_receipts": "attach"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
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

## Generated Story 835731949456336628
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* approve
    - approve_report
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
    - utter_okay
* pendingreport
    - pending_report
    - slot{"pending_report_list": [{"amt": "0.00", "compexpid": "E000180", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56300, "expname": "kxcvk", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000179", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56299, "expname": "Winchester parade 1", "reportType": "report", "travType": "Expense"}, {"amt": "0.00", "compexpid": "E000178", "displayType": "Expense", "expdt": "Apr 22, 2019", "expid": 56298, "expname": "dec 2018 summit", "reportType": "report", "travType": "Expense"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_penidngreport
    - slot{"name": "kxcvk"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* noreceipts
    - no_receipt
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
* createreport{"name": "feb - mar-2015"}
    - slot{"name": "feb - mar-2015"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"compexpid": "E000181"}
    - slot{"expid": 56302}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* submit
    - action_submit_report
    - reset_slots
    - action_slot_reset
    - reset_slots
    - utter_okay
* bye
    - utter_goodbye

## Generated Story 7195348733200801584
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - followup{"name": "action_listen"}
* go_to_pendingreports
    - action_goto_pendingreports
    - reset_slots

## Generated Story -609346297831193402
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - followup{"name": "action_listen"}
* go_to_pendingreports
    - action_goto_pendingreports
    - reset_slots

## Generated Story 1844885622348341008
* greet
    - action_greet
    - followup{"name": "action_approve_report"}
    - action_approve_report
    - slot{"appr_report_list": [{"amt": "132.00", "compexpid": "E000177", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 22, 2019", "expid": 56297, "expname": "dec 25th", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "152.00", "compexpid": "E000176", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56283, "expname": "june_trip", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}, {"amt": "235.00", "compexpid": "E000173", "crtuserid": "9364", "currency": "USD", "expdt": "Apr 18, 2019", "expid": 56280, "expname": "Sherry November 2015", "reportType": "report", "requestType": "Expense", "subby": "Admin Web"}]}
    - followup{"name": "action_listen"}
* enterdata
    - action_select_report
    - slot{"compexpid": "E000176"}
    - slot{"expid": 56283}
    - followup{"name": "action_listen"}
* approve
    - approve_report
    - slot{"appr_or_rej": "approve"}
    - approve_report_form
    - form{"name": "approve_report_form"}
    - slot{"requested_slot": "comments"}
* form: enterdata
    - form: approve_report_form
    - slot{"comments": "no comments to this report"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_okay

## Generated Story 5192469297440233584
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"name": "dec 2100"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submit_report
    - reset_slots
    - utter_okay
* pendingreport
    - pending_report
    - slot{"name": "dec 2100"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* deny{"adlt_or_sub": "submit"}
    - slot{"adlt_or_sub": "submit"}
    - action_submit_report
    - reset_slots
    - utter_okay

## Generated Story -4163432887399513166
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"name": "dec 2100"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
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
    - action_slot_reset
    - reset_slots
    - utter_okay
* pendingreport
    - pending_report
    - slot{"name": "dec 2100"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submit_report
    - reset_slots
    - utter_okay

## Generated Story -658763898088526845
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"name": "march2021"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
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
    - action_slot_reset
    - reset_slots
    - utter_okay

## Generated Story 6594574081413066794
* greet
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"name": "march2021"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* submit
    - action_submit_report
    - reset_slots
    - utter_okay
* showapprvls
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"name": "march2021"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* affirm{"adlt_or_sub": "addlineitem"}
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
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

## Generated Story 4256274627386694609
* init
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - slot{"name": "dec002"}
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"name": null}
    - form: followup{"name": "create_report_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata{"name": "xyz"}
    - slot{"name": "xyz"}
    - form: create_report_form
    - slot{"name": "xyz"}
    - slot{"compexpid": "E000192"}
    - slot{"expid": 56318}
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

## Generated Story -7194660232929707581
* init
    - action_greet
    - followup{"name": "pending_report"}
    - pending_report
    - followup{"name": "utter_ask_addline_or_submit"}
    - utter_ask_addline_or_submit
* addlineitem
    - action_addlineitem_to_report
    - slot{"adlt_or_sub": "addlineitem"}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* noreceipts
    - no_receipt
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
    - action_slot_reset
    - reset_slots
    - utter_okay
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "december 2015"}
    - slot{"compexpid": "E000193"}
    - slot{"expid": 56319}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* opencamera
    - open_camera
    - slot{"no_more_receipts": "camera"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_receipt"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_receipt
* deny
    - no_receipt
    - slot{"no_more_receipts": "No"}
    - add_receipt_form
    - form{"name": "add_receipt_form"}
    - form: followup{"name": "utter_ask_submit_report"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_submit_report
* deny
    - utter_okay
* bye
    - utter_goodbye

