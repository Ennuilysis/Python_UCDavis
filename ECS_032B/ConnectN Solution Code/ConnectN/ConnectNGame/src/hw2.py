from typing import List, Set, Generator, Union
class Item(object):
    def __init__(self, name: str, weight: int, value: int) -> None:
        self.name = name
        self.weight = weight
        self.value = value

    def __lt__(self, other: "Item"):
        if self.value == other.value:
            if self.weight == other.weight:
                return self.name < other.name
            else:
                return self.weight < other.weight
        else:
            return self.value < other.value

    def __eq__(self, other: "Item") -> bool:
        if isinstance(other, Item):
            return (self.name == other.name and
                    self.value == other.value and
                    self.weight == other.weight)
        else:
            return False

    def __ne__(self, other: "Item") -> bool:
        return not (self == other)

    def __str__(self) -> str:
        return f'A {self.name} worth {self.value} that weighs {self.weight}'

def get_best_backpack(items: List[Item], max_capacity: int) -> List[Item]:
    max_val = 0
    best_backpack = []

    def wt_check(answer) -> bool:
        bag_weight = sum([x.weight for x in answer])

        return bag_weight <= max_capacity

    def return_all_but(mylist: List, x: int):
        """returns a new list of the original except the selected index, without mutating the orignal"""
        return mylist[:x] + mylist[x + 1:]

    def _combo_generator(Units: Union[List[Item], None], answer: Union[List[Item], List[None]] = []) -> Generator[
        Set[Item], None, None]:
        """"Yield Valid Bags, where the weight of the bag is always below the maximum holding of the bag. Other wise """
        if Units == [] and wt_check(answer):
            answer_val = sum([t.value for t in x])
            if answer_val > max_val:
                max_val = answer_val
                best_backpack = answer
        elif wt_check(answer):
            answer_val = sum([t.value for t in x])
            if answer_val > max_val:
                max_val = answer_val
                best_backpack = answer
            for pos, val in enumerate(Units):
                new_units = return_all_but(Units, pos)
                new_answer = answer + [val]
                yield from _combo_generator(new_units, new_answer)

    # Cant handle duplicates
    list_of_sets = list(_combo_generator(Units=items, answer=[]))

    # Ok. assuming lists_of_sets has all the permutations
    max_val = 0
    best_bag = []
    for x in list_of_sets:
        x_val = sum([t.value for t in x])
        if x_val > max_val:
            max_val = x_val
            best_bag = x
    return best_bag
import unittest


class TestBestBackpack(unittest.TestCase):
    def test_best_backpack_with_no_items(self):
        items = []
        self.assertEqual(items, get_best_backpack(items, 20))

    def test_best_backpack_with_one_item_that_fits(self):
        items = [Item('Ring', 10, 500)]
        self.assertEqual(items, get_best_backpack(items, 20))

    def test_best_backpack_with_items_that_will_not_fit(self):
        items = [Item('Ring', 10, 500),
                 Item('Diamond', 25, 2),
                 Item('Necklace', 68, 10000)]
        self.assertEqual([items[0]], get_best_backpack(items, 20))

    def test_best_backpack_first_2_will_fit(self):
        items = [Item('Ring', 10, 500),
                 Item('Diamond', 25, 2),
                 Item('Necklace', 68, 10000)]
        self.assertEqual([items[0],items[1]], get_best_backpack(items, 35))

    def test_best_backpack_only_big_item_best(self):
        items = [Item('Ring', 43, 43),
                 Item('Earring', 36, 30),
                 Item('Necklace', 80, 100),
                 Item('Diamond', 70, 68)]
        self.assertEqual([items[2]], get_best_backpack(items, 80))

    def test_best_backpack_avg_case(self):
        items = [Item('Ring', 43, 43),
                 Item('Earring', 36, 40),
                 Item('Necklace', 80, 80),
                 Item('Diamond', 70, 68)]
        self.assertEqual([items[0],items[1]], get_best_backpack(items, 90))

if __name__ == '__main__':
    unittest.main()
