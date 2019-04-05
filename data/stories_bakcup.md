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
* bye
    - utter_goodbye

## Create report with line item affirm
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "uk report"}
    - slot{"requested_slot": "startdate"}
* form: enterdata
    - form: create_report_form
    - slot{"startdate": "13th feb 2019"}
    - slot{"requested_slot": "enddate"}
* form: enterdata
    - form: create_report_form
    - slot{"enddate": "20th feb 2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_lineitem
* affirm
    - nav_to_lineitems
* bye
    - utter_goodbye

## Create report with line item deny
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "uk report"}
    - slot{"requested_slot": "startdate"}
* form: enterdata
    - form: create_report_form
    - slot{"startdate": "13th feb 2019"}
    - slot{"requested_slot": "enddate"}
* form: enterdata
    - form: create_report_form
    - slot{"enddate": "20th feb 2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_lineitem
* deny
    - utter_okay
* bye
    - utter_goodbye

## Create report with line item deny along with pending report
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "second report"}
    - slot{"requested_slot": "startdate"}
* form: enterdata
    - form: create_report_form
    - slot{"startdate": "24th jan 2018"}
    - slot{"requested_slot": "enddate"}
* form: enterdata
    - form: create_report_form
    - slot{"enddate": "20th feb 2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_lineitem
* deny
    - utter_okay
* pendingreport
    - pending_report
* bye
    - utter_goodbye

## create report full with affirm lineitem
* createreportfull{"startdate": "jan 15th", "enddate": "jan 20th", "name": "trip to new york"}
    - slot{"enddate": "jan 20th"}
    - slot{"name": "trip to new york"}
    - slot{"startdate": "jan 15th"}
    - create_report_form
    - form{"name": "create_report_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_lineitem
* affirm
    - nav_to_lineitems
* bye
    - utter_goodbye

## create report full with deny lineitem
* createreportfull{"startdate": "jan 15th", "enddate": "jan 20th", "name": "trip to new york"}
    - slot{"enddate": "jan 20th"}
    - slot{"name": "trip to new york"}
    - slot{"startdate": "jan 15th"}
    - create_report_form
    - form{"name": "create_report_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_lineitem
* deny
    - utter_okay
* bye
    - utter_goodbye
    
    
## Generated Story -3920549272918082505
* bye
    - utter_goodbye

## Generated Story -4080747822277795457
* greet
    - utter_greet
* createreportfull{"name": "Nov_travel", "startdate": "29 - 5 - 2018", "enddate": "29-6-2019"}
    - slot{"enddate": "29-6-2019"}
    - slot{"name": "Nov_travel"}
    - slot{"startdate": "29 - 5 - 2018"}
    - create_report_form
    - form{"name": "create_report_form"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_lineitem
* deny
    - utter_okay
* bye
    - utter_goodbye

## Generated Story 2308451252466435333
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Lauren Kristick Expenses"}
    - slot{"requested_slot": "startdate"}
* form: enterdata
    - form: create_report_form
    - slot{"startdate": "Jan 2019"}
    - slot{"requested_slot": "enddate"}
* form: enterdata
    - form: create_report_form
    - slot{"enddate": "Dec 2019"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_lineitem
* affirm
    - nav_to_lineitems
* pendingreport
    - pending_report
* bye
    - utter_goodbye

## Generated Story 935356270827042538
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Delhi"}
    - slot{"requested_slot": "startdate"}
* form: enterdata
    - form: create_report_form
    - slot{"startdate": "jan 26th"}
    - slot{"requested_slot": "enddate"}
* form: enterdata
    - form: create_report_form
    - slot{"enddate": "dec 18th"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_lineitem
* affirm
    - nav_to_lineitems
* pendingreport
    - pending_report
* bye
    - utter_goodbye

## Generated Story 6746415488072468526
* greet
    - utter_greet
* createreport
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "india-2018"}
    - slot{"requested_slot": "startdate"}
* form: enterdata
    - form: create_report_form
    - slot{"startdate": "20-03-2018"}
    - slot{"requested_slot": "enddate"}
* form: enterdata
    - form: create_report_form
    - slot{"enddate": "30-04-2018"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_lineitem
* deny
    - utter_okay
* bye
    - utter_goodbye
* pendingreport
    - pending_report

## Generated Story 2369050880694273926
* pendingreport
    - pending_report
* createreportfull{"name": "trip to paris"}
    - slot{"name": "trip to paris"}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "startdate"}
* form: enterdata
    - form: create_report_form
    - slot{"startdate": "march 13th"}
    - slot{"requested_slot": "enddate"}
* form: enterdata
    - form: create_report_form
    - slot{"enddate": "april 4th"}
    - slot{"name": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - create_report_form
    - form{"name": "create_report_form"}
    - slot{"requested_slot": "name"}
* form: enterdata
    - form: create_report_form
    - slot{"name": "Cash Advance May"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_lineitem
* affirm
    - nav_to_lineitems
* pendingreport
    - pending_report
* bye
    - utter_goodbye

