MOD = 10**9 + 7

def countGoodDigitStrings(n: int) -> int:
    even_digits = [0, 2, 4, 6, 8]  
    prime_digits = [2, 3, 5, 7]    
    
    even_count = len(even_digits)
    prime_count = len(prime_digits)
    
    even_positions = (n + 1) // 2 
    odd_positions = n // 2      
    
    result = pow(even_count, even_positions, MOD) * pow(prime_count, odd_positions, MOD) % MOD
    
    return result

n = 4
print(countGoodDigitStrings(n))  
