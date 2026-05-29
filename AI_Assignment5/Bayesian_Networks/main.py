from bayes.network import BayesianNetwork
from bayes.inference import BayesianInference


def main():

    network = BayesianNetwork()

    inference = BayesianInference(network)

    print("=" * 55)
    print("         BAYESIAN NETWORK DEMONSTRATION")
    print("=" * 55)

    network.display_network()

    print("\nEvidence Entered:")
    print("Wet Grass = True")


    probability = (
        inference.probability_rain_given_wet_grass()
    )

    print("\nInference Result :")

    print(
        f"Probability of Rain given Wet Grass = "
        f"{probability:.4f}"
    )

    print("\nInterpretation:")
    print(
        f"If we observe that the grass is wet, "
        f"there is a {probability * 100:.2f}% "
        f"chance that it rained."
    )
    print("\nInference Completed Successfully")


if __name__ == "__main__":
    main()