def trimf(x,a,b,c):
   y=np.max(np.min((x-a)/(b-a), (c-x)/(c-b)),0)
   return y

def trapmf(x,a,b,c,d):
   y=np.max(np.min((x-a)/(b-a), 1, (d-x)/(d-c)),0)
   return y
