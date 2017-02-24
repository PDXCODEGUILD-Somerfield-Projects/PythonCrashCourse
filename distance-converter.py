"""
 Asks user for a distance in units to convert,
 converts the distance and prints the new
 unit conversion for the user.
 """

# dictionary of conversion constants
# multiply by to convert units to meters
# divide by to convert meters to distance unit
conversion_constants = {'mi': 1609.34, 'km': 1000, 'ft': 0.3048,
                     'in': 0.0254, 'cm': 0.01, 'm': 1}

def convert_to_meters(distance, units_to_convert_from):
    """Converts original distance to meters

    Finds the conversion constant in dictionary
    by the units_to_convert_from, multiplies those together
    and returns the converted distance in meters

    :param distance:
    :param units_to_convert_from:
    :return:
    """
    conversion_multiplier = conversion_constants[units_to_convert_from]
    distance_in_meters = conversion_multiplier * distance
    return distance_in_meters



def convert_from_meters(meters_distance, units_to_convert_to):
    """Converts target distance from meters

    Finds the conversion constant in dictionary
    by the units_to_convert_to, divides those units by the constant
    and returns the target distance

    :param meters_distance:
    :param units_to_convert_to:
    :return:
    """
    conversion_divider = conversion_constants[units_to_convert_to]
    target_distance = meters_distance / conversion_divider
    return target_distance


def name_unit_conversion(units):
    """Checks a unit name to make sure its in the conversion_constants dictionary

    ** if the name doesn't fit a recognized format the program exits

    :param units:
    :return:
    """
    if units == 'mi' or units == 'miles':
        unit_conversion = 'mi'
    elif units == 'km' or  units == 'kilometers':
        unit_conversion = 'km'
    elif units == 'ft' or  units == 'feet':
        unit_conversion = 'ft'
    elif units == 'in' or  units == 'inches':
        unit_conversion = 'in'
    elif units == 'cm' or  units == 'centimeters':
        unit_conversion = 'cm'
    elif units == 'm' or  units == 'meters':
        unit_conversion = 'm'
    else:
        print(units + ' is not a recognized unit.')
        exit()
    return unit_conversion



def main():
    """Takes input from user, converts a distance, and outputs conversion to user

    Takes the distance, unit-to-convert-from, and unit-to-convert-to from the user
    checks the unit names for consistancy to use in the conversion_constant dictionary,
    converts the unit-to-convert-from distance to meters, then converts the distance
    into the unit-to-convert-to and outputs the result

    :return:
    """

    # ------ INPUTS FROM USER -----------

    # Get the distance, the units to convert from,
    # and the units to convert to from the user
    orig_dist = float(input("Enter a distance > "))
    orig_unit = input("Enter units (mi, km, m, ft, in, cm) >")
    target_unit = input("Enter target units (mi, km, m, ft, in, cm) >")

    # -------- CONVERSION -----------------

    # checks the name of the units-to-convert-from
    # and changes it to orig_unit_name for consistancy
    orig_unit_name = name_unit_conversion(orig_unit)

    # checks the name of the units-to-convert-to
    # and changes it to target_unit_name for consistancy
    target_unit_name = name_unit_conversion(target_unit)

    # converts the distance to meters
    dist_in_meters = convert_to_meters(orig_dist, orig_unit_name)

    # converts the meters-distance to the distance in units-to-convert-to
    dist_in_target_unit = convert_from_meters(dist_in_meters, target_unit_name)

    # ------- OUTPUT TO USER --------------

    print(str(int(orig_dist)) + ' ' + orig_unit + ' is ' + (str(dist_in_target_unit)) + ' ' + target_unit + '.')


if __name__ == '__main__':
    main()









