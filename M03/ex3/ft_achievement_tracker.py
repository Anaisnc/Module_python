#!/usr/bin/env python3

print("=== Achievement Tracker System ===")

alice = {'Master Explorer', 'Boss Slayer', 'Collector Supreme',
         'World Savior', 'Crafting Genius', 'Untouchable'}
bob = {'Master Explorer', 'Strategist', 'Collector Supreme',
       'World Savior', 'Crafting Genius', 'Untouchable', 'Unstoppable'}
charlie = {'Master Explorer', 'Strategist', 'Collector Supreme',
           'Untouchable', 'Speed Runner', 'Survivor', 'Treasure Hunter',
           'First Steps', 'Sharp Mind'}
dylan = {'Strategist', 'Speed Runner', 'Untouchable',
         'Unstoppable', 'Boss Slayer'}

hidden = {'Hidden Path Finder'}

players = {'Alice': alice, 'Bob': bob, 'Charlie': charlie, 'Dylan': dylan}

for name, achievements in players.items():
    print(f"Player {name}: {achievements}")

all_achievements = alice | bob | charlie | dylan
common = alice & bob & charlie & dylan

print(f"\nAll distinct achievements: {all_achievements}")
print(f"Common achievements: {common}")

for name, achievements in players.items():
    others = set()
    for other_name, other_ach in players.items():
        if other_name != name:
            others |= other_ach
    print(f"Only {name} has: {achievements - others}")

print()
all_with_hidden = all_achievements | hidden
for name, achievements in players.items():
    print(f"{name} is missing: {all_with_hidden - achievements}")