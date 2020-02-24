# string 타입의 복소수의 두수의 연산을 입력받아
# 서로 곱하고 출력을 다시 string으로 하시요
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# 설명: (1 - i) * (1 - i) = 1 - i - i + i^2 = -2i,

def complexNumberMultiply(a, b):
    aa = a.split("+")
    bb = aa[1].split("i")
    aaa = aa[0]
    bbb =bb[0]
    cc = b.split("+")
    dd = cc[1].split("i")
    ccc = cc[0]
    ddd =dd[0]
    a=int(aaa)
    b=int(bbb)
    c=int(ccc)
    d=int(ddd)
    f = (a*c)-(b*d)
    g = (b*c)+(a*d)
    answer =  str(f)+"+"+str(g)+"i"
    return answer
