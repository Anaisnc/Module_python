#!/usr/bin/env python3

import sys

print("=== Player Score Analytics ===")

scores = []
for arg in sys.argv[1:]:
    try:
        scores.append(int(arg))
    except ValueError:
        print(f"Invalid parameter: '{arg}'")

if not scores:
    print("No scores provided.")
    print(f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
else:
    total = sum(scores)
    average = total / len(scores)
    high = max(scores)
    low = min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")