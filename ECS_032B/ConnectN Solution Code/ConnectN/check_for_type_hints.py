from typing import Iterable
import argparse
import subprocess
import sys

try:
    from mypy import api as mypy_api
except ModuleNotFoundError:
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'mypy'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError as err:
        print(err.stderr)
        exit(2)
    from mypy import api as mypy_api


def main():
    locations = ['BoardPrinter']  # files and directories to search
    # additional options to my py
    options = ['--disallow-untyped-defs', '--disallow-incomplete-defs', '--check-untyped-defs']
    mistakes_to_forgive = 5
    penalty_per_mistake = 5  # percent
    score = score_type_hints(locations, options, mistakes_to_forgive, penalty_per_mistake)
    mimir.set_score(score)


def score_type_hints(locations: Iterable[str], options: Iterable[str], num_mistakes_to_forgive: int,
                     mistake_penalty: float):
    mypy_args = list(locations) + list(options)
    output, errors, exit_code = mypy_api.run(mypy_args)

    score = 100

    if errors:
        print('Mypy could not finish parsing your submission due to the following errors')
        print(errors)
        if output:
            print('Here are the issues mypy was able to locate before it found an error')
            print(output)
        score = 0
    elif output and exit_code != 0:  # some mistakes were made
        lines = output.split('\n')
        num_mistakes = int(lines[-2].split()[1])
        score = score - max(num_mistakes - num_mistakes_to_forgive, 0) * mistake_penalty

        print(f'Mypy found {num_mistakes} problems with your submission.')
        print(f'Each mistakes is {mistake_penalty}% but we ignore your first {num_mistakes_to_forgive} mistakes')
        print(f'This leaves you with a score of {score}/100')
        print(f'Here are the mistakes mypy found\n{output}')
    elif exit_code == 0:
        print('Nice Job. No Errors Found')

    return score


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('locations',
                        nargs='+',
                        help='The paths to the files and directories for mypy to analyse')
    parser.add_argument('-m', '--mypy_args',
                        nargs='+',
                        default=['disallow-untyped-defs', 'disallow-incomplete-defs'],
                        help='The additional command line arguments to pass to mypy without the leading --')

    parser.add_argument('-p', '--penalty',
                        type=float,
                        default=5,
                        help='The percent penatly to apply for each mistake. 15 would mean 15%')
    parser.add_argument('-f', '--forgive',
                        type=int,
                        default=5,
                        help='How many problems reported by mypy to ignore before applying penalties')
    return parser


if __name__ == '__main__':
    main()
