def floodFill(image, sr, sc, color):
        de=image[sr][sc]
        if de==color:
            return image
        m=len(image)
        n=len(image[0])
        def img(x,y):
            if (0 <= x < m) and (0 <= y < n) and image[x][y] == de:
                image[x][y]=color
                img(x+1,y)
                img(x-1,y)
                img(x,y+1)
                img(x,y-1)
        img(sr,sc)
        return image
image=[]
for i in range(len(image)):
    for j in range(len(image[0])):
        image[i][j]=int(input("Enter the value of array: "))
color=int(input("Enter the color: "))
sr=int(input("Enter the starting row: "))
sc=int(input("Enter the starting row1: "))
print(floodFill(image,sr,sc,color))