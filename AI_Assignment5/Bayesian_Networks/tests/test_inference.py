from bayes.network import BayesianNetwork
from bayes.inference import BayesianInference


def test_probability_wet_grass():

    network = BayesianNetwork()

    inference = BayesianInference(
        network
    )

    result = inference.probability_wet_grass()

    assert 0 <= result <= 1


def test_probability_rain_given_wet_grass():

    network = BayesianNetwork()

    inference = BayesianInference(
        network
    )

    result = (
        inference.probability_rain_given_wet_grass()
    )

    assert 0 <= result <= 1