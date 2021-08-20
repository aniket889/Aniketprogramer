#2write a program to input marks of five subjet physics chemistry biology maths and computer calculate percentage and grade according to fololowing:
marks1=(float)(input("enter the marks of physics"))
marks2=(float)(input("enter the marks of biology"))
marks3=(float)(input("enter the marks of chemistry"))
marks4=(float)(input("enter the marks of maths"))
marks5=(float)(input("enter the marks of computer"))

total_ob=marks1+marks2+marks3+marks4+marks5

per=(total_ob/500)*100

print("grade is",per)
if "per"<=90:
    print("grade A")
elif "per"<=80:
    print("grade B")
elif "per"<=70:
    print("grade C")
elif "per"<=60:
    print("grade D")
elif "per"<=40:
    print("grade E")
else :
    print("grade F")
    