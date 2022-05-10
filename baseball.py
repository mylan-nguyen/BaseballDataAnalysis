YEAR = 0
LEAGUE = 1
TEAM = 2
GAMES_PLAYED = 3
GAMES_WON = 4
GAMES_LOST = 5
WON_WS = 6
RUNS = 7
AT_BAT = 8
HITS = 9
DOUBLES = 10
TRIPLES = 11
HOME_RUNS = 12
ATTENDANCE = 13

# what is this for...
NON_INT_COLS = [LEAGUE,TEAM,WON_WS]

# ===================================================
# Function read in the teams.csv file
# ===================================================
def read_file(filename):
    my_file = open(filename, 'r')
    my_file.readline()  # read the first line to ignore header
    list_all_data = my_file.readlines()
    # print(lines)

    #create an empty list for the data
    my_list = []

    for lines in list_all_data:
        lines = lines.strip()
        my_team_info = lines.split(",")
        my_list.append(my_team_info)

    return my_list

# ===================================================
# QUESTION 1
# Function find team with the highest number of home runs in a season
# ===================================================
def home_run(list_all_data):

    # collect data for year, team and hr score of first line in list of lists
    my_year = list_all_data[0][YEAR]
    # print(my_year)
    my_team = list_all_data[0][TEAM]
    # print(my_team)
    hr_score = int(list_all_data[0][HOME_RUNS])
    # print(hr_score)

    for line in list_all_data:
        if int(line[HOME_RUNS]) > hr_score:
            hr_score = int(line[HOME_RUNS])
            my_year = line[YEAR]
            my_team = line[TEAM]
    print("The year is", my_year, ", the team is", my_team, ", and number of HR", hr_score)

# ===================================================
# QUESTION 2
# Function find the total attendance at all games in 1999
# ===================================================
def attendance(list_all_data):
    attendance_list = []

    for line in list_all_data:
        year = line[0]
        attendance_num = line[13]
        if "1999" in year:
            # print(attendance_num)
            attendance_list.append(attendance_num)
            # print(attendance_list)

    #convert list of strings to list of integers
    attendance_list = [int(i) for i in attendance_list]
    # print ("Modified list is : " + str(attendance_list))

    my_list = sum(attendance_list)

    return my_list


# ===================================================
# QUESTION 3
# What team had the lowest percentage of games won (i.e., games won / total games played)
# and also won the world series in a season?
# ===================================================
def low_game_wins(list_all_data):
    # easier way to skip the header
    # new_list = list_all_data[1:]
    # print(new_list)

    my_year = list_all_data[0][YEAR]
    # print(my_year)
    my_team = list_all_data[0][TEAM]
    # print(my_team)
    won_world_series = list_all_data[0][WON_WS]

    games_won = int(list_all_data[0][GAMES_WON])
    total_games = int(list_all_data[0][GAMES_PLAYED])
    my_min = games_won/total_games

    for line in list_all_data:
        if line[WON_WS] == 'Y':
            if my_min > int(line[GAMES_WON])/int(line[GAMES_PLAYED]):
                my_year = line[YEAR]
                my_team = line[TEAM]
                my_min = int(line[GAMES_WON])/int(line[GAMES_PLAYED])
        # print("The percentage of games won:", my_min, "by the team", my_team, " in the year ", my_year)

    print("Lowest percentage of games won:", my_min, "by the team", my_team, " in the year ", my_year)


# ===================================================
# QUESTION 4
# What team had the highest percentage of games won (i.e., total games / won games
# played) and also lost the world series in a season?
# ===================================================
def high_game_wins(list_all_data):
    # easier way to skip the header
    # new_list = list_all_data[1:]
    # print(new_list)

    my_year = list_all_data[0][YEAR]
    # print(my_year)
    my_team = list_all_data[0][TEAM]
    # print(my_team)
    won_world_series = list_all_data[0][WON_WS]

    games_won = int(list_all_data[0][GAMES_WON])
    total_games = int(list_all_data[0][GAMES_PLAYED])
    my_max = games_won/total_games

    for line in list_all_data:
        if line[WON_WS] == 'N':
            if int(line[GAMES_WON])/int(line[GAMES_PLAYED]) > my_max:
                my_year = line[YEAR]
                my_team = line[TEAM]
                my_max = int(line[GAMES_WON])/int(line[GAMES_PLAYED])
        # print("The percentage of games won:", my_max, "by the team", my_team, " in the year ", my_year)

    print("Highest percentage of games won:", my_max, "by the team", my_team, " in the year ", my_year)

# ===================================================
# QUESTION 5
# In what four seasons did all teams play the same number of games in the season?
# DO: find the year in which all teams played the same number of games
# ===================================================
def four_season(list_all_data):
    # try to pick a year and check for this particular year first.
    # Once you can validate True/False for any particular year, you can apply the same logic to check all other years.
    # In the end, you should find 4 cases.

    list_of_years = []
    list_of_games_played = []

    for line in list_all_data:
        if line[YEAR] not in list_of_years:
            list_of_years.append(line[YEAR])
    print(list_of_years)

    for y in list_of_years:
        # print("*", y)
        list_temp = []
        for line in list_all_data:
            if line[YEAR] == y:
                # print(line, "and what we look for is", line[GAMES_PLAYED])
                list_temp.append(line[GAMES_PLAYED])

        # print(list_temp)

        # print(isAllNumerSame(list_temp))

        if isAllNumerSame(list_temp) == True:
            print(list_temp)

            print("the record we used:", line)
            print(y, " all teams play the same number of games: ", list_temp[0])

    #for year in list_of_years:
        #print("the year is ", year)
        #for line in list_all_data:
            #if line[YEAR] == year:
            #print("we are on this line: ", line)
            #capture = line[GAMES_PLAYED]
            #print("I want to capture this: ", capture)
            #list_of_games_played.append(capture)
            #print(list_of_games_played)
            #if isAllNumerSame(list_of_games_played) == True:
                #print(year, " all teams play the same number of games: ", capture)
            #else:
            #print("wtf is happening")









# ===================================================
# Main Function - execute program
# ===================================================
def main():
    list_all_data = read_file("Teams.csv")
    # print(list_all_data)

    baseball_dict = home_run(list_all_data)
    # print(baseball_dict)

    #WORKS
    # attendance_num = attendance(list_all_data)
    # print(attendance_num)

    low_games_won = low_game_wins(list_all_data)
    # print(low_games_won)

    high_games_won = high_game_wins(list_all_data)
    # print(high_games_won)

    same_four = four_season(list_all_data)
    print(same_four)


    # Exercise to train your mind for question 5
    # given you 3 list:
    list1 = [1, 1, 1, 1, 1, 1, 1, 1]
    list2 = [2, 2, 2, 2, 2, 1] #false
    list3 = [162, 162, 162, 162, 162, 162]
    list4 = [0, 1]
    list5 = [1, 1, 2, 2, 3, 3]
    list6 = [0, 0, 12, 23]
    #print(isAllNumerSame(list1))
    #print(isAllNumerSame(list2))
    #print(isAllNumerSame(list3))
    #print(isAllNumerSame(list4))
    #print(isAllNumerSame(list5))
    #print(isAllNumerSame(list6))
    # print(read_file_new("Teams.csv"))


def isAllNumerSame(numbers):
    # do your condition here, return true if all numbers are the same
    # return false otherwise
    # .... code to write here
    first_num = numbers[0]
    flag = True

    for num in numbers:
          if(first_num != num):
                 flag = False
                 break;
    if(flag == True):
          return True
    else:
          return False



def read_file_new(filename):
    print("hello world")
    my_file = open(filename, 'r')
    my_file.readline()  # read the first line to ignore header
    list_all_data = my_file.readlines()
    my_list = []

    for lines in list_all_data:
        lines = lines.strip()
        my_team_info = lines.split(",")
        # ** MP ** I am glad you asked the below, I'll show you how to use it here:
        # "... may have missed the hint of NON_INT_COLS = [LEAGUE,TEAM,WON_WS]
        # Because, I do not know where to use it..."
        for i in range(len(my_team_info)):
            if i not in NON_INT_COLS:
                my_team_info[i] = int(my_team_info[i])
        my_list.append(my_team_info)



    return my_list


main()


