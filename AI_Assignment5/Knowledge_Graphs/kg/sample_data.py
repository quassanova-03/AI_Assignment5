from kg.graph import KnowledgeGraph


def create_graph():

    kg = KnowledgeGraph()

    kg.add_fact(
        "Goa",
        "hasBeach",
        "Baga Beach"
    )

    kg.add_fact(
        "Goa",
        "hasFood",
        "Fish Curry Rice"
    )

    kg.add_fact(
        "Goa",
        "locatedIn",
        "India"
    )

    kg.add_fact(
        "India",
        "hasCapital",
        "New Delhi"
    )

    kg.add_fact(
        "Jaipur",
        "hasFort",
        "Amber Fort"
    )

    kg.add_fact(
        "Jaipur",
        "locatedIn",
        "India"
    )

    return kg