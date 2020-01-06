<!-- good bye stories -->
## Generated Story -563498545592324679
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545592325679
* goodbye
    - utter_goodbye
	- action_restart_conversation
    - action_restart_conversation

## Generated Story -563498545592327679
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545592328679
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545592329679
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545592323679
* goodbye
    - utter_goodbye
	- action_restart_conversation
	
<!-- good bye stories -->


<!-- deny stories -->
## Generated Story -563498145592323679
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498245592323679
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498345592323679
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498445592323679
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498645592323679
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498745592323679
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498845592323679
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498945592323679
* deny
    - utter_no_email_sent
	- action_restart_conversation
<!-- deny stories -->


<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and email -->
## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation


## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation						
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
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
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
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
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 9999999999
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
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 2732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "kanpur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 3732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "jaipur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 4732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation


<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and email -->

<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and no email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation


## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

<!-- stories starting with only bare restaurant_search with complete restaurant_searchation and no email -->





<!-- stories starting with location restaurant_search with complete restaurant_searchation and sent email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
<!-- stories starting with location restaurant_search with complete restaurant_searchation and sent email -->


<!-- stories starting with location restaurant_search with complete restaurant_searchation and no sent email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Amritsar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nagpur"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
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
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
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
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
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
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
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
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
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
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
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
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
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
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
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
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation


<!-- stories starting with location restaurant_search with complete restaurant_searchation and no sent email -->


<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and sent email -->

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* send_email{"email": "zjiom@gasf.co.in"}
    - slot{"email": "zjiom@gasf.co.in"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chennai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Gwalior"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Surat"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and sent email -->

<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and no sent email -->

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chennai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Gwalior"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Surat"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

<!-- stories starting with cuisine restaurant_search with complete restaurant_searchation and no sent email -->



<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_searchation and sent email -->
## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Chandigarh"}
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
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Guwahati"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Guwahati"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Guwahati"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation

<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_searchation and sent email -->


<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_searchation and no sent email -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165514
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bhopal"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bhopal"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bhopal"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation

## Generated Story -2126870891193165654
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart_conversation


## Generated Story -2126870891193165634
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation


## Generated Story -2126870891193165610
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Kozhikode"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kozhikode"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Kozhikode"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation


## Generated Story -2126870891193165613
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "mumbai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "mumbai"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart_conversation
<!-- stories starting with cuisine and location restaurant_search, with complete restaurant_searchation and no sent email -->

<!-- misc -->
## Generated Story -563498545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592326379
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation


<!-- misc -->
<!-- leave in between -->


## Generated Story -563498545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation

## Generated Story -563498545592426679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart_conversation
	- action_restart_conversation


## Generated Story -563498545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
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
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545595326679
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545596326679
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545792326679
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498548592326679
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* goodbye
    - utter_goodbye
	- action_restart_conversation

## Generated Story -563498545502322679
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart_conversation

<!-- leave in between -->




<!-- condition checkpoints -->

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conversation


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conversation


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conversation


## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation


## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patnait"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conversation


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conversation


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conversation


## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Bangla"}
    - slot{"location": "Bangla"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation


## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patnait"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patnait"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conversation

## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conversation


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart_conversation


## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart_conversation


## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story 5732454364351689134
* greet
    - utter_greet
* restaurant_search{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation


## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -563498545592326678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patnait"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patnait"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_validate_city
    - slot{"city_status": "Invalid"}
    - utter_location_not_found
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

<!-- condition checkpoints -->

<!-- all the restaurant_searchation in one go -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation


## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "299"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "299"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

<!-- all restaurant_searchation in one go. -->



<!-- starting with budget and location -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

<!-- starting with cuisine and budget -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -2126870891193165614
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation

## Generated Story -56349
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation
    
## Generated Story -5634985
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Bhilwara"}
    - slot{"location": "Bhilwara"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation
    
## Generated Story -56349856
* greet
    - utter_greet
* restaurant_search{"location": "Bhilwara"}
    - slot{"location": "Bhilwara"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart_conversation
    
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

## Generated Story 21
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
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

## Generated Story 22
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
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

## Generated Story 23
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
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

## Generated Story 24
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
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
	
## Generated Story 56
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chandigarh"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 57
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
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
	
## Generated Story 58
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_city
    - slot{"city_status": "Service"}
    - utter_ask_price_range
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chandigarh"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "foodierestbotai@gmail.com"}
    - slot{"email": "foodierestbotai@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart_conversation
	
## Generated Story 59
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"city_status": "No_Service"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
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