echo "--------------------------"
echo "Booting Rasa Core Server"
python -m rasa_core_sdk.endpoint --actions actions.foodie_actions --port 9001 &
echo "--------------------------"
echo "Running Rasa Core"
python -m rasa_core.run --enable_api -d models/dialogue -u models/current/restaurant_nlu --endpoints config/endpoints.yml -o logs/rasa_core_terminal.log
