import yaml

with open("Practice.yaml") as f:
    data = yaml.safe_load(f)

print(data)