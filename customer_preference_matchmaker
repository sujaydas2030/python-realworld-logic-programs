#Customer Preference Matchmaker
# Import literal_eval to safely evaluate string input as a Python literal
from ast import literal_eval
from itertools import combinations
# Taking the input
preferences = literal_eval(input())

def generate_valid_pairs(preferences):
    # Write your code here
  preference_list=[]
  all_comb= combinations(preferences,2)
  for comb_tuple in all_comb:
    if preferences[0]in comb_tuple  or preferences[1] in comb_tuple:
      sorted_pair = tuple(sorted(list(comb_tuple)))
      preference_list.append(sorted_pair)
  return sorted(preference_list)


# Print the output
result = generate_valid_pairs(preferences)
print(result)
