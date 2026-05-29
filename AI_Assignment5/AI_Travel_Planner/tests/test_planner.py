from planner.recommender import TravelRecommender


def test_goa():

    rec = TravelRecommender()

    places, food = rec.recommend(
        "Goa",
        "Beaches"
    )

    assert len(places) > 0