#Marley Schneider, Rene Trujillo
#11/13/23
# Program that ueses decorators to build two different plate objects and loads them with food
import concrete_plate
import fooddecorations
import check_input

def examine_plate(plate):
  print(plate.description())
  area_left = plate.area()
  weight_left = plate.weight()

  #if statements to check if plate failed
  if weight_left < 0:
    print('The food was too heavy and the plate failed!')
    return True

  if area_left < 0:
    print('Your plate isn\'t big enough for this much food! Your food spillsover the edge.')
    return True

  #if statements to determine what the hint for the area will be
  if 0 <= area_left <= 20:
    area_hint = 'Tiny bit'
  elif 21 <= area_left <=40:
    area_hint = 'Some'
  elif area_left >= 41:
    area_hint = 'Plenty'

  #if statements to see  what the hint for the weight will be
  if 0 <= weight_left <= 6:
    weight_hint = 'Bending'
  elif 7 <= weight_left <= 12:
    weight_hint = 'Weak'
  elif weight_left >= 13:
    weight_hint = 'Strong'

  #printing area hint, weight hint, and return False because plate is good
  print(f'Sturdiness: {weight_hint}')
  print(f'Space available: {area_hint}')
  return False

def main():
  print("Choose a plate:")
  print("1. Small Sturdy Plate")
  print("2. Large Flimsy Plate")

  # has the user enter a number between 1 and 2
  plate_choice = check_input.get_int_range("Enter your choice: ", 1, 2)
  if plate_choice == 1:
    plate = concrete_plate.Small_Plate()
  else:
    plate = concrete_plate.Large_Plate()

  # Presents the user with several different food choices
  while True:
    print()
    print("1. Turkey")
    print("2. Stuffing")
    print("3. Potatoes")
    print("4. Green Beans")
    print("5. Pie")
    print("6. Quit")
    food_choice = check_input.get_int_range("Enter your choice: ", 1, 6)
    print()
    
    if food_choice == 1:
      plate = fooddecorations.Turkey(plate)
    elif food_choice == 2:
      plate = fooddecorations.Stuffing(plate)
    elif food_choice == 3:
      plate = fooddecorations.Potatoes(plate)
    elif food_choice == 4:
      plate = fooddecorations.GreenBeans(plate)
    elif food_choice == 5:
      plate = fooddecorations.Pie(plate)

    # If user quits this will wrap up the plate
    if food_choice == 6:
      print()
      print(plate.description())
      print(f"Good job! You made it to the table with {plate.count()} items.")
      print(f"There was still {plate.area()} square inches left on your plate.")
      print(f"Your plate could have held {plate.weight()} more ounces of food.")
      print('Don\'t worry, you can always go back for more. Happy Thanksgiving!')
      break
      
    if examine_plate(plate):
      break
      
main()