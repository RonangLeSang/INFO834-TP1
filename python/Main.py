# -*- coding: utf-8 -*-

import json
import sys
# sys.path.append('C:\\Users\\ronan\\PycharmProjects\\INFO834 TP1\\venv\\bin\\python\\Lib\\site-packages\\redis')
import redis
from datetime import datetime, timedelta


def clean_list(timeList):
    for i, time in enumerate(timeList):
        if time < (datetime.now() - timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S") and i > 0:
            timeList = timeList[i:]
            break
    return timeList


r = redis.Redis(host='localhost', port=6379, decode_responses=True)

user_id = sys.argv[1]
if r.exists(f"user:{user_id}"):
    timeList = clean_list(json.loads(r.get(f"user:{user_id}"))["timeStamp"])
    if len(timeList) < 10:
        timeList.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        user = {"timeStamp": timeList}
        user = json.dumps(user)
        r.set(f"user:{user_id}", user)
        print(True)
    else:
        print(False)
else:
    user = {"timeStamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}
    user = json.dumps(user)
    r.set(f"user:{user_id}", user)
    print(True)
