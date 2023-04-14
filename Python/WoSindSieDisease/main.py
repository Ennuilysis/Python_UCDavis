# This is a sample Python script.
#This package is open source and allowed for editing.
import os, csv, json
from AlBrAt_data_2_ich_objeckt import Expressioniveau_correct, Mehr_Anatomie, Lesset_csv, Schreiber_csv
#import Brain_Baum_Nodes
def fun_get_files(dev: str,Krakheit: str)->str:
    files=os.listdir(os.getcwd())
    for i in files:
        file_end=i[-5:-1]+i[-1]
        words=i.split("_")
        if file_end==".json" and words[0]==dev:
            Brain_Baum_seed=i
        elif words[0]==dev and Krakheit in words:
            working_folder=i
    return working_folder,Brain_Baum_seed

# Brain Baum is now a "tree" dictionary. It has a hierachy of anatomy.
Liste_Krakheit = ["Patient", "Autism", "Schizophrenia"]


def datei_2_ich_objeckt(folder_name, tree_select) -> None:
    if not os.access("/" + folder_name + "/Expressioniveau_meister.csv", os.F_OK):
        Expressioniveau_correct(folder_name)
        Mehr_Anatomie(folder_name)
    print("Drei. Files are ready for processing, and building brain network.")
    return build_brain(tree_select)

# def build_brain(tree_select:str):
#     Ygdrasil=Brain_Baum_Start(tree_select)
#     Sigmun_Jahn=Brain_Baum_Explorer()


def start_function() -> None:
    Liste_Krakheit = ["Patient", "Autism", "Schizophrenia"]
    no_disease = True
    while no_disease:
        search_input = int(input("Eins. Wilkommen Herr Gerrik. Wo Sind Sie Krankenheits? Wie heist sind? Wie buchstabiert los?\n" \
                        "0 " + Liste_Krakheit[0] + " 1 " + Liste_Krakheit[1] + " 2 " + Liste_Krakheit[2] + "\n"))
        try:
            dev_choice: int =int(input(f'Zwei. Danke. Wie shall hunt {Liste_Krakheit[search_input]}. But which range? 0 Developing, or 1 Postnatal?\n'))
            ages=["dev","postnatal"]
            Kreikhat,dev=fun_get_files(ages[dev_choice],Liste_Krakheit[search_input])
            no_disease=False
        except:
            print("Falsche Wahl, Dummkpoff")
    if search_input == "0":
        return print("no files")
    return datei_2_ich_objeckt(Kreikhat,dev)

start_function()
# Save the following shit.
# with open("file_name.csv", "w", newline="\n") as file:
#     csv_write = csv.writer(file, delimiter=",")
#     x = [1, 2, 3, 4, 5]
#     y = ["A", "B", "C"]
#     string_add = []
#     list_number = 0
#     for y_val in y:
#         # string_add.append([])
#         # list_number=list_number+1
#         for x_val in x:
#             string_add.append(y_val + str(x_val))
#         csv_write.writerow(string_add)

    # a csv is written as
    # |1,2,3,4|
    # |5,6|,|7,8|
    # ect.
    # The "," is a delimiter.
    # qoutechar is whats used to surround the rows/fields that hold delimiters.
