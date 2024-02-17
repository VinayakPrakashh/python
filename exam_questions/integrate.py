from scipy.integrate import quad

def model(t):
    return 4*(t**3)+2*t+3
x = quad(model,0,2)
print(x)