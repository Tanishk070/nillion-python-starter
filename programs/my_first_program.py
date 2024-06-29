from nada_dsl import *
import math

def nada_main():
    party1 = Party(name="Party1")
    radius = SecretInteger(Input(name="radius", party=party1))

    # Compute the area of the circle using the radius
    area = math.pi * (radius ** 2)

    # Define the output based on the computed area
    return [Output(area, "circle_area", party1)]
