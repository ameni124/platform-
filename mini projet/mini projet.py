#mot de passe pour administrateur admin
#mot de passe pour job seeker  admino
 
from tkinter import *
from tkinter.messagebox import *
import csv
import os
def change ():
    l=[]
    f = open('user11.csv','r')
    lecture= csv.reader(f,delimiter=";")
    for ligne in lecture :
        if ligne[0]!=jobid_entry.get():
            l.append(ligne)
    f.close()
    os.remove("user11.csv")
    file=open("user11.csv",'a',newline='')
    writer=csv.writer(file,delimiter=';')
    writer.writerows(l)
    file.close()
    add()       


def update ():
    global jobid_entry
    f3=Tk()
    job=StringVar()
    f3.title("updating a job offer")
    f3.geometry("400x400")
    jobid_text=Label(f3,text="tape the jobid")
    jobid_text.pack(side=LEFT,padx=5,pady=5)
    jobid_text.place(x = 18, y =60)
    jobid_entry=Entry(f3,textvariable=job)
    jobid_entry.pack(side=LEFT,padx=5,pady=5)
    jobid_entry.place(x = 18, y =120)
    b7=Button(f3,text="add the new information",command=change)
    b7.pack()
    b7.place(x = 200, y =120)
def delete():
    l=[]
    f = open('user11.csv','r')
    lecture= csv.reader(f,delimiter=";")
    for ligne in lecture :
        if ligne[0]!=jobid_entry.get():
            #print (ligne [0])
            l.append(ligne)
    f.close()
    os.remove("user11.csv")
    file=open("user11.csv",'a',newline='')
    writer=csv.writer(file,delimiter=';')
    writer.writerows(l)
    file.close()
def update1():
    global jobid_entry
    f3=Tk()
    job=StringVar()
    f3.title("deleting a job offer")
    f3.geometry("400x400")
    jobid_text=Label(f3,text="tape the jobid")
    jobid_text.pack(side=LEFT,padx=5,pady=5)
    jobid_entry=Entry(f3,textvariable=job)
    jobid_entry.pack(side=LEFT,padx=5,pady=5)
    print(jobid_entry)
    b7=Button(f3,text="delete",command=delete)
    b7.pack()
    
    
    

                
            
        
    
    
def add ():
    screen = Tk()
    screen.geometry("600x600")
    screen.title("adding job offer")
    heading = Label(screen ,text = " new job offer", bg = "grey", fg = "black", width = "500", height = "3")
    heading.pack()
 
    jobid_text = Label(screen,text = "jobid * ",)
    adresse_text = Label(screen,text = "adresse * ",)
    phone_text = Label(screen,text = "phone * ",)
    email_text=Label(screen,text="email*",)
    degree_text=Label(screen,text="degree*",)
    qualification_text=Label(screen,text="qualification",)
    domain_text=Label(screen,text="domain",)




    jobid_text.place(x = 15, y = 70)
    adresse_text.place(x = 15, y = 120)
    phone_text.place(x = 15, y = 200)
    email_text.place(x = 15, y = 260)
    degree_text.place(x = 15, y = 300)
    qualification_text.place(x = 15, y = 360)
    domain_text.place(x = 200, y = 70)
    





    jobid = IntVar()
    adresse =StringVar()
    phone = IntVar()
    email=StringVar()
    degree=StringVar()
    qualification=StringVar()
    domain=StringVar()

    jobid_entry = Entry(screen,textvariable = jobid, width = "30")
    adresse_entry = Entry(screen,textvariable = adresse, width = "30")
    phone_entry = Entry(screen,textvariable = phone, width = "30")
    email_entry = Entry(screen,textvariable = email, width = "30")
    degree_entry = Entry(screen,textvariable = degree, width = "30")
    qualification_entry = Entry(screen,textvariable = qualification, width = "30")
    domain_entry = Entry(screen,textvariable = domain , width = "30")

    jobid_entry.place(x = 15, y = 100)
    adresse_entry.place(x = 15, y = 160)
    phone_entry.place(x = 15, y = 220)
    email_entry.place(x=15,y=280) 
    degree_entry.place(x=15,y=340)
    qualification_entry.place(x=15,y=380)
    domain_entry.place(x=200,y=100)
    
    def save_info():
      jobid_info =  jobid_entry.get()
      adresse_info = adresse_entry.get()
      phone_info = phone_entry.get()
      email_info=email_entry.get()
      degree_info=degree_entry.get()
      qualification_info=qualification_entry.get()
      domain_info=domain_entry.get()
      
      phone_info = str(phone_info)
      jobid_info=str(jobid_info)
      

      file = open("user11.csv", "a",newline='')
      writer=csv.writer(file,delimiter=';')
      writer.writerow([jobid_info ,adresse_info,phone_info,email_info,degree_info,qualification_info,domain_info])
      file.close()


      
          

      jobid_entry.delete(0, END)
      adresse_entry.delete(0, END)
      phone_entry.delete(0, END)
      email_entry.delete(0, END)
      degree_entry.delete(0,END)
      qualification_entry.delete(0,END)
      domain_entry.delete(0,END)
      
      

    b6= Button(screen,text = "add", width = "30", height = "2", command = save_info, bg = "red")
    b6.place(x = 18, y =460)
    
def searching ():
    a=[]
    f = open('user11.csv','r')
    lecture= csv.reader(f,delimiter=";")
    for ligne in lecture :
       
        if ligne [0]== jobid_entry.get():
            a.append("** ".join(ligne))
        if ligne[1]==location_entry.get():
            a.append(" **".join(ligne))
        if ligne[5]==domain_entry.get():
            a.append(" **".join(ligne))


    
    line="\n".join(a)
    
    f3=Tk()
    f3.title("availble job offer")
    f3.geometry("400x400")
    jobid_text=Label(f3,text=line)
    jobid_text.pack(side=LEFT,padx=5,pady=5)
                

    


def search():
    global jobid_entry
    global location_entry
    global domain_entry
    screen = Tk()
    screen.geometry("500x500")
    screen.title("searching job offer")
    heading = Label(screen ,text = " search according to ", bg = "grey", fg = "red", width = "500", height = "3")
    heading.pack()
 
    jobid_text = Label(screen,text = "jobid  ",)
    location_text = Label(screen,text = "location  ",)
    domain_text = Label(screen,text = "domain  ",)
    



    jobid_text.place(x = 15, y = 70)
    location_text.place(x = 15, y = 120)
    domain_text.place(x = 15, y = 200)
    




    jobid = IntVar()
    location =StringVar()
    domain = StringVar()
    
    jobid_entry = Entry(screen,textvariable = jobid, width = "30")
    location_entry = Entry(screen,textvariable = location, width = "30")
    domain_entry = Entry(screen,textvariable = domain, width = "30")
    

    jobid_entry.place(x = 15, y = 100)
    location_entry.place(x = 15, y = 160)
    domain_entry.place(x = 15, y = 220)
    b6= Button(screen,text = "search", width = "30", height = "2", command = searching, bg = "red")
    b6.place(x = 18, y =460)



def apply():
    screen = Tk()
    screen.geometry("800x800")
    screen.title("apply for a job offer job offer")
    heading = Label(screen ,text = " please tape your information here", bg = "grey", fg = "black", width = "500", height = "3")
    heading.pack()
    personal_text=Label(screen,text = "personal informations ",)
    idcard_text = Label(screen,text = "idcard * ",)
    name_text = Label(screen,text = "full name * ",)
    adresse_text = Label(screen,text = "adress * ",)
    phone_text=Label(screen,text="phone numbre*",)
    education_text=Label(screen,text = "education ",)    
    degree_text=Label(screen,text=" university degree*",)
    professional_text=Label(screen,text = "professional informations ",)
    experience_text=Label(screen,text="experience",)
    competence_text=Label(screen,text="competence",)
    jobid_text=Label(screen,text="jobid ",)


    personal_text.place(x=15, y=50)
    idcard_text.place(x = 15, y = 90)
    name_text.place(x = 15, y = 140)
    adresse_text.place(x = 15, y = 220)
    phone_text.place(x = 15, y = 280)
    education_text.place(x = 15, y = 320)
    degree_text.place(x = 15, y = 360)
    professional_text.place(x = 300, y = 50)
    experience_text.place(x=300,y=90)
    competence_text.place(x = 300, y = 140)
    jobid_text.place(x=300,y=190)





    jobid = IntVar()
    adresse =StringVar()
    phone = IntVar()
    name=StringVar()
    degree=StringVar()
    experience=StringVar()
    competence=StringVar()
    idcard = IntVar()
    

    idcard_entry = Entry(screen,textvariable = idcard, width = "30")
    name_entry = Entry(screen,textvariable = name, width = "30")
    adresse_entry = Entry(screen,textvariable = adresse, width = "30")
    phone_entry = Entry(screen,textvariable = phone, width = "30")
    degree_entry = Entry(screen,textvariable = degree, width = "30")
    experience_entry = Entry(screen,textvariable = experience, width = "30")
    competence_entry = Entry(screen,textvariable = competence, width = "30")
    jobid_entry = Entry(screen,textvariable = jobid, width = "30")
    

    idcard_entry.place(x = 15, y = 120)
    name_entry.place(x = 15, y = 180)
    adresse_entry.place(x = 15, y = 240)
    phone_entry.place(x=15,y=300) 
    degree_entry.place(x=15,y=380)
    experience_entry.place(x=300,y=110)
    competence_entry .place(x=300,y=160)
    jobid_entry.place(x=300,y=210)
    def save_information():
        idcard_info =  idcard_entry.get()
        name_info = name_entry.get()
        adresse_info = adresse_entry.get()
        phone_info=phone_entry.get()
        degree_info=degree_entry.get()
        experience_info=experience_entry.get()
        competence_info=competence_entry.get()
        jobid_info =  jobid_entry.get()
        
        idcard_info = str(idcard_info)
        phone_info = str(phone_info)
        jobid_info=str(jobid_info)
      

        file = open("user112.csv", "a",newline='')
        writer=csv.writer(file,delimiter=';')
        writer.writerow([idcard_info ,name_info,adresse_info,phone_info,degree_info,experience_info,competence_info,jobid_info])
        file.close()


      
          

        idcard_entry.delete(0, END)
        name_entry.delete(0, END)
        adresse_entry.delete(0, END)
        phone_entry.delete(0, END)
        degree_entry.delete(0,END)
        experience_entry.delete(0,END)
        competence_entry.delete(0,END)
        jobid_entry.delete(0,END)

    b6= Button(screen,text = "apply now", width = "30", height = "2", command = save_information, bg = "red")
    b6.place(x = 18, y =460)
    
def changing ():
    l=[]
    f = open('user112.csv','r')
    lecture= csv.reader(f,delimiter=";")
    for ligne in lecture :
        if ligne[0]!=idcard_entry.get():
            l.append(ligne)
    f.close()
    os.remove("user112.csv")
    file=open("user112.csv",'a',newline='')
    writer=csv.writer(file,delimiter=';')
    writer.writerows(l)
    file.close()
    apply()        


def updating ():
    global idcard_entry
    f3=Tk()
    card=StringVar()
    f3.title("updating job seeker's informations")
    f3.geometry("400x400")
    idcard_text=Label(f3,text="tape your id card here please !!")
    idcard_text.pack(side=LEFT,padx=5,pady=5)
    idcard_text.place(x = 18, y =60)
    idcard_entry=Entry(f3,textvariable=card)
    idcard_entry.pack(side=LEFT,padx=5,pady=5)
    idcard_entry.place(x = 18, y =120)
    b7=Button(f3,text="add the new information",command=changing)
    b7.pack()
    b7.place(x = 200, y =120)
def all_job():
    r=[]
    f = open('user112.csv','r')
    read= csv.reader(f,delimiter=";")
    for l in read :
       
        r.append("".join(l[1]))
        


    
    line="\n".join(r)
    
    f3=Tk()
    f3.title("the list of all job seekers that applied for all job offers")
    f3.geometry("400x400")
    jobid_text=Label(f3,text=line)
    jobid_text.pack(side=LEFT,padx=5,pady=5)
def same():
    r=[]
    f = open('user112.csv','r')
    read= csv.reader(f,delimiter=";")
    
    for l in read :
        if c.get()==l[7]:
            r.append("".join(l[1]))
        


    
    line="\n".join(r)
    
    f3=Tk()
    f3.title("the list of all job seekers that applied for this job offer")
    f3.geometry("400x400")
    jobid_text=Label(f3,text=line)
    jobid_text.pack(side=LEFT,padx=5,pady=5)
    


def same_job():
    global c
    f=Tk()
    f.title('job seekers for this id_job')
    l=Label(f,text='tape here the job_id')
    l.pack(side=LEFT,padx=5,pady=5)
    job_id=StringVar()
    c=Entry(f,textvariable=job_id,bg='bisque',fg='maroon')
    c.focus_set()
    c.pack(side=LEFT,padx=5,pady=5)
    b=Button(f,text='view the list ',command=same)
    b.pack(side=LEFT,padx=5,pady=5)
    f.mainloop()
    
                





def liste():
    f0=Tk()
    f0.title("list of job seekers")
    l0=Label(f0,text='veillez choisir!!',fg='pink')
    l0.pack()
    b0=Button(f0,text="list of all job seekers ",command =all_job)
    b0.pack()
    b01=Button(f0,text="list of job seekers that applied for the same job offer",command =same_job)
    b01.pack()
    f0.mainloop()


    
    


    
        
            
            


            










def choisir():
    if c1.get()!="admin":
        showwarning('warning','password invalide !!!')
        password.set('')
    else:
        f2=Tk()
        l2=Label(f2,text='veillez choisir !!',fg='green')
        l2.pack()
        b2=Button(f2,text='add new job offer',command=add)
        b2.pack()
        b3=Button (f2,text='update job offer',command=update)
        b3.pack()
        b4=Button (f2,text='delete job offer',command=update1)
        b4.pack()
        b5=Button (f2,text='brrow list of job seekers ',command =liste)
        b5.pack()
        f2.mainloop()
def choix():
     if c.get()!="admino":
        showwarning('warning','password invalide !!!')
        motdepass.set('')
     else:
        fenetre=Tk()
        l22=Label(fenetre,text='veillez choisir !!',fg='green')
        l22.pack()
        b22=Button(fenetre,text='search a job offer',command=search)
        b22.pack()
        b33=Button (fenetre,text='brow and apply for a job offer',command=apply)
        b33.pack()
        b4=Button (fenetre,text='update job seeker',command=updating)
        b4.pack()
       
        fenetre.mainloop()
    
        
def jobseeker():
    global c
    f=Tk()
    f.title('jobseeker')
    l=Label(f,text='password')
    l.pack(side=LEFT,padx=5,pady=5)
    motdepass=StringVar()
    c=Entry(f,textvariable=motdepass,show= '*',bg='bisque',fg='maroon')
    c.focus_set()
    c.pack(side=LEFT,padx=5,pady=5)
    b=Button(f,text='enter',command=choix)
    b.pack(side=LEFT,padx=5,pady=5)
    f.mainloop()






def administrator():
    global c1

    f1=Tk()
    f1.title('administrator')
    l1=Label(f1,text='password')
    l1.pack(side=LEFT,padx=5,pady=5)
    password=StringVar()
    c1=Entry(f1,textvariable=password,show= '*',bg='bisque',fg='maroon')
    c1.focus_set()
    c1.pack(side=LEFT,padx=5,pady=5)
    b1=Button(f1,text='enter',command=choisir)
    b1.pack(side=LEFT,padx=5,pady=5)
    f1.mainloop()

f0=Tk()
f0.title("system")
l0=Label(f0,text='veillez choisir!!',fg='blue')
l0.pack()
b0=Button(f0,text="administrator",command =administrator)
b0.pack()
b01=Button(f0,text="job seeker",command =jobseeker)
b01.pack()
f0.mainloop()





