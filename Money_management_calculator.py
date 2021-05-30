import tkinter
from data import *

root = tkinter.Tk()
root.title("Money Management Calculator")
root.geometry("1125x500")

#fungsi


def combine_fungsi(*funcs):
    def combined_fungsi(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_fungsi


def risk_trade():
    global modal
    modal = int(input_1.get())
    global risk1
    risk1 = modal * 2/100
    global risk_1_a
    risk_1_a = tkinter.Label(root, text=rupiah.rupiah(risk1), width=20, height=1, bg="DodgerBlue2", relief="groove")
    risk_1_a.grid(row=1, column=7)

    global risk2
    risk2 = modal * 15/10/100
    global risk_2_a
    risk_2_a = tkinter.Label(root, text=rupiah.rupiah(risk2), width=20, height=1, bg="DodgerBlue2", relief="groove")
    risk_2_a.grid(row=2, column=7)

    global risk3
    risk3 = modal * 1/100
    global risk_3_a
    risk_3_a = tkinter.Label(root, text=rupiah.rupiah(risk3), width=20, height=1, bg="DodgerBlue2", relief="groove")
    risk_3_a.grid(row=3, column=7)

def risk():
    global buy
    buy = int(input_2.get())
    global stop
    stop = int(input_3.get())
    global risk_x_a
    global risk_x_b
    risk_x_a = buy - stop
    risk_x_b = risk_x_a / buy * 100
    global risk_x_c
    risk_x_c = tkinter.Label(root, text=risk_x_a, width=7, height=1, bg="white", relief="groove")
    risk_x_c.grid(row=7, column=6)
    global risk_x_d
    risk_x_d = tkinter.Label(root, text=koma.koma(risk_x_b)+"%", width=20, height=1, bg="white", relief="groove")
    risk_x_d.grid(row=7, column=7)

def reward():
    target_1 = int(input_4.get())
    if target_1 > buy:
        reward_1_a = target_1 - buy
        global reward_1_b
        reward_1_b = reward_1_a / buy * 100
        global reward_1_c
        reward_1_c = tkinter.Label(root, text=rupiah.rupiah(reward_1_a), width=7, height=1, bg="white", relief="groove")
        reward_1_c.grid(row=9, column=6)
        global reward_1_d
        reward_1_d = tkinter.Label(root, text=koma.koma(reward_1_b)+"%", width=20, height=1, bg="green", fg="white", relief="groove")
        reward_1_d.grid(row=9, column=7)
    else:
        reward_1_b = 0
        reward_1_c = tkinter.Label(root, text="Target <  Buy!", width=20, height=1, bg="green", fg="white", relief="groove")
        reward_1_c.grid(row=9, column=7)

    target_2 = int(input_5.get())
    if target_2 > buy:
        reward_2_a = target_2 - buy
        global reward_2_b
        reward_2_b = reward_2_a / buy * 100
        global reward_2_c
        reward_2_c = tkinter.Label(root, text=rupiah.rupiah(reward_2_a), width=7, height=1, bg="white", relief="groove")
        reward_2_c.grid(row=10, column=6)
        global reward_2_d
        reward_2_d = tkinter.Label(root, text=koma.koma(reward_2_b)+"%", width=20, height=1, bg="green", fg="white", relief="groove")
        reward_2_d.grid(row=10, column=7)
    else:        
        reward_2_b = 0
        reward_2_c = tkinter.Label(root, text="Target <  Buy!", width=20, height=1, bg="green", fg="white", relief="groove")
        reward_2_c.grid(row=10, column=7)

    target_3 = int(input_6.get())
    if target_3 > buy:
        reward_3_a = target_3 - buy
        global reward_3_b
        reward_3_b = reward_3_a / buy * 100
        global reward_3_c
        reward_3_c = tkinter.Label(root, text=rupiah.rupiah(reward_3_a), width=7, height=1, bg="white", relief="groove")
        reward_3_c.grid(row=11, column=6)
        global reward_3_d
        reward_3_d = tkinter.Label(root, text=koma.koma(reward_3_b)+"%", width=20, height=1, bg="green", fg="white", relief="groove")
        reward_3_d.grid(row=11, column=7)
    else:        
        reward_3_b = 0
        reward_3_c = tkinter.Label(root, text="Target <  Buy!", width=20, height=1, bg="green", fg="white", relief="groove")
        reward_3_c.grid(row=11, column=7)

def risk_reward():
    global risk_reward1
    risk_reward1 = reward_1_b / risk_x_b
    global risk_reward_1
    risk_reward_1 = tkinter.Label(root, text=koma.koma(risk_reward1), width=10, height=1, bg="green", fg="white", relief="groove")
    risk_reward_1.grid(row=9, column=10)

    global risk_reward2
    risk_reward2 = reward_2_b / risk_x_b
    global risk_reward_2
    risk_reward_2 = tkinter.Label(root, text=koma.koma(risk_reward2), width=10, height=1, bg="green", fg="white", relief="groove")
    risk_reward_2.grid(row=10, column=10)

    global risk_reward3
    risk_reward3 = reward_3_b / risk_x_b
    global risk_reward_3
    risk_reward_3 = tkinter.Label(root, text=koma.koma(risk_reward3), width=10, height=1, bg="green", fg="white", relief="groove")
    risk_reward_3.grid(row=11, column=10)

def lot():
    global lot_1
    lot_1 = risk1 / risk_x_a / 100
    lot_1_a = tkinter.Label(root, text=koma.koma(lot_1), width=8, height=1, bg="DodgerBlue2", relief="groove")
    lot_1_a.grid(row=17, column=2)
    lot_1_b = tkinter.Label(root, text=int(lot_1), width=9, height=1, bg="pink", relief="groove")
    lot_1_b.grid(row=17, column=3)

    global lot_2
    lot_2 = risk2 / risk_x_a / 100
    lot_2_a = tkinter.Label(root, text=koma.koma(lot_2), width=8, height=1, bg="DodgerBlue2", relief="groove")
    lot_2_a.grid(row=18, column=2)
    lot_2_b = tkinter.Label(root, text=int(lot_2), width=9, height=1, bg="pink", relief="groove")
    lot_2_b.grid(row=18, column=3)

    global lot_3
    lot_3 = risk3 / risk_x_a / 100
    lot_3_a = tkinter.Label(root, text=koma.koma(lot_3), width=8, height=1, bg="DodgerBlue2", relief="groove")
    lot_3_a.grid(row=19, column=2)
    lot_3_b = tkinter.Label(root, text=int(lot_3), width=9, height=1, bg="pink", relief="groove")
    lot_3_b.grid(row=19, column=3)

def dana():
    dana_1_a = buy * int(lot_1) *100
    dana_1_b = dana_1_a / modal *100
    dana_1_c = tkinter.Label(root, text="Rp. "+ rupiah.rupiah(dana_1_a), width=15, height=1, bg="DodgerBlue2", relief="groove")
    dana_1_c.grid(row=17, column=5)
    dana_1_d = tkinter.Label(root, text=koma.koma(dana_1_b)+"% dari Modal", width=28, height=1, bg="DodgerBlue2", relief="groove")
    dana_1_d.grid(row=17, column=6, columnspan=2)

    dana_2_a = buy * int(lot_2) *100
    dana_2_b = dana_2_a / modal *100
    dana_2_c = tkinter.Label(root, text="Rp. "+rupiah.rupiah(dana_2_a), width=15, height=1, bg="DodgerBlue2", relief="groove")
    dana_2_c.grid(row=18, column=5)
    dana_2_d = tkinter.Label(root, text=koma.koma(dana_2_b)+"% dari Modal", width=28, height=1, bg="DodgerBlue2", relief="groove")
    dana_2_d.grid(row=18, column=6, columnspan=2)

    dana_3_a = buy * int(lot_3) *100
    dana_3_b = dana_3_a / modal *100
    dana_3_c = tkinter.Label(root, text="Rp. "+rupiah.rupiah(dana_3_a), width=15, height=1, bg="DodgerBlue2", relief="groove")
    dana_3_c.grid(row=19, column=5)
    dana_3_d = tkinter.Label(root, text=koma.koma(dana_3_b)+"% dari Modal", width=28, height=1, bg="DodgerBlue2", relief="groove")
    dana_3_d.grid(row=19, column=6, columnspan=2)

def proyeksi():
    profit_1_a = risk1 * risk_reward1
    profit_1_b = risk1 * risk_reward2
    profit_1_c = risk1 * risk_reward3
    print_profit_1_1 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(risk1), width=12, bg="pink", relief="groove").grid(row=17, column=12)
    print_profit_1_2 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(int(profit_1_a)), width=12, bg="light green", relief="groove").grid(row=17, column=13)
    print_profit_1_3 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(int(profit_1_b)), width=12, bg="light green", relief="groove").grid(row=17, column=14)
    print_profit_1_4 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(int(profit_1_c)), width=12, bg="light green", relief="groove").grid(row=17, column=15)

    profit_2_a = risk2 * risk_reward1
    profit_2_b = risk2 * risk_reward2
    profit_2_c = risk2 * risk_reward3
    print_profit_2_1 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(risk2), width=12, bg="pink", relief="groove").grid(row=18, column=12)
    print_profit_2_2 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(int(profit_2_a)), width=12, bg="light green", relief="groove").grid(row=18, column=13)
    print_profit_2_3 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(int(profit_2_b)), width=12, bg="light green", relief="groove").grid(row=18, column=14)
    print_profit_2_4 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(int(profit_2_c)), width=12, bg="light green", relief="groove").grid(row=18, column=15)

    profit_3_a = risk3 * risk_reward1
    profit_3_b = risk3 * risk_reward2
    profit_3_c = risk3 * risk_reward3
    print_profit_3_1 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(risk3), width=12, bg="pink", relief="groove").grid(row=19, column=12)
    print_profit_3_2 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(int(profit_3_a)), width=12, bg="light green", relief="groove").grid(row=19, column=13)
    print_profit_3_3 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(int(profit_3_b)), width=12, bg="light green", relief="groove").grid(row=19, column=14)
    print_profit_3_4 = tkinter.Label(root, text="Rp. "+rupiah.rupiah(int(profit_3_c)), width=12, bg="light green", relief="groove").grid(row=19, column=15)

#GUI
#frame
frame = tkinter.Label(root, text=" ", width=20, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=1, column=7)
frame = tkinter.Label(root, text=" ", width=20, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=2, column=7)
frame = tkinter.Label(root, text=" ", width=20, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=3, column=7)

frame = tkinter.Label(root, text=" ", width=7, height=1, bg="white", relief="groove")
frame.grid(row=7, column=6)
frame = tkinter.Label(root, text=" ", width=20, height=1, bg="white", relief="groove")
frame.grid(row=7, column=7)

frame = tkinter.Label(root, text=" ", width=7, height=1, bg="white", relief="groove")
frame.grid(row=9, column=6)
frame = tkinter.Label(root, text=" ", width=20, height=1, bg="green", relief="groove")
frame.grid(row=9, column=7)

frame = tkinter.Label(root, text=" ", width=7, height=1, bg="white", relief="groove")
frame.grid(row=10, column=6)
frame = tkinter.Label(root, text=" ", width=20, height=1, bg="green", relief="groove")
frame.grid(row=10, column=7)

frame = tkinter.Label(root, text=" ", width=7, height=1, bg="white", relief="groove")
frame.grid(row=11, column=6)
frame = tkinter.Label(root, text=" ", width=20, height=1, bg="green", relief="groove")
frame.grid(row=11, column=7)

frame = tkinter.Label(root, text=" ", width=10, height=1, bg="green", fg="white", relief="groove")
frame.grid(row=9, column=10)
frame = tkinter.Label(root, text=" ", width=10, height=1, bg="green", fg="white", relief="groove")
frame.grid(row=10, column=10)
frame = tkinter.Label(root, text=" ", width=10, height=1, bg="green", fg="white", relief="groove")
frame.grid(row=11, column=10)

frame = tkinter.Label(root, text=" ", width=8, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=17, column=2)
frame = tkinter.Label(root, text=" ", width=8, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=18, column=2)
frame = tkinter.Label(root, text=" ", width=8, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=19, column=2)

frame = tkinter.Label(root, text=" ", width=9, height=1, bg="pink", relief="groove")
frame.grid(row=17, column=3)
frame = tkinter.Label(root, text=" ", width=9, height=1, bg="pink", relief="groove")
frame.grid(row=18, column=3)
frame = tkinter.Label(root, text=" ", width=9, height=1, bg="pink", relief="groove")
frame.grid(row=19, column=3)

frame = tkinter.Label(root, text=" ", width=15, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=17, column=5)
frame = tkinter.Label(root, text=" ", width=15, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=18, column=5)
frame = tkinter.Label(root, text=" ", width=15, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=19, column=5)

frame = tkinter.Label(root, text=" ", width=28, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=17, column=6, columnspan=2)
frame = tkinter.Label(root, text=" ", width=28, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=18, column=6, columnspan=2)
frame = tkinter.Label(root, text=" ", width=28, height=1, bg="DodgerBlue2", relief="groove")
frame.grid(row=19, column=6, columnspan=2)

frame = tkinter.Label(root, text=" ", width=12, bg="pink", relief="groove")
frame.grid(row=17, column=12)
frame = tkinter.Label(root, text=" ", width=12, bg="pink", relief="groove")
frame.grid(row=18, column=12)
frame = tkinter.Label(root, text=" ", width=12, bg="pink", relief="groove")
frame.grid(row=19, column=12)

frame = tkinter.Label(root, text=" ", width=12, bg="light green", relief="groove")
frame.grid(row=17, column=13)
frame = tkinter.Label(root, text=" ", width=12, bg="light green", relief="groove")
frame.grid(row=18, column=13)
frame = tkinter.Label(root, text=" ", width=12, bg="light green", relief="groove")
frame.grid(row=19, column=13)

frame = tkinter.Label(root, text=" ", width=12, bg="light green", relief="groove")
frame.grid(row=17, column=14)
frame = tkinter.Label(root, text=" ", width=12, bg="light green", relief="groove")
frame.grid(row=18, column=14)
frame = tkinter.Label(root, text=" ", width=12, bg="light green", relief="groove")
frame.grid(row=19, column=14)

frame = tkinter.Label(root, text=" ", width=12, bg="light green", relief="groove")
frame.grid(row=17, column=15)
frame = tkinter.Label(root, text=" ", width=12, bg="light green", relief="groove")
frame.grid(row=18, column=15)
frame = tkinter.Label(root, text=" ", width=12, bg="light green", relief="groove")
frame.grid(row=19, column=15)

#blank space
blank_0 = tkinter.Label(root, text=" ")
blank_0.grid(row=0, column=0)

blank_1 = tkinter.Label(root, text=" ")
blank_1.grid(row=12, column=0)

blank_2 = tkinter.Label(root, text=" ")
blank_2.grid(row=18, column=0)

blank_3 = tkinter.Label(root, text=" ")
blank_3.grid(row=6, column=0)

blank_4 = tkinter.Label(root, text=" ")
blank_4.grid(row=8, column=0)

blank_5 = tkinter.Label(root, text=" ")
blank_5.grid(row=14, column=0)

blank_6 = tkinter.Label(root, text=" ")
blank_6.grid(row=0, column=4)

blank_7 = tkinter.Label(root, text=" ")
blank_7.grid(row=0, column=8)

blank_7 = tkinter.Label(root, text=" ")
blank_7.grid(row=0, column=11)

#label input
label_1 = tkinter.Label(root, text="MODAL : ", width=15, borderwidth=2, bg="black", fg="white")
label_1.grid(row=1, column=0, columnspan=2)

label_2 = tkinter.Label(root, text="BUY : ", width=15, borderwidth=2, bg="black", fg="white")
label_2.grid(row=5, column=0, columnspan=2)

label_3 = tkinter.Label(root, text="STOP LOSS : ", width=15, borderwidth=2, bg="black", fg="white")
label_3.grid(row=7, column=0, columnspan=2)

label_4 = tkinter.Label(root, text="Target Profit 1 : ",  width=15, borderwidth=2, bg="black", fg="white")
label_4.grid(row=9, column=0, columnspan=2)

label_5 = tkinter.Label(root, text="Target Profit 2 : ",  width=15, borderwidth=2, bg="black", fg="white")
label_5.grid(row=10, column=0, columnspan=2)

label_6 = tkinter.Label(root, text="Target Profit 3 : ",  width=15, borderwidth=2, bg="black", fg="white")
label_6.grid(row=11, column=0, columnspan=2)


#Input-an
input_1 = tkinter.Entry(root, width=20, borderwidth=4, bg="orange", fg="black")
input_1.grid(row=1, column=2, columnspan=2)

input_2 = tkinter.Entry(root, width=20, borderwidth=4, bg="orange", fg="black")
input_2.grid(row=5, column=2, columnspan=2)

input_3 = tkinter.Entry(root, width=20, borderwidth=4, bg="orange", fg="black")
input_3.grid(row=7, column=2, columnspan=2)

input_4 = tkinter.Entry(root, width=20, borderwidth=4, bg="orange", fg="black")
input_4.grid(row=9, column=2, columnspan=2)

input_5 = tkinter.Entry(root, width=20, borderwidth=4, bg="orange", fg="black")
input_5.grid(row=10, column=2, columnspan=2)

input_6 = tkinter.Entry(root, width=20, borderwidth=4, bg="orange", fg="black")
input_6.grid(row=11, column=2, columnspan=2)

# Tombol
tombol_1 = tkinter.Button(root, text="ANALISIS", font="20", bg="red3", fg="white", width=25, borderwidth=10, height=3, command=combine_fungsi(risk_trade, risk, reward, risk_reward, lot, dana, proyeksi))
tombol_1.grid(row=13, column=0, columnspan=4)

#output 1
risk_a = tkinter.Label(root, text="Risk per Trade", padx=15, pady=25, bg="black", fg="white")
risk_a.grid(row=1, rowspan=3, column=5,)

risk_1 = tkinter.Label(root, text="2,00 %", width=7, height=1, bg="DodgerBlue4")
risk_1.grid(row=1, column=6)

risk_2 = tkinter.Label(root, text="1,50 %", width=7, height=1, bg="DodgerBlue4")
risk_2.grid(row=2, column=6)

risk_3 = tkinter.Label(root, text="1,00 %", width=7, height=1, bg="DodgerBlue4")
risk_3.grid(row=3, column=6)

label = tkinter.Label(root, text="Max Risk per Trade 2%", width=25, height=4, bg="pink", relief="groove")
label.grid(row=1, rowspan=3, column=8, columnspan=3)

#output 2
risk_b = tkinter.Label(root, text="Risk", width=15, bg="black", fg="white", relief="groove")
risk_b.grid(row=7, column=5)

label = tkinter.Label(root, text="Risk Max 10%", width=25, height=1, bg="pink", relief="groove")
label.grid(row=7, column=8, columnspan=3)

reward_a = tkinter.Label(root, text="Reward", width=15, bg="black", fg="white", relief="groove")
reward_a.grid(row=9, column=5)

reward_b = tkinter.Label(root, text="Reward", width=15, bg="black", fg="white", relief="groove")
reward_b.grid(row=10, column=5)

reward_c = tkinter.Label(root, text="Reward", width=15, bg="black", fg="white", relief="groove")
reward_c.grid(row=11, column=5)

risk_reward_a = tkinter.Label(root, text="Risk : Reward  ", bg="white", relief="groove")
risk_reward_a.grid(row= 9, column=9)

risk_reward_b = tkinter.Label(root, text="Risk : Reward  ", bg="white", relief="groove")
risk_reward_b.grid(row= 10, column=9)

risk_reward_c = tkinter.Label(root, text="Risk : Reward  ", bg="white", relief="groove")
risk_reward_c.grid(row= 11, column=9)

#output 3
lot_ideal = tkinter.Label(root, text="LOT IDEAL", padx=95, pady=10, bg="light green", relief="groove")
lot_ideal.grid(row= 15, rowspan=2, column=0, columnspan=4)

lot_risk = tkinter.Label(root, text="RISK", width=8, height=4, bg="pink", relief="groove")
lot_risk.grid(row= 17, rowspan=3, column=0,)

lot_2 = tkinter.Label(root, text="2,00 %", width=7, height=1, bg="DodgerBlue4", relief="groove")
lot_2.grid(row= 17, column=1,)

lot_1_5 = tkinter.Label(root, text="1,50 %", width=7, height=1, bg="DodgerBlue4", relief="groove")
lot_1_5.grid(row= 18, column=1,)

lot_1 = tkinter.Label(root, text="1,00 %", width=7, height=1, bg="DodgerBlue4", relief="groove")
lot_1.grid(row= 19, column=1,)

dana_digunakan = tkinter.Label(root, text="Dana Yang Digunakan", padx=95, pady=10, bg="light green", relief="groove")
dana_digunakan.grid(row= 15, rowspan=2, column=5, columnspan=3)

label = tkinter.Label(root, text="Max 25% s.d 30% dari Modal", width=25, height=4, bg="pink", relief="groove")
label.grid(row=17, rowspan=3, column=8, columnspan=3)

proyeksi = tkinter.Label(root, text="Proyeksi", width=51, bg="yellow", relief="groove")
proyeksi.grid(row= 15, column=12, columnspan=4)

proyeksi_stop = tkinter.Label(root, text="Stop Loss", width=12, bg="yellow", relief="groove")
proyeksi_stop.grid(row=16, column=12)

proyeksi_1 = tkinter.Label(root, text="Profit 1", width=12, bg="yellow", relief="groove")
proyeksi_1.grid(row=16, column=13)

proyeksi_2 = tkinter.Label(root, text="Profit 2", width=12, bg="yellow", relief="groove")
proyeksi_2.grid(row=16, column=14)

proyeksi_3 = tkinter.Label(root, text="Profit 3", width=12, bg="yellow", relief="groove")
proyeksi_3.grid(row=16, column=15)


root.mainloop()
