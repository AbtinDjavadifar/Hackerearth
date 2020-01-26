flag = True

while flag:
    try:
        inp = list(map(lambda x: int(x), input().split()))
        print(inp[0] + inp[1])
    except EOFError:
        flag = False