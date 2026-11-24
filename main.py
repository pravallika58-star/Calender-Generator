
# Case Study: Nested Loop Calendar Generator

print("==========================================")
print("          MONTHLY CALENDAR GENERATOR")
print("==========================================")

# Get month details
month = input("Enter month name: ")

print("\nWeekday Codes:")
print("0 - Sunday")
print("1 - Monday")
print("2 - Tuesday")
print("3 - Wednesday")
print("4 - Thursday")
print("5 - Friday")
print("6 - Saturday")

weekday_input = input("\nEnter starting weekday (0-6): ")
days_input = input("Enter number of days (28-31): ")

# Validate numeric inputs
if not weekday_input.isdigit() or not days_input.isdigit():

    print("\nInvalid input! Enter numbers only.")

else:

    start_day = int(weekday_input)
    total_days = int(days_input)

    # Validate starting weekday
    if start_day < 0 or start_day > 6:
        print("\nInvalid weekday! Enter a value from 0 to 6.")

    # Validate number of days
    elif total_days < 28 or total_days > 31:
        print("\nInvalid month length! Enter 28, 29, 30 or 31.")

    else:

        weekdays = [
            "Sun", "Mon", "Tue", "Wed",
            "Thu", "Fri", "Sat"
        ]

        print("\n==========================================")
        print("             ", month.upper())
        print("==========================================")

        # Display weekday headings
        for day in weekdays:
            print("%4s" % day, end="")

        print()

        # Calculate number of calendar weeks
        total_weeks = (start_day + total_days + 6) // 7

        date = 1

        # Generate calendar using nested loops
        for week in range(total_weeks):

            for day in range(7):

                position = week * 7 + day

                if position < start_day or date > total_days:
                    print("    ", end="")

                else:
                    print("%4d" % date, end="")
                    date += 1

            print()

        print("\n==========================================")
        print("        CALENDAR GENERATED")
        print("==========================================")
