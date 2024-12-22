"""
Evaluating Resistors

"""


def color_code(color):
    """
    Returns the associated value of each color band.

    """
    colors = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    for index, c in enumerate(colors):
        if c == color:
            return index


def value(colors):
    """
    Calculates the resistance value of a resistor
    with two bands based on its color bands

    """
    if len(colors) > 1:
        return int(str(color_code(colors[0])) + str(color_code((colors[1]))))
    else:
        return int(str(color_code(colors[0])))


def label(colors):
    """
    Calculates the resistance value of a resistor based on its color bands.

    The third color band represents a multiplier in powers of ten.
    This function applies metric scale labels (ohms, kiloohms, megaohms, gigaohms)
    to the computed resistance value based on the multiplier.
    """
    if len(colors) > 1:
        # Calculate the base resistance value
        base = int("".join(str(color_code(color)) for color in colors[:-1]))
        base *= 10 ** color_code(colors[-1])

        # Determine the appropriate metric scale and format the output
        if base >= 1000000000:
            val = base / 1000000000
            unit = " gigaohms"
        elif base >= 1000000:
            val = base / 1000000
            unit = " megaohms"
        elif base >= 1000:
            val = base / 1000
            unit = " kiloohms"
        else:
            val = base
            unit = " ohms"

        # Convert to int if there's no decimal value, otherwise keep as float
        if val % 1 == 0:  # Check if value is an integer
            val = int(val)
        return f"{val}{unit}"
    else:
        # Single color case
        base = color_code(colors[0])
        return f"{base} ohms"


def tolerance(color):
    tolerance_values = {
        "Grey": "±0.05%",
        "Violet": "±0.1%",
        "Blue": "±0.25%",
        "Green": "±0.5%",
        "Brown": "±1%",
        "Red": "±2%",
        "Gold": "±5%",
        "Silver": "±10%",
    }
    return tolerance_values.get(color.title(), "Invalid color")


def resistor_label(colors):
    """
    Final form

    """
    if len(colors) == 1:
        return label(colors)
    else:
        return label(colors[:-1]) + " " + tolerance(colors[-1])