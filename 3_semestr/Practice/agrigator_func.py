import math

def matfunc(x):
    print("((math.sin(2)**2)-(-6)*math.cos(x))*((x**2)-15)")
    return(((math.sin(2)**2)-(-6)*math.cos(x))*((x**2)-15))

def input_form():
    text1 = "((math.sin(2)**2)-(-6)*math.cos(x))*((x**2)-15)"
    text1 = text1.replace("math.","")
    return(text1)

