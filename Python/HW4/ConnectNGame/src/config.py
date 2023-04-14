from typing import List


class Config:
    def __init__(self, path_to_config_file: str) -> None:
        with open(path_to_config_file) as file:
            for line in file:
                line: List[str] = line.split(":")  # type: ignore
                key, value = line
                key: str = key.strip()
                value: str = value.strip()
                if key == "num_rows":
                    self.num_rows: int = int(value)
                if key == "num_cols":
                    self.num_columns: int = int(value)
                if key == "blank_char":
                    self.blank_character: str = value
                if key == 'num_pieces_to_win':
                    self.num_pieces_to_win: int = int(value)
