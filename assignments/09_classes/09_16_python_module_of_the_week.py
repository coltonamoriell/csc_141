from collections import Counter

# Let's say we simulated a bunch of lottery draws and got these results
lottery_draws = [7, 'b', 3, 'e', 7, 4, 'b', 7, 10, 'e', 3, 7]

# Count the frequency of each item instantly
result_counts = Counter(lottery_draws)

print("Frequency of each drawn item:")
print(result_counts)

# You can easily find the most common items
print("\nMost common item:")
print(result_counts.most_common(1))