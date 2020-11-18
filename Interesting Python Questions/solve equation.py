def f(x):
    return ((2*(x**4))+(3*(x**3))-(6*(x**2))+(5*x)-8)

def reachEnd(previousm,currentm):
    if abs(previousm - currentm) <= 10**(-6):
        return True
    return False

def printFormat(a,b,c,m,count):
    print("Step %s" %count)
    print("a=%.6f b=%.6f c=%.6f" %(a,b,c))
    print("f(a)=%.6f f(b)=%.6f f(c)=%.6f" %(f(a),f(b),f(c)))
    print("m=%.6f f(m)=%.6f" %(m,f(m)))

def main(a,b,c):
    if (not (a < b and c < b)) or (not(f(a) > f(c) and f(b) > f(c))):
        return False
    count = 0
    previousm = b+1
    while True:
        if (b - c) >= (c - a):
            m = (b+c)/2
            if f(m) >= f(c):
                b = m
            else:
                a = c
                c = m
        else:
            m = (a+c)/2
            if f(m) >= f(c):
                a = m
            else:
                b = c
                c = m
        printFormat(a,b,c,m,count)
        if reachEnd(previousm,m):
            print("Minimum value=%.6f occurring at %.6f" %(f(m),m))
            break
        previousm = m
        count += 1

main(-3,-1,-2.2)
