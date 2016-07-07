from __future__ import division, print_function
from math import floor

# Might to valour ratio
VALOUR_DIVIDER = 100.0


def combat(living_might, immortal_might, living_units=0, immortal_units=0):
    living_adjusted_might **= 2
    immortal_adjusted_might **= 2
    living_wins = True if living_adjusted_might > immortal_adjusted_might else 0
    if living_wins:
        print("Living wins")
        survivality = 1.0 - immortal_adjusted_might / living_adjusted_might
        survivors = living_units * survivality
        valour = immortal_might / VALOUR_DIVIDER
    else:
        print("Immortal wins")
        survivality = 1.0 - living_adjusted_might / immortal_adjusted_might
        survivors = immortal_units * survivality
        might_per_unit = immortal_might / immortal_units
        valour = (immortal_units - survivors) * might_per_unit / VALOUR_DIVIDER

    print("Survival probability:", survivality)
    print("Expected survivors:", survivors)
    print("Expected valour:", floor(valour))


def rcombat(attack_might, defenders_might, defender_units=0):
    survivality = 1.0 - attack_might / defenders_might
    survivors = defender_units * survivality
    might_per_unit = defenders_might / defender_units
    valour = (defender_units - survivors) * might_per_unit / VALOUR_DIVIDER
    print("Survival probability:", survivality)
    print("Expected survivors:", survivors)
    print("Expected valour:", floor(valour))
