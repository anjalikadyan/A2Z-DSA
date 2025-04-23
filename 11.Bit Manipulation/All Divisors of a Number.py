def all_divisors(n):
    divisors = set()
    i = 1
    while (i * i) <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    return sorted(divisors)

num = 36
print(f"All divisors of {num} are:", all_divisors(num))
