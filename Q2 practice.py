def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return "YES" 
        left_sum += num
    return "NO"
a = [int(x) for x in input("Enter the elements of the array separated by space: ").split()]
print(find_equilibrium_index(a))