import subprocess
from typing import List


def main():
    min_score = 8
    locations = ['ConnectNGame', 'main.py']
    get_pylint_rating(locations, min_score)


def get_pylint_rating(locations: List[str], min_score: float = 8) -> None:
    rating = 0
    try:
        result = subprocess.run(['pylint', '--rcfile=.pylintrc'] + locations, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
                                universal_newlines=True)
        print(f'Nice job, pylint did not find any issues with your submission.')
        rating = 10
    except subprocess.CalledProcessError as error:
        fatal_error = 1
        usage_error = 32
        if error.returncode & (fatal_error | usage_error):
            print(f'pylint failed to run on {locations} due to\n{error.stderr}')
            print(f'plyint was able to find these issues before failing\n{error.stdout}')
        else:
            lines = error.stdout.split('\n')
            for line in reversed(lines):
                if line.startswith('Your code has been rated at'):
                    rating = line.split()[6]
                    rating = float(rating.split('/')[0])
                    break
            else:
                print('Error could not find a rating for this assignment')
            print(f'pylint found the following issues with your submission\n{error.stdout}')

    if rating >= min_score:
        rating = 10
    rating *= 10  # convert to percent
    # mimir.set_score(rating)


if __name__ == '__main__':
    main()