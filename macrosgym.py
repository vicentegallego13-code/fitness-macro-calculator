import os
# Constants (Standard nutritional values)
PROTEIN_CAL_PER_GRAM= 4
CARB_CAL_PER_GRAM = 4
FAT_CAL_PER_GRAM = 9
# Ratios for bodyweight
MAINTENANCE_MULTIPLIER = 15
PROTEIN_PER_KG = 2.0 
FAT_PER_KG = 0.5   
# Goal settings
CALORIE_ADJUSTMENT = 300
def kg_to_pounds(weight_kg):
    """Converts body weight from kilograms to pounds."""
    result = weight_kg * 2.2 
    return result
def final_calories(maintenance_calories, goal):
  """Adjusts maintenance calories based on the user's fitness goal."""
  if goal == "cut":
    result = maintenance_calories - CALORIE_ADJUSTMENT
    message = f"Final calories: {int(result)} calories, your body will go into deficit."
    return result, message
  elif goal == "bulk":
    result = maintenance_calories + CALORIE_ADJUSTMENT
    message = f"Final calories: {int(result)} calories, your body will go into calorie surplus."
    return result, message
  else: 
    message = f"Sorry, {goal} that's not a valid option. Please, choose 'cut' or 'bulk'."
    return maintenance_calories, message
def main():
  """Main program flow: gets user input, calculates macros, and saves a report to a text file."""
  # Clear terminal and get user data
  os.system('cls' if os.name == 'nt' else 'clear')
  while True: 
    try:
      weight_kg = float(input("\nEnter your weight in kg: "))
      break
    except ValueError:
      print("Error: Please enter a valid number (e.g., 75.5)")
  # Macronutrient calculations based on body weight
  pounds = kg_to_pounds(weight_kg)
  maintenance_calories = pounds * MAINTENANCE_MULTIPLIER
  print(f"Maintenance calories: {int(maintenance_calories)} calories")
  protein = weight_kg * PROTEIN_PER_KG
  protein_calories = protein * PROTEIN_CAL_PER_GRAM
  print(f"Proteins: {int(protein)} grams; equivalent to {int(protein_calories)} calories")
  fat = weight_kg * FAT_PER_KG
  fat_calories = fat * FAT_CAL_PER_GRAM
  print(f"Fats: {int(fat)} grams; equivalent to {int(fat_calories)} calories")
  carbs_calories = maintenance_calories - (protein_calories + fat_calories)
  carbs = carbs_calories / CARB_CAL_PER_GRAM
  print(f"Carbs: {int(carbs)} grams; equivalent to {int(carbs_calories)} calories")
  # Adjust calories according to fitness goal (cut/bulk)
  goal = input("Is your goal to bulk up or cut down?: ").lower()
  calories_target, message_goal = final_calories(maintenance_calories, goal) 
  print(message_goal)
  if goal == "cut" or goal == "bulk":    
      final_carbs_grams = (calories_target - (protein_calories + fat_calories)) / 4
      print(f"Your final carbohydrates for the chosen goal are: {int(final_carbs_grams)} grams. The remaining macronutrients are maintained at the same maintenance levels.")
      # Save results to a text file report
      with open("diet.txt", "w") as file:
          file.write(f"--- DIET REPORT: {goal.upper()} ---\n")
          file.write(f"{message_goal}\n")
          file.write("-" * 30 + "\n")
          file.write(f"Proteins: {int(protein)}g\n")
          file.write(f"Fats: {int(fat)}g\n")
          file.write(f"Carbs: {int(final_carbs_grams)}g\n")
          file.write("-" * 30)
if __name__ == "__main__":
    main()