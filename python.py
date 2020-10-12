#[1]
the_list=[45,223,87,56,1,4,89]
the_list
print(the_list[6])
#2
print(the_list[5])
#[3]
the_list2=[9,24,85,12,89,554,91]
new_list= the_list + the_list2
new_list
print(new_list)
#[4]
first=new_list[0]
last=new_list[-1]
new_list[0]=last
new_list[-1]=first
print(new_list)