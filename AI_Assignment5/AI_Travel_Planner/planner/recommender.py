from knowledge_base.places import PLACES
from knowledge_base.food import FOOD


class TravelRecommender:

    def recommend(self, city, interest):

        places = PLACES[city].get(
            interest,
            []
        )

        food = FOOD.get(city, [])

        return places, food