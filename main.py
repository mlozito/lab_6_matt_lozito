print("Hello!\n"
      "------")
while True:
    print("0. Quit\n"
          "1. Add\n"
          "2. Subtract\n")
    user_operation = int(input("What would you like to do?", ))
    if user_operation == 0:
        quit()
    if user_operation == 1:
        user_input_1 = int(input("Please select your first integer.", ))
        user_input_2 = int(input("Please select your second integer.", ))
        sum = user_input_1 + user_input_2
        print(f"The sum of your two integers is {sum}.\n")
    if user_operation == 2:
        user_input_1 = int(input("Please select your first integer.", ))
        user_input_2 = int(input("Please select your second integer.", ))
        difference = user_input_1 - user_input_2
        print(f"The difference of your two integers is {difference}.\n")
