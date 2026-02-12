# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.


def main():
    total_tickets = 0
    another_movie = True
    while another_movie == True:
        input("Name of Movie: ")
        tickets = float(input("Number of tickets: "))
        total_tickets += tickets
        if input("Would you like to get more tickets? (y or n)") == 'y':
            another_movie = True
        else:
            another_movie = False
    print(f"Here is your total ticket count: {total_tickets: .0f}")
    


if __name__ == '__main__':
    main()