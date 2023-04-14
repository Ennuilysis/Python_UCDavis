import csv
import json

class Brain_Baum_node:
    def __init__(self, info: dict, parent):
        self.__id__: int = info["id"]
        self.parent__ = parent
        self.location__ = str = info["name"]
        self.children__: list = info["children"]
        self.__csv_line__: int = Dict_CSV[self.__id__]
        child_list = []
        for s in self.__children__:
            child_list.append(Brain_Baum_node.__init__(s, self))
        self.__children__ = child_list
        self.__class__ = Brain_Baum_node


def Brain_Baum_Start(self, file_seed: str,file_expression):
    Baum_seed = json.load(open(file_seed, "r"))
    Dict_CSV=csv.DictReader(open(file_expression,"r"))
    global  Dict_CSV
    return Brain_Baum_node(Baum_seed["msg"][0], None)


class Brain_Baum_explorer:
    def __init__(self, file_loc):
        self.__top__ = Brain_Baum_Start(file_loc)
        self.__current_pos__: str = self.__top__

    def go_parent(self):

    def go_child(self):

    def go_to_region(self, ):

    def report_transcriptome(self):

    def where_am_I(self):
        print("I am at"+self.__current_pos__.__location__)
        return self.__current_pos__

    def where_can_I_go(self):

    def give_node(self):

    def free_explore(self):
        # no children, has gene expression value, pos1
        # children, gene expression value, pos2
        # no children, no gene expression value, pos3
        # I start at top, then go down via children. Need to use recursion.
        counter = [0, 0, 0]

        def read_Expressionview_meister()


def _test_():
    try:
        Ygdrasil = Brain_Baum_Start("Tester/Brain_Baum_Test_Seed")
    except:
        print("Something went wrong creating Brain Baum. Couldn't initialize.")


_test_()
