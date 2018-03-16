############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        #mututate self.pairings attribute, add items to list
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, "Muskmelon")
    cas = MelonType('cas', 2003, 'orange', False, False, "Casaba")
    cren = MelonType('cren', 1996, 'green', False, False, "Crenshaw")
    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")

    musk.add_pairing("mint")
    cas.add_pairing("strawberry")
    cas.add_pairing("mint")
    cren.add_pairing("proscuitto")
    yw.add_pairing("ice cream")

    all_melon_types.append(musk)
    all_melon_types.append(cas)
    all_melon_types.append(cren)
    all_melon_types.append(yw)

    return all_melon_types    # list of melon objects


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print "{} pairs with".format(melon.name)
        for pairing in melon.pairings:
            print "- {}".format(pairing)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    #take in MelonType object LIST
    #return dictionary: KEYS--reporting codes as strings, VALUES--objects
    all_melons = {}
    for melon in melon_types:
        all_melons[melon.code] = melon
    return all_melons

melon_types = make_melon_types()    # list of melon objects
print_pairing_info(melon_types)
melons_by_id = make_melon_type_lookup(melon_types)    # dict of melon type by code

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_field = harvested_field
        self.harvester = harvester

    def is_sellable(self):
        return (self.shape_rating > 5 and self.color_rating > 5 and self.harvested_field != 3)


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    harvested_melons = []

    melons_by_id = make_melon_type_lookup(melon_types)
    
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    harvested_melons.append(melon_1)
    harvested_melons.append(melon_2)
    harvested_melons.append(melon_3)
    harvested_melons.append(melon_4)
    harvested_melons.append(melon_5)
    harvested_melons.append(melon_6)
    harvested_melons.append(melon_7)
    harvested_melons.append(melon_8)
    harvested_melons.append(melon_9)

    return harvested_melons    # list of melon objects that were harvested


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() is True:
            sellable = "CAN BE SOLD"
        else:
            sellable = "NOT SELLABLE"
        print "Harvested by {} from Field # {} {}".format(melon.harvester, melon.harvested_field, sellable)


melons = make_melons(melon_types)
get_sellability_report(melons)
