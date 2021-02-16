from collections import Counter
import matplotlib.pyplot as plt
import statistics

num_friends = [100, 49, 41, 40, 25, 23, 20, 13, 8, 7, 25, 9, 11, 98, 40,
               59, 49, 10, 1, 2, 0, 0, 0, 1, 24, 10, 14, 8, 4, 3, 43, 32,
               7, 6, 61, 93, 100, 83, 49, 41, 25, 24, 25, 25, 52, 25, 12,
               21, 32, 12, 12, 12, 12, 12, 1, 5]
friends_counts = Counter(num_friends)
xs = range(101)
ys = [friends_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 8])
plt.title('Histogram of Friend Counts')
plt.xlabel('# of friends')
plt.ylabel('# of people')
# plt.show()

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

friends_mean = statistics.mean(num_friends)
friends_median = statistics.median(num_friends)

print(f'mean: {friends_mean} | median: {friends_median}')
