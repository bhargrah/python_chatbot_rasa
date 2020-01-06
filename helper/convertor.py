# converter utility file which is needed to convert training data from json format to md format

from rasa_nlu.convert import convert_training_data
convert_training_data(data_file="./data/nlu.json", out_file="./data/nlu.md", output_format="md", language="")