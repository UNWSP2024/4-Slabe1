# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    year_number = int(input("How many Years? "))
    if year_number < 1:
        print("ERROR Please input a number greater than 0")
        year_number = int(input("How many Years?"))

    total_rainfall = 0
    total_months = 0
    for years in range(1, year_number + 1):
        month = 1
        for month in range(1, 13):
            rainfall = float(input(f"Input rainfall for month {month} in year {years}: "))
            if rainfall < 0:
                print("ERROR Please input positive number")
                rainfall = float(input(f"Input rainfall for month {month} in year {years}: "))
            total_rainfall += rainfall
            month += 1
            total_months += 1
        years += 1
    
    print(f"total months: {total_months}")
    avg_rainfall = total_rainfall/total_months
    print(f"total rainfall: {total_rainfall}")
    print(f"average rainfall: {avg_rainfall}")



if __name__ == '__main__':
    main()