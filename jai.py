from tkinter import*
import random
import time
import datetime
import pymysql

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'bold'),text="Billing System for Hotel ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
x=random.randint(10908,500876)
randomRef=str(x)
CoIdly=0
CoD=0
CoDosa=0
CoKesari=0
CoPulav=0
CoKarabath=0
CostofMeal=0
PayTax=0
OverAllCost=0
def Ref():
    
    rand.set(randomRef)

    if (Idly.get()==""):
        CoIdly=0
    else:
        CoIdly=float(Idly.get())


    
    if (Dosa.get()==""):
        CoDosa=0
    else:
        CoDosa=float(Dosa.get())



    if (Kesari.get()==""):
        CoKesari=0
    else:
        CoKesari=float(Kesari.get())



    if (Pulav.get()==""):
        CoPulav=0
    else:
        CoPulav=float(Pulav.get())

        
    if (Karabath.get()==""):
        CoKarabath=0
    else:
        CoKarabath=float(Karabath.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofIdly =CoIdly * 25
    CostofDrinks=CoD * 20
    CostofDosa = CoDosa* 35
    CostofKesari = CoKesari * 25
    CostPulav = CoPulav* 35
    CostKarabath=CoKarabath * 20
    CoM=CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav+CostKarabath

    CostofMeal= "Rs", str('%.2f' % (CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav+CostKarabath))

    PayTax=((CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav+CostKarabath) * 0.18)

    TotalCost=(CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav+CostKarabath)
 
    Ser_Charge= ((CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav+CostKarabath)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)
    oc=str ('%.2f' % (PayTax+TotalCost+Ser_Charge)) 
    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))
    pt=str ('%.2f' % PayTax)

    PaidTax= "Rs", str ('%.2f' % PayTax)
    idly_count=int(CoIdly)
    dosa_count=int(CoDosa)
    kesari_count=int(CoKesari)
    pulav_count=int(CoPulav)
    shawarmacount=int(CoKarabath)
    drinks_count=int(CoD)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    print(randomRef,idly_count,dosa_count,kesari_count,pulav_count,shawarmacount,drinks_count,CoM,pt,oc)
   #return(CoIdly,CoDosa,CoKesari,CoPulav,CoKarabath,CoD,CostofMeal,PayTax,OverAllCost)
    cl(randomRef,idly_count,dosa_count,kesari_count,pulav_count,shawarmacount,drinks_count,CoM,pt,oc)
def cl(randomRef,idly_count,dosa_count,kesari_count,pulav_count,shawarmacount,drinks_count,CoM,pt,oc):
    conn=pymysql.connect(host='localhost',user='root',passwd='',db='python')
    cursor=conn.cursor()
    sql=("Insert into jai (Reference, Idly, Dosa, Kesari, Pulav, Shawarma, Drinks, Cost, Tax, TCost) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    val=(randomRef,idly_count,dosa_count,kesari_count,pulav_count,shawarmacount,drinks_count,CoM,pt,oc)
    cursor.execute(sql,val)
    conn.commit()
    print(cursor.rowcount, "record inserted.")
def qExit():
    #root.destroy()
    connection=pymysql.connect(host='localhost',user='root',passwd='',db='python')
    cur=connection.cursor()
    cur.execute('SELECT Tax FROM jai')

    data = cur.fetchall()
    tot = 0
    for row in data:
            
            tot += float(row[0])
    print(tot)
    totaltax.set(tot)
def Reset():
    rand.set("") 
    Idly.set("")
    Dosa.set("")
    Kesari.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Pulav.set("")
    Karabath.set("")
    
#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Idly=StringVar()
Dosa=StringVar()
Kesari=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Pulav=StringVar()
Karabath=StringVar()
totaltax=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblIdly= Label(f1, font=('arial', 16, 'bold'),text="Idly",bd=16,anchor="w")
lblIdly.grid(row=1, column=0)
txtIdly=Entry(f1, font=('arial',16,'bold'),textvariable=Idly,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtIdly.grid(row=1,column=1)


lblDosa= Label(f1, font=('arial', 16, 'bold'),text="Dosa",bd=16,anchor="w")
lblDosa.grid(row=2, column=0)
txtDosa=Entry(f1, font=('arial',16,'bold'),textvariable=Dosa,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDosa.grid(row=2,column=1)


lblKesari= Label(f1, font=('arial', 16, 'bold'),text="Kesari",bd=16,anchor="w")
lblKesari.grid(row=3, column=0)
txtKesari=Entry(f1, font=('arial',16,'bold'),textvariable=Kesari,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtKesari.grid(row=3,column=1)

lblPulav= Label(f1, font=('arial', 16, 'bold'),text="Pulav",bd=16,anchor="w")
lblPulav.grid(row=4, column=0)
txtPulav=Entry(f1, font=('arial',16,'bold'),textvariable=Pulav,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPulav.grid(row=4,column=1)

lblKarabath= Label(f1, font=('arial', 16, 'bold'),text="Shawarma",bd=16,anchor="w")
lblKarabath.grid(row=5, column=0)
txtKarabath=Entry(f1, font=('arial',16,'bold'),textvariable=Karabath,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtKarabath.grid(row=5,column=1)

lblKarabath= Label(f1, font=('arial', 16, 'bold'),text="Shawarma",bd=16,anchor="w")
lblKarabath.grid(row=5, column=0)
txtKarabath=Entry(f1, font=('arial',16,'bold'),textvariable=Karabath,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtKarabath.grid(row=5,column=1)

#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)
#============================================================================================================
#                             Tax
#========================================================================================

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Total Tax",bd=16,anchor="w")
lblDrinks.grid(row=0, column=4)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=totaltax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=5)
#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total Tax",bg="powder blue",command= qExit).grid(row=7,column=3)


root.mainloop()


