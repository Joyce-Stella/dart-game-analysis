# 1. Importing modules
import csv
import matplotlib.pyplot as plt
def get_dart_data():
    data = []
    with open('dart_hits.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            player = int(line[0])
            x = float(line[1])
            y = float(line[2])
            data.append([player, x, y])
    return data
data = get_dart_data()

# 3. Data Representation
#Plot scatter for one player
def individual_scatter_plot(data, player_number):
    x = []
    y = []
    for throw in data:
        if throw[0] == player_number:
            x.append(throw[1])
            y.append(throw[2])
    plt.scatter(x, y, color='black', marker='+')
    plt.title(f"Player {player_number}'s Dart Hits", color='red')
    plt.xlabel('X', color='blue')
    plt.ylabel('Y', color='blue')
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.grid(True)
    plt.show()
#Plot scatter for all players
def plot_all_players(data):
    player1_x = []
    player1_y = []
    player2_x = []
    player2_y = []
    player3_x = []
    player3_y = []
    for point in data:
        player_num = point[0]
        x = point[1]
        y = point[2]
        if player_num == 1:
                player1_x.append(x)
                player1_y.append(y)
        elif player_num == 2:
                player2_x.append(x)
                player2_y.append(y)
        elif player_num == 3:
                player3_x.append(x)
                player3_y.append(y)
    plt.scatter(player1_x, player1_y, color='black', marker='+', label='Player 1')
    plt.scatter(player2_x, player2_y, color='green', marker='x', label='Player 2')
    plt.scatter(player3_x, player3_y, color='blue', marker='o', label='Player 3')
    plt.title("Dart Hits for All Players", color='red')
    plt.xlabel("X Coordinate", color='blue')
    plt.ylabel("Y Coordinate", color='blue')
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.legend()
    plt.grid(True)
    plt.show()
#Stacked Bar Chart
def plot_stacked_bar_chart(data):
    player1_scores = [0, 0, 0, 0]
    player2_scores = [0, 0, 0, 0]
    player3_scores = [0, 0, 0, 0]
    for hit in data:
        player = hit[0]
        x = hit[1]
        y = hit[2]
        distance = (x ** 2 + y ** 2) ** 0.5
        if distance <= 1:
            score_index = 0
        elif distance <= 2:
            score_index = 1
        elif distance <= 3:
            score_index = 2
        else:
            score_index = 3
        if player == 1:
            player1_scores[score_index] += 1
        elif player == 2:
            player2_scores[score_index] += 1
        elif player == 3:
            player3_scores[score_index] += 1
    players = ['Player 1', 'Player 2', 'Player 3']
    tens = [player1_scores[0], player2_scores[0], player3_scores[0]]
    fives = [player1_scores[1], player2_scores[1], player3_scores[1]]
    ones = [player1_scores[2], player2_scores[2], player3_scores[2]]
    zeros = [player1_scores[3], player2_scores[3], player3_scores[3]]
    plt.bar(players, tens, color='red', label='10 points')
    plt.bar(players, fives, bottom=tens, color='blue', label='5 points')
    plt.bar(players, ones, bottom=[tens[i] + fives[i] for i in range(3)], color='green', label='1 point')
    plt.bar(players, zeros, bottom=[tens[i] + fives[i] + ones[i] for i in range(3)], color='purple', label='0 points')
    plt.title('Dart Scores', color='red')
    plt.xlabel('Players', color='blue')
    plt.ylabel('No. of Hits', color='blue')
    plt.legend()
    plt.grid(True)
    plt.show()

#4. Analyse Data
import math
def analyse_data(data):
    player_scores = {}
    players = [1, 2, 3]
    player_displacements = {}
    for player in players:
        hits = []
        for point in data:
            if point[0] == player:
                hits.append(point)
        total_score = 0
        total_x = 0
        total_y = 0
        for point in hits:
            player_num = point[0]
            x = point[1]
            y = point[2]
            distance = (x ** 2 + y ** 2) ** 0.5
            total_x += x
            total_y += y
            if distance <= 1:
                total_score += 10
            elif distance <= 2:
                total_score += 5
            elif distance <= 3:
                total_score += 1
        if len(hits) > 0:
            avg_x = (total_x / len(hits))
            avg_y = (total_y / len(hits))
        else:
            avg_x = 0
            avg_y = 0
        if player not in player_scores:
            player_scores[player] = total_score
        else:
            player_scores[player] = total_score
        if player not in player_displacements:
            player_displacements[player] = (avg_x, avg_y)
        else:
            player_displacements[player] = (avg_x, avg_y)

    for player in players:
        avg_x = player_displacements[player][0]
        avg_y = player_displacements[player][1]
        print(f"Player {player}:")
        print(f"  Total Score: {player_scores[player]}")
        print(f"  Average Displacement: ({avg_x:.2f}, {avg_y:.2f})")
    max_score = 0
    for score in player_scores.values():
        if score > max_score:
            max_score = score
    winners = []
    for player in player_scores:
        if player_scores[player] == max_score:
            winners.append(player)
    if len(winners) == 1:
        print("The winner is Player", winners[0], "!")
    else:
        print("It's a tie between:", end=" ")
        for i in range(len(winners)):
            print("Player", winners[i], end="")
            if i < len(winners) - 1:
                print(", ", end="")
        print()

#2. Navigation Menu
is_running = True
while is_running:
    print("""Choose an option: 
    1. Plots
    2. Analyse Data
    3. Exit""")
    choice = input("Enter your choice: ")
    if choice == '1':
        print("""Choose an option: 
        1. Scatter plot for Player 1
        2. Scatter plot for Player 2
        3. Scatter plot for Player 3
        4. Scatter plot for all three players
        5. Stacked bar chart showing score distribution for each player
        6. Go back""")
        choice1 = input("Enter your choice: ")
        if choice1 == '1':
            individual_scatter_plot(data, 1)
        elif choice1 == '2':
            individual_scatter_plot(data, 2)
        elif choice1 == '3':
            individual_scatter_plot(data, 3)
        elif choice1 == '4':
            plot_all_players(data)
        elif choice1 == '5':
            plot_stacked_bar_chart(data)
        elif choice1 == '6':
            print("Returning to main menu")
        else:
            print("Invalid choice.")
    elif choice == '2':
        analyse_data(data)
    elif choice == '3':
        print("Exiting...")
        is_running = False
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")