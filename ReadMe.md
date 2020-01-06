# Project Summary 

An Indian startup wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience.

In this project, we will learn to build a domain-specific chatbot: a restaurant search chatbot. The bot will be able to 'talk' to users in English and will help them search for restaurants in several cities, of multiple cuisine types, budgets etc. You’re going to use an open source framework for building conversational bots  - Rasa.

# Installations Steps

# Cloud installations 
- Create VM on GCloud
![](https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/vm.png)

- Execute below command for Git Installation 
``` python
sudo apt-get install git
```
- Clone the repo from GIT
![](https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/git.png)

- Intall below 
``` python
cd installations 
cloud_installations.sh
```

-  conda installations 
``` python
cd /tmp
curl -O https://repo.continuum.io/archive/Anaconda3-2018.12-Linux-x86_64.sh
sha256sum Anaconda3-2018.12-Linux-x86_64.sh
bash Anaconda3-2018.12.0-Linux-x86_64.sh
source ~/.bashrc
conda info
```
![](https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/conda.png)


-  One time step [Create virtual environment name zomato]
``` python
conda create --name zomato python=3.7
conda activate zomato
```

-  Execute below commands [Make sure commands executed in virtual environment only or execute install.sh (under helper folder)]
``` python
python3 --version
pip --version

cd installations 
sh rasa_installations.sh

pip install rasa_nlu
pip install rasa_core
pip install rasa_core_sdk
pip install rasa_nlu[spacy]
python -m spacy download en
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
pip install rasa_nlu[tensorflow]
```

-  Train NLU
``` python
python train_nlu_model.py
```

-  Train Core
``` python
python train_core_model.py
```

-  Core sever
``` python
sh run_bot_on_terminal.sh
```

-  ngrok installations
``` python
cd installations 
unzip ngrok-stable-linux-amd64.zip
./ngrok authtoken 1RrcQOSk0ImwjZL3RRGPLDKkQ3S_6MtgwdgLt135ik5Fqd1MG
./ngrok help
./ngrok 8080
```
![](https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/ngrok.png)


- Slack Configuration 
https://api.slack.com/apps
![](https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/slack_img_1.png)
![](https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/slack_img_2.png)
![](https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/slack_img_3.png)


Start chatting with bot :)

# Slack Demo Screen Shot 
<p float="left">
<img src="https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/IMG_1.PNG" width="320" height="600">
<img src="https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/IMG_2.PNG" width="320" height="600">
<img src="https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/IMG_3.PNG" width="320" height="600">
<img src="https://github.com/bhargrah/foodie_chatbot/blob/master/screenshots/IMG_4.jpeg" width="320" height="600">
</p>
