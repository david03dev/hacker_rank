"""Given an array of integers, where all elements but one occur twice, find the unique element.

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    for i in a:
        count = 0
        for j in a:
            if i ==j:
                count += 1
        if count == 1:
            return i

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
