# Fake news Headline Generator

import random as rd

names = ["Shah Rukh Khan", "Aamir Khan", "Salman Khan", "Ranbir Kapoor", "Hrithik Roshan", "Ranveer Singh", "Akshay Kumar", "Ajay Devgn", "Varun Dhawan", "Siddharth Malhotra", "Deepika Padukone", "Katrina Kaif", "Alia Bhatt", "Priyanka Chopra", "Kareena Kapoor", "Anushka Sharma", "Kangana Ranaut", "Rani Mukerji", "Kajol", "Madhuri Dixit", "Narendra Modi", "Rahul Gandhi", "Amit Shah", "Sonia Gandhi", "Manmohan Singh", "Arvind Kejriwal", "Mamata Banerjee", "Nitin Gadkari", "Yogi Adityanath", "Sharad Pawar", "Pranab Mukherjee", "L. K. Advani", "P. Chidambaram", "Sushma Swaraj", "Digvijaya Singh",  "Jyotiraditya Scindia", "Mayawati", "K. Chandrashekar Rao"
         ]


verbs = ["run", "jump", "speak", "eat", "sleep", "write", "read", "walk",
         "listen", "play", "study", "think", "create", "build", "drive", "sing"]

places = ["India Gate", "Taj Mahal", "Jaipur", "Goa", "Kerala",
          "Varanasi", "Leh-Ladakh", "Mysore", "Rishikesh", "Amritsar", "Udaipur"]

prepositions = ["in", "on", "at", "by", "with", "about", "against", "between", "under",
                "over", "through", "during", "before", "after", "to", "from", "up", "down", "off", "over"]

adverbs = ["quickly", "slowly", "well", "very", "never", "always", "here", "there", "now", "then",
           "quietly", "easily", "badly", "almost", "too", "enough", "just", "loudly", "happily", "daily"]

interjections = ["oh", "wow", "ouch", "hey", "hurray",
                 "alas", "oops", "bravo", "ah", "yuck", "hey", "ugh"]

dates = ["today", "yesterday", "last night",
         "this morning", "on Monday", "on Independence Day"]

organizations = ["CBI", "Income Tax Department", "BJP", "Congress", "NASA"]

events = ["Oscars", "IPL final", "Parliament session",
          "Film launch", "Press conference"]

adjectives = [
    "amazing", "astonishing", "baffling", "beautiful", "bizarre",
    "breathtaking", "brilliant", "colossal", "controversial", "courageous",
    "creative", "critical", "curious", "daring", "dazzling", "devious",
    "dramatic", "dynamic", "electrifying", "enormous", "epic", "exceptional",
    "extraordinary", "fabulous", "fantastic", "flamboyant", "frightening",
    "groundbreaking", "heroic", "hilarious", "historic", "incredible",
    "ingenious", "innovative", "intense", "jaw-dropping", "legendary",
    "magical", "massive", "miraculous", "mysterious", "outrageous",
    "overwhelming", "peculiar", "phenomenal", "powerful", "provocative",
    "puzzling", "rare", "remarkable", "revolutionary", "scandalous",
    "shocking", "spectacular", "spine-tingling", "staggering", "startling",
    "strange", "stunning", "surprising", "unbelievable", "unprecedented",
    "unusual", "visionary", "weird", "wild", "wondrous"
]

objects = [
    "movie", "policy", "event", "product", "festival", "scandal", "conference",
    "meeting", "technology", "strategy", "initiative", "campaign", "project",
    "celebration", "contract", "agreement", "show", "series", "documentary",
    "speech", "report", "announcement", "launch", "merger", "acquisition",
    "exhibition", "debate", "invention", "device", "competition", "experiment",
    "bill", "statement", "publication", "trend", "protest", "demonstration",
    "app", "partnership", "venture", "award", "summit", "mission", "challenge",
    "platform", "solution", "reform", "movement", "alliance"
]


templates = [
    "{interj}! {name} {verb} {adj} {obj} at {place} {date}",
    "In {place}, {name} {verb} {obj} {date}",
    "{adj_title}! {name} {verb} {obj} {date} at {place}"
    "{name} and {org} {verb} {adj} {event} in {place} {date}",
    "{name} says '{interj}! I will {verb} the {obj} {date} at {place}'",
    "Why did {name} {verb} {obj} {date}? {adj_title} reasons revealed!",
    "{interj}! {name} spotted {adv} {verb} at {place} during {event}",
    "{name} {verb}s {obj} with {org} in {place}, {date}",
    "{place} witnesses {adj} {event} as {name} {verb}s",
    "{event} turns {adj} as {name} {verb}s {obj} {date}",
    "{name} {verb}s {adj} {obj} at {place} with {org} {date}",
    "{interj}! {name} {verb}s {event} at {place}, shocks {org}",
    "{name} to {verb} {adj} {obj} in {place} says {adv} {date}",
    "{adj_title}! {event} in {place} as {name} and {org} {verb} together {date}",
    "{interj}! {org} invites {name} to {verb} {obj} at {place} {date}"

]


def generate_headline():
    data = {
        "name": rd.choice(names),
        "verb": rd.choice(verbs),
        "place": rd.choice(places),
        "prep": rd.choice(prepositions),
        "adv": rd.choice(adverbs),
        "interj": rd.choice(interjections).title(),
        "date": rd.choice(dates),
        "org": rd.choice(organizations),
        "event": rd.choice(events),
        "adj": rd.choice(adjectives),
        "adj_title": rd.choice(adjectives).title(),
        "obj": rd.choice(objects)
    }
    template = rd.choice(templates)
    return template.format(**data)


while True:
    print("=" * 40)
    print("Do you want to spread fake news??")
    z = input('yes/no :').strip().lower()
    if z in ['yes', 'y', 'ye']:
        headline = generate_headline()
        print(f'Breaking News: {headline}')
    else:
        print('Thank you')
        break
