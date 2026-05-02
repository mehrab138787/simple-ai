import json

with open("result.json") as f:
    data = json.load(f)
    answer = data["choices"][0]["message"]["content"]
    with open("answer.txt", "w", encoding="utf-8") as out:
        out.write(answer)
