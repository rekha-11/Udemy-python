def student_discount(sp):
    return sp-(sp/100)*10

def regular_discount(sp):
    return sp-(sp/100*5)
sp = 100
student = input("are you a student? y/n ")
if(student == "y"):
    dis_sp= student_discount(sp)
    print(dis_sp)
else:
    dis_sp = regular_discount(student_discount(sp))
    print(dis_sp)




