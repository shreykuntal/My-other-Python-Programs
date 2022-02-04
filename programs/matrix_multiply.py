def mat_mul(M1, M2):
    R = []
    row_M1 = len(M1)
    col_M2 = len(M2[0])
    common = len(M1[0])
    for p in range(row_M1):
        R.append([])
        for q in range(col_M2):
            R[p].append(0)
    for i in range(row_M1):
        for j in range(col_M2):
            for k in range(common):
                R[i][j] += M1[i][k]*M2[k][j]
    return R
M1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
M2 = [[1,2,3,4,10],[5,6,7,8,4],[9,10,11,12,6],[6,7,8,2,1]]
print(mat_mul(M1,M2))