all_players = set(range(1, 41))
hockey_players = set(range(1, 22))
both_sports_players = set(range(1, 11))
cricket_only_players = set(all_players.difference(hockey_players))

print("Total players =", len(all_players))
print("Players exclusively into hockey =", len(hockey_players.difference(both_sports_players)))
print("Players exclusively into cricket =", len(cricket_only_players))
print("Players involved in both sports =", len(both_sports_players))
