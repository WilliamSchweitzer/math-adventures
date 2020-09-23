# for loop, for test cases 't'
for x in range(int(input())):
    # take 'n' as input 't' times
    n = int(input())
    # the result will always be n+1, because
    # there must always be 1 extra item to ensure
    # there are enough items to match all pairs.
    print(str(n+1))
