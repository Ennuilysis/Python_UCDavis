import numpy as np
from typing import Any, List
import math
from Bio.PDB import PDBParser, Superimposer, QCPSuperimposer


def bio_python_control_run(target_file: str, model_file: str ) -> np.number:
    t_file = open(target_file)
    m_file = open(model_file)
    RMSD_impose = QCPSuperimposer.QCPSuperimposer()
    RMSD_transform = Superimposer()
    PDB_P = PDBParser()
    target = PDB_P.get_structure("target", t_file)
    model = PDB_P.get_structure("model", m_file)
    target_atoms = list(target.get_atoms())
    target_CA = []
    for a in target_atoms.keys:
        if target_atoms(a).get_id()=="CA":
            target_CA += a
    model_CA = []
    model_atoms = list(model.get_atoms())
    for a in model_atoms.keys:
        if model_atoms(a).get_id() =="CA":
            model_CA += a
    RMSD_transform.set_atoms(target_CA, model_CA)
    RMSD_transform.apply(model_CA)
    RMSD_impose.set(target_CA, model_CA)
    RMSD_impose.run()
    return RMSD_impose.rms()

def find_lambda_max(model: Any, target: Any) -> Any:
    R = find_r(model, target)
    F = construct_f(R)
    eigen = np.linalg.eig(F)
    lambda_max = max(eigen[0])
    return lambda_max


def calculate_RMSD(modelfilename: str, targetfilename: str, type=None) -> Any:
    # need to figure out what is x^2
    model = readPDBfile(modelfilename)
    target = readPDBfile(targetfilename, type)

    modelmatrix = weightmatrix(model[3])
    targetmatrix = weightmatrix(target[3])

    lambda_max = find_lambda_max(modelmatrix, targetmatrix)
    return RMSDformula(modelmatrix, targetmatrix, lambda_max)


def weightmatrix(matrix: Any) -> [Any]:  # matrix has to be array
    sum = np.zeros(shape=(1, 3))
    for k in range(len(matrix)):
        sum = np.add(sum, matrix[k])
    return matrix - sum / len(matrix)


def RMSDformula(model: Any, target: Any, lambda_max: Any) -> Any:
    sum = 0

    for k in range(len(model)):
        sum += np.linalg.norm(model[k]) ** 2 + np.linalg.norm(target[k]) ** 2

    e = math.sqrt(abs((sum - 2 * lambda_max) / len(model)))

    return e


def find_r(model: Any, target: Any) -> List:  # (matrix: X(3 x k), matrix: Y(3 x k) -> matrix(3 X 3)
    # by linear algebra, matrix A(m by n) times matrix B(m by n), the resulting matrix will have size
    # as m by n. (easy: take the m from A and n from B)
    # X = [[1,3,4],...,[1,3,4]] # Ask linear algebra professor which way to do it can be faster
    trans_y: Any = np.transpose(target)  # function to transpose matrix Y

    # make an empty R matrix
    R = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    # for each R, R11 = sum of the multiplications of the x of X and x of Y for each k

    # for loop
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(len(model)):  # may vary depends on what format X will be
                R[i][j] += model[k][i] * trans_y[j][k]
    return R


def construct_f(R: Any) -> List:
    F: List = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

    for i in range(4):
        for j in range(4):
            if i == 0:
                if j == 0:
                    F[i][j] = R[0][0] + R[1][1] + R[2][2]
                elif j == 1:
                    F[i][j] = R[1][2] - R[2][1]
                elif j == 2:
                    F[i][j] = R[2][0] - R[0][2]
                elif j == 3:
                    F[i][j] = R[0][1] - R[1][0]
            elif i == 1:
                if j == 1:
                    F[i][j] = R[0][0] - R[1][1] - R[2][2]
                elif j == 2:
                    F[i][j] = R[0][1] + R[1][0]
                elif j == 3:
                    F[i][j] = R[0][2] + R[2][0]
                else:
                    F[i][j] = F[j][i]
            elif i == 2:
                if j == 2:
                    F[i][j] = -R[0][0] + R[1][1] - R[2][2]
                elif j == 3:
                    F[i][j] = R[1][2] + R[2][1]
                else:
                    F[i][j] = F[j][i]
            elif i == 3:
                if j == 3:
                    F[i][j] = -R[0][0] - R[1][1] + R[2][2]
                else:
                    F[i][j] = F[j][i]

    return F


# from website https://wwwx.cs.unc.edu/Courses/comp116-s16/A4.html#:~:text=Read%20PDB%20files.&text=Write%20a%20function%20readPDBfile(filename,serial%20number%20for%20each%20atom.
def readPDBfile(filename, type=None) -> List:
    '''read a PDB file, extract the ATOM lines, and return
       atom number, atom name, residue number, and coords for each'''
    # build them up in lists because they are cheap to append

    id = []
    element = []
    residue = []
    coords = []
    sequenceid = []
    aminum = []

    # your work goes here. You should read the ATOM lines and append the appropriate
    # fields to the lists anum, aname, resno, and coords
    # from website https://stackoverflow.com/questions/10324674/parsing-a-pdb-file-in-python

    for line in open(filename):
        list = line.split()
        if list[0] == "ATOM":
            if list[4] == type:
                if list[2] == "CA":
                    id.append(list[0])
                    element.append(list[2])
                    residue.append(list[3])
                    sequenceid.append(list[4])
                    if list[5] not in aminum: aminum.append(list[5])
                    coords.append([float(list[6]), float(list[7]), float(list[8])])
            else:
                if list[2] == "CA":
                    id.append(list[0])
                    element.append(list[2])
                    residue.append(list[3])
                    sequenceid.append(list[4])
                    if list[5] not in aminum: aminum.append(list[5])
                    coords.append([float(list[6]), float(list[7]), float(list[8])])

    # print(aminum)
    # print(residue)
    id = np.array(id)
    element = np.array(element)
    residue = np.array(residue)
    coords = np.array(coords)

    # return the 4 results
    return (id, element, residue, coords)
