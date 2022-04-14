#coding: utf-8

# Day 4: Dictionaries in Python
# Thanks to your help, Dot found their seat and enjoyed a relaxing but long flight. At the end of the voyage, they arrived at their first European destination, Munich. They took a taxi to the hotel after landing. Out of the car window, Dot stared in awe at the beautiful centuries-old buildings with elegant stone facades and gorgeous towers. They were so excited to begin exploring the city and taking in its rich history. Dot checked into their hotel room and threw down their belongings before heading out to the city.

# First on Dot’s list to see was the Asam Church, a structure from the 18th century constructed by two brothers. The inspiring Baroque monument was filled with incredible columns, fixtures, and sculptures, including many little golden angels and cherubs. As they regarded this feat of architecture, Dot tried to let the spirit of wonder enter them. But instead, they were filled with the spirit of hunger. Dot hadn’t had much to eat since they were on the plane and were starved. So they ran to a nearby restaurant, excited to try some authentic German food and, of course, beer. We can help Dot look through the menu using data analysis.


# Challenge
# Dot doesn't travel to Europe often, so they decide to take the most expensive option for each course as well as drink. Create a new dictionary called meals that will contain the names of the courses as the keys (starters, mains...), and the name of the food or drink item as the values.

# After assembling the dictionary appropriately, when Dot gives a 10% tip on this meal, how much will the tip come out to?

starters = {
    "Potato Pancakes": 7.99,
    "Salami Platter": 10.29,
    "Brezel": 6.99,
    "Maultaschen": 9.99,
    "Fried Potatoes": 4.99
}

mains = {
    "Braised Beef Short Ribs": 18.99,
    "Paprika Beef Goulash": 15.5,
    "Jager Schnitzel": 16.99,
    "House-mase Bratwurst": 11.99,
    "Kasespatzle": 14.99,
    "German Ravioli": 12.79,
    "Curry Wurst": 10.99
}

desserts = {
    "Chilled Chocolate Fondant": 7.9,
    "Pepermint Crisp Tart": 5.9,
    "Ginger Cobbler": 6.9,
    
}

beers = {
    "Stigel Radler": 6.9,
    "Munich Lager": 7.9,
    "Kong Ludwig Weissbier": 8.9,
    "Warsteiner Punkel": 7.5,
}


# if you want to see the keys of the dictionary in the list: 
# keys = list(starters.keys())
# if you want to see the keys of the dictionary in the list: 
# values = list(starters.values())


maxStarterPrice = (max(list(starters.values())))
maxMainPrice = (max(list(mains.values())))
maxDessertPrice = (max(list(desserts.values())))
maxBeerPrice = (max(list(beers.values())))

maxStarter = list(starters.keys())[list(starters.values()).index(maxStarterPrice)]
maxMain = list(mains.keys())[list(mains.values()).index(maxMainPrice)]
maxDessert = list(desserts.keys())[list(desserts.values()).index(maxDessertPrice)]
maxBeer = list(beers.keys())[list(beers.values()).index(maxBeerPrice)]

meals = {
  maxStarter: maxStarterPrice,
  maxMain: maxMainPrice,
  maxDessert: maxDessertPrice,
  maxBeer: maxBeerPrice
}

tip = sum(list(meals.values())) * 0.1
print (tip)