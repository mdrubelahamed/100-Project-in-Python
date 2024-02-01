# # store information in key value pairs

# monthConversions={
#     "jan": "january",
#     "feb": "february",
#     "mar": "march",
#     "apr": "april",
#     "may": "may",
#     "jun": "june",
#     "jul": "july",
#     "aug": "august",
#     "sep": "september",
#     "oct": "october",
#     "nov": "november",
#     "dec": "december",
#     1: "first number"
# }

# # print(monthConversions["jan"])
# print(monthConversions.get("job",". get fuction, not a valid key"))



# focus={
#     1 : "know what you are doing",
#     2 : "be hungry and be curious about your work",
#     3 : "belive in the process",
#     4 : "process is not a one day work,it's day by day work",
#     5 : "everyday take a step more"
# }

# # print(type(focus))

# # print(focus[5])

# # print(focus)
# # add value in dictionary
# focus[6]= "step more will help me to reach my goal faster"

# # print(focus[5]=="step more will help me to reach my goal faster")

# # print(focus[6])
# # focus[6] -- calling by key
# # del focus[6] ##-- deleting by key

# focus.pop(6) #-- deletion by pop using 
# print(focus)
# print(len(focus))


thisdict = dict(name = "John", age = 36, country = ["india","bangladesh","china"])
print(thisdict)
print(thisdict["country"])
print(thisdict["country"][0])