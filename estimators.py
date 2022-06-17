def newton(z, f, df):
    a = f(z)
    b = df(z)
    return z - a / b

def halley(z, f, df, ddf):
    a = f(z)
    b = df(z)
    c = ddf(z)
    return z - (2*a*b) / (2*b**2 - a*c)

def steffensen(z, f):
    a = f(z)
    return z - a / (f(z+a) / a - 1)