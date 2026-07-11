#Email list with duplicates
original_list = ["a@mail.com", "b@mail.com", "c@mail.com","a@mail.com", "d@mail.com", "e@mail.com","b@mail.com","f@mail.com"]

#Convert Email list to set
unique_set = set(original_list)

print(f"Original List: {original_list}")
#Print Unique Addresses by length of set
print(f"Number of unique Addresses in original list = {len(unique_set)}")