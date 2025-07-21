num_gcd = list(map(int, input().split()))
num_lcm = num_gcd[0]*num_gcd[1]
while True:
    num_gcd[0], num_gcd[1] = num_gcd[1], num_gcd[0] % num_gcd[1]
    if num_gcd[1] == 0:
        print(num_gcd[0]) # gcd = num_gcd[0]
        break
print(num_lcm//num_gcd[0])