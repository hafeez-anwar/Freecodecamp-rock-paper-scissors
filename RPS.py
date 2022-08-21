# Created by: Dr. Hafeez Anwar
# Date: August 20, 2022
# This is the solution to the first exercise of the course MACHINE LEARNING with PYTHON on freecodecamp.org
# There are FOUR opponent players namely 1.quincy 2.mrugesh 3.kris and 4.Abbey
# Each player has it own strategy. We will design a solution in the FUNCTION PLAYER, to win from all these opponents 
# with a winning rate of >60%

# Our strategy is simple,
# FIRST: Each time, the LIST opponent_history is cleared, becuase it accumulates all histories of the previous plays
# as well. Hence, the opponent_history starts with an empty string

# SECOND: Play one move for FIRST FIVE TIMES i.e. GUESS = 'P'
# This allows us to spot the opponent's strategy which is
# unique for every opponent. We use this trick, to identify
# the opponent and then play accordingly.

# THIRD: quincy's strategy is straight forward, hence, we
# track the last four positions opponent_history[-4,-3,-2,-1]
# and predict the fifth play accordingly
def quincy_strategy(opponent_history):
    if opponent_history[-4]=='R' and opponent_history[-3]=='P' and opponent_history[-2]=='P' and opponent_history[-1]=='S':
        return 'P'
    elif opponent_history[-4]=='P' and opponent_history[-3]=='P' and opponent_history[-2]=='S' and opponent_history[-1]=='R':
        return 'P'
    elif opponent_history[-4]=='P' and opponent_history[-3]=='S' and opponent_history[-2]=='R' and opponent_history[-1]=='R':
        return 'S'
    elif opponent_history[-4]=='S' and opponent_history[-3]=='R' and opponent_history[-2]=='R' and opponent_history[-1]=='P':
        return 'S'
    elif opponent_history[-4]=='R' and opponent_history[-3]=='R' and opponent_history[-2]=='P' and opponent_history[-1]=='P':
        return 'R'

# THIRD: kris strategy is based on our previous reply,
#                      0   1   2   3   4
# Initially, we send ['P','P','P','P','P']
# it will now send 'S' in reponse to our 'P' at position 4
# and 5%3 = 2, so we send 'S' in response to 'S'
# in response to 'S', it will now send 'R'
# and 6%3=0, so we send 'P'
# in response to 'P', it will send 'S'
# and 7%3=1. we send 'R'
# and in response 'R', it will send 'P'
# and 8%3=2, we will send 'S'

# To summarize,
# @ (opponent_history)%3==0
# it sends R
# we send P
# @ (opponent_history)%3==1
# it sends S
# we send R
# @ (opponent_history)%3==2
# it sends P
# we send S

def kris_strategy(opponent_history):

    if len(opponent_history)%3==0:
        return 'P'
    if len(opponent_history)%3==1:
        return 'R'
    if len(opponent_history)%3==2:
        return 'S'

# FOURTH: Abbey' strategy is to look at our Strategy
# Hence, we change our strategy according to abbey's
# last three plays, which makes our play somehow
# random and confusing for him.

# if the last two plays by abbey are identical,
# then our guess is the ideal reponse of the last
# play. If it continues the same play, we win. if
# it sends the ideal response to its last play, it
# makes a tie and hence our losing probability falls
# to 33%.

# If the last two plays are not identical, we look
# for plays are [-2] and [-3]. and repeat the same
# response, but this time, if [-2]!=[-3]

# otherwise, repeat the last play of abbey.

def abbey_strategy(prev_play,opponent_history):
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    if opponent_history[-2]==opponent_history[-1]:
        if prev_play=='P':
            return ideal_response[prev_play]
        elif prev_play=='R':
            return ideal_response[prev_play]
        elif prev_play=='S':
            return ideal_response[prev_play]
    elif opponent_history[-2]!=opponent_history[-1]:
        if opponent_history[-3]!=opponent_history[-2]:
            if prev_play=='P':
                return ideal_response[opponent_history[-4]]
            elif prev_play=='R':
                return ideal_response[opponent_history[-4]]
            else:
                return ideal_response[opponent_history[-4]]
        else:
            return prev_play

def player(prev_play, opponent_history=[]):

    # This is very important as the the opponent_history keeps
    # growing one after the other player. Hence, at the Start
    # of each play, it should be cleared so that the history of
    # previous player does not get appended
    if not prev_play:
        opponent_history.clear()

    # Initial Play is a trick to know the opponent whether it is
    # quincy, kris, abbey or mrugesh
    # This is to let know about the strategy of the other player.
    # Once, we get the last ten moves of the opponent, we can
    # observe the first 4 moves to decide which player is playing
    # againt us.
    if len(opponent_history)<=5:
        guess = 'P'

    # Strategy for Kris
    # First FOUR moves of KRIS are ['','P','S','S']
    elif opponent_history[1]== 'P' and opponent_history[2]=='S' and opponent_history[3]=='S':
        guess = kris_strategy(opponent_history)

    # Strategy for Abbey
    # First FOUR moves of KRIS are ['','P','P','S']
    elif opponent_history[1]== 'P' and opponent_history[2]=='P' and opponent_history[3]=='S':
        guess = abbey_strategy(prev_play,opponent_history)

    # Abbey's strategy works for mrugesh
    # First FOUR moves of KRIS are ['','R','R','S']
    elif opponent_history[1]== 'R' and opponent_history[2]=='R' and opponent_history[3]=='S':
        guess = abbey_strategy(prev_play,opponent_history)

    # Strategy for quincy
    # First FOUR moves of KRIS are ['','R','P','P']
    elif opponent_history[1]== 'R' and opponent_history[2]=='P' and opponent_history[3]=='P':
        guess = quincy_strategy(opponent_history)

    opponent_history.append(prev_play)
    return guess
