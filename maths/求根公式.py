import math
print("求根公式解一元二次方程")
while True:
    try:
        A = int(input("a=?"))
    except ValueError:
        print("你输入的是数字吗?")
        continue
    try:
        B = int(input("b=?"))
    except ValueError:
        print("你输入的是数字吗?")
        continue
    try:
        C = int(input("c=?"))
    except ValueError:
        print("你输入的是数字吗?")
        continue
    
    DRT = B*B-4*A*C
    """
    if A == 0:
        print("如果a=0,那么这个方程不是一元二次方程")
    """
    if DRT >=0 :
        X1 = (-B + math.sqrt(DRT))/2*A
        X2 = (-B - math.sqrt(DRT))/2*A
        if  X1== X2:
            print("X=",X1)
            print("读法:",-B,"加减根号",DRT,"除以",2*A)
        else:
            print("x1=",X1)
            print("x2=",X2)
            print("读法:",-B,"加减根号",DRT,"除以",2*A)
    elif DRT < 0:
        print("方程无实数根")
    else:
        print("无效")