"""A collection of function for doing my project."""
import time

def say_intro_get_name():
	print('Hi, my name is Vifa and I will be your virtual financial advisor!')
	time.sleep(1.25)
	print('My goal is to help you come up with a financial plan based on your current spending and your desired spending.')
	time.sleep(1.25)

	name = str(input('Please type in your name here: '))
	print('Nice to meet you, ' + name + "! Well, let's begin with some questions on your current spending?")

	return name


def is_number_valid(input_value):
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
		'transportation': '(gas, public transit, etc)',
		'entertainment': '(travel, subscription services, etc)',
		'personal': '(clothing, gifts, etc)'
	}

	for category, spending_amt in current_spending.items():
		spending_amt = input('Please enter spending amt: ')

		while (is_number_valid(spending_amt) == False):
			spending_amt = input("Sorry, not valid. Please enter spending amt: ")

		current_spending[category] = spending_amt

	return current_spending


def calculate_total_spending(user_name, current_spending):
	total_spending = 0
	for category, spending_amt in current_spending.items():
		total_spending += float(spending_amt)

	total_spending = round(total_spending, 2)

	print('Thank you, ' + user_name + '. From my calculations, it seems that your current spending totals to ' + str(total_spending))
	return (total_spending)


def is_saving_valid(user_saving_response):
	if user_saving_response.isnumeric():
		return False

	try:
		possible_valid_responses = [1, 2, 3]
		user_saving = int(user_saving_response)

		if user_saving in possible_valid_responses:
			return True
		else:
			return False
	except:
		return False


def get_user_saving(user_name):
	print("How much savings do you want for this new budget?")
	print("1 = Conservative, 2 = Moderate, 3 = Intense")
	user_saving = input("Please enter the number that best corresponds to how much you want me to adjust the budget: ")

	while(is_saving_valid(user_saving) == False):
		print("I'm sorry " + user_name + " but I don't understand. Response should be only 1, 2, or 3")
		print("Remember that 1 = Conservative, 2 = Moderate, 3 = Intense")
		user_saving = input("Please enter the number that fits the intensity of adjustment here:  ")

	print('Perfect! Thank you ' + user_name + ".")
	return (int(user_saving))


def are_all_categories_listed(user_ranking_list):
	original_category_list = ['housing', 'utilities', 'food', 'transportation', 'entertainment', 'personal']
	
	if set(user_ranking_list) == set(original_category_list):
		return True
	else:
		return False 


def parse_user_ranking(user_ranking):
	user_ranking = user_ranking.lower()
	user_ranking = user_ranking.replace(" ", "")

	ranking_list = user_ranking.split(",")
	return ranking_list


def get_user_ranking():
	print("To help me finalize your new budget breakdown, could you rank your categories from LEAST flexible to MOST flexible?")
	print("Do not number each category and separate each category with a comma.")
	print("For your convenience, the 6 categories are housing, utilities, food, transportation, entertainment, and personal.")
	print("Here is an example ranking input: transportation, housing, utilities, entertainment, food, personal")
	
	user_ranking = input("Type out your ranking here: ")
	ranking_list = parse_user_ranking(user_ranking) 
	
	while are_all_categories_listed(ranking_list) == False:
		print("I'm sorry but I couldn't understand...")
		print("Please remember to separate each category w/ a comma and spell each category exactly as I've listed above")
		print("Here is an example ranking: transportation, housing, utilities, entertainment, food, personal")

		user_ranking = input("Please retype your ranking here: ")
		ranking_list = parse_user_ranking(user_ranking) 

	return ranking_list


def calculate_new_budget(user_category_ranking, user_desired_saving):
	adjust_percentage_1 = [0.0, 0.05, 0.05, 0.10, 0.15, 0.20] 
	adjust_percentage_2 = [0.0, 0.05, 0.10, 0.15, 0.25, 0.35] 
	adjust_percentage_3 = [0.0, 0.10, 0.20, 0.30, 0.40, 0.50] 

	saving_adjust_dict = {
		1: adjust_percentage_1
		2: adjust_percentage_2
		3: adjust_percentage_3 
	}

	user_adjust_percentage = saving_adjust_dict[user_desired_saving]
	user_new_budget = []

	for i in range(user_choice):
		decrease_amount = user_adjust_percentage[i]

		new_budget = user_category_ranking[i] - (user_category_ranking[i] * decrease_amount)
		new_budget = round(new_budget, 2)

		user_new_budget.append(new_budget)

	return user_new_budget


def start_program():
	user_name = say_intro_get_name()
	current_spending = ask_for_current_spending(user_name)
	total_current_spending = calculate_total_spending(user_name, current_spending)
	user_desired_saving = get_user_saving(user_name)
	user_category_ranking = get_user_ranking()
	user_new_budget = calculate_new_budget(user_category_ranking, user_desired_saving)
	announce_new_budget(user_category_ranking, user_new_budget) 


#start_program()
#print(is_ranking_valid('hi, Alvin, game'))
print(get_user_ranking())

	
