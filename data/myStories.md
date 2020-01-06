## Generated Story 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - utter_searching
    - action_restaurant
    - slot{"location": "bengaluru"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
	
## Generated Story 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "800"}
    - slot{"budget": "800"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Allahabad"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "kolkata"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Mumbai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chandigarh"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Chandigarh"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chandigarh"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation