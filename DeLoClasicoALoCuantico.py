import numpy as np
def print_hi(name):
    print(f'Hi, {name}')
#Experimento de las canicas
def multi(M,Vn,c):
    while c>=1:
        c -= 1
        Vn = np.matmul(M,Vn)
    return np.array(Vn).tolist()

#Experimento de las rendijas
def rendijas(m,e,c):
    ne = e
    m1 = m
    for i in range(c-1):
        m = np.matmul(m1,m1)
    ne = np.dot(m, e)
    return np.array(ne).tolist()

#Experimento de las rendijas en lo cuántico
def scuantico(m,e,c):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = np.linalg.norm(m[i][j])
    ne = e
    m1 = m
    for i in range(c-1):
        m = np.matmul(m1,m1)
    ne = np.dot(m, e)
    for i in range(len(m)):
        if ne[i] > 1:
            ne[i] = 0
        for j in range(len(m)):
            if m[i][j] > 1:
                m[i][j] = 0
    return np.array(ne).tolist()



if __name__ == '__main__':
    
   print_hi('PyCharm')