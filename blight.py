from __future__ import division, print_function


def combat(living_might, immortal_might, living_units=0, immortal_units=0):
    living_might **= 2
    immortal_might **= 2
    living_wins = True if living_might >= immortal_might else 0
    if living_wins:
        print("Living wins")
        higher, lower = living_might, immortal_might
        survivor_pool = living_units
    else:
        print("Immortal wins")
        higher, lower = immortal_might, living_might
        survivor_pool = immortal_units

    survivality = 1.0 - lower / higher
    print("Survival probability:", survivality)
    print("Expected survivors:", survivor_pool * survivality)


def rcombat(attack_might, defenders_might, defender_units=0):
    survivality = 1.0 - attack_might / defenders_might
    print("Survival probability:", survivality)
    print("Expected survivors:", defender_units * survivality)
