from tabulate import tabulate
import sys
# place where the comparison will happen and thieves will be caught
# paste likers list here
# TODO: make list of likers automatically added to the likers_lists array
likers_lists = ['array of likers here']


# convert all the likers to lowercase
likers_set = set()
for liker in likers_lists:
    if isinstance(liker, str):
        likers_set.add("@" + liker.lower())


# # uncomment the code below  to add @ to each name in the likers_lists [if you want to use it]
# # # iterate through the likers_lists and add @ to each name
# for i in range(len(likers_lists)):
#     likers_lists[i] = "@" + likers_lists[i]

# paste whatdapp_to_twitter array here in the format below as returned by the get whatsapptotwitter function
data =[   
    {'name': 'None', 'number': None, 'twitter_username': None},
    {'name': 'None', 'number': None, 'twitter_username': None},
    {'name': 'None', 'number': None, 'twitter_username': None},
    {'name': 'None', 'number': None, 'twitter_username': None},
    {'name': 'None', 'number': None, 'twitter_username': None},

]
# compare likers list and bring out entries in data that their twitter_username is not in the likers list
purge_list = []
for i in range(len(data)):
    twitter_username = data[i]['twitter_username']
    if twitter_username is not None:
        # Convert twitter_username to lowercase for case-insensitive comparison
        twitter_username_lower = twitter_username.lower()
        if twitter_username_lower not in likers_set:
            # push the data to the purge_list
            purge_list.append(data[i])
   
# remove entries where the twitter_username is None or blank
purge_list = [i for i in purge_list if i['twitter_username']]

# print the purge_list
print('purge this ones:', purge_list)

# use tabulate to print the purge_list in a table format
print(tabulate(purge_list, headers='keys', tablefmt='grid'))


