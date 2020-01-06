import logging
from rasa_core_sdk import Action
import zomatopy
import json
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import UserUtteranceReverted
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted

logfile = 'logs/foodie_actions.log'

dict_mail = {}


class ActionRestartedConversation(Action):
    def name(self):
        return 'action_restart_conversation'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]


class ActionSendMailService(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        logging.basicConfig(filename=logfile, level=logging.DEBUG)
        email = tracker.get_slot('email')

        # for slack handling format [  mailto:@gmail.com|@gmail.com ]
        if len(email.split("|")) == 2:
            email = email.split("|")[1]

        import smtplib
        from email.message import EmailMessage
        msg = EmailMessage()

        msg['Subject'] = 'Restaurant Recommendations'
        msg['From'] = "need to specify mail"
        msg['To'] = email

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login("### need to specify mail", "#### password")

        message_body = "Hi Guest \n\nHope you are doing well!!! \nThe details of all the restaurants you inquried. \n\n"
        global dict_mail
        sorted_list = list(sorted(dict_mail.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
        counter_flag = len(sorted_list)
        if counter_flag == 0:
            message_body = message_body + "Oops! No restaurant found for your query.Please refine your search.\n\n"
        else:
            loop_terminate = 10
            for iCnt in range(counter_flag):
                message_body = message_body + str(iCnt + 1) + ". " + sorted_list[iCnt][0]
                if loop_terminate == iCnt + 1:
                    break

        message_body = message_body + "\nHope you have a great day ahead. \n\nThanks & Regads\n Foodie Bot"
        msg.set_content(message_body)
        try:
            smtp.send_message(msg)
            smtp.quit()
        except:
            dispatcher.utter_message("Something went wrong , could not sent mail to " + email)

        dict_mail = {}
        return [AllSlotsReset()]


class ActionValidateService(Action):
    def name(self):
        return 'action_validate_city'

    def run(self, dispatcher, tracker, domain):
        logging.basicConfig(filename=logfile, level=logging.DEBUG)
        loc = tracker.get_slot('location')
        operate = False
        validcity = "Bangalore, Chennai, Delhi, Hyderabad, Kolkata, Mumbai, Ahmedabad, Pune,Agra, Ajmer, Aligarh, " \
                    "Amravati, Amritsar, Asansol, Aurangabad, Bareilly, Belgaum, Bhavnagar, Bhiwandi, Bhopal, " \
                    "Bhubaneswar, Bikaner, Bilaspur, Bokaro Steel City, Chandigarh,Coimbatore Nagpur, Cuttack, " \
                    "Dehradun, Dhanbad, Bhilai, Durgapur, Erode, Faridabad, Firozabad, Ghaziabad, Gorakhpur, " \
                    "Gulbarga, Guntur, Gwalior, Gurgaon, Guwahati, Hubli–Dharwad, Indore, Jabalpur, Jaipur, " \
                    "Jalandhar, Jammu, Jamnagar, Jamshedpur, Jhansi, Jodhpur, Kakinada, Kannur, Kanpur, Kochi, " \
                    "Kottayam, Kolhapur, Kollam, Kota, Kozhikode, Kurnool, Ludhiana, Lucknow, Madurai, Malappuram, " \
                    "Mathura, Goa, Mangalore, Meerut, Moradabad, Mysore, Nanded, Nashik, Nellore, Noida, Palakkad, " \
                    "Patna, Pondicherry,Purulia ,Allahabad, Raipur, Rajkot, Rajahmundry, Ranchi, Rourkela, Salem, " \
                    "Sangli, Siliguri, Solapur, Srinagar, Thiruvananthapuram, Thrissur, Tiruchirappalli, Tirupati, " \
                    "Tirunelveli, Tiruppur, Tiruvannamalai, Ujjain, Bijapur, Vadodara, Varanasi, Vasai-Virar City, " \
                    "Vijayawada, Vellore, Warangal, Surat , Visakhapatnam"

        validcity_list = [city.lower().strip() for city in validcity.split(',')]
        city = str(loc).lower().strip()
        if city.lower() in validcity_list:
            return [SlotSet('city_status', "Service")]
        else:
            zomato = zomatopy.initialize_app({"user_key": "## your Zomato key"})
            try:
                result = zomato.get_city_ID(city)
                return [SlotSet('city_status', "No_Service")]
            except:
                return [SlotSet('city_status', "Invalid")]

        return [SlotSet('city_status', "Service")]


class ActionSearchRestaurants(Action):

    def name(self):
        return 'action_restaurant'

    def run(self, dispatcher, tracker, domain):
        logging.basicConfig(filename=logfile, level=logging.DEBUG)
        zomato = zomatopy.initialize_app({"user_key": "## your Zomato key"})

        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')

        location_detail = zomato.get_location(loc, 1)

        json_data = json.loads(location_detail)

        latitude = json_data["location_suggestions"][0]["latitude"]
        longitude = json_data["location_suggestions"][0]["longitude"]

        cuisines_dict = {
            'american': 1,
            'mexican': 73,
            'italian': 55,
            'thai': 95,
            'chinese': 25,
            'north indian': 50,
            'cafe': 30,
            'bakery': 5,
            'biryani': 7,
            'south indian': 85
        }

        # Query zomato API to find restaurant
        results = zomato.restaurant_search("", latitude, longitude, str(cuisines_dict.get(cuisine)), 150)

        restaurant_date = json.loads(results)

        # Handling response
        response = ""
        dict = {}

        if restaurant_date['results_found'] == 0:
            response = "Sorry, we didn't find any results for this query"
        else:
            dict = self.filterRestaurantBasedOnBudgetAndCusine(str(cuisine), str(budget), restaurant_date)

        sorted_list = list(sorted(dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))

        index = len(sorted_list)

        if index == 0:
            response = "Oops! No restaurant found for this query.Please refine your search."
        elif index < 5:
            for i in range(len(sorted_list)):
                response = response + sorted_list[i][0]
            response = response + "\n For more results please adjust budget range...\n"
        else:
            for i in range(5):
                response = response + sorted_list[i][0]

        dispatcher.utter_message(str(response))
        return [SlotSet('location', loc)]

    def filterRestaurantBasedOnBudgetAndCusine(self, userCuisine, userBudget, allRestaurants):
        rangeMin = 0
        rangeMax = 20000
        userbudget = 300

        import re
        try:
            userBudget = str(userBudget)
            if '<' in userBudget:
                userbudget = int(re.findall(r'\d+', userBudget)[0]) - 1
            elif '>' in userBudget:
                userbudget = int(re.findall(r'\d+', userBudget)[0]) + 1
            elif '-' in userBudget:
                userbudget = int(re.findall(r'\d+', userBudget)[1])
            else:
                userbudget = str(userBudget)
        except:
            userbudget = str(userBudget)

        userbudget = str(userbudget)

        if userbudget.isdigit():
            price = int(userbudget)
            if price == 1:
                rangeMax = 299
            elif price == 2:
                rangeMin = 300
                rangeMax = 700
            elif price == 3:
                rangeMin = 701
            elif price < 300:
                rangeMax = 299
            elif price < 701 and price >= 300:
                rangeMin = 300
                rangeMax = 700
            else:
                rangeMin = 701
        else:
            rangeMin = 300
            rangeMax = 700

        dict_local = {}
        global dict_mail
        dict_mail = {}
        for restaurant in allRestaurants['restaurants']:
            name = restaurant['restaurant']['name']
            address = restaurant['restaurant']['location']['address']
            rating = restaurant['restaurant']['user_rating']['aggregate_rating']

            # Filtering using below fields
            average_cost_for_two = restaurant['restaurant']['average_cost_for_two']
            cuisines = restaurant['restaurant']['cuisines']

            if average_cost_for_two <= rangeMax and average_cost_for_two >= rangeMin:
                for item in [x.strip() for x in str(cuisines).split(",")]:
                    if str(userCuisine).lower() == item.lower():
                        dict_local.update(
                            {(name + " in " + address + " has been rated " + str(rating) + "\n"): float(rating)})
                        dict_mail.update({(name + " in " + address + " has been rated " + str(
                            rating) + " with cost for two as " + str(average_cost_for_two) + "\n"): float(rating)})

        return dict_local
