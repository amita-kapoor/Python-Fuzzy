def trimf(x,a,b,c):
   y=np.max(np.min((x-a)/(b-a), (c-x)/(c-b)),0)
   return y
