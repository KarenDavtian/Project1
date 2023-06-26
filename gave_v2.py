state = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def print_state(state):
    print("  0 1 2")
    for i in range(len(state)):
        row = state[i]
        print(str(i) + " " + " ".join(row))

def analyze_status(state, symbol):
    for i in range(3):
        if all(cell == symbol for cell in state[i]):
            return True
        if all(state[j][i] == symbol for j in range(3)):
            return True


    if state[0][0] == state[1][1] == state[2][2] == symbol:
        return True
    if state[0][2] == state[1][1] == state[2][0] == symbol:
        return True

    return False

# Makes move if cell is not busy and returns True. If cell is busy returns False.
def make_move_if_possible(i, j, player):
    if state[i][j] != '-':
        print("Клетка уже занята. Сделайте другой ход.")
        return False

    state[i][j] = player
    return True

def read_move():
    move = input('Делай ход (формат:x y):')
    move = move.split()

    if len(move) != 2:
        print('Формат введенных данных неверен. Корректный формат:x y')
        return None
    
    if not all(value.isdigit() for value in move):
        print('Значения координат хода не целочисленные')
        return None

    move = list(map(int, move))
    if not all(value >=0 and value < 3 for value in move):
        print ('Значения координат должны находиться в диапазоне от 0 до 2.')
        return None
        
    return move

player = 'x'

while True:
    print_state(state)
    move = read_move()
    if not move:
        continue

    move_made = make_move_if_possible(*move, player)
    if not move_made:
        continue

    if analyze_status(state, player):
        print_state(state)
        print("Игрок", player, "победил!")
        break
    elif all(state[i][j] != '-' for i in range(3) for j in range(3)):
        print_state(state)
        print("Ничья!")
        break

    player = 'o' if player == 'x' else 'x'