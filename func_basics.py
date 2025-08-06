def abc(a=None,c=None,b=None,*args,**kwargs):   #dynamically typed lang is slower cus datatype declaration is not made INTV Q
    pass

# abc(1,c=2,b=2)  
#you cant do abc(c=2,1,b=2)  

# abc(1,2,3,4,5,i=11,j=10,k=10)

int_list = list()
str_list = list()
float_list = list()

def random_func(*args,**kwargs):
    def child_func(arg):
        if isinstance(arg,int):
                int_list.append(arg)
        elif isinstance(arg,str):
                str_list.append(arg)
        elif isinstance(arg,float):
                float_list.append(arg)
        else:
                print('none matched')
        
    for i in args:
            child_func(i)
        
    for key,val in kwargs.items():
            child_func(val)
            

       
       
random_func(1,2,'e',1.24,i='1',j=70.99,name='einul',sign='aquarius')

print(int_list,str_list,float_list)
  
    
    
    


random_func(12,'einul',14.35)

