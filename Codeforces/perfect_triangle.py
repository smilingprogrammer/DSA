t = int(input())

for i in range(t):

    num_angles = int(input())

    # for j in range(num_angles):
    angles = list(map(int, input().split()))

    angles.sort()
    times = float('inf')

    for i in range(num_angles - 2):
        # for j in range(i + 1, num_angles):
        #     for k in range(j+1, num_angles):
        cost = angles[i + 2] - angles[i]
        times = min(times, cost)
        
        # print(angles)

    print(times)