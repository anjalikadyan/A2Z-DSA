class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == b:
            return 1
        count = 1
        source = a
        while len(source) < len(b):
            count += 1
            source += a
        if source == b:
            return count
        if self.Rabin_Karp(source, b) != -1:
            return count
        if self.Rabin_Karp(source + a, b) != -1:
            return count + 1
        return -1

    def Rabin_Karp(self, source: str, target: str) -> int:
        BASE = 1000000
        if not source or not target:
            return -1
        
        m = len(target)
        power = 1
        for _ in range(m):
            power = (power * 31) % BASE
        
        targetCode = 0
        for ch in target:
            targetCode = (targetCode * 31 + ord(ch)) % BASE
        
        hashCode = 0
        for i in range(len(source)):
            hashCode = (hashCode * 31 + ord(source[i])) % BASE
            if i < m - 1:
                continue
            if i >= m:
                hashCode = (hashCode - ord(source[i - m]) * power) % BASE
            if hashCode < 0:
                hashCode += BASE
            if hashCode == targetCode:
                if source[i - m + 1:i + 1] == target:
                    return i - m + 1
        return -1
if __name__ == "__main__":
    a = input("Enter string A: ")
    b = input("Enter string B: ")
    solution = Solution()
    result = solution.repeatedStringMatch(a, b)
    print("Minimum number of repetitions needed:", result)