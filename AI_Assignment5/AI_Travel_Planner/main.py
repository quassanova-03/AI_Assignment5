from planner.recommender import TravelRecommender
from planner.itinerary import ItineraryPlanner


def main():

    city = input(
        "Enter destination: "
    )

    interest = input(
        "Interest (Beaches/History/Food): "
    )

    days = int(
        input("Number of days: ")
    )

    budget = input(
        "Budget (Low/Medium/High): "
    )

    recommender = TravelRecommender()

    places, food = recommender.recommend(
        city,
        interest
    )

    planner = ItineraryPlanner()

    plan, cost = planner.create_plan(
        city,
        places,
        food,
        days,
        budget
    )

    print("\nPERSONALIZED TRAVEL PLAN\n")

    for i, activities in enumerate(
        plan,
        start=1
    ):

        print(f"Day {i}")

        for item in activities:
            print("-", item)

        print()

    print(
        f"Estimated Cost: ₹{cost}"
    )


if __name__ == "__main__":
    main()