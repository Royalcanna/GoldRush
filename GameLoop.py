import math
from geopy import distance



def airportinfo(): #icao
    #sql database ident, name, latitude_deg, longitude_deg

def airportdistance(current, target):
    # lasketaan lentomatka lentokenttien välillä
    start = airportinfo(current)
    end = airportinfo(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km



player_name = input("Enter your name: ")
money = 100  # Starting money
player_range = 0  # Starting range
player_lives = 3  # Starting lives
game_over = False
win = False

starting_airport = "KJFK"  # New York
current_airport = starting_airport
end_airport = "LAX"  # Los Angeles

#test question
questions = [
    {
        "question": "Mikä on kullan kemiallinen merkki?",
        "choices": ["k", "au", "ag", "cu"],
        "correctanswer": "au",
        "time_limit": 15
    }
]

# Game loop
while not game_over:
    # Check if the player has reached the destination
    if current_airport == end_airport:
        print("You win! You have reached your destination!")
        game_over = True
        win = True

    # Display player's current status
    airport = 'JFK Airport'  # Starting at JFK Airport
    print(f"You have {money}$, {player_lives} lives left and {player_range} range")
    print("\033[34m---------------------------------------\033[0m")

    # Ohjeita pelaajalle
    print("You need to answer questions to get range")
    print("You have 15 seconds to answer the question")
    input("\033[34mPress Enter when you are ready to answer\033[0m") # Pauses the game before question

    # need timelimit
    # testi kysymys
    print(questions[0]['question'])
    answer = input("Enter your answer: ")

    # add: if all answers incorrect, goes back one airport
    if answer.lower() == questions[0]['correctanswer'].lower():
        print("Correct answer!")
        player_range += 500
    else:
        print("Wrong answer! You lose range")
        if player_range > 0:
            player_range -= 100




     # calculate distance between airports
    distance_km = airportdistance(current_airport, end_airport)

    if player_range >= distance_km:
        print(f"You have enough range to get to {end_airport}") #end_airport name
        input(f"\033[32mPress Enter to use {distance_km} range\033[0m")

        # moves to next airport
        print("Welcome to {next airport}")
        player_range -= airportdistance

    elif player_range <= 0 and money >= 100:
        print("You have run out of range")
        print("You have chosen to buy another change for 100$")
        money -= 100
        # takaisin kysymykset kohtaan

    elif player_range <= 0 < player_lives and money <= 0:
        print("You have run out of range and money")
        print("You have lost one life")
        print(f"{player_lives} lives left")
        player_lives -= 1
        # takaisin kysymykset kohtaan
    else:
        print("You have run out of range, money and lives")
        print("You have lost the game")
        game_over = True
