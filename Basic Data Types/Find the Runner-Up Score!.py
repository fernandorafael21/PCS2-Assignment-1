if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    no_repetitions = list(dict.fromkeys(arr))
    no_repetitions.sort()
    print(no_repetitions[-2])

print("fernando!")
