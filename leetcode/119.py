class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
 
        triangles = []
        for i in range(rowIndex + 1):
            triangles.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    triangles[i].append(1)
                else:
                    triangles[i].append(triangles[i - 1][j - 1] + triangles[i - 1][j])

        return triangles[rowIndex]