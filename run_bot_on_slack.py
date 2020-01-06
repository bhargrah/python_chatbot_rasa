import logging
from rasa_core import config
from rasa_core import utils
from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
import train_core_model
import warnings
warnings.filterwarnings("ignore")

logfile = "logs/dialogue_model.log"

domain_file = './config/restaurant_domain.yml'
dialogue_model_path = './models/dialogue'
training_data_file = './data/stories.md'
policy_file = './config/policy.yml'

nlu_model_path = './models/current/restaurant_nlu'
endpoints = './config/endpoints.yml'
credentials = './config/credentials.yml'

def run_core(core_model_path, nlu_model_path, action_endpoint_url, slack_token):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    nlu_interpreter = RasaNLUInterpreter(nlu_model_path)
    action_endpoint = EndpointConfig(url=action_endpoint_url)
    agent = Agent.load(core_model_path, interpreter=nlu_interpreter, action_endpoint=action_endpoint)
    input_channel = SlackInput(slack_token)
    agent.handle_channels([input_channel], 5004, serve_forever=True)

    print("Your bot is ready to talk! Type your messages here or send 'stop'")
    while True:
        a = input()
        if a == 'stop':
            break
        responses = agent.handle_text(a)
        for response in responses:
            print(response["text"])
    return agent


if __name__ == '__main__':
    actionConfig = utils.read_yaml_file(endpoints)
    slackConfig = utils.read_yaml_file(credentials)
    #train_core_model.train_core(domain_file, dialogue_model_path ,training_data_file, policy_file)
    run_core(dialogue_model_path, nlu_model_path,
             actionConfig["action_endpoint"]["url"], slackConfig["slack"]["slack_token"])
