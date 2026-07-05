#!/usr/bin/python3
# written by: atholcomb
# make_out_word.py


def make_out_word(out, word):
    #print(out[:2]+word+out[2:])
    return out[:2]+word+out[2:]

print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))
