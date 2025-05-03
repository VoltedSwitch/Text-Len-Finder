# Initial update for ‘Text Len Comparer Program

import os


def difference_both_lengths(first_t, second_t):
    first_text_length = len(first_t)
    second_text_length = len(second_t)

    if first_text_length > second_text_length:
        difference = first_text_length - second_text_length
    elif second_text_length > first_text_length:
        difference = second_text_length - first_text_length
    else:
        difference = 0

    return difference, first_text_length, second_text_length


def sentence(difference, text1_len, text2_len):
    def character_or_characters(n):
        return 'character' if n == 1 else 'characters'

    if text1_len > text2_len:
        return (f"Your first text is {text1_len} {character_or_characters(text1_len)} long "
                f"and {difference} {character_or_characters(difference)} longer than your second text, "
                f"which is {text2_len} {character_or_characters(text2_len)} in length.")

    elif text2_len > text1_len:
        return (f"Your second text is {text2_len} {character_or_characters(text2_len)} long "
                f"and {difference} {character_or_characters(difference)} longer than your first text, "
                f"which is {text1_len} {character_or_characters(text1_len)} in length.")

    else:
        return (f"Both of your texts are equal in length to each other. The first text is "
                f"{text1_len} {character_or_characters(text1_len)}, while your second text is "
                f"{text2_len} {character_or_characters(text2_len)} in length, and the difference "
                f"in length is {difference}.")


while True:
   print("Welcome to number of characters comparer!")
   print()
   print("Compare second text with first text and vice versa in length.")
   print()

   text1 = input("Enter text: ")
   text2 = input("Enter second text: ")
   print()

   text1 = "".join(text1.split())
   text2 = "".join(text2.split())

   difference, text1_len, text2_len = difference_both_lengths(text1, text2)
   print(sentence(difference, text1_len, text2_len))
   print()

   again = input("Try again?(y/n): ").strip().lower()
   if again == "y":
       os.system("clear")
   else:
       break

