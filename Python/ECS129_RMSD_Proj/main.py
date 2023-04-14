import sys
from src import functions
def main() -> None:
    """
    Run the program
    :return:
    """
    # x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # r = functions.find_r(x, y)
    # print(r)
    # f = functions.construct_f(r)
    # print(f)
    # eigen = np.linalg.eig(f)
    # lambda_max = max(eigen[0])
    # print(lambda_max)
    model_file = sys.argv[1]
    target_file = sys.argv[2]
    RMSDScore = functions.calculate_RMSD(model_file, target_file)
    print(f'The RMSDScore for your protein is:', RMSDScore)

    target_file = sys.argv[1]
    model_file = sys.argv[2]
    RMSDScore = functions.calculate_RMSD(target_file, model_file)
    control_score = functions.bio_python_control_run(target_file, model_file)
    print(f'The RMSDScore based on our code for your protein is:', RMSDScore)
    print(f'Our code vs biopython:', control_score-RMSDScore)


if __name__ == '__main__':
    main()
