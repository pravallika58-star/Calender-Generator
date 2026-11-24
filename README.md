# Calender-Generator
# Case Study: Nested Loop Calendar Generator

## Python Activity-Based Learning

### Student Details

- **Name:** DURGA SURYA PRAVALLIKA
- **Roll Number:** N26V01A0383
- **Branch:** CSE
- **Section:** 5
- **Programming Language:** Python

---

## 1. Problem Statement

The Nested Loop Calendar Generator is a Python-based program that generates a formatted monthly calendar using the starting weekday and total number of days provided by the user.

The program arranges dates correctly under weekday headings, aligns weeks properly and validates invalid inputs such as incorrect weekday numbers and invalid month lengths.

## 2. Objectives

- To generate a monthly calendar using Python.
- To arrange dates according to the starting weekday.
- To display dates in properly aligned rows and columns.
- To understand the use of nested loops.
- To validate the starting weekday and number of days.
- To improve logical thinking and programming skills.

## 3. Assumptions

1. The calendar starts with Sunday.
2. Weekday numbers range from 0 to 6.
3. The user provides the month name.
4. The number of days must be 28, 29, 30 or 31.
5. The starting weekday must be between 0 and 6.
6. The starting weekday and month length are assumed to be correct for the selected month.
7. The calendar displays seven days in each week.

### Weekday Numbering

| Number | Weekday |
|---|---|
| 0 | Sunday |
| 1 | Monday |
| 2 | Tuesday |
| 3 | Wednesday |
| 4 | Thursday |
| 5 | Friday |
| 6 | Saturday |

## 4. Algorithm

1. Start the program.
2. Enter the month name.
3. Display weekday numbers from 0 to 6.
4. Enter the starting weekday.
5. Enter the total number of days.
6. Check whether the inputs are numeric.
7. Validate the starting weekday.
8. Validate the number of days.
9. Initialize the weekday names.
10. Display the month heading.
11. Display the weekday headings.
12. Calculate the total number of weeks.
13. Use an outer loop to generate calendar weeks.
14. Use an inner loop to generate seven weekday columns.
15. Print blank spaces before the starting weekday.
16. Print the dates in the correct positions.
17. Display the completed calendar.
18. Stop the program.

## 5. Pseudocode

```text
START

INPUT month_name
INPUT starting_weekday
INPUT total_days

IF inputs are not numeric
    DISPLAY Invalid input

ELSE IF starting_weekday < 0 OR starting_weekday > 6
    DISPLAY Invalid weekday

ELSE IF total_days < 28 OR total_days > 31
    DISPLAY Invalid month length

ELSE

    INITIALIZE weekday names

    DISPLAY month name
    DISPLAY weekday headings

    CALCULATE total weeks

    SET date = 1

    FOR each week

        FOR each weekday

            CALCULATE position

            IF position < starting_weekday
                PRINT blank space

            ELSE IF date > total_days
                PRINT blank space

            ELSE
                PRINT date
                INCREASE date
            END IF

        END FOR

        PRINT new line

    END FOR

    DISPLAY Calendar Generated

END IF

STOP
```

## 6. Python Source Code

**File name:** `calendar_generator.py`

The complete Python implementation is available in this folder.

## 7. Test Cases

| Test Case | Starting Weekday | Number of Days | Expected Result |
|---|---:|---:|---|
| 1 | 0 | 30 | Calendar generated |
| 2 | 1 | 31 | Calendar generated |
| 3 | 3 | 28 | Calendar generated |
| 4 | 6 | 29 | Calendar generated |
| 5 | 7 | 30 | Invalid weekday |
| 6 | 2 | 32 | Invalid month length |
| 7 | 2 | 25 | Invalid month length |
| 8 | abc | 30 | Invalid input |

## 8. Expected Output

```text
MONTHLY CALENDAR GENERATOR

Enter month name: November
Enter starting weekday: 0
Enter number of days: 30

NOVEMBER

 Sun Mon Tue Wed Thu Fri Sat
   1   2   3   4   5   6   7
   8   9  10  11  12  13  14
  15  16  17  18  19  20  21
  22  23  24  25  26  27  28
  29  30

CALENDAR GENERATED
```

## 9. Conclusion

The Nested Loop Calendar Generator successfully generates a monthly calendar based on the starting weekday and total number of days entered by the user.

This project helps us understand Python variables, data types, operators, conditional statements, for loops and nested loops. It also demonstrates how nested loops can be used to organize dates into rows and columns and create a properly formatted calendar.

---

**Project:** Python Activity-Based Learning  
**Topic:** Nested Loop Calendar Generator
