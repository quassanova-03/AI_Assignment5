class BayesianInference:

    def __init__(self, network):
        self.network = network

    def probability_wet_grass(self):

        p_rain = self.network.p_rain
        p_sprinkler = self.network.p_sprinkler
        cpt = self.network.p_wet_grass

        total = 0

        combinations = [

            (True, True),
            (True, False),
            (False, True),
            (False, False)

        ]

        for rain, sprinkler in combinations:

            p_r = p_rain if rain else (1 - p_rain)
            p_s = p_sprinkler if sprinkler else (1 - p_sprinkler)

            total += cpt[(rain, sprinkler)] * p_r * p_s

        return total

    def probability_rain_given_wet_grass(self):

        p_rain = self.network.p_rain
        p_sprinkler = self.network.p_sprinkler
        cpt = self.network.p_wet_grass

        numerator = 0

        rain_cases = [

            (True, True),
            (True, False)

        ]

        for rain, sprinkler in rain_cases:

            p_s = p_sprinkler if sprinkler else (1 - p_sprinkler)

            numerator += (
                cpt[(rain, sprinkler)]
                * p_rain
                * p_s
            )

        denominator = self.probability_wet_grass()

        return numerator / denominator