echo "--------------------------"
echo "Booting Rasa Core Server"
python -m rasa_core_sdk.endpoint --actions actions.foodie_actions --port 9001 &
echo "--------------------------"
echo "Running Rasa Core"
python run_bot_on_slack.py