I=[['3', '5', '7', '8', '9'], '1', '4', ['3', '7', '8', '9'], ['3', '6', '7', '8', '9'], ['3', '7', '8', '9'], ['1', '3', '7', '9'], '6', '2']
PR=['3','5','7','8','9']  
n=0
R=[0,1,2,3,4,5,6,7,8]
DEFAULT=list(str(123456789))

while(n<=8):
    if(len(I[n])!=1):
    
        def same_list(LST1,LST2):
            LST5=[X for X in LST1 if X in LST2]
            #LST7=[X for X in LST6 if X in LST4]
                    
            #print(n,"Function block 4 running",m,"times")
            return LST5
        R[n]=same_list(PR,I[n])
    else:
        R[n]=I[n]
    n=n+1
print("I",R)
