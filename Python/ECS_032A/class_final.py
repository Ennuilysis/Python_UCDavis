# You can add methods to this class if you wish.
# The only thing you cannot do is change the names
# of the member variables.
# The argument could be made that Hero and Object should
# be the same class, but I did not do this because:
#   - In my own solution, I have some additional, different
#     methods in each of these two classes.
#   - I thought it might introduce some unnecessary confusion.
from prog6 import draw_entity

class Hero:
    def __init__(self, symbol, start_x, start_y):
        self.symbol = symbol
        self.x = start_x
        self.y = start_y

    # You don't have to use this if you don't want to.
    def draw_on_board(self, board):
        board[self.y][self.x] = self.symbol

# You can add methods to this class if you wish.
# The only thing you cannot do is change the names
# of the member variables.
class Object: #collectible
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y

    # You don't have to use this if you don't want to.
    def draw_on_board(self, board):
        board[self.y][self.x] = self.symbol

class Building:
    def __init__(self, x, y):
        self.width = 6
        self.height = 4
        self.door_height = 2
        self.door_width = 2
        self.x = x #top_left_x
        self.y = y #top_left-y
        self.ceiling='-'
        self.wall='|'
        self.door='&'
        self.floor='-'

    def draw_on_board(self, board):
        # make a building
        for bleh in range(self.x,self.x+self.width):
            board[self.y][bleh]=self.ceiling #build ceiling
        for bleh in range(self.x,self.x+self.width):
            board[(self.y+self.height-1)][bleh]=self.floor   #build floor
        for s in range(self.y+1,self.y+self.height-1): #dont build wall over ceiling
            board[s][self.x]=self.wall
            board[s][self.x+self.width-1]=self.wall
        for s in (self.y+self.height-self.door_height,self.y+self.height-1):
            for bleh in range(self.x+2,self.x+2+self.door_width):
                board[s][bleh]=self.door

    # Returns True if given the location of this building, the point
    # indicated by (x,y) touches this building in any way.
    def contains(self, x, y):
        part1= x in range(self.x, self.x+self.width)
        part2= y in range(self.y, self.y+self.height)
        if part1==True and part2==True:
            return True
        else:
            return False

# You don't need to use this function, but I found it useful
# when I wanted to inspect the board from the Interpreter /
# after running the program.
def print_board(board):
    for row in board:
        for spot in row:
            print(spot, end='')
        print()

class Game:
    def __init__(self, input_file_name):
        # You can add member variables to this class.
        # However, you cannot change the names of any of
        # the member variables below; the autograder will
        # expect these member variables to have the names
        # that they have.
        file=open(input_file_name,"r")
        self.num_objects = 0
        self.list=file.readlines()
        l=[]
        for x in self.list:
            g=x[:-1]
            g=g.split()
            l+=g
            #['20', '16', 'X', '3', '8', 'w', 'a', 's', 'd', 'o', '$', '8', '14', 'b', '5', '2', 'o', '$', '17', '1']
        for x in l:
            if x=='o':
                self.num_objects+=1
        self.buildings = []
        for x in range(len(l)):
            if l[x]=='b':
                self.buildings+=l[(x+1)]+l[(x+2)]
        self.board = [[' '] * int(l[0]) for i in range(int(l[1]))]
        self.hero = [int(l[14]),int(l[15])]
        self.objects = [(l[10]),int(l[11]),int(l[12])]
        self.down_key = l[7]
        self.up_key = l[5]
        self.right_key = l[8]
        self.left_key = l[6]
        self.read_input_file(input_file_name)
        self.hero.draw_on_board(self.board)
        self.user_quit = False

    def draw_on_board(self, board):
    def read_input_file(self, input_file_name):
        # TODO: Implement.
        pass

    def print_game(self):
        for row in self.board:
            for spot in row:
                print(spot, end='')
            print()

    def game_ended(self):
        return self.all_objects_collected() or self.user_quit

    def all_objects_collected(self):
        return self.num_objects == 0

    def run(self):
        # TODO: Finish the implementation. Implement movement
        # and collision detection. You have much flexibity in
        # how you modify this function. For example, you can
        # remove the definitions and usages of the game_ended()
        # and all_objects_collected() methods if you don't want
        # to use those. (My own implementation uses those methods.)
        quit_cmds = ['q', 'end', 'exit']
        while not self.game_ended():
            self.print_game()
            inp = input("Enter: ")
            if inp in quit_cmds:
                self.user_quit = True
            else:
                print("Invalid command")
        self.print_game()
        if self.user_quit:
            print("You are a quitter!")
        else:
            print("Congratulations: you've collected all of the items!")

#board = [[' '] * 12 for i in  range (10)]
#b1 = Building(2, 1)
#b1.draw_on_board(board)
#print_board(board)
#g=Game("prob4.txt")
# You can have lines like these when you run the program,
# but make sure that they are commented out or removed
# when you submit this file to the autograder.
# g = Game("prob4.txt")
# g.run()