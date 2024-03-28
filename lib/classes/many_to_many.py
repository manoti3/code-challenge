class Customer:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._first_name = name
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._last_name = name

    def reviews(self):
        return [review for review in Review.all if review.customer == self]

    def restaurants(self):
        return list(dict.fromkeys([review.restaurant for review in Review.all if review.customer == self]))

    def num_negative_reviews(self):
        return len([review.rating for review in Review.all if review.customer == self and review.rating <= 2])
        

    def has_reviewed_restaurant(self, restaurant):
        return restaurant in [review.restaurant for review in Review.all if review.customer == self] 
    
class Restaurant:
    all = []

    def __init__(self, name):
        self._name = name
        Restaurant.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 1:
            self._name = name


    def reviews(self):
        return [review for review in Review.all if review.restaurant == self]

    def customers(self):
        return list(dict.fromkeys([review.customer for review in Review.all if review.restaurant == self]))

    def average_star_rating(self):
        ratings = [review.rating for review in Review.all if review.restaurant == self]
        return round(sum(ratings) / len(ratings), 1) if ratings else 0.0

    @classmethod
    def top_two_restaurants(cls):
        restaurant_with_avg_rating = {}
        for restaurant in cls.all:
            ratings = [review.rating for review in Review.all if review.restaurant == restaurant]
            avg_rating = round(sum(ratings) / len(ratings), 1) if ratings else 0.0
            restaurant_with_avg_rating[restaurant] = avg_rating
        sorted_restaurant_with_avg_rating = dict(sorted(restaurant_with_avg_rating.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_restaurant_with_avg_rating.keys())[:2] if Review.all else None

class Review:
    all = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        if isinstance(rating, int) and 1 <= rating <= 5:
            self._rating = rating
        Review.all.append(self)

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        raise AttributeError("can't set attribute")
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value

    @property
    def restaurant(self):
        return self._restaurant
    
    @restaurant.setter
    def restaurant(self, value):
        if isinstance(value, Restaurant):
            self._restaurant = value
