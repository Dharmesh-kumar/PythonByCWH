class Employee:
    no_of_leaves=8
    pass

manu = Employee()
rohan =Employee()

manu.name="Manu"
manu.salary= 455
manu.role="Instructor"

rohan.name="Rohan"
rohan.salary=4554
rohan.role= "Student"
print(rohan.salary)         #object kae apne variables hai uska class se koe leena dena nhi hai
#agr apko kuch chiye jo is object ko ap class se link krao to apko uske liye class mai kuch rkhna pdega
print(Employee.no_of_leaves)     #jo ye numbr of leaves hai vo nahi kisi persnl object se hai vo employee  class se derive hokr aayi hai jo ki sbhi access kr skte hai ya to unhe objct name se access krlo  ya fir claas name se bhi acces hojati hai
#here rohan is a instance which can access the numbr of leaves in the class
#but if we want to change the numbr of leaves of only rohan by the name of object
print(Employee.__dict__) #jo ki defined attribute hota hai sb classes mai or ye dictionary define krta hai
Employee.no_of_leaves=9   #ye class se koe lena dena nhi hga fir ye apne hi ap me var form hai jo ki only for this instance ke liye use hga aage
print(Employee.__dict__)    #no_of_leaves jo hai vo Employee ki property hai jitne bhi objects bnege employee ke vo SHARE krege uske andr ke variables ko otherwise appne personal bnakr krege
print(Employee.no_of_leaves)   #it CAN NOT change here
# because Jb bhi mai rohan.no_of_leaves likhta hu to vo ek nya instance variable(rohan)object ki apni property bnata hai
#YOU CANNOT CHANGE THE VARIABLE OF CLASS BY ANY INSTANCE if you want to do so make their own variable anf=d then use it as new