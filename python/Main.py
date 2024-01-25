import json

import redis
from datetime import datetime


if __name__ == "__main__":
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    user1 = {"timeStamp": []}
    # Get the current timestamp
    user1["timeStamp"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user1["timeStamp"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user1["timeStamp"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user1["timeStamp"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user1["timeStamp"].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    user1 = json.dumps(user1)

    r.set('user:1', user1)

    feur = r.get('user:1')

    print(json.loads(feur)["timeStamp"])

