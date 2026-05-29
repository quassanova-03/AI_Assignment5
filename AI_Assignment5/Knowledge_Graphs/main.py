from kg.sample_data import create_graph


def main():

    kg = create_graph()

    print("=" * 50)
    print("KNOWLEDGE GRAPH DEMONSTRATION")
    print("=" * 50)

    kg.display()

    print("\nQuery Example")
    print("-" * 50)

    subject = input(
        "\nEnter Subject: "
    )

    predicate = input(
        "Enter Predicate: "
    )

    results = kg.query(
        subject=subject,
        predicate=predicate
    )

    print("\nResults:\n")

    if not results:
        print("No matching facts found.")

    else:

        for s, p, o in results:
            print(
                f"{s} --{p}--> {o}"
            )


if __name__ == "__main__":
    main()