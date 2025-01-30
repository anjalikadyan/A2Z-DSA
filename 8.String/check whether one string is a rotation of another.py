
s = "abcde", goal = "cdeab"
def rotateString(self, s, goal):
        n=len(s)
        m=len(goal)
        if n != m:
            return False
        return goal in (s + s)
print(rotateString(s,goal))