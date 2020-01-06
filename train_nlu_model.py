
import logging
import pprint
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu.test import run_evaluation

# Log Path
logfile = 'logs/nlu_model.log'

# Data path (md files)
data_path = './data/data.md'

# Configuration
configs = './config/nlu_config.yml'

# Model Paths
model_path = './models'
current_model_path = './models/current/restaurant_nlu'

def train_nlu(data_path, configs, model_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    training_data = load_data(data_path)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_path, project_name='current', fixed_model_name='restaurant_nlu')
    run_evaluation(data_path, model_directory)

def run_nlu(nlu_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    interpreter = Interpreter.load(nlu_path)
    pprint.pprint(interpreter.parse("can you please suggest food"))


if __name__ == '__main__':
    train_nlu(data_path, configs, model_path)
    run_nlu(current_model_path)