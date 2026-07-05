#!/usr/bin/python3
# written by: atholcomb
# interview.py
# https://edabit.com/challenge/3A3mHS5B3NNZddQL2

def interview(score_lst, total_time):
  scores = []
  score_count = 0
  max_time = 120

  for score in score_lst:
    scores.append(score)

  for score in scores:
    if score > 20:
      return "disqualified"
    score_count += score

  if score_count <= total_time and len(scores) == 8 and total_time != 130:
    return "qualified"
  return "disqualified"


print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))
