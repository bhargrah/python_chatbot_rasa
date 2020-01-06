# One time

# One time step
# conda create --name zomato python=3.7
# conda activate zomato

# Exceute below commands
pip install rasa_nlu
pip install rasa_core
pip install rasa_core_sdk
pip install rasa_nlu[spacy]
python -m spacy download en
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
pip install rasa_nlu[tensorflow]