from knowledge_base.budgets import BUDGETS


class ItineraryPlanner:

    def create_plan(
        self,
        city,
        places,
        food,
        days,
        budget
    ):

        plan = []

        place_index = 0

        for day in range(days):

            activities = []

            if place_index < len(places):
                activities.append(
                    places[place_index]
                )
                place_index += 1

            if food:
                activities.append(
                    f"Try {food[day % len(food)]}"
                )

            plan.append(activities)

        estimated_cost = (
            BUDGETS[budget] * days
        )

        return plan, estimated_cost