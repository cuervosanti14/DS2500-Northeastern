# LAB EXERCISE 01

# PROBLEM 01
num = 25
subject = "Computer Science"
is_active = True

# PROBLEM 02
text = "Data Science"
first_char = text[0]
last_char = text[-1]
text_length = len(text)
text_upper = text.upper()
second_word = text[5:12]
text1 = text.replace("Data", "Computer")

# PROBLEM 03
fruits = ["banana", "apple", "orange"]
fruits.append("grapes")
fruits[1] = "mango"
first_item = fruits[0]
last_item = fruits[-1]

# PROBLEM 04
spam = ("Spam spam Spam spam Spam spam Spam Spam Spam spam "
        "spams spams spams spams spams spams spams Spam "
        "Spam Spam Spams Spam spam spam Spam spams spams "
        "Spam Spam Spam Spams Spam spam spam Spam spams "
        "spam spam spams spams")
count_Spam = spam.count("Spam")
count_spam = spam.count("spam")
count_spams = spam.count("spams")
spam_lower = spam.lower()
spam_clean = spam_lower.replace("spams", "spam")
count_spam_clean = spam_clean.count("spam")
spam_list = spam_clean.split(" ")
count_items = len(spam_list)
spam_list_sliced = spam_list[0:4]