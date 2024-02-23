# Link to Challenge : https://edabit.com/challenge/mm2fm6ynbR7HQQm9z

pos_x = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
pos_y = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}


def get_pos_x(index):
    return pos_x.get(pos_y.get(index, -1), None)


def knights_jump(pos):
    maybe_pos = [["", 9, 9], ["", 9, 9], ["", 9, 9], ["", 9, 9]]
    x_coordinate = pos_x[pos[0]]
    y_coordinate = int(pos[1])

    maybe_pos[0][0] = pos_y.get(x_coordinate - 2, None)
    maybe_pos[1][0] = pos_y.get(x_coordinate - 1, None)
    maybe_pos[2][0] = pos_y.get(x_coordinate + 1, None)
    maybe_pos[3][0] = pos_y.get(x_coordinate + 2, None)

    minus_plus=0
    for i in range(4):
        if i == 0 or i == 3:
            minus_plus = 1
        elif i == 1 or i == 2:
            minus_plus = 2
        if not maybe_pos[i][0] == None:
            maybe_pos[i][1] = get_pos_x(y_coordinate + minus_plus)
            maybe_pos[i][2] = get_pos_x(y_coordinate - minus_plus)

    coordinates = ""
    for y_points in range(9):
        for i in range(4):
            for number_index in range(2):
                if maybe_pos[i][number_index + 1] == y_points:
                    coordinates += maybe_pos[i][0] + str(maybe_pos[i][number_index + 1]) + ", "
    coordinates = coordinates[0:coordinates.__len__() - 2]
    print(coordinates)


knights_jump("D3")  # 'C1,E1,B2,F2,B4,F4,C5,E5'
knights_jump('A1')  # 'C2,B3'
knights_jump('H1')  # 'F2,G3'
knights_jump('F4')  # 'E2,G2,D3,H3,D5,H5,E6,G6'
knights_jump('E5')  # 'D3,F3,C4,G4,C6,G6,D7,F7'
knights_jump('A7')  # 'B5,C6,C8'
knights_jump('B4')  # 'A2,C2,D3,D5,A6,C6'
knights_jump('F3')  # 'E1,G1,D2,H2,D4,H4,E5,G5'
knights_jump('C8')  # 'B6,D6,A7,E7'
knights_jump('E4')  # 'D2,F2,C3,G3,C5,G5,D6,F6'
knights_jump('G1')  # 'E2,F3,H3'
knights_jump('G7')  # 'F5,H5,E6,E8'
knights_jump('F3')  # 'E1,G1,D2,H2,D4,H4,E5,G5'
knights_jump('C8')  # 'B6,D6,A7,E7'
knights_jump('B6')  # 'A4,C4,D5,D7,A8,C8'
knights_jump('E2')  # 'C1,G1,C3,G3,D4,F4'
knights_jump('H5')  # 'G3,F4,F6,G7'
knights_jump('D1')  # 'B2,F2,C3,E3'
knights_jump('G1')  # 'E2,F3,H3'
