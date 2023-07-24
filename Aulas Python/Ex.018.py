import math
n=float(input("Digite um angulo "))
r=math.radians(n)
sin=math.sin(r)
cos=math.cos(r)
tan=math.tan(r)
print("O seno de {} é {:.2f}, o cosseno de {} é {:.2f} e a tangente de {} é {:.2f}".format(n,sin,n,cos,n,tan))
