class BayesianNetwork:

    def __init__(self):

        # Prior probabilities

        self.p_rain = 0.2
        self.p_sprinkler = 0.5

        # Conditional Probability Table

        self.p_wet_grass = {

            (True, True): 0.99,
            (True, False): 0.90,
            (False, True): 0.80,
            (False, False): 0.00

        }

    def display_network(self):

        print("\nNetwork Structure:\n")

        print("Rain ------\\")
        print("             ---> Wet Grass")
        print("Sprinkler --/")