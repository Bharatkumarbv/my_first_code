l = {
"black" : "\u001b[30m",
"red"  : "\u001b[31m",
"green" : "\u001b[32m",
"yellow" : "\u001b[33m",
"blue" : "\u001b[34m",
"magenta" : "\u001b[35m",
"cyan": "\u001b[36m",
"white": "\u001b[37m",
 }
close = "\u001b[0m"

choose = {
    '~':'~', "!":"!", "@":"@", "#":"#", "$":"$", "%":"%", "^":"^", "&":"&", "*":"*", "?":"?", "()":"()", "/":"/"
}

def print_row(*col):
    for i in range(5):
        if i in col:
            print(f"{l[color]}{choose[symbol]}{close}",end=" ")
        else:
            print(" ",end=" ")


def row_1to3():
    print_row(1,2,3)

def row_0_4():
    print_row(0,4)

def row_0to3():
    print_row(0,1,2,3)

def row_0to4():
    print_row(0,1,2,3,4)

def row_0():
    print_row(0)

def row_2():
    print_row(2)

def row_1to4():
    print_row(1,2,3,4)

def G3():
    print_row(0,2,3,4)

def row_0_2():
    print_row(0,2)

def row_0_3():
    print_row(0,3)

def row_1_3():
    print_row(1,3)

def row_0_2_4():
    print_row(0,2,4)

def row_0_13_4():
    print_row(0,1,3,4)

def K3():
    print_row(0,1)

def row_1_2():
    print_row(1,2)

def row_4():
    print_row(4)

def N3():
    print_row(0,1,4)

def N5():
    print_row(0,3,4)

def Q4():
    print_row(0,2,3)

def Q6():
    print_row(1,2,4)

def Z2():
    print_row(3)

def Z4():
    print_row(1)

A0=C0=O0=C6=O6=S0=S6=U6=S3=row_1to3

A1=A2=A4=A5=A6=B1=B2=B4=B5=C1=C5=D1=D2=D3=D4=D5=G4=G5=H0=H1=H2=H4=H5=H6=K0=K6=M0=N2=N6=O1=O2=O3=O4=O5=P1=P2=R1=R2=R6=S1=S5=U0=U1=U2=U3=U4=U5=V1=V2=V3=V4=V0=W0=W1=W2=W3=W6=X0=X1=X5=X6=Y0=M3=M4=M5=M6=row_0_4

B0=B3=B6=D0=D6=F3=P0=P3=R0=R3=row_0to3

A3=E0=E3=E6=F0=H3=I0=I6=J0=L6=T0=Z0=Z6=row_0to4

E1=F1=G1=E2=E4=E5=C2=C3=C4=F2=F4=F5=F6=G2=L0=L1=L2=L3=L4=L5=P4=P5=P6=S2=Z5=row_0

I1=I2=I3=I4=I5=J1=J2=J3=T1=T2=T3=T4=T5=T6=Z3=X3=Y2=Y3=Y4=Y5=Y6=V6=row_2

G0=G6=row_1to4

J4=J5=K2=K4=R4=row_0_2

K1=K5=R5=Q1=Q2=Q3=Q5=row_0_3

X2=X4=Y1=V5=row_1_3

M2=W4=N4=row_0_2_4

M1=W5=row_0_13_4

Q0=J6=row_1_2

N0=S4=Z1=N1=row_4

word = input("enter your name = ").upper()
print("~ ! @ # $ % ^ & * ? () /")
symbol = input("Please enter your output symbol = ")
print("0-Black\n 1-Red\n 3-Green\n 4-Yellow\n 5-Blue\n 6-Magenta\n 7-Cyan \n 8-White \n")
color = input("please enter your fav color = ").lower()
for i in range(7):
    for ch in word:
        if ch != " ":
            exec(ch + str(i) + '()' )
            print(end=" ")
        else:
            print("  ", end=" ")
    print()
