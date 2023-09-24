# this is an excercise solution for exercism.org


def is_criticality_balanced(temperature, neutrons_emitted):

    test_1 = False
    test_2 = False
    test_3 = False
    if temperature < 800:
        test_1 = True
    if neutrons_emitted > 500:
        test_2 = True
    mult = neutrons_emitted * temperature
    if mult < 500000:
        test_3 = True
    return test_1 == True and test_2 == True and test_3 == True


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    perc = generated_power/theoretical_max_power*100
    if perc >= 80:
        return "green"
    if perc >= 60:
        return "orange"
    if perc >= 30:
        return "red"
    return "black"



def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    load = temperature * neutrons_produced_per_second
    if load < threshold*90/100:
        return "LOW"
    if load >= threshold*90/100 and load <= threshold*110/100:
        return "NORMAL"
    return "DANGER"
