#dictionaries
mysore={
    "places-visited":["Mysore Palace","Jaganmohini Palace","St. Philomena's Church"],
    "places-to-go":["Chamundi Hills","Sand Museum","Shuka Vana"]
}

bangalore={
    "places-visited":['Everywhere','Everything'],
    "places-to-go":['Nowhere','Nothing']
}
print(mysore["places-visited"])

#adding new
mysore["places-to-go"].append("R.K Narayan Museum")

#modifying
mysore["places-to-go"].append("Jayalakshmi Vilas")

#print keys and values
for key in mysore:
    print(f"{key}:{mysore[key]}")

#nesting
travel_log={
    "Mysore":mysore,
    "Bengaluru":{"places-visited":['Everywhere','Everything'],"places-to-go":['Nowhere','Nothing']},
    "Bangalore":bangalore
}


for key in travel_log:
    print("\n\n\n")
    print(travel_log[key])

cities=[mysore,bangalore]