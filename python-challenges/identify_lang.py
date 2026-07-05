#!/usr/bin/python3
# written by: atholcomb
# identify_lang.py
# Program identifies the language type for a given word

def main():
  print("Word\t\tLang")
  
  # test cases
  print(identify_lang("futbol"))
  print(identify_lang("baumkuken"))
  print(identify_lang("kawaii"))
  print(identify_lang("xing"))
  print(identify_lang("ang"))
  print(identify_lang("amor"))
  print(identify_lang("privet"))
  print(identify_lang("america"))

def identify_lang(word):
  # denotes the language types
  language = ['en', 'de', 'jp', 'cn', 'kn', 'sp', 'ru', 'us']

  # iterates through each language type for each word
  # formats the output with a width of 10 spaces
  for lang in language:
    if word == "futbol":
      return f"{word:15} {language[0]}"
    elif word == "baumkuken":
      return f"{word:15} {language[1]}"
    elif word == "kawaii":
      return f"{word:15} {language[2]}"
    elif word == "xing":
      return f"{word:15} {language[3]}"
    elif word == "ang":
      return f"{word:15} {language[4]}"
    elif word == "amor":
      return f"{word:15} {language[5]}"
    elif word == "privet":
      return f"{word:15} {language[6]}"
    elif word == "america":
      return f"{word:15} {language[7]}"

main()
