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
def calculate_maintenance(weight_kg, height, age, gender, activity):
    """Calculate the Basal Metabolic Rate (BMR) using the Harris-Benedict formula and apply the physical activity factor."""
    if gender == "male":
     bmr = 66.47 + (13.75 * weight_kg) + (5 * height) - (6.75 * age)
    else:
     bmr = 655.1 + (9.56 * weight_kg) + (1.85 * height) - (4.67 * age)
    physical_activity = {"1": 1.2, "2": 1.375, "3": 1.55, "4": 1.725, "5": 1.9}
    return bmr * physical_activity.get(activity, 1.2)
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
  elif goal == "maintenance":
    result = maintenance_calories
    message = f"Final calories: {int(result)} calories, you will maintain your current weight."
    return result, message
def save_diet_report(goal, message_goal, protein, fat, final_carbs_grams):
  with open("diet.txt", "w") as file:
      file.write(f"--- DIET REPORT: {goal.upper()} ---\n")
      file.write(f"{message_goal}\n")
      file.write("-" * 30 + "\n")
      file.write(f"Proteins: {int(protein)}g\n")
      file.write(f"Fats: {int(fat)}g\n")
      file.write(f"Carbs: {int(final_carbs_grams)}g\n")
      file.write("-" * 30)
def main():
  """Main program flow: gets user input, calculates macros, and saves a report to a text file."""
  # Clear terminal and get user data
  os.system('cls' if os.name == 'nt' else 'clear')
  while True: 
    try:
      weight_kg = float(input("\nEnter your weight in kg (e.g.; 75): "))
      height = float(input("\nEnter your height in cm (e.g., 175) " ))
      age = int(input("\nEnter your age: "))
      break
    except ValueError:
      print("Error: Please enter a valid number")
  while True:
    gender = (input("\nEnter 'male' or 'female': ")).lower()
    if gender in ["male", "female"]:
      break
    print("Invalid option, try again.")
  print("\n- Physical Activity Level -")
  print("1: Sedentary (Little or none)")
  print("2: Light (1-3 days/week)")
  print("3: Moderate (3-5 days/week)")
  print("4: Vigorous (6-7 days/week)")
  print("5: Very Vigorous (Athlete/Physical Work)")
  while True:
      activity = (input("Choose an option (1-5): "))
      if activity in ["1", "2", "3", "4", "5"]:
        break
      print("Error: Please, choose a number from 1 to 5")
  maintenance_calories = calculate_maintenance(weight_kg, height, age, gender, activity)
  while True:
      goal = input("Is your goal to bulk up, cut down or maintain your current weight?: ").lower().strip()
      if goal in ["bulk", "cut", "maintenance"]:
        break
      print(f"Sorry, '{goal}' that's not a valid option. Please, choose 'cut', 'bulk' or 'maintenance'.")
  calories_target, message_goal = final_calories(maintenance_calories, goal) 
  print(f"Maintenance calories: {int(maintenance_calories)} calories")
  # Calculation of fixed macronutrients (Protein and Fat)
  protein = weight_kg * PROTEIN_PER_KG
  protein_calories = protein * PROTEIN_CAL_PER_GRAM
  print(f"Proteins: {int(protein)} grams; equivalent to {int(protein_calories)} calories")
  fat = weight_kg * FAT_PER_KG
  fat_calories = fat * FAT_CAL_PER_GRAM
  print(f"Fats: {int(fat)} grams; equivalent to {int(fat_calories)} calories")
  print(message_goal)
  if goal in ["cut", "bulk", "maintenance"]:
      # Carbohydrates are calculated by difference to reach the calorie goal
      carbs_total_cal = calories_target - (protein_calories + fat_calories)
      final_carbs_grams = max(0, carbs_total_cal / CARB_CAL_PER_GRAM)
      print(f"Your final carbohydrates for the chosen goal are: {int(final_carbs_grams)} grams. The remaining macronutrients are maintained at the same maintenance levels.")
      # Save results to a text file report
      save_diet_report(goal, message_goal, protein, fat, final_carbs_grams)    
if __name__ == "__main__":
    main()