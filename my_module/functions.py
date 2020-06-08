"""A collection of function for doing my project."""
import time

def say_intro_get_name():
	"""Print out introduction and get user's name from their input. 
    
    Parameters
    ----------
    None
    
    Returns
    -------
    name : string
        The name that the user inputs. 
    """
	print('Hi, my name is Vifa and I will be your virtual financial advisor!')
	print('My goal is to help you come up with a financial plan based on your current spending and your desired spending.')

	name = str(input('Please type in your name here: '))
	print('Nice to meet you, ' + name + "! Well, let's begin with some questions on your current spending?")
	time.sleep(1)

	return name


def is_number_valid(input_value):
	"""Checks to see if user's input is actually a valid spending number (int or float)
    
    Parameters
    ----------
    input_value : string
        The user's input that needs to be checked. 
    
    Returns
    -------
    boolean
        Whether or not the input string can be converted to a float 
    """

	if input_value.isnumeric():
		return True

	try:
		#Checks to see if the value can be typecasted to a float. If yes, it returns True
		check_if_float = float(input_value)
		return True
	except:
		return False


def ask_for_current_spending(user_name):
	"""Gets the user's spending amounts for each category and stores them in a dictionary 
    
    Parameters
    ----------
    user_name : string
        The name of the user (used for more personalized print statements). 
    
    Returns
    -------
    current_spending : dictionary
        Keys represent the spending category (str) and Values represent the spending amt (str) in that category. 
    """

   	#This dictionary is what will be populated by the user's inputs
	current_spending = {
		'housing': None,
		'utilities': None,
		'food': None,
		'transportation': None,
		'entertainment': None,
		'personal': None
	}

	#This dictionary is created so we can print out the descriptions in the for loop in a cleaner manner
	category_descriptions = {
		'housing': '(rent, mortgage, etc)' ,
		'utilities': '(cell phone, internet, etc)',
		'food': '(groceries, restaurants, etc)',
		'transportation': '(gas, public transit, etc)',
		'entertainment': '(travel, subscription services, etc)',
		'personal': '(clothing, gifts, etc)'
	}

	for category, spending_amt in current_spending.items():
		spending_amt = input('Please enter your monthly spending amount on ' + category + " " + category_descriptions[category] + ": ")

		while (is_number_valid(spending_amt) == False):
			print("Sorry, I don't understand.")
			spending_amt = input("Could you please re-enter your spending amount for " + category + " " + category_descriptions[category] + ": ")

		current_spending[category] = spending_amt

	return current_spending


def calculate_total_spending(user_name, current_spending):
	"""Sums up all the spending amounts to give user their total monthly spending. 
    
    Parameters
    ----------
    user_name : string
        The name of the user (used for more personalized print statements) 
    current_spending : dictionary
        Keys represent the spending category (str) and Values represent the spending amt (str) in that category.
    
    Returns
    -------
    total_spending_amount : float
        The result from summing up all the spending amts in every category. 
    """
	total_spending = 0
	for category, spending_amt in current_spending.items():
		total_spending += float(spending_amt)

	#We want to round the total_spending to two decimals so it best represents cents
	total_spending = round(total_spending, 2)

	print('Thank you, ' + user_name + '. From my calculations, it seems that your current monthly spending totals to ' + str(total_spending))
	time.sleep(1)
	return (total_spending)


def is_saving_valid(user_saving_response):
	"""Check to make sure that the user selected a valid saving choice. 
    
    Parameters
    ----------
    user_saving_response : string
        What the user typed in as their response. 
    
    Returns
    -------
    boolean
        Whether or not input was a valid value (should be 1, 2, or 3). 
    """
	if user_saving_response.isnumeric() == False:
		return False

	try:
		possible_valid_responses = [1, 2, 3]
		user_saving = int(user_saving_response)

		#This checks to make sure that the response is 1, 2, or 3
		if user_saving in possible_valid_responses:
			return True
		else:
			return False
	except:
		return False


def get_user_saving(user_name):
	"""Asks the user to choose how much they want to adjust the budget and gets their choice. 
    
    Parameters
    ----------
    user_name : string
        The name of the user (used for more personalized print statements). 
    
    Returns
    -------
    user_saving: string
        Value that user inputted as their savings intensity choice. 
    """
	print("How much savings do you want for this new budget?")
	print("1 = Conservative, 2 = Moderate, 3 = Intense")

	time.sleep(1)
	user_saving = input("Please enter the number that best corresponds to how much you want me to adjust the budget: ")

	#Checks to make sure user input is valid. It keeps querying the user until it is valid.
	while(is_saving_valid(user_saving) == False):
		print("I'm sorry " + user_name + " but I don't understand. Response should be only 1, 2, or 3")
		print("Remember that 1 = Conservative, 2 = Moderate, 3 = Intense")
		time.sleep(1)
		user_saving = input("Please enter the number that fits the intensity of adjustment here:  ")

	print('Perfect! Thank you ' + user_name + ".")
	time.sleep(1)
	return user_saving


def are_all_categories_listed(user_ranking_list):
	"""Checks to see if user's ranking list contains all the categories. 
    
    Parameters
    ----------
    user_ranking_list : list
        List that contains user's rankings of category based on priority. 
    
    Returns
    -------
    boolean
        Whether or not list contains all categories. 
    """
	original_category_list = ['housing', 'utilities', 'food', 'transportation', 'entertainment', 'personal']
	
	# sets allow us to compare two list for equality without taking the arrangement into account
	if set(user_ranking_list) == set(original_category_list):
		return True
	else:
		return False 


def parse_user_ranking(user_ranking):
	"""Parses user's input and converts it to a ranking list. 
    
    Parameters
    ----------
    user_ranking : string
        User's input that needs to be parsed. 
    
    Returns
    -------
    ranking_list : list
        Category ranking list that results from parsing user's input. 
    """
	user_ranking = user_ranking.lower()
	user_ranking = user_ranking.replace(" ", "")

	ranking_list = user_ranking.split(",")
	return ranking_list


def get_user_ranking():
	"""Asks the user to rank the spending categories from least to most flexible. 
    
    Parameters
    ----------
    None
    
    Returns
    -------
    ranking_list : list
        User's ranking list of the spending categories. 
    """
	print("To help me finalize your new budget breakdown, could you rank your categories from LEAST flexible to MOST flexible?")
	print("Do not number each category and separate each category with a comma.")
	print("For your convenience, the 6 categories are housing, utilities, food, transportation, entertainment, and personal.")
	print("Here is an example ranking input: transportation, housing, utilities, entertainment, food, personal")
	time.sleep(1)
	
	user_ranking = input("Type out your ranking here: ")
	ranking_list = parse_user_ranking(user_ranking) 
	
	while are_all_categories_listed(ranking_list) == False:
		print("I'm sorry but I couldn't understand...")
		print("Please remember to separate each category w/ a comma and spell each category exactly as I've listed above")
		time.sleep(1)

		user_ranking = input("Please retype your ranking here: ")
		ranking_list = parse_user_ranking(user_ranking) 

	return ranking_list


def calculate_new_budget(user_category_ranking, user_desired_saving, current_spending):
	"""Utilzies the user's rankings, savings intensity choice, and current spending amts to create a new budget. 
    
    Parameters
    ----------
    user_category_ranking : list
        User's ranking list of the spending categories. 
    user_desired_saving : string
        Value that user inputted as their savings intensity choice.
    current_spending : dictionary
        Keys represent the spending category (str) and Values represent the spending amt (str) in that category.   
    
    Returns
    -------
    user_new_budget : list
        Budget that reflects the new finalized spending amounts (that include savings). 
    """

    #Depending on user's saving choice, the percent to adjust their current budget changes
	adjust_percentage_1 = [0.0, 0.05, 0.05, 0.10, 0.15, 0.20] 
	adjust_percentage_2 = [0.0, 0.05, 0.10, 0.15, 0.25, 0.35] 
	adjust_percentage_3 = [0.0, 0.10, 0.20, 0.30, 0.40, 0.50] 

	saving_adjust_dict = {
		'1': adjust_percentage_1,
		'2': adjust_percentage_2,
		'3': adjust_percentage_3, 
	}

	user_adjust_percentage = saving_adjust_dict[user_desired_saving]
	user_new_budget = []

	for i in range(len(user_adjust_percentage)):
		decrease_amount = user_adjust_percentage[i]
		current_category = user_category_ranking[i]

		new_budget = float(current_spending[current_category]) - (float(current_spending[current_category]) * decrease_amount)
		new_budget = round(new_budget, 2)

		user_new_budget.append(new_budget)

	return user_new_budget


def announce_new_budget(user_category_ranking, user_new_budget):
	"""Goes through the two lists and prints out the new budget to the user. 
    
    Parameters
    ----------
    user_category_ranking : list
        User's ranking list of the spending categories. 
    user_new_budget : list
        Budget that reflects the new finalized spending amounts (that include savings).
    
    Returns
    -------
    final_budget : dictionary
        Keys are the spending category and Values are the new adjusted spending amounts.  
    """
	final_budget = {}

	for i in range(len(user_category_ranking)):
		final_budget[user_category_ranking[i]] = user_new_budget[i]

	print("Alright, after taking everything into consideration...Here is your new budget breakdown!")
	time.sleep(1)

	for category, budget in final_budget.items():
		print(str(category) + ": " + str(budget))

	time.sleep(1)
	print("Thank you for letting me help you save money and have a great day!")

	return final_budget


def start_program():
	"""Script that runs the program by calling the necessary functions. 
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None 
    """
	user_name = say_intro_get_name()
	current_spending = ask_for_current_spending(user_name)
	total_current_spending = calculate_total_spending(user_name, current_spending)
	user_desired_saving = get_user_saving(user_name)
	user_category_ranking = get_user_ranking()
	user_new_budget = calculate_new_budget(user_category_ranking, user_desired_saving, current_spending)
	final_budget = announce_new_budget(user_category_ranking, user_new_budget) 




	
