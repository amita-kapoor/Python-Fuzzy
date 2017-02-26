import time
import webbrowser

max_breaks=10
time_in_min=60
time_in_sec=time_in_min*60
count=0
while (count < max_breaks):
    time.sleep(time_in_sec)
    webbrowser.open("https://www.youtube.com/watch?v=HRkNfdlm5Qs")
    count=count+1