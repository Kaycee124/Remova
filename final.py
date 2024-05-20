# place where the magic happens

data = {'comparison_data here'}
merged_likers = set()

for likers in data.values():
    merged_likers.update(likers)

print('people that liked',list(merged_likers)) 