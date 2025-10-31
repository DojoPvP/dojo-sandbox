#!/usr/bin/env python3
import yaml
import os
import re

challenges = os.listdir("./basket")

MAX_ID_LEN = 32

def sanitize_id(chall_id):
    chall_id = chall_id.lower()
    chall_id = re.sub(r'[^a-z0-9-]', '-', chall_id) # lowercase only and valid chars
    return chall_id[:MAX_ID_LEN] # keep it under id limit

def get_name(chall_id):
    parts = chall_id.split('-')
    parts = parts[1:]
    return ' '.join(word.capitalize() for word in parts)

data = {
    "id": "basket",
    "name": "basket",
}

data["challenges"] = []
for chall in sorted(challenges):
    chall_id = sanitize_id(chall)
    name = get_name(chall)
    data["challenges"].append({
        "id": chall,
        "name": name,
        "type": "challenge",
    })

with open("./module.yml", "w") as f:
    yaml.dump(data, f, sort_keys=False)
