"""A collection of function for doing my project."""
import time

def say_intro_get_name():
	print('Hi, my name is Vifa and I will be your virtual financial advisor!')
	time.sleep(1.25)
	print('My goal is to help you come up with a financial plan based on your current spending and your desired spending.')
	time.sleep(1.5)

	name = str(input('Please type in your name here: '))
	print('Nice to meet you, ' + name + "! Well, let's begin with some questions on your current spending?")

	return name


def is_input_valid(input_value):
	if input_value.isnumeric():
		return True
	try:
		check_if_float = float(input_value)
		return True
	except:
		return False


def ask_for_current_spending(user_name):
	current_spending = {
		'housing': None,
		'utilities': None,
		'food': None,
		'transportation': None,
		'entertainment': None,
		'personal': None
	}

	category_descriptions = {
		'housing': '(rent, mortgage, etc)' ,
		'utilities': '(cell phone, internet, etc)',
		'food': '(groceries, restaurants, etc)',
		'transportation': '(cell phone, internet, etc)',
		'entertainment': '(cell phone, internet, etc)',
		'personal': '(cell phone, internet, etc)'
	}

	for category, spending_amt in current_spending:
		spending_amt = input('Please enter spending amt: ')
		while (is_input_valid(spending_amt) == False):
			spending_amt = input("Sorry, not valid. Please enter spending amt: ")



def start_program():
	user_name = say_intro_get_name()
	current_spending = ask_for_current_spending(user_name)

#start_program()

	
