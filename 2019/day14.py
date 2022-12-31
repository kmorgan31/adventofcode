#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "157 ORE => 5 NZVS",
    "165 ORE => 6 DCFZ",
    "44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL",
    "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ",
    "179 ORE => 7 PSHF",
    "177 ORE => 5 HKGWZ",
    "7 DCFZ, 7 PSHF => 2 XJWVT",
    "165 ORE => 2 GPVTF",
    "3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT",
]


class Output:

    def __init__(self, name, qty, cost):
        self.name = name
        self.qty = qty      # quantity produced
        self.cost = cost    # cost to create qty


class Factory:

    def __init__(self, data):
        self.get_reactions(data)
        self.inventory = {k: 0 for k in self.reactions}

    def get_reactions(self, data):

        def split_materials(lst):
            return {
                y: int(x) for x, y in map(lambda x: x.split(), lst.split(", "))
            }

        self.reactions = {}
        for line in data:
            inp, out = [split_materials(x) for x in line.split(" => ")]

            oname, oqty = list(out.items())[0]
            self.reactions[oname] = Output(oname, oqty, inp)


def main(data, part=None):

    factory = Factory(data)
    factory.inventory["ORE"] = 0
    factory.inventory["FUEL"] = -1

    while not all(v > -1 for k, v in factory.inventory.items() if k != "ORE"):
        for k, v in factory.inventory.items():
            if k == "ORE":
                continue

            if v < 0:
                # create some of the ingredient
                ingredients = factory.reactions[k].cost
                for ingredient, qty in ingredients.items():
                    # find the corresponding ingredient in the inventory and reduce
                    factory.inventory[ingredient] -= qty

                # increase the inventory item by the qty created
                factory.inventory[k] += factory.reactions[k].qty

    fuel_cost = -factory.inventory["ORE"]
    if part == 1:
        return fuel_cost

    # update "FUEL" and "ORE"
    fuel_inventory = factory.inventory.copy()
    fuel_inventory["ORE"] = 0
    fuel_inventory["FUEL"] = 0

    fuel_created = 0
    total_ore = 1000000000000
    while total_ore >= fuel_cost:
        # CREATE FUEL
        fuel = total_ore // fuel_cost
        total_ore -= (fuel_cost * fuel)

        # update created fuel
        fuel_created += fuel
        print(f'Fuel Created: {fuel_created}')

        # update inventory according to the fuel created
        for k in factory.inventory:
            if k in ["ORE", "FUEL"]:
                continue
            factory.inventory[k] += fuel_inventory[k] * fuel

        # BREAK UP UNUSED INVENTORY
        break_up = True
        while break_up:
            break_up = False
            for k, v in factory.inventory.items():
                if k in ["ORE", "FUEL"]:
                    continue

                mul = v // factory.reactions[k].qty
                if mul == 0:
                    continue

                else:
                    break_up = True
                    # reduce qty of current item
                    factory.inventory[k] -= factory.reactions[k].qty * mul

                    # increase qty of ingredients
                    for i, j in factory.reactions[k].cost.items():
                        if i == "ORE":
                            total_ore += mul * j
                        else:
                            factory.inventory[i] += mul * j

    return fuel_created


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
