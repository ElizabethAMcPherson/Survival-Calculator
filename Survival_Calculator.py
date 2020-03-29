print("Welcome to your cost of living calculator!\n")

income_option = int(input("Do you currently have a job (enter '1') or are you unemployed looking for work (enter '2')? "));
living_option = int(input("\nAre you currently living/located somewhere (enter '1') , or are you looking for somewhere to go (enter '2')? "))
age = int(input("How old are you? "))
if age <= 14:
    print("You are 14 or younger. In general, you should not be working. Please reach out for assistance or help. ")
    print("If you are in need of help or safety, reach out to the National Human Trafficking Hotline:")
    print("Call: 1-888-373-7888  or  Text: 233733  to learn more.")
elif age <= 16:
    print("You are 16 or under. This means your terms of employment and pay are different.")
    print("For example: there are strict restriction on how many hours you can work, and on what days.")
    print("To learn more about working at 16 or under, check [here]")
    print("If your employers are not following these restrictions, or if you are in need of help or safety, reach out to the National Human Trafficking Hotline:")
    print("Call: 1-888-373-7888  or  Text: 233733  to learn more.")
elif age < 18:
    print("You are under the age of 18. This means your terms of employment and pay are different. ")
    print("For example: in many jobs you are not allowed to work at night, and are entitled to 30 minutes of break for every 4 1/2 hour period of work.")
    print("To learn more about working while under 18, check [here]")
    print("If your employers are not following these restrictions, or if you are in need of help or safety, reach out to the National Human Trafficking Hotline:")
    print("Call: 1-888-373-7888  or  Text: 233733  to learn more.")


if (income_option == 1):

    print("\nDo you need help calculating your income amount? [yes/no]")

    global hours_per_week, weeks_per_hour, work_hours_per_year, hour_income, annual_income
    hours_per_week = int(input("\nEnter the the amount of hours per week you work: "))
    if hours_per_week > 40:
        print("Over 40 hours of work per week is usually considered overtime. You should reach out to your employer and make sure you are getting over-time pay.\n");
    weeks_per_year = int(input("Enter the number of weeks you work out of the year (0-52): "))
    work_hours_per_year = hours_per_week * weeks_per_year
    print("Hours worked per year: " + str(work_hours_per_year))
    hour_income = int(input("\nEnter your hourly income: "))
    if hours_per_week > 40 and hour_income <10:
        print("It seems that you are working high hours with low wages - if you are in need of help or safety, reach out to the National Human Trafficking Hotline:")
        print("Call: 1-888-373-7888  or  Text: 233733  to learn more.")
    elif hour_income < 10:
        print(
            "It seems that you are or may be working less than the legal minimum wage, to check your state's minimum wage, check [here].")
    annual_income = work_hours_per_year * hour_income
    print("\nAnnual Income: " + str(annual_income))



    #Have an income and a place to live - budget and expense tracker.
    if (living_option == 1):
        global annual_rent, annual_food, annual_med, annual_transp, clothes_expense, annual_emergency
        annual_rent = int(input("\nEnter your annual rent: "))
        annual_food = int(input("Enter an estimate for your annual food and water costs: "))
        annual_med = int(input("Enter an estimate for your annual medication costs: "))
        annual_transp = int(input("Enter an estimate for your annual transportation cost: "))
        clothes_expense = int(input("Enter an estimate for how much annually you spend on clothes? "))
        # annual emergency relief should be around 6 months of pay
        annual_emergency = (hours_per_week * 6) * hour_income
        employer_fees = int(input("Do you pay any additional 'living' fees to your employer, or any other type of fees? If so, enter the amount:"))
        if employer_fees > 0:
            print("\n(Paying fees to your employer is not a common practice, and is often times unethical and can be dangerous.")
            print("If you are in need of help or safety, reach out to the National Human Trafficking Hotline:")
            print("Call: 1-888-373-7888  or  Text: 233733  to learn more.")
            print("If you need more information, check [here].)\n")

        def survival_calc(rent, food, med, trans, emer, clothes, fees):
            total_expenses = rent + food + med + trans + emer + clothes + fees
            return total_expenses
        survival_cost = survival_calc(annual_rent, annual_food, annual_med, annual_transp, annual_emergency, employer_fees,
                                      clothes_expense)
        money_left_over_survival = annual_income - survival_cost

        def comfort_calc():
            print("\nNext, we can check any additional expenses you might have.")
            pet_expense = int(input("\nEnter an estimate of your annual pet expenses (food, vet, etc): "))
            comfort_extra_food = int(input("Ideally, how much more annually would you like to spend on food? "))
            comfort_extra_trans = int(input("If you have a car, excluding the transportation amount listed above, how much annually do you spend using your car? "));
            comfort_entertainment = int(input("How much annually do you spend on entertainment? (Movies, amusement parks, toy/activity costs): "))
            total_expenses = survival_cost + pet_expense + comfort_extra_food + comfort_extra_trans + comfort_entertainment
            return (total_expenses)

        print("\nSummary:")
        print("Your Annual Income: " + str(annual_income))
        print("Your total cost of just surviving is: " + str(survival_cost))
        if (money_left_over_survival < 0):
            print(
                "Your annual expenses are " + str((money_left_over_survival * -1)) + " more than your annual income.")
            print("(If you need financial assistance, or are in need of help or safety, please check [here])")
        else:
            print("After these costs, you have " + str(money_left_over_survival) + " left over.")

        comfort_total_cost = comfort_calc()
        money_left_over_comfort = annual_income - comfort_total_cost
        print("\nIf you would like to live comfortably, the total cost of living is: " + str(comfort_total_cost))
        if money_left_over_comfort < 0:
            print("Your annual expenses are " + str((money_left_over_comfort + -1)) + " more than your annual income.")
            print("Try lowering these additional expenses first, to see if you can stay within your annual income. ")
            print("If you need financial assistance, please check [here]")
        else:
            print("After these costs, you have: " + str(money_left_over_comfort) + " left over.\n")
    #Have an income and looking for places to go/move to. Based on current income.
    elif living_option == 2:

        current_location = str(input("\nWhere do you want to live? "))
        if current_location == 'Washington DC':
            average_housing_cost = 2,253 * 12
            public_transportation_cost = 1860
            average_clothing_cost = 323
            average_food_cost = 11,207

            location_average_total_cost = 40426

            print("In " + str(current_location) + " the average annual housing cost is: " + str(average_housing_cost))
            print("In " + str(current_location) + " the average annual transportation cost is: " + str(public_transportation_cost))
            print("In " + str(current_location) + " the average annual food/water cost is: " + str(average_food_cost))
            print("In " + str(current_location) + " the average annual clothes cost is: " + str(average_clothing_cost))
            print("\nThe average total cost of living in " + str(current_location) + " is " + str(location_average_total_cost) + ".")

            if annual_income < location_average_total_cost :
                print("\nYour current total income is not enough to cover the cost of living in " + current_location + ".")
                print("You need to make " + str((location_average_total_cost - annual_income)) + " more to start surviving in " + current_location + ".")
            else:
                print("\nYour current total income is enough to start surviving in " + current_location + ".")

        else:
            print("Invalid Input");

    else:
        print("Invalid Input");

elif(income_option == 2):
    skills = str(input("\nWhat skills do you have? "))
    if skills == 'Cooking':
        print("\nHere are some possible employment options with the skill: " + str(skills) + ".")
        print("Restaurant Chef\nFast Food Cood\nPersonal Chef\nAnother example\nAnother example\n(All taken from live legitimate online job sources)\n")
    else:
        print("Invalid Input (for now:) )")


    if(living_option == 1):
        current_location = str(input("\nWhere do you currently live? "));
        if current_location == 'Washington DC':
            print("\nOkay, here are statistics about working in " + str(current_location) + ":")
            print("The current general hourly minimum wage in " + current_location + " is: $14.00")
            print("The current average for " + str(skills) + " in " + str(current_location) + " is: $21,092 per year.")
            print("\nHere are some current openings for " + str(skills) + " in " + str(current_location) + ":")
            print("Cook (Hourly) - Pizza Hut: $9\nCook (Hourly) - Marriott International: $15-17\nCook (Hourly - Panera Bread: #13-14 \nCook (Salary) - Hyatt: $26-28,000")

            average_housing_cost = 2, 253 * 12
            public_transportation_cost = 1860
            average_clothing_cost = 323
            average_food_cost = 11, 207

            location_average_total_cost = 40426

            print("\nIn " + str(current_location) + " the average annual housing cost is: " + str(average_housing_cost))
            print("In " + str(current_location) + " the average annual transportation cost is: " + str(
                public_transportation_cost))
            print("In " + str(current_location) + " the average annual food/water cost is: " + str(average_food_cost))
            print("In " + str(current_location) + " the average annual clothes cost is: " + str(average_clothing_cost))
            print("\nThe average total cost of living in " + str(current_location) + " is " + str(location_average_total_cost) + ".\n")
            print("If you are in need of assistance (financial or otherwise), help or safety in " + current_location + " here are some resources [here]")

            potential_job = str(input("\nOut of the potential jobs listed, which one caught your eye? "))
            if potential_job == 'Marriott':
                print("\nYour annual salary would be around $30,000 and 34,000.")
                print("This is not enough to cover the average annual living costs.")
                print("Let's check with other jobs and opportunities, or would you like to try a different skillset? [try again or new skills]")


            #if location_average_total_cost > 21092:
                #print("It seems that the average annual salary for " + str(skills) + " is not enough to cover the average annual living cost.")
                #print("Let's check with other jobs and opportunities.")
            #else:
                #print("The average annual salary for " + str(skills) + " is enough to cover the average annual living cost.")
                #print("After these costs, you will have " + str((21092 - location_average_total_cost)) + " left over.")

    elif(living_option == 2):
        print("The current average salary for " + str(skills) + " is: $21,092 per year.\n")
        if age < 18:
            print("You are under 18 and looking for a job and somewhere to move. If you are in need of help or assistance, please check [here].")
            print("If you need to move locations urgently, please check [here], or please reach out to the National Human Trafficking Hotline:")
            print("Call: 1-888-373-7888  or  Text: 233733  to learn more.\n")

        move_location = int(input("Do you know where you want to move [enter 1] or are you looking for somewhere affordable? [enter 2] "))
        if move_location == 1:
            current_location = str(input("Where do you want to move? "))
            if current_location == 'Washington DC':
                average_housing_cost = 2, 253 * 12
                public_transportation_cost = 1860
                average_clothing_cost = 323
                average_food_cost = 11, 207

                location_average_total_cost = 40426

                print("\nIn " + str(current_location) + " the average annual housing cost is: " + str(
                    average_housing_cost))
                print("In " + str(current_location) + " the average annual transportation cost is: " + str(
                    public_transportation_cost))
                print(
                    "In " + str(current_location) + " the average annual food/water cost is: " + str(average_food_cost))
                print("In " + str(current_location) + " the average annual clothes cost is: " + str(
                    average_clothing_cost))
                print("\nThe average total cost of living in " + str(current_location) + " is " + str(location_average_total_cost) + ".\n")

        if move_location == 2:
            user_input = str(input("Where are you right now? "))
            print("\nBased on your skill set(s) and job opportunities, here are some affordable places near " + str(user_input) + ".")
            print("Frederick, MD\nHyattsville, MD\nManassas, VA\n")
            print("Do you need help or assistance moving from [Washington DC] to one of these locations? If so, please check [here].")
            print("If you are in need of help or safety, reach out to the National Human Trafficking Hotline:")
            print("Call: 1-888-373-7888  or  Text: 233733  to learn more.")
        else:
            print("")
    else:
        print("")
else:
    print("Invalid Input")
