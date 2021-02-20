# Uses BFS to determine the best solution to the missionaries and cannibals game

class GameState:
    def __init__(self, ml = 0, cl = 0, mr = 3, cr = 3, b = 'r'):
        self.ml = ml
        self.cl = cl
        self.mr = mr
        self.cr = cr
        self.b = b

    def is_goal(self):
        return self.mr == 0 and self.cr == 0 #There are no missionaries or cannibals on the right side

    def is_legal(self):
        return (self.mr + self.ml == 3) and (self.cr + self.cl == 3) and (self.ml >= 0) and (self.mr >= 0) and (self.cl >= 0) and (self.cr >= 0)

    def is_dead(self):
        return (self.cr > self.mr and self.mr > 0) or (self.cl > self.ml and self.ml > 0)

    def __eq__(self, other):
        return self.ml == other.ml and self.cl == other.cl and self.mr == other.mr and self.cr == other.cr and self.b == other.b
    
    def create_children(self):
        children = []

        if self.b == 'r':
            child1 = GameState(self.ml + 2, self.cl, self.mr - 2, self.cr, 'l')
            child2 = GameState(self.ml + 1, self.cl, self.mr - 1, self.cr, 'l')
            child3 = GameState(self.ml + 1, self.cl + 1, self.mr - 1, self.cr - 1, 'l')
            child4 = GameState(self.ml, self.cl + 1, self.mr, self.cr - 1, 'l')
            child5 = GameState(self.ml, self.cl + 2, self.mr, self.cr - 2, 'l')

            if child1.is_legal() and not child1.is_dead():
                children.append(child1)

            if child2.is_legal() and not child2.is_dead():
                children.append(child2)

            if child3.is_legal() and not child3.is_dead():
                children.append(child3)

            if child4.is_legal() and not child4.is_dead():
                children.append(child4)

            if child5.is_legal() and not child5.is_dead():
                children.append(child5)
        else:
            child1 = GameState(self.ml - 2, self.cl, self.mr + 2, self.cr, 'r')
            child2 = GameState(self.ml - 1, self.cl, self.mr + 1, self.cr, 'r')
            child3 = GameState(self.ml - 1, self.cl - 1, self.mr + 1, self.cr + 1, 'r')
            child4 = GameState(self.ml, self.cl - 1, self.mr, self.cr + 1, 'r')
            child5 = GameState(self.ml, self.cl - 2, self.mr, self.cr + 2, 'l')

            if child1.is_legal() and not child1.is_dead():
                children.append(child1)
            if child2.is_legal() and not child2.is_dead():
                children.append(child2)
            if child3.is_legal() and not child3.is_dead():
                children.append(child3)
            if child4.is_legal() and not child4.is_dead():
                children.append(child4)
            if child5.is_legal() and not child5.is_dead():
                children.append(child5)
        
        return children

class StateNode:
    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent
    
    def print_path(self):
        if self.parent != None:
            self.parent.print_path()
        else:
            print("Starting Game")
        print(f"Left: {self.state.ml} missionaries, {self.state.cl} cannibals. Right: {self.state.mr} missionaries, {self.state.cr} cannibals. Boat: {self.state.b}")

def is_visited(visited, state):
    for i in visited:
        if i == state:
            return True
    return False

def play_game(start):
    frontier = []
    visited = []

    start_node = StateNode(start)
    frontier.append(start_node)

    while True:
        if len(frontier) == 0:
            return None

        state_node = frontier.pop(0)

        visited.append(state_node.state)
        children = state_node.state.create_children()

        for child in children:
            if not is_visited(visited, child):
                child_node = StateNode(child, state_node)

                if child_node.state.is_goal():
                    return child_node

                frontier.append(child_node)

def main():
    start = GameState()
    end = play_game(start)
    if end == None:
        print('Failed.')
    else:
        end.print_path()

if __name__ == "__main__":
    main()


    
