def need_wun(string1, string2, mat_e, d):
    # creating a matrix
    mat = []
    for j in range(len(string2) + 1):
        mat.append([0 for i in range(len(string1) + 1)])
    # filling the matrix
    for i in range(len(string1) + 1):
        for j in range(len(string2) + 1):
            if i == 0 or j == 0:
                mat[i][j] = (i+j) * d
            else:
                match = mat[i-1][j-1] + int(mat_e[(string1[i-1], string2[j-1])])
                delete = mat[i-1][j] + d
                insert = mat[i][j-1] + d
                mat[i][j] = max(match, insert, delete)
    # finding the answer
    ans1 = ""
    ans2 = ""
    i = len(string1)
    j = len(string2)
    while i > 0 or j > 0:
        score = mat[i][j]
        score_diag = mat[i-1][j-1]
        score_up = mat[i][j-1]
        score_left = mat[i-1][j]
        if score == score_diag + int(mat_e[(string1[i-1], string2[j-1])]):
            ans1 = string1[i-1] + ans1
            ans2 = string2[j-1] + ans2
            i -= 1
            j -= 1
        elif score == score_up + d:
            ans1 = '-' + ans1
            ans2 = string2[j-1] + ans2
            j -= 1
        elif score == score_left + d:
            ans1 = string1[i-1] + ans1
            ans2 = '-' + ans2
            i -= 1
    while i > 0:
        ans1 = string1[i-1] + ans1
        ans2 = '-' + ans2
        i -= 1
    while j > 0:
        ans1 = '-' + ans1
        ans2 = string2[j-1] + ans2
        j -= 1
    return ans1 + '\n' + ans2


def advanced_main(file_name):
    f = open(file_name)
    lines = []
    for line in f:
        lines.append(line[0:-1])
    f.close()
    strings = []
    symbols = []
    mat_equivalent = {}
    d = 0
    # reading the lines
    for i in range(len(lines)):
        # reading the strings
        if i < 2:
            strings.append(lines[i])
        # creating a dict, key == pair(sym1, sym2), value == similarity
        elif i == 2:
            symbols = lines[i].split()
            for j in range(len(symbols)):
                for k in range(len(symbols)):
                    mat_equivalent[(symbols[i], symbols[j])] = 0
        # filling the dict
        elif i < len(lines) - 1:
            line = lines[i].split()
            now_symbol = line[0]
            for j in range(len(symbols)):
                mat_equivalent[(now_symbol, symbols[j])] = line[j+1]
        # assigning a forfeit
        else:
            d = int(lines[i])
    return need_wun(strings[0], strings[1], mat_equivalent, d)


def main(string1, string2):
    mat_equivalent = {}
    d = -1
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                mat_equivalent[(string1[i], string2[j])] = 1
            else:
                mat_equivalent[(string1[i], string2[j])] = -1
                mat_equivalent[(string2[j], string1[i])] = -1
    print(need_wun(string1, string2, mat_equivalent, d))


string1 = "DADCCDDACAADEDCCEECB"
string2 = "DDEDDDCDCCEAECEEBCEA"
main(string1, string2)
