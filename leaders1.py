def find_leaders(A):
    leaders = []
    max_element = A[-1]
    leaders.append(max_element)
    for i in range(len(A) - 2, -1, -1):
        if A[i] > max_element:
            leaders.append(A[i])
            max_element = A[i]
    leaders.reverse()
    return leaders
