import logging
from rasa_core import config
from rasa_core import utils
from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig


logfile = 'logs/dialogue_model.log'

domain_file = './config/restaurant_domain.yml'
dialogue_model_path = './models/dialogue'
training_data_file = './data/stories.md'
policy_file = './config/policy.yml'

def train_core(domain_file, model_path, training_data_file, policy_config):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    agent = Agent(domain_file, policies=config.load(policy_config))
    training_data = agent.load_data(training_data_file)
    agent.train(training_data)
    agent.persist(model_path)
    return agent

if __name__ == '__main__':
    train_core(domain_file,dialogue_model_path , training_data_file, policy_file)
