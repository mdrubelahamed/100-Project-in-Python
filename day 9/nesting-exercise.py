travel_log = [
{
    "country": "france",
    "visits": 3,
    "cities": ["Paris","little","dijon"],
},
{
    "country": "germany",
    "visits": 3,
    "cities": ["berlin", "hamburg", "stuttgart"],
}
]

#add func
def add_new_country(c_name,c_visits,c_cities):
    new_country = {}
    new_country["country"] = c_name
    new_country["visits"] = c_visits
    new_country["cities"] = c_cities

    travel_log.append(new_country)



add_new_country("Russia",2,["moscow","saint petersberg"])
print(travel_log)