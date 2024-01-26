# -*- coding: utf-8 -*-

import json
import sys
import redis
from datetime import datetime, timedelta


def clean_list(timeList):
    """enlève les timecodes vieux de plus de 10 minutes de la liste passee en parametre"""
    for i, time in enumerate(timeList):
        if time < (datetime.now() - timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S") and i > 0:
            timeList = timeList[i:]
            break
    return timeList


r = redis.Redis(host='localhost', port=6379, decode_responses=True)

user_id = sys.argv[1]
if r.exists(f"user:{user_id}"): # si l'utilisateur existe, on charge sa liste de timestamp, on la nettoie, verifie sa taille et lui ajoute le timestamp actuel
    timeList = clean_list(json.loads(r.get(f"user:{user_id}"))["timeStamp"])
    if len(timeList) < 10:
        timeList.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        user = {"timeStamp": timeList}
        user = json.dumps(user)
        r.set(f"user:{user_id}", user)
        print(True)
    else:
        print(False)
else:  # si l'utilisateur n'existe pas, on lui cree une clee
    user = {"timeStamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}
    user = json.dumps(user)
    r.set(f"user:{user_id}", user)
    print(True)
