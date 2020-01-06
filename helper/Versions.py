rasa_nlu_depenedencies = "jsonschema, numpy, simplejson, klein, ruamel.yaml, scikit-learn, typing, future, coloredlogs, tqdm, requests, boto3, gevent, matplotlib, cloudpickle, packaging"

rass_core_dependencies ="pika, colorhash, tqdm, fbmessenger, networkx, rasa-core-sdk, terminaltables, jsonschema, scikit-learn, packaging, pykwalify, jsonpickle, rocketchat-API, python-dateutil, typing, fakeredis, mattermostwrapper, flask-cors, pymongo, pytz, ruamel.yaml, flask, apscheduler, twilio, webexteamssdk, tensorflow, flask-jwt-simple, scipy, redis, python-telegram-bot, colorclass, pydot, questionary, python-socketio, rasa-nlu, requests, gevent, slackclient, coloredlogs, numpy"


for item in rasa_nlu_depenedencies.split(","):
    print("pip show "+item.strip())

for item in rass_core_dependencies.split(","):
    print("pip show "+item.strip())