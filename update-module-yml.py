#!/usr/bin/env python3
import yaml
import os

challenges = os.listdir("./basket")


with open("./module.yml") as f:
    data = yaml.safe_load(f)

def get_name(chall_id):
    parts = chall_id.split('-')
    parts = parts[1:]
    return ' '.join(word.capitalize() for word in parts)

data["challenges"] = []
for chall in sorted(challenges):
    name = get_name(chall)
    data["challenges"].append({
        "id": chall,
        "name": name
    })

with open("./module.yml", "w") as f:
    yaml.dump(data, f, sort_keys=False)
