import Needleman_Wunsch


test_num = input()
answer = Needleman_Wunsch.advanced_main("test" + test_num + ".txt")
f = open("answer" + test_num + ".txt")
if answer.split() == f.read().split():
    print("correct answer\n", answer, sep='')
else:
    print("incorrect answer")
f.close()
