# print("hello world")
# firstname = "onyinye"
# lastname = "iloanugo"
# # age = "25"
# # origin = "USA"

# # statement = f"{firstname} {lastname}, is {age} and is from {origin}"
# # print(statement)

# product1 = "apple"
# product2 = "pear"
# price1 = 200
# price2 = 250
# buyer = f"{firstname} {lastname}"
# quantity1 = 4
# quantity2 = 4
# total = price1 * quantity1 + price2 * quantity2

# statement = f"hello {buyer}, you have purchased {quantity1} {product1} at {price1} and {quantity2} {product2} at {price2} each and your total is {total}"

# print(statement)

# x = input("enter first number")
# y = input("enter second number")
# z = input("enter third number")
# sumofvar = int(x) + int(y) + int(z)
# print(sumofvar)

# buyer = "titi"
# product = input("enter item")
# price = input("enter price")
# quantity = input("enter quantity")
# total = int(price) * int(quantity)

# statement = f"hello {buyer} you purchased {product} for {price} each and you total is {total}."
# print(statement)

# radius = input("enter radius")
# pie = 3.142
# circumference_of_circle =round( 2 * (pie) * int(radius))
# print(circumference_of_circle)

# statement = f"the circumference of the circle with radius {radius} is {circumference_of_circle}"
# print(statement)

# x = int(input("enter x"))
# y = int(input("enter y"))
# a = int(input("enter a"))
# b = int(input("enter b"))
# numerator = (x * b) + (y * b) 
# denominator = (y * b)
# statement = f"{numerator}/{denominator}"
# print(statement)

# 

# code = '+23401'
# x = input('enter number')
# word = code
# word[1:-2:]
# x[1::]
# print(word[1:-2:])
# print(x[1::])

# code = '+23401'
# x = input('enter number')
# code[1:-2:]
# x[1::]
# correct_code = (code[1:-2:])
# correct_number = (x[1::])

# statement = f'{correct_code + correct_number}'
# print(statement)
# statement = 

# showing students pass mark, using true or false
# score = int(input('score point'))
# pass_mark = 70
# response =f"pass : {score >= pass_mark}"
# print(response)

# country_name = input('country name : ')
# age = int(input('how old are you : '))
# nigeria_age = 18
# usa_age = 21
# response_1 = f'can drink in nigeria : {country_name == "nigeria" and age >=nigeria_age}'
# response_2 = f'can drink in usa : {country_name == "USA" and age >=usa_age}'
# print(response_1)
# print(response_2)

# 
# word = input('test for pal...: ')
# test = word[::-1]
# statement = f'test for pal... : {word == test}'
# print(statement)

# sentence = input('give a sentence: ')
# check_word = input('check a word: ')
# print(check_word in sentence)
# print(check_word not in sentence)


# new_file = open('sample.txt','a')
# new_file.writelines('python')
# new_file.close()

# new_file = open('sample.txt','r')
# line = new_file.readlines()
# print(line)


# range(0,20)
# date = input('input your date of birth: ')
# replace = date.replace(' ','-')
# print(replace)

# data = input('input your text: ')
# splitt = data.split()
# print(splitt)

# join = '+'.join(splitt)
# print(join)

# word = input('input your name: ').lower()
# name = word.count('o')

# print(name)

# numbers = [1,2,3]
# mapp = map(lambda x : 2, numbers)
# print(list(mapp))

# mapp = map(lambda x : x*x, numbers)
# print(list(mapp))
# #1x1 2x2 3x3
# #1 4 9 

# mapp = map(lambda x : x*2, numbers)
# print(list(mapp))


# alp = ['boy','girl','house']
# mapp = map(lambda x :len(x), alp)
# print(list(mapp))

# mapp = map(lambda x :(len(x),x), alp)
# print(list(mapp))

# sentence = input('input a sentence: ')  #to show the highest number in a sentence
# sentence_2 = sentence.split(' ')
# mapp = map(lambda x :len(x), sentence_2)
# maxx = max(mapp)
# print(maxx)

# scores = [30,20,60,70,45,70,75,50]
# sum_num = sum(scores)
# num_of_vals = len(scores)
# mean = sum_num/num_of_vals
# mean_deviation = map(lambda score: score - mean, scores)
# print(list(mean_deviation))

#for square root
# print(16**0.5)

# new_file = open('sample.txt','a')
# new_file.writelines('python')
# new_file.close()

# new_file = open('sample.txt','a')
# name = input('place your name: ')
# note = input('write a note: ')
# statement =f'{name} : {note}\n'
# new_file.writelines(statement)
# new_file.close()

# file = open('population.csv','w') #CSV IS USED FOR EXCEL
# file.writelines(f'python, population\n')
# for country, population in zip(countries, population):
# file.close()

# a = int(input('enter value for a: '))
# b = int(input('enter value for b: '))
# c = (a**2+b**2)
# c2 = (c**0.5)
# print(c2)

# scores = input('enter numbers: ')
# scores = int(scores)
# print(scores)
# sum_of_score = sum(scores)
# sum_of_values = len(scores)
# mean = sum_of_score/sum_of_values
# print(mean)

scores = input('enter a list of numers for x seperated by space: ').split()
sum_num_x = sum(int(x) for x in scores)
print(sum_num_x)
num_of_values = len(scores)
mean_x = int(sum_num_x/num_of_values)
mean_num = f'mean x = {mean_x}'
print(mean_num)
mean_deviation_x = map(lambda score: score - mean_x,(int(x) for x in scores))
print(list(mean_deviation_x))

scores_2 = input('enter a list of numers for y seperated by space: ').split()
sum_num_y = sum(int(y) for y in scores_2)
print(sum_num_y)
num_of_values = len(scores)
mean_y = int(sum_num_y/num_of_values)
mean_num = f'mean y = {mean_y}'
print(mean_num)
mean_deviation_y = map(lambda score: score - mean_y,(int(y) for y in scores_2))
print(list(mean_deviation_y))

#delete later
# scores = input('enter a list of numers for x seperated by space and comma: ')
# sum_num = sum(scores)
# print(sum_num)

# sum_num_x = sum(int(x) for x in scores)
# print(sum_num_x)
# num_of_values = len(scores)
# mean_x = int(sum_num_x/num_of_values)
# mean_num = f'mean x = {mean_x}'
# print(mean_num)
# mean_deviation_x = map(lambda score: score - mean_x,(int(x) for x in scores))
# print(list(mean_deviation_x))

# a = [1,2,3,4]
# a = a.split( )
# print(list)(a)

# scores_2 = input('enter a list of numers for y seperated by space: ').split()
# sum_num_y = scores_2.replace(''),()
# print(sum_num_y)
#  sum(int(y) for y in scores_2)
# print(sum_num_y)
# num_of_values = len(scores)
# mean_y = int(sum_num_y/num_of_values)
# mean_num = f'mean y = {mean_y}'
# print(mean_num)
# mean_deviation_y = map(lambda score: score - mean_y,(int(y) for y in scores_2))
# print(list(mean_deviation_y))
  
# scores = input('enter numbers: ').split()
# print(scores)






































