#coding: utf-8
# Day 5: Control Structures: for loops and if statements¶
# After spending some time in Munich, Dot moved on to their next destination: London, the capital of the United Kingdom. When they arrived, the first thing they did was settle in at a tea room over a steaming cup of English Breakfast. Then, as they let the soothing beverage warm them and the caffeine perk them up, Dot started to think about what they wanted to visit in London. The clock tower with Big Ben, London Bridge, the Natural History Museum…the possibilities were endless and a bit overwhelming.

# Dot overheard some other tourists talking about their day at the table next to them. “I’m telling you, we must have waited a good 45 minutes just to be able to see the structure!” a man exclaimed to his partner. Wait times are something Dot didn’t think about — Dot hated waiting, even to see something magnificent and historical. Actually, waiting in line was Dot’s number one fear, coincidentally. If they waited in line for more than 15 minutes, they might have an emotional meltdown and become psychologically disconnected from the world around them, which wouldn’t bode well for their invigorating, joyful vacation. So let’s help Dot sidestep their #1 fear by using data to guide them towards only landmarks with a waiting time of fewer than fifteen minutes.


landmarks = {
    "Big Ben": 12,
    "Tower Bridge": 25,
    "Buckingham Palace": 15,
    "Madame Tussauds": 25,
    "London Eye": 40,
    "Tower of London": 25,
    "Emirates Air Line cable car": 16,
    "London Transport Museum": 7,
    "Wembley Stadium": 8,
    "Hyde Park": 0,
    "The View from The Shard": 14
}

array = []

for k in landmarks:
  if landmarks[k] < 15:
    array.append(k)

print array, len(array)