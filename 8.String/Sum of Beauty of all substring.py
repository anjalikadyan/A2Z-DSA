s = "aabcb"
def beautySum(self, s):
        n = len(s)
        total_beauty = 0

        for i in range(n): 
            freq = [0] * 26  
            
            for j in range(i, n): 
                freq[ord(s[j]) - ord('a')] += 1 
                
                max_freq = max(freq)
                min_freq = min(f for f in freq if f > 0) 
                
                total_beauty += (max_freq - min_freq)

        return total_beauty
print(beautySum(s))