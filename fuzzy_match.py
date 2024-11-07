from thefuzz import fuzz

questions = ['Provide total cost to serve the German market in 2023.',
        'Provide commentary on how these costs have evolved compared to 2022?',
        'What are the drivers of increase in transport costs?',
        'What are the drivers of increase in secondary transport costs?',
        'What are the levers using which the average pallets per trip can be controlled / improved.',
        'Explore reduction of SLA of top 40 customers and generate scenarios to identify cost savings.',
        'Explore reduction of SLA of top 20 customers and generate scenarios to identify cost savings.',
        'Specify cost savings for Customer ID Dir_239',
        'Specify cost savings for Customer ID Dir_121']

ques = [x.lower() for x in questions]

def check_closest_match(inputt):
    ratings = []
    for que in ques:
        ratings.append(fuzz.ratio(inputt.lower(), que))
    print(max(ratings))
    if max(ratings)>=30:
        maxx = ratings.index(max(ratings))
        
        return ques[maxx]
    else:
        return 'Null'


