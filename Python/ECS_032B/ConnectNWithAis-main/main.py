from ConnectNGame.src.game import Game
from ConnectNGame.src.config import Config
import sys, random


def main() -> None:
    try:
        random.seed(int(sys.argv[2]))
    except IndexError:
        pass
    game_config = Config(sys.argv[1])
    connect_n = Game(game_config)
    Game.play(connect_n)


if __name__ == '__main__':
    main()
