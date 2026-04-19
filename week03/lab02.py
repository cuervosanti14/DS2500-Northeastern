# LAB EXERCISE 02
# PROBLEM 01
# PART A
sum_1_1000 = 0
for i in range(1001):
    sum_1_1000 += i
print(sum_1_1000)
# PART B
sum_odd_1_2501 = 0
for i in range(2502):
    if i % 2 == 1:
        sum_odd_1_2501 += i
print(sum_odd_1_2501)

# PROBLEM 02
# PART A
fruits = ["apple", "pear", "grapes", "peach"]
letter2fruits = {}
for fruit in fruits:
    first_letter = fruit[0]
    if first_letter in letter2fruits:
        letter2fruits[first_letter].append(fruit)
    else:
        letter2fruits[first_letter] = [fruit]
print(letter2fruits)
# PART B
common_letters = []
first_word = fruits[0]
for char in first_word:
    if char not in common_letters:
        in_all = True
        for fruit in fruits[1:]:
            if char not in fruit:
                in_all = False
                break
        if in_all:
            common_letters.append(char)
print(common_letters)

# PROBLEM 03
# PART A
numbers = [6, 7, 8, 9, 10]
total_sum = 0
for i in numbers:
    while total_sum < 2500:
        total_sum += i
        break
print(total_sum)
# PART B
numbers2 = [1, 2, 3, 4, 5, 6]
limited_sum = 0
for i in numbers2:
    while i % 2 != 0:
        limited_sum += i
        break
    else:
        break
print(limited_sum)

# PROBLEM 04
### SETUP BEGINS -- DO NOT MODIFY
course_description = ("Offers intermediate to advanced Python programming for data "
                      "science. Covers object oriented design patterns using Python, including"
                      " encapsulation, composition, and inheritance. Advanced programming skills cover"
                      " software architecture, recursion, profiling, unit testing and debugging, lineage"
                      " and data provenance, using advanced integrated development environments, and"
                      " software control systems. Uses case studies to survey key concepts in data science"
                      " with an emphasis on machine learning (classification, clustering, deep learning);"
                      " data visualization; and natural language processing. Additional assigned readings"
                      " survey topics in Ethics, Model Bias, and Data Privacy pertinent to todays Big Data"
                      " world. Offers students an opportunity to prepare for more advanced courses in data"
                      " science and to enable practical contributions to software development and data"
                      " science projects in a commercial setting. ")
### SETUP
# PART A
course_description = course_description.lower()
punctuation = ".,;()'"
for char in punctuation:
    course_description = course_description.replace(char, "")
words = course_description.split()
# PART B
word2count = {}
for word in words:
    if word != "":
        if word in word2count:
            word2count[word] += 1
        else:
            word2count[word] = 1
print(word2count)