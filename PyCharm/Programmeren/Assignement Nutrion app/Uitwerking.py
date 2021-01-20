"""Provide an overview of the nutritional values of a recipe"""

__author__ = "Gijs Boeve"

import os

def get_recipe_ingredients():
    """
    Asks the user for a list of ingredients that will be included in a recipe
    """
    ingredient_list = []
    ingredient = str(input("Give the name of an ingredient included in the recipe "))
    while ingredient != "":
        ingredient_list.append(ingredient)
        ingredient = str(input("Give the name of the next ingredient in the recipe (leave empty when complete) "))

    return ingredient_list

def get_nutritional_values(ingredient_list, file_name="nutritional_values.csv"):
    """
    Tries to get nutritional values for each of the ingredients in the list from a file
    Asks the user for the nutritional values if not yet available in the file and writes them to the file for future use
    """
    nutritional_value_dict = {}
    string_format = "{0:<8}\t{1:<8}\t{2:<10}\t{3:<6}\t{4:<12}\t{5:<7}\n"

    if not os.path.isfile(file_name):
        with open(file_name, "w") as nutritional_value_file:
            nutritional_value_file.write(string_format.format("Name", "Unit", "Kcalories", "Fat", "Carbohydrate", "Protein"))
            for line in nutritional_value_file:
                ingredient, unit, kcalories, fat, carbohydrate, protein = line.format(string_format)
                nutritional_value_dict[ingredient] = (str(unit), float(kcalories), float(fat), float(carbohydrate), float(protein))

    for ingredient in ingredient_list:
        if ingredient not in nutritional_value_dict:
            unit = str(input("Please provide the units in which " + ingredient + " are used "))
            kcalories = float(input("Please provide the amount of kcalories of " + ingredient + " "))
            fat = float(input("Please provide the amount of fat in " + ingredient + " "))
            carbohydrate = float(input("Please provide the amount of carbohydrate in " + ingredient + " "))
            protein = float(input("Please provide the amount of protein in " + ingredient + " "))
            nutritional_value_dict[ingredient] = (unit, kcalories, fat, carbohydrate, protein)

    with open("nutritional_values.csv", "w") as nutritional_value_file:
        nutritional_value_file.write(string_format.format("Ingredient", "Unit", "Kcalories", "Fat", "Carbohydrate", "Protein"))
        for ingredient in nutritional_value_dict:
            unit, kcalories, fat, carbohydrate, protein = nutritional_value_dict[ingredient]
            nutritional_value_file.write(string_format.format(ingredient + ":", str(unit), str(kcalories), str(fat), str(carbohydrate), str(protein)))

    return nutritional_value_dict

def get_amounts(ingredient_list, nutritional_value_dict):
    """
    Given a list of ingredients and a dictionary of nutritional values
    ask the user to provide how much of each ingredient should be used in the recipe
    """
    amounts = {}
    for ingredient in ingredient_list:
        unit, kcalories, fat, carbohydrate, protein = nutritional_value_dict[ingredient]
        amount = float(input("How much " + unit + " of " + ingredient + " do you need in the recipe? "))
        amounts[ingredient] = amount

    return amounts

def generate_table(amounts, nutritional_value_dict):
    """
    ask the user for a quantity per ingredient
    generate a table with nutrient information per ingredient and a total for the recipe
    also generate a line of the total per portion (ask the user for the number of portions)
    """
    string_format = "{0:<8}\t{1:<12}\t{2:<10}\t{3:<8}\t{4:<11}\t{5:<8}"
    string_format_2 = "{0:<8}\t{1:<7}{2:1}{3:<5}\t{4:<10}\t{5:<8}\t{6:<11}\t{7:<8}\n"
    first_line = string_format.format("Ingredient", "Use in Unit", "Kcalories", "Fat", "Carbohydrate", "Protein")
    second_line = "-" * 75
    total_values = []
    print("")
    print(first_line)
    print(second_line)
    for ingredient in ingredients:
        unit, kcalories, fat, carbohydrate, protein = nutritional_value_dict[ingredient]
        amount = amounts[ingredient]
        print(string_format_2.format(ingredient + ":", amount, "/", unit, kcalories, fat, carbohydrate, protein))
        total_values.append(int(amount * kcalories))
        total_values.append(int(amount * fat))
        total_values.append(int(amount * carbohydrate))
        total_values.append(int(amount * protein))
    print(string_format.format("Totaal:", "", total_values[0], total_values[1], total_values[2], total_values[3]))

    file_name = "nutritional_values_table.txt"
    with open(file_name, "w") as assignment_output:
        assignment_output.write(first_line + "\n")
        assignment_output.write(second_line + "\n")
        for ingredient in ingredients:
            unit, kcalories, fat, carbohydrate, protein = nutritional_value_dict[ingredient]
            amount = amounts[ingredient]
            assignment_output.write(string_format_2.format(ingredient + ":", amount, "/", unit, kcalories, fat, carbohydrate, protein))
            #assignment_output.write(string_format.format("Totaal:", "", total_nutritional_value_kcal, total_nutritional_value_fat, total_nutritional_value_carbohydrate, total_nutritional_value_protein))


    #print(sum(total_nutritional_value_fat), sum(total_nutritional_value_kcal), sum(total_nutritional_value_carbohydrate), sum(total_nutritional_value_protein))

    #total_nutritional_value = (sum(kcalories)
    #print(total_nutritional_value_fat, total_nutritional_value_kcal, total_nutritional_value_carbohydrate, total_nutritional_value_protein)
        #ingredient, unit, kcalories, fat, carbohydrate, protein = nutritional_value_dict
        #assignment_output.write(string_format.format(ingredient + ":", str(unit), str(kcalories), str(fat), str(carbohydrate), str(protein)))
        #assignment_output.write(amounts * nutritional_value_dict[unit])

    #print(table_string)

if __name__ == '__main__':

    # 1.  Ask for a list of ingredients.
    ingredients = get_recipe_ingredients()

    # 2. Get nutrient information for each of these ingredients.
    nutritional_values = get_nutritional_values(ingredients)

    # 3. Ask for a list of amounts for each of the ingredients.
    amounts_list = get_amounts(ingredients, nutritional_values)

    # 4. Based on the information retrieved generate a meaningful output.
    generate_table(amounts_list, nutritional_values)

