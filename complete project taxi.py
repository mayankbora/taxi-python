
ADMIN_ID="cab"
ADMIN_PASSWORD="verna"
import time
import pickle
import os
class  vehicle:
      def inputdata(self):
            print ()
            self.taxi_name=input("\t\t\t\tenter the name of taxi\t\t\t:")
            self.regno=input("\t\t\t\tenter the registration no. of the taxi\t\t:")
            print()
            print("\t\t\t\t\tenter the following:-mini(3 seater) OR micro(4seater) OR suv(7 seater)")
            print()
            self.cab_type=input("\t\t\t\tenter the type of the taxi\t\t\t:")
            self.luggage=int(input("\t\t\t\tenter the luggage space\t\t\t:"))
            self.cab_ac=input("\t\t\t\tenter is the taxi is ac or non ac (ac/non ac)\t\t:")
            self.driver_name=input("\t\t\t\tenter the name of driver\t\t\t:")
            self.licno=int(input("\t\t\t\tenter the license no. of the taxi driver\t\t:"))
            self.contact=int(input("\t\t\t\tenter  driver phone number\t\t\t:"))
            self.status=input("\t\t\t\tenter the status\t\t\t\t:")

      def  showdata(self):
            print (self.taxi_name,"\t\t",self.regno,"\t\t",self.cab_type,"\t\t",self.luggage,"\t\t",self.cab_ac,"\t",self.driver_name,"\t\t",self.licno,"\t\t",self.status,"\t\t",self.contact)

      def show_data(self):
            print(" \t\t\t\tname of taxi is\t\t\t\t\t:",self.taxi_name)
            print(" \t\t\t\tluggage space is\t\t\t\t\t:",self.luggage)
            print(" \t\t\t\tname of driver is\t\t\t\t\t:",self.driver_name)
            print(" \t\t\t\tlicense no. of the taxi driver is\t\t\t\t:",self.licno)
            print(" \t\t\t\ttype of taxi is\t\t\t\t\t:",self.cab_type)
            print(" \t\t\t\tac type is(ac/non ac)\t\t\t\t\t:",self.cab_ac)

      def change(self):
           self.lic_no=input("\t\t\t\tenter the name of the new taxi driver\t\t:")

class  customer():
      def create(self):
           self.reg_no=input("\t\t\t\tenter the registration no. of the taxi\t\t\t\t:")
           self.location=input("\t\t\t\tenter the exact location(full address) where journey start\t\t:")
           self.time=input("\t\t\t\tenter the time to be picked up\t\t\t\t\t: ")
           self.phone=input("\t\t\t\tenter your  phone number\t\t\t\t\t:")

      
          
      def show(self):
            print ("\t\t\t\t",self.reg_no,"\t\t\t",self.location,"\t\t",self.time,"\t\t",self.phone)

      
      

      def cancel(self):
            self.reg__no=raw_input("\t\t\t\tenter the registration no. of the taxi \t\t:")


def create():
      f=open("driver.txt","ab")
      v=vehicle()
      v.inputdata()
      pickle.dump(v,f)
      print ()
      print ("\t\t\t\t\t\tYOUR TAXI HAS BEEN REGISTERED")
      f.close()
      
      
def display():
      f=open("driver.txt","rb")
      print ()
      print ("taxi name\t\tregistration no.\ttype of car\tluggage space\tac type\tdriver name\tlicense no.\t\t status\t\tphone no.")
      print ("-"*230  )
      print ()
      while True:
            try:
                  y=pickle.load(f)
                  y.showdata()
            except EOFError:
                   break
      f.close()          

def search():
      z=input("\t\t\t\tenter the car type\t\t\t:")
      q=input("\t\t\t\tyou want ac type car (enter ac/non ac)\t:")
      f=open("driver.txt","rb")
      print ("taxi name\t\tregistration no.\ttype of car\tluggage space\tac type\tdriver name\tlicense no.\t\tstatus\t\tphone no.")
      print ("-"*230)     
      while True:
            try:
                  y=pickle.load(f)
                  if y.cab_type==z and y.cab_ac==q:
                        y.showdata()
        
            except EOFError:
                  break
           
                         
      else:
          print ()
          print ("\t\t\t\t\t\tNO TAXI AVAILABLE")  
      f.close()       


     
      
def detail():
      f=open("abc.txt","rb")
      z=input("\t\t\t\tenter the registration number\t\t:")      
      print () 
      print("\t\t\t\t","-"*50,"CUSTOMER DETAILS","-"*50)
      print ()
      print ("\t\t\t\tregistration number\t\tlocation\t\t\ttime\t\tphone.no")
      while True:
            try:
                  y=pickle.load(f)
                  if y.reg_no==z:
                        y.show()
                        break
                  
             
            except EOFError:
                   break
      f.close()   
      



def create_customer():
      f=open("abc.txt","ab")
      v=customer()
      v.create()
      pickle.dump(v,f)
      print ()
      print ("\t\t\t\t\t\tTAXI BOOKED")
      f.close()
      return v.reg_no



def cancel_customer():
      f=open("abc2.txt","ab")
      v=customer()
      v.cancel()
      pickle.dump(v,f)
      print ()
      print ("\t\t\t\t\t\tTAXI CANCELLED")
      f.close()
      return v.reg__no


def payment():
    print   ()
    reg=input("\t\t\t\tenter the registration\t\t\t\t\t:")  
    f=open("driver.txt","rb")
    s=open("temp.txt","wb")
    flag=0
    while True:
            try:
                  y=pickle.load(f)
                  if y.regno==reg :
                      y.show_data()
                      y.status="available"
                      pickle.dump(y,s)
                      print ("\n")
                      location=raw_input("\t\t\t\tenter the location where journey start\t\t\t:")
                      destination=raw_input("\t\t\t\tenter the destination\t\t\t\t\t:")
                      distance=input("\t\t\t\tenter the distance in (km)\t\t\t\t:")
                      print ("\n")
                      print(" \t\t\t\tthe location where journey start is\t\t\t:",location)
                      print(" \t\t\t\tthe destination is\t\t\t\t\t:",destination)
                      print(" \t\t\t\tthe distance is\t\t\t\t\t:",distance)
                      print(" \t\t\t\ttax(GST and other taxes)\t\t\t\t:100")
                      if distance<=8:
                              if y.cab_type=="mini" and y.cab_ac=="ac":
                                  fare=(distance*10)+100
                              if y.cab_type=="mini" and y.cab_ac=="non ac":
                                  fare=(distance*8)+100
                              if y.cab_type=="micro" and y.cab_ac=="ac":
                                  fare=(distance*12)+100
                              if y.cab_type=="micro" and y.cab_ac=="non ac":
                                  fare=(distance*10)+100
                              if y.cab_type=="suv" and y.cab_ac=="ac":
                                  fare=(distance*14)+100
                              if y.cab_type=="suv" and y.cab_ac=="non ac":
                                  fare=(distance*12)+100
                      else:
                               if y.cab_type=="mini" and y.cab_ac=="ac":
                                   fare=(distance*12)+100
                               if  y.cab_type=="mini" and y.cab_ac=="non ac":
                                  fare=(distance*10)+100
                               if y.cab_type=="micro" and y.cab_ac=="ac":
                                  fare=(distance*14)+100
                               if y.cab_type=="micro" and y.cab_ac=="non ac":
                                  fare=(distance*12)+100
                               if y.cab_type=="suv" and y.cab_ac=="ac":
                                  fare=(distance*16)+100
                               if y.cab_type=="suv" and y.cab_ac=="non ac":
                                  fare=(distance*14)+100
                      print()
                      print("\t\t\t\ttotal fare is\t\t\t\t\t:",fare)
                      flag+=1
                  else:
                        pickle.dump(y,s)
            
            except EOFError:
                  if flag==0:
                        print()
                        print("\t\t\t\t\t\tINVALID REGISTRATION")
                  break
    
    f.close()
    s.close()
    os.remove("driver.txt")
    os.rename("temp.txt","driver.txt")
    return reg

def dele(reg):
    f=open("abc.txt","rb")
    s=open("temp1.txt","ab")
    while True:
            try:
                  a=pickle.load(f)
                  
                  if a.reg_no!=reg:
                        pickle.dump(a,s)
                  
                  
                      
            except EOFError:
                  break
    f.close()
    s.close()
    os.remove("abc.txt")
    os.rename("temp1.txt","abc.txt")

def dele2(reg):
    f=open("abc2.txt","rb")
    s=open("temp1.txt","ab")
    while True:
            try:
                  a=pickle.load(f)
                  
                  if a.reg_no!=reg:
                        pickle.dump(a,s) 
                  
                  
                                        
            except EOFError:
                  break
    f.close()
    s.close()
    os.remove("abc2.txt")
    os.rename("temp1.txt","abc2.txt")

def modify(regno):
    f=open("driver.txt","rb")
    s=open("temp.txt","wb")
    while True:
            try:
                  a=pickle.load(f)
                  
                  if a.regno==regno:
                        a.status="booked"
                        pickle.dump(a,s)
                  else:
                        pickle.dump(a,s)
                  
                  
                      
            except EOFError:
                  break
    f.close()
    s.close()
    os.remove("driver.txt")
    os.rename("temp.txt","driver.txt")
    
    
def cancel(regno):
    f=open("driver.txt","rb")
    s=open("temp.txt","wb")
    while True:
            try:
                  a=pickle.load(f)
                  
                  if a.regno==regno:
                        a.status="available"
                        pickle.dump(a,s)
                  else:
                        pickle.dump(a,s)
            except EOFError:
                  break
    f.close()
    s.close()
    os.remove("driver.txt")
    os.rename("temp.txt","driver.txt")



       
      
class user:
        def __init__(self):
                self.q=0
        def inputdata(self):
                self.name=input('\t\t\t\tEnter Your Name\t\t:')
                
                while True:
                        self.email=input("\t\t\t\tEnter Your E-mail\t\t:")
                        X=self.email.split('@')
                        if X[-1][5:]!='.com':
                                print()
                                print('\t\t\t\t\t\tINVALID EMAIL')
                                print()
                        
                        else:
                                break
                self.q=0
        def username(self):
                self.userId=input('\t\t\t\tEnter Your USERNAME\t:')
                self.password=input('\t\t\t\tEnter Your password\t\t:')
                
def signup1():
        print()
        print("\t\t\t\t\t\tSIGN-UP")
        print()
        o=user()
        o.inputdata()
        o.username()
        x=0
        while True:
                x=check(o)
                if x==1:
                        print()
                        print("\t\t\t\t\t\tuser name already exist try another one")
                        break
                else:
                        p=open('login.txt','ab')
                        pickle.dump(o,p)
                        print()
                        print ("\t\t\t\t\t\tSIGN-UP SUCCESSFUL")
                        p.close()
                        break
def signup2():
        print()
        print("\t\t\t\t\t\tSIGN-UP")
        print()
        o=user()
        o.inputdata()
        o.username()
        x=0
        while True:
                x=check(o)
                if x==1:
                        print()
                        print("\t\t\t\t\t\tuser name already exist try another one")
                        break
                else:
                        p=open('login2.txt','ab')
                        pickle.dump(o,p)
                        print()
                        print ("\t\t\t\t\t\tSIGN-UP SUCCESSFUL")
                        p.close()
                        break                   
        

def check(o):
          p=open('login.txt','rb')
          while True:
                try:
                        x=pickle.load(p)
                        if x.userId==o.userId :
                                return 1
                            
                except EOFError:
                        break
          p.close()

        
def check2(o):
          p=open('login2.txt','rb')
          while True:
                try:
                        x=pickle.load(p)
                        if x.userId==o.userId :
                                return 1
                            
                except EOFError:
                        break
          p.close()



def login1():
    login_id=input("\t\t\t\tEnter Your Login ID\t\t:")
    password=input("\t\t\t\tEnter Your Password\t\t:")
    p=open('login.txt','rb')

    flag=0
    while True:
          try:
                  x=pickle.load(p)
                  if x.userId==login_id and x.password== password:
                      time.sleep(2)
                      print()
                      print("\t\t\t\t\t\tLOGIN SUCCESSFULLY")
                      driver()
                      flag+=1
                      break
             
          except EOFError:
                if flag==0:
                      print()
                      print("\t\t\t\t\t\tINVALID ID")
                break

    p.close()




def login2():
          login_id=input("\t\t\t\tEnter Your Login ID\t\t:")
          password=input("\t\t\t\tEnter Your Password\t\t:")
          p=open('login2.txt','rb')
          flag=0
          while True:
                try:
                        x=pickle.load(p)
                        if x.userId==login_id and x.password== password:
                            time.sleep(2)
                            print()
                            print("\t\t\t\t\t\tLOGIN SUCCESSFUL")
                            customer_care()
                            flag+=1
                            break
                except EOFError:
                        if flag==0:
                              print()
                              print("\t\t\t\t\t\tINVALID ID")
                        break

             
          p.close()       

            
def customer_care():
    while True:
        print ("\n")
        print ("\n")
        print("\t\t\t\t","*"*70)
        print("\t\t\t\t\t\t\tWELCOME  AS CUSTOMER TO THE TAXI SERVICE")
        print("\t\t\t\t","*"*70)
        print("\t\t\t\t\t\t\t1.SEE ALL THE  TAXIS")
        print("\t\t\t\t\t\t\t2.BOOK A TAXI")
        print("\t\t\t\t\t\t\t3.CANCELTHE BOOKED TAXI")
        print("\t\t\t\t\t\t\t4.SEARCH FOR A DESIRED TAXI")
        print("\t\t\t\t\t\t\t5.LOGOUT")
        print("\t\t\t\t","*"*70)
        print ("\n")
        print ("\n")
        choice=int(input("\t\t\t\t\tENTER THE CHOICE\t\t:"))
        print()
        if choice==1:
              display()
        if choice==2:
              a=create_customer()
              modify(a)
              
        if choice==3:
              a=cancel_customer()
              cancel(a)
              dele(a)
              
        if choice==4:
              search()
              
        if choice==5:
              time.sleep(2)
              print()
              print("\t\t\t\t\t\tLOG OUT SUCCESSFULLY")
              break
        

def remove_detail():
    
    f=open("driver.txt","rb")
    s=open("remove.txt","ab")
    reg=input("\t\t\t\tenter registration number of taxi to be removed\t\t:")
    while True:
            try:
                  a=pickle.load(f)
                  if a.regno!=reg:
                        pickle.dump(a,s)
                  if a.regno==reg:
                        print()
                        print ("\t\t\t\t\t\tREMOVED SUCCESSFULLY")
                        
                        
            except EOFError:
                  break
                 
      
    f.close()
    s.close()
    os.remove("driver.txt")
    os.rename("remove.txt","driver.txt")
    
def update():
    f1=open("driver.txt","rb")
    f2=open("temp1.txt","wb")
    x=int(input("\t\t\t\tenter the license no. to be updated\t\t:"))
    while True:
        try:
            obj=pickle.load(f1)
            if obj.licno!=x:
                pickle.dump(obj,f2)
       

            if obj.licno==x:
                z=input("\t\t\t\tenter the name of new driver\t\t\t:")
                q=int(input("\t\t\t\tenter the license number of new driver\t\t:"))
                l=int(input("\t\t\t\tenter the phone no. of new driver\t\t\t:"))
                obj.driver_name=z
                obj.licno=q
                obj.contact=l
                pickle.dump(obj,f2)
                print()
                print ("\t\t\t\t\t\t DRIVER DETAILS UPDATED")


        except EOFError:
             break
    f1.close()
    f2.close()
    os.remove("driver.txt")
    os.rename("temp1.txt","driver.txt")        


def admin():
    while True:
        print ("\n")
        print ("\n")
        print("\t\t\t\t","*"*70)
        print("\t\t\t\t\t\t\tWELCOME  ADMIN ")
        print("\t\t\t\t","*"*70)
        print("\t\t\t\t\t\t\t1.SEE ALL THE  TAXIS")
        print("\t\t\t\t\t\t\t2.ADD DETAILS OF TAXI")
        print("\t\t\t\t\t\t\t3.SEARCH FOR A PARTICULAR TAXI")
        print("\t\t\t\t\t\t\t4.REMOVE DETAILS OF TAXI")
        print("\t\t\t\t\t\t\t5.UPDATE DETAILS OF DRIVER")
        print("\t\t\t\t\t\t\t6.LOGOUT")
        print("\t\t\t\t","*"*70)
        print ("\n")
        print ("\n")
        choice=int(input("\t\t\t\t\tEnter The Choice\t\t:"))
        print()
        if choice==1:
              display()

        if choice==2:
             create()
             
        if choice==3:
              search()
             
        if choice==4:
            remove_detail()

        if choice==5:
              update()
              
             
            
        if choice==6:
              time.sleep(2)
              print()
              print("\t\t\t\t\t\tLOG OUT SUCCESSFULLY")
              break


def driver():
     while True:
        print ("\n")
        print ("\n")
        print("\t\t\t\t","*"*70)
        print("\t\t\t\t\t\t\tWELCOME  AS DRIVER TO THE TAXI SERVICE")
        print("\t\t\t\t","*"*70)
        print("\t\t\t\t\t\t\t1.PROCEED FOR PAYMENT")
        print("\t\t\t\t\t\t\t2.CUSTOMER DETAILS")
        print("\t\t\t\t\t\t\t3.LOGOUT")
        print("\t\t\t\t","*"*70)
        print ("\n")
        print ("\n")
        choice=int(input("\t\t\t\t\tEnter The Choice\t\t:"))
        print()
              
        if choice==1:
              a=payment()
              dele(a)
        if choice==2:

               detail()
            
        if choice==3:
              time.sleep(2)
              print()
              print("\t\t\t\t\t\tLOG OUT SUCCESSFULLY")
              break
                
def signup():
     while True:
        print ("\n")
        print ("\n")
        print("\t\t\t\t","*"*70)
        print("\t\t\t\t\t\t\tWELCOME TO SIGN UP  IN THE TAXI SERVICE")
        print("\t\t\t\t","*"*70)
        print("\t\t\t\t\t\t\t1.SIGN UP AS DRIVER")
        print("\t\t\t\t\t\t\t2.SIGN UP AS CUSTOMER")
        print("\t\t\t\t\t\t\t3.LOGOUT")
        print("\t\t\t\t","*"*70)
        print ("\n")
        print ("\n")
        choice=int(input("\t\t\t\t\tEnter The Choice\t\t:"))
        print()
        if choice==1:
             signup1()
             
        if choice==2:
             signup2()
             
        if choice==3:
              time.sleep(2)
              print()
              print("\t\t\t\t\t\tLOG OUT SUCCESSFULLY")
              break              

while True:
      print ("\n")
      print ("\n")
      print("\t\t\t\t","*"*70)
      print("\t\t\t\t\t\t\tWELCOME TO THE TAXI SERVICE")
      print("\t\t\t\t","*"*70)
      print("\t\t\t\t\t\t\t1.LOGIN AS ADMIN")
      print("\t\t\t\t\t\t\t2.LOGIN AS DRIVER")
      print("\t\t\t\t\t\t\t3.LOGIN AS CUSTOMER")
      print("\t\t\t\t\t\t\t4.SIGN UP")
      print("\t\t\t\t\t\t\t5.Exit")
      print("\t\t\t\t","*"*70)
      print ("\n")
      print ("\n")
      n=int(input("\t\t\t\t\tEnter The Choice For Login\t\t:"))
      print()
      count=0
      if (n==1):
            while count<3:
                  login_id=input("\t\t\t\tEnter Your Login ID\t\t:")
                  password=input("\t\t\t\tEnter Your Password\t\t:")
                  if (login_id==ADMIN_ID   and password==ADMIN_PASSWORD):
                        time.sleep(2)
                        print()
                        print ("\t\t\t\t\t\tLOGIN SUCCESSFUL")
                        count=4
                        admin()
                        break
                  else:
                        count+=1
                  if count>3:
                        break               
                        print()
                        print ("\t\t\t\t\t\tRE ENTER THE CORRECT ID AND PASSWORD")
            else:
                  print  ()
                  print ("\t\t\t\t\t\tLOGIN AFTER 10 MINUTES")
                  time.sleep(10)
      if (n==2):
            login1()
      if (n==3):
            login2()
      if (n==4):
            signup()
      if (n==5):
            print("\n")
            print("\t\t\t\t","*"*70)
            print("\t\t\t\t\t\t\t\tTHANK YOU ")
            print("\t\t\t\t\t\t\t\tVISIT AGAIN")
            print("\t\t\t\t","*"*70)
            break
        
        






            



                      
    
    

            
        




      
