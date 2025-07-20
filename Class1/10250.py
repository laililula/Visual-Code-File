for _ in range(int(input())):
    h, w, n = map(int, input().split())
    print(f"{n % h}{(n // h)+1:02d}") if n%h != 0 else print(f"{h}{(n // h):02d}")