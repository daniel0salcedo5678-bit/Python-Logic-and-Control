# Written by: Daniel Salcedo
# Javelin Toss Program - Created 09/15/2026
#
# This application is to be used for finding the following: the average distance tossed,
# the maximum distance tossed, the minimum distance tossed for each Javelin Athlete and group of Athlete.
# The program will prompt the user for: total number of athletes competing and total number of tosses per Athlete.
# Then the user will be prompted for the distance thrown for each Athlete.
#

# Setting up the first loop that will determine if the user will wish to continue
# after they are finished with the program
Keep_Going = 'Y'

while Keep_Going == "Y":  # (Outer Most Loop - Run Program - Conditional Loop)
    
    # Setting the variables I will be referencing throughout the code
    toss = 0.0
    athlete_total = 0.0
    total_dist_avg = 0.0
    Maxtoss = 0.0
    Mintoss = float('inf')
    TotalMaxtoss = 0.0
    TotalMintoss = float('inf')
    
    
    # Startup Banner
    print("\n===========================================")
    print("Javelin Competition Toss Program")
    print("===========================================")

    # Requesting user input
    num_athletes = int(input("How many athletes will be competing? "))
    num_toss_per_athlete = int(input("How many tosses do all athletes get? "))

    # Setting up the second loop - number of athletes we will be montoring
    for athlete in range(num_athletes):  # (Next Outer Loop - athlete Counter)
        print('\n\n----------------------------------')    
        print(f"Athlete {athlete + 1} - Enter Distance")
        print('----------------------------------')

        # Setting up the third loop that will prompt the user to input the weight of the toss from the amount of
        # toss listed in the num_toss_per_athlete variable 
        for attempt in range(1, num_toss_per_athlete + 1):  # (Inner Most Loop - toss per athlete Counter)
            toss = float(input(f"Javelin Toss {attempt}: What was the distance for the attempt? "))
            athlete_total += toss # Accepted toss for athlete
            
            if toss < Mintoss:
                Mintoss = toss
                
            if toss > Maxtoss:
                Maxtoss = toss
                
            if Mintoss < TotalMintoss:
                TotalMintoss = Mintoss
                
            if Maxtoss > TotalMaxtoss:
                TotalMaxtoss = Maxtoss
           
        total_dist_avg += float(athlete_total / num_toss_per_athlete)
        # Display summary after each athlete - Table Header
        print("\n==============================================")
        print(f" Javelin Athlete {athlete + 1} Distance Summary")
        print("==============================================")

        # Calculated deliverables from the input within the 3rd loop
        print(f"How many javelin tosses were recorded: {num_toss_per_athlete}")
        print(f"What was the average distance for Athlete {athlete + 1}: "
              f"{float(athlete_total / num_toss_per_athlete):.2f} meters")
        print(f'The furthest javelin toss for Athlete {athlete + 1} was: {Maxtoss:.2f} meters')
        print(f'The shortest javelin toss for Athlete {athlete + 1} was: {Mintoss:.2f} meters')
        print("==============================================\n")

        # This section accumulates the total values from each iteration (athlete) while also resetting
        # the original variables for the next loop.
        
        athlete_total = 0.0
        Maxtoss = 0.0
        Mintoss = float('inf')

    # Once the inner-inner loop is finished it will display a summary of all the deliverables requested
    # As well as provide a means for the user to exit the loop when finished.
    print("\n\n***************************************************************************")
    print("\t\t\t\t\tAll Javelin Athlete Distance Summary")
    print("***************************************************************************")

    # Calculated deliverables from all iterations of the 2nd loop
    print(f"Total number of javelin athletes: {num_athletes}")
    print(f"Total number of all javelin tosses (All Athletes combined): {num_athletes * num_toss_per_athlete} ")
    print(f"Overall average distance of all Athletes tosses combined: {total_dist_avg/ num_athletes:.2f} meters")
    print(f'The furthest javelin toss for All Athletes was: {TotalMaxtoss:.2f} meters')
    print(f'The shortest javelin toss for All Athletes was: {TotalMintoss:.2f} meters')
    print("***************************************************************************")
        
   
    Keep_Going = input("To start over enter 'Y', to exit enter 'N': ")
    
    # Confirm exit if the user selected N.
    if Keep_Going == "N":
        confirm_exit = input("\nAre you sure you want to exit? Enter Y for yes or N for no: ")

        if confirm_exit == "Y":
            Keep_Going = "N"
        else:
            Keep_Going = "Y"   

# If the user declines to use the app again this message will display on the screen
print("\n\nThank you for using the Javelin Competition Toss Program, GOODBYE!")
