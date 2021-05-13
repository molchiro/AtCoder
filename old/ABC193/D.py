def score(hand):
    return sum([(i+1)*10**(hand.count(str(i+1))+1) for i in range(9)])

K = int(input())
S = input()[:4]
T = input()[:4]
deck = [K - (S+T).count(str(i+1)) for i in range(9)]

all_events = 0
target_events = 0
for i in range(9):
    for j in range(9):
        current_deck = deck[:]
        takahashi_draw = current_deck[i]
        current_deck[i] -= 1
        aoki_draw = current_deck[j]
        current_deck[j] -= 1

        if len([x for x in current_deck if x < 0]):
            continue

        current_event = takahashi_draw*aoki_draw
        all_events += current_event
        if score(S+str(i+1)) > score(T+str(j+1)):
            target_events += current_event

print(target_events/all_events)