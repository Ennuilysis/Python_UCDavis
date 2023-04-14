from typing import List
class Donor(object):
    """
    Maybe it would be a good idea to a make a simple donor class
    """
    def __init__(self,list_string:List[str]):
        self.donor_name=list_string[0]
        self.donor_val=int(list_string[1])
    def __str__(self):
        return f"{self.donor_name}  with a donation of {self.donor_val}"

