import sqlite3
conn = sqlite3.connect('Sqlite3 Databases')
c = conn.cursor

c.execute('CREATE TABLE food(food_name VARCHAR(20), calories NUMBER(5), protein NUMBER(5), fat NUMBER(5), quantity NUMBER(5))')
c.execute('CREATE TABLE meal(meal_name VARCHAR(20), ingredients VARCHAR(50), time_to_make NUMBER(5))')

conn.commit()
conn.close()


class Food(object):

    def __init__(self, food_name, calories, protein, fat, quantity):
        self.food_name = food_name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.quantity = quantity

    def set_value(self, macro_type, quantity):
        if macro_type == 'calories':
            self.calories = quantity
        elif macro_type == 'protein':
            self.protein = quantity
        elif macro_type == 'fat':
            self.fat = quantity
        self.add_to_food_table()

    def add_to_food_table(self):
        c.execute('INSERT INTO food(food_name, calories, protein, fat, quantity(self.food_name, self.calories, self.protein, \
                  self.fat, self.quantity))')

        conn.commit()
        conn.close()


class Meal(object):

    def __init__(self, meal_name, ingredients, time_to_make):
        self.meal_name = meal_name
        self.ingredients = ingredients
        self.time_to_make = time_to_make
        self.total_calories = 0
        self.total_protein = 0
        self.total_fat = 0

    def calc_time_to_make(self, time_to_make, amount):
        self.time_to_make = time_to_make*amount

    def calc_macros(self, ingredients):
        total_calories = 0
        total_protein = 0
        total_fat = 0
        for i in ingredients:
            total_calories = total_calories + i.calories
            total_protein = total_protein + i.protein
            total_fat = total_fat + i.fat

        self.total_calories = total_calories
        self.total_protein = total_protein
        self.total_fat = total_fat

    def add_to_meal_table(self, ingredients):
        ', '.join(ingredients)
        c.execute('INSERT INTO meal(meal_name, ingredients, time_to_make(self.food_name, self.ingredients, self.time_to_make))')

        conn.commit
        conn.close


def create_ingredients():
    user_foods = int(input('How many foods does the meal contain? '))
    ingredients = []
    food_dict = {}
    for n in range(user_foods):
        print('For each food: ')
        calories = float(input('Enter calories per 100g: '))
        protein = float(input('Enter protein per 100g: '))
        fat = float(input('Enter fat per 100g: '))
        quantity = float(input('Enter quantity of food in grams: '))
        food_name = input('What is the name of the food? ')
        if food_name not in food_dict:
            food_dict[food_name] = Food(food_name, calories, protein, fat, quantity)
        else:
            print('There is already an entry with that name.')
        ingredients.append(food_dict[food_name])
    for i in ingredients:
        i.add_to_food_table()
    return ingredients

    # Are there any other ways to get the user input to create an instance of the Food class? DICTIONARIES


def create_meal(ingredients):
    meal_dict = {}
    meal_name = input('What is the name of the meal?')
    time_to_make = float(input('How long does the meal take to make?'))
    if meal_name not in meal_dict:
        meal_dict[meal_name] = Meal(meal_name, ingredients, time_to_make)
    else:
        print('There is already an entry with that name.')
        meal_dict[meal_name].add_to_meal_table()
    return meal_dict[meal_name] # Returns a single meal in a dict, with the attribute 'ingredients'


def query_tables():
    type_choice = input('Would you like to query a meal or a food?')
    if type_choice == 'meal':
        specific_meal_choice = input('Which meal would you like to query?')
        c.execute(SELECT * FROM meal WHERE meal_name = specific_meal_choice)
        all_rows = c.fetchall()
        print(all_rows)
    elif type_choice == 'food':
        specific_food_choice = input('Which food would you like to query?')
        c.execute(SELECT * FROM food WHERE food_name = specific_food_choice)
        all_rows = c.fetchall()
        print(all_rows)


def check_close(close):
    close_choice = input('Would you like to make another entry')
    if close_choice == 'yes':
        close = True
    elif close_choice == 'no':
        close = False
    else:
        print('That is not an available option, please re-enter')
        check_close()

def main_loop():
    close = False
    while close = False:
        ingredients = create_ingredients() # Creates a list of ingredients
        meal_dict[meal_name] = create_meal(ingredients) # Creates a single meal
        query_choice = input('Would you like to query a table?')
        if query_choice == 'yes':
            query_tables()
        else:
            pass
        check_close(close)


main_loop()








