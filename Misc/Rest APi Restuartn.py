import requests


def bestRestaurant(city, cost):
    api_url = "https://jsonmock.hackerrank.com/api/food_outlets"
    page = 1
    
    rating = 0
    min_cost = cost
    hotel_name =  ''

    while True:
        response_data = requests.get(f"{api_url}?city={city}&page={page}")
        response = response_data.json()
        for hotel in response['data']:
            if (hotel['user_rating']['average_rating'] > rating and hotel['estimated_cost'] < cost) or (hotel['user_rating']['average_rating'] == rating and hotel['estimated_cost'] < min_cost):
                    min_cost = hotel['estimated_cost']
                    rating = hotel['user_rating']['average_rating']
                    hotel_name = hotel['name']
                

        page+=1
        if page >= response['total_pages']:
            break
    
    return hotel_name
    
print("hotle_name: ", bestRestaurant("Miami", 100))
# print("hotle_name: ", bestRestaurant("Seattle", 120))


response = {
    "page": 1,
    "per_page": 10,
    "total": 400,
    "total_pages": 40,
    "data": [
        {
            "city": "Seattle",
            "name": "Cafe Juanita",
            "estimated_cost": 160,
            "user_rating": {"average_rating": 4.9, "votes": 16203},
            "id": 41,
        },
        {
            "city": "Seattle",
            "name": "Cafe Munir",
            "estimated_cost": 160,
            "user_rating": {"average_rating": 4.9, "votes": 4699},
            "id": 42,
        },
        {
            "city": "Seattle",
            "name": "Flechazo",
            "estimated_cost": 140,
            "user_rating": {"average_rating": 4.8, "votes": 2663},
            "id": 43,
        },
        {
            "city": "Seattle",
            "name": "Vanilla Sky",
            "estimated_cost": 120,
            "user_rating": {"average_rating": 4.6, "votes": 645},
            "id": 44,
        },
        {
            "city": "Seattle",
            "name": "The Shambles",
            "estimated_cost": 110,
            "user_rating": {"average_rating": 4.4, "votes": 2116},
            "id": 45,
        },
        {
            "city": "Seattle",
            "name": "Stories",
            "estimated_cost": 150,
            "user_rating": {"average_rating": 4.5, "votes": 2087},
            "id": 46,
        },
        {
            "city": "Seattle",
            "name": "Big Pitcher",
            "estimated_cost": 180,
            "user_rating": {"average_rating": 4.7, "votes": 9011},
            "id": 47,
        },
        {
            "city": "Seattle",
            "name": "The Black Pearl",
            "estimated_cost": 150,
            "user_rating": {"average_rating": 4.8, "votes": 6976},
            "id": 48,
        },
        {
            "city": "Seattle",
            "name": "Truffles",
            "estimated_cost": 90,
            "user_rating": {"average_rating": 4.7, "votes": 14611},
            "id": 49,
        },
        {
            "city": "Seattle",
            "name": "Biergarten",
            "estimated_cost": 240,
            "user_rating": {"average_rating": 4.7, "votes": 299},
            "id": 410,
        },
    ],
}
