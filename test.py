import requests

with open("toxic.txt", "r") as f:
    for line in f:
        try:
            req = f"http://localhost:8000/sentiment/toxicity?q={line}"
            resp = requests.get(req).json()
            if "toxicity" not in resp: raise KeyError
        except KeyError:
            # If there is a # in the message it may not be parsed correctly
            req = f"http://localhost:8000/sentiment/toxicity?q=\"{line}\""
            resp = requests.get(req).json()

        if resp["toxicity"] < 0.01:
            print(line)