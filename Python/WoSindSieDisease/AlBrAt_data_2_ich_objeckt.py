import os, csv, pandas


def Schreiber_csv(file_path: str):
    csv_file = open(file_path, "w", newline="\n")
    return csv.writer(csv_file, delimiter=",")


def Lesset_csv(file_path: str):
    csv_file = open(file_path, "r", newline="\r\n")
    return csv.reader(csv_file)


def Expressioniveau_correct(Name_Krankheit: str) -> None:
    print(Name_Krankheit)
    if os.path.isdir(Name_Krankheit + "/Expressioniveau_meister.csv"):
        return
    else:
        print("Creating Krankheit tables")
    Bekundung_matrix = Lesset_csv(Name_Krankheit + "/Expression.csv")
    probe_matrix = Lesset_csv(Name_Krankheit + "/Probes.csv")
    datei_write = Schreiber_csv(Name_Krankheit + "/Expressioniveau_matrix.csv")
    probe_gene_key = {}
    for probe in probe_matrix:
        probe_gene_key.update({probe[0]: probe[3]})

    for row in Bekundung_matrix:
        row.insert(1,probe_gene_key[row[0]])
        datei_write.writerow(row)


def Mehr_Anatomie(Name_Krankheit: str) -> None:
    anatomie_matrix = Lesset_csv(Name_Krankheit + "/Columns.csv")
    meister = Schreiber_csv(Name_Krankheit + "/Expressioniveau_meister.csv")
    datei_read=Lesset_csv(Name_Krankheit + "/Expressioniveau_matrix.csv")
    anatomie_counter = 1
    def Mehr_Anatomie_part2(anatomie_counter) -> dict:  # time cost center
        file = open(Name_Krankheit + "/Expressioniveau_matrix.csv", "r", newline="\r\n")
        datei_read = csv.reader(file)
        liste_E = {}
        for row_express in datei_read:
            liste_E.update({row_express[0]+","+row_express[1]: row_express[anatomie_counter]})
        file.close()
        return liste_E

    for row_anatomie in anatomie_matrix:
        if row_anatomie[0] == "donor_id":
            row_anatomie.append("Dict")
            row_anatomie.insert("Short_Name_Anatomy")
            meister.writerow(row_anatomie)
            anatomie_counter+=1
            continue  # works
        row_anatomie.append(Mehr_Anatomie_part2(anatomie_counter))
        #print(type(row_anatomie))
        #print(row_anatomie[11])
        row_anatomie.insert(0,row_anatomie[11])
        meister.writerow(row_anatomie)
        anatomie_counter += 1

def test_Express():
    try:
        os.remove("Tester/Expressioniveau_matrix.csv")
    except:
        pass
    folder = "Tester"
    Expressioniveau_correct(folder)

def test_Mehr_Anatomie():
    try:
        os.remove("Tester/Expressioniveau_meister.csv")
    except:
        pass
    folder = "Tester"
    Mehr_Anatomie(folder)

#
test_Express()
test_Mehr_Anatomie()

# with open("Tester/file_name.csv", "w", newline="\n") as file:
#     csv_write = csv.writer(file, delimiter=",")
#     x = [1, 2, 3, 4, 5]
#     y = ["A", "B", "C"]
#     for y_val in y:
#         string_add = []
#         for x_val in x:
#             string_add.append(y_val + str(x_val))
#         csv_write.writerow(string_add)
