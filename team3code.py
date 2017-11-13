#Vinny & Lizzie
def move(my_history, their_history, my_score, their_score):
    if my_history == 0:
        return 'c'
    if (their_history[len(their_history)-1]) == 'c':
        return 'c'
    else:
        return 'b'
    