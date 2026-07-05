#!/usr/bin/python3
# written by: atholcomb
# Given a dictionary of top scores, return only the
# name and top score for each given entry

import json

def top_notes(score_list):
  result = {}

  for d in score_list:
    for k, v in d.items():
      if k == "name":
        result[k] = v
      if k == "notes":
        result["top_note"] = max(v)

  return json.dumps(result, indent=3)

print(top_notes([{"name": "John", "notes": [3, 4, 5]}]))
print(top_notes([{"name": "Max", "notes": [1, 6, 4]}]))
print(top_notes([{"name": "Zy", "notes": [1, 2, 3]}]))
