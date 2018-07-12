############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        return self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    yellow_watermel = MelonType("yw", 2013, "yellow", False, True, 
    							"Yellow Watermelon")

    # add known pairings to melon(s)
    muskmelon.add_pairing("mint")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    crenshaw.add_pairing("proscuitto")
    yellow_watermel.add_pairing("ice cream")

	# put MelonType objects in list
    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermel]

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
    	print("{} pairs with".format(melon.name))
    	for pair in melon.pairings:
    		print("- {}".format(pair))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {}

    for melon in melon_types:
    	melon_codes[melon.code] = melon

    return melon_codes

# print(make_melon_type_lookup(make_melon_types()))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):

    	self.melon_type = melon_type
    	self.shape_rating = shape_rating
    	self.color_rating = color_rating
    	self.harvested_from = harvested_from
    	self.harvested_by = harvested_by

    def is_sellable(self):

    	if self.shape_rating > 5 and self.color_rating > 5:
    		return True
    	else:
    		return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_lookup = make_melon_type_lookup(melon_types)

    # make a bunch of Melon objects
    melon_1 = Melon(melon_lookup["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melon_lookup["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melon_lookup["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melon_lookup["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melon_lookup["cren"], 8 ,9, 35, "Michael")
    melon_6 = Melon(melon_lookup["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melon_lookup["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melon_lookup["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melon_lookup["yw"], 7, 10, 3, "Sheila")

    return [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, 
    		 melon_8, melon_9]




def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


# list of MelonType objects
melon_types = make_melon_types()

print(make_melons(melon_types))
