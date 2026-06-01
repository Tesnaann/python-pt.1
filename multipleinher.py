class phone:
    def call (self,number):
        print(f"calling {number}")
class camera:
    def cam(self):
        print("capturing photo")
class smartphone(phone,camera):
    def browse (self):
        print("browsing internrt")
sm=smartphone()
sm.cam()
sm.browse()







#multiple
class A:
    def __init__(self):
        print("Hello methoda")
        B.__init__(self) #only A will work if this is not written .ie,output=hello methoda
class B:
    def __init__(self):
        print("Hello methodb")
class C(A,B): #A will work first and then B 
    pass
oc=C()






