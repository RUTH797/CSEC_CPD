def determine_winner(n, s):
    anton_wins = s.count('A')
    danik_wins = s.count('D')

    if anton_wins > danik_wins:
        return "Anton"
    elif danik_wins > anton_wins:
        return "Danik"
    else:
        return "Friendship"

n = int(raw_input())
s = raw_input().strip()

result = determine_winner(n, s)

print(result)
