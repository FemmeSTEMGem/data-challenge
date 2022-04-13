#coding: utf-8

# Day 1: Variables and Numbers in Python¶
# The chilly wetness of the west coast’s winter had descended upon Vancouver, and Dot wasn’t too happy about it. The rain pattered down on the city’s streets all day long, the dark rainclouds obscuring the beautiful view of the Pacific coastline that Dot loved so much. Staring out the window from the home they remotely worked from, Dot began to think that it was time to take a trip. Dot had been saving up their vacation time at work — everything lined up perfectly. They even had a friend who would be eager to watch over their pet snake, Python. The more they thought about it, the more appealing the idea seemed. It was time for Dot to take a courageous leap and go international…to Europe and beyond!

# Dot opened a browser on their laptop and started looking into flights. Their savings account wasn’t bottomless, and the trip would be expensive, so they had to make sure to do things efficiently. Plus, the intercontinental flight would be very long, and Dot got restless on planes — they wanted to book a flight that would give them the best value per hour of flight duration. Dot wanted to fly to Europe from the Canadian city that would give them the best combination of value/duration. Dot could manually browse through all the available flights to compare them, but they knew there was a better way to do things — we can use data skills to map out the flights for them and decide from which city they should fly out.

# Challenge
# Dot wants to find a connection to Europe that will give them the best value per hour of travel time. The following tickets are available for the connection:

# Vancouver - Toronto: 250 CAD, travel time 3.5 hours
# Vancouver - Ottawa: 280 CAD, travel time 4 hours
# Vancouver - Montreal: 240 CAD, travel time 4 hours
# Vancouver - Edmonton: 150 CAD, travel time 1.5 hours
# Vancouver - Calgary: 180 CAD, travel time 1 hour
# These tickets are available for the second leg of the trip:

# Ottawa - Berlin: 1350 CAD, layover: 3.5 hours, travel time 9 hours
# Montreal - London: 1300 CAD, layover: 2 hours, travel time 8 hours
# Edmonton - London: 1200 CAD, layover: 5 hours, travel time 10 hours
# Calgary - London: 1400 CAD, layover: 2.5 hours, travel time 10 hours
# Toronto - Munich: 990 CAD, layover: 1.5 hours, travel time 9.5 hours
# Using math operators in Python, find out which flight will give Dot the best value per hour of travel time.

# value = price_paid / travel_time

van_tor_price = 250
van_ott_price = 280
van_mon_price = 240
van_edm_price = 150
van_cal_price = 180

van_tor_travel_time = 3.5
van_ott_travel_time = 4
van_mon_travel_time = 4
van_edm_travel_time = 1.5
van_cal_travel_time = 1

ott_ber_price = 1350
mon_lon_price = 1300
edm_lon_price = 1290
cal_lon_price = 1400
tor_mun_price = 990

ott_layover = 3.5
mon_layover = 2
edm_layover = 5
cal_layover = 2.5
tor_layover = 1.5

ott_ber_travel_time = 9
mon_lon_travel_time = 8
edm_lon_travel_time = 10
cal_lon_travel_time = 10
tor_mun_travel_time = 9.5

van_tor_value = (van_tor_price + tor_mun_price) / (van_tor_travel_time + tor_layover + tor_mun_travel_time)
van_ott_value = (van_ott_price + ott_ber_price) / (van_ott_travel_time + ott_layover + ott_ber_travel_time)
van_mon_value = (van_mon_price + mon_lon_price) / (van_mon_travel_time + mon_layover + mon_lon_travel_time)
van_edm_value = (van_edm_price + edm_lon_price) / (van_edm_travel_time + edm_layover + edm_lon_travel_time)
van_cal_value = (van_cal_price + cal_lon_price) / (van_cal_travel_time + cal_layover + cal_lon_travel_time)

print ("Vancouver --> Toronto --> Munich: ", int(round(van_tor_value)))
print ("Vancouver --> Ottawa --> Berlin: ", int(round(van_ott_value)))
print ("Vancouver --> Montreal --> London: ", int(round(van_mon_value)))
print ("Vancouver --> Edmonton --> London: ", int(round(van_edm_value)))
print ("Vancouver --> Calgary --> London: ", int(round(van_cal_value)))