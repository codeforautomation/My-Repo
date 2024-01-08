
#INPUT ROW DATASET
R=[0,1,2,3,4,5,6,7,8]

R[0]=list(str(input("enter row1 ")))
R[1]=list(str(input("enter row2 ")))
R[2]=list(str(input("enter row3 ")))
R[3]=list(str(input("enter row4 ")))
R[4]=list(str(input("enter row5 ")))
R[5]=list(str(input("enter row6 ")))
R[6]=list(str(input("enter row7 ")))
R[7]=list(str(input("enter row8 ")))
R[8]=list(str(input("enter row9 ")))

r1=0;

while(r1<=8): #Represent how many times this code run

    #COLUMN DATASET
    C=[0,1,2,3,4,5,6,7,8]

    C[0]=[R[0][0],R[1][0],R[2][0],R[3][0],R[4][0],R[5][0],R[6][0],R[7][0],R[8][0]]
    C[1]=[R[0][1],R[1][1],R[2][1],R[3][1],R[4][1],R[5][1],R[6][1],R[7][1],R[8][1]]
    C[2]=[R[0][2],R[1][2],R[2][2],R[3][2],R[4][2],R[5][2],R[6][2],R[7][2],R[8][2]]
    C[3]=[R[0][3],R[1][3],R[2][3],R[3][3],R[4][3],R[5][3],R[6][3],R[7][3],R[8][3]]
    C[4]=[R[0][4],R[1][4],R[2][4],R[3][4],R[4][4],R[5][4],R[6][4],R[7][4],R[8][4]]
    C[5]=[R[0][5],R[1][5],R[2][5],R[3][5],R[4][5],R[5][5],R[6][5],R[7][5],R[8][5]]
    C[6]=[R[0][6],R[1][6],R[2][6],R[3][6],R[4][6],R[5][6],R[6][6],R[7][6],R[8][6]]
    C[7]=[R[0][7],R[1][7],R[2][7],R[3][7],R[4][7],R[5][7],R[6][7],R[7][7],R[8][7]]
    C[8]=[R[0][8],R[1][8],R[2][8],R[3][8],R[4][8],R[5][8],R[6][8],R[7][8],R[8][8]]

    #BLOCK DATASET
    B=[0,1,2,3,4,5,6,7,8]

    B[0]=[R[0][0],R[0][1],R[0][2],R[1][0],R[1][1],R[1][2],R[2][0],R[2][1],R[2][2]]
    B[1]=[R[0][3],R[0][4],R[0][5],R[1][3],R[1][4],R[1][5],R[2][3],R[2][4],R[2][5]]
    B[2]=[R[0][6],R[0][7],R[0][8],R[1][6],R[1][7],R[1][8],R[2][6],R[2][7],R[2][8]]
    B[3]=[R[3][0],R[3][1],R[3][2],R[4][0],R[4][1],R[4][2],R[5][0],R[5][1],R[5][2]]
    B[4]=[R[3][3],R[3][4],R[3][5],R[4][3],R[4][4],R[4][5],R[5][3],R[5][4],R[5][5]]
    B[5]=[R[3][6],R[3][7],R[3][8],R[4][6],R[4][7],R[4][8],R[5][6],R[5][7],R[5][8]]
    B[6]=[R[6][0],R[6][1],R[6][2],R[7][0],R[7][1],R[7][2],R[8][0],R[8][1],R[8][2]]
    B[7]=[R[6][3],R[6][4],R[6][5],R[7][3],R[7][4],R[7][5],R[8][3],R[8][4],R[8][5]]
    B[8]=[R[6][6],R[6][7],R[6][8],R[7][6],R[7][7],R[7][8],R[8][6],R[8][7],R[8][8]]


    #Processing ROW DATASET
    PR=[0,1,2,3,4,5,6,7,8]
    n=0
    while(n<=8):
        #Function block 1
        def sub_list(LST1,LST2):
            LST3=[X for X in LST1 if X not in LST2]
            #print("Function block 1 running",n,"times")
            return LST3
        DEFAULT=list(str(123456789))
        PR[n]=sub_list(DEFAULT,R[n])
        if(len(PR[n])==0):
           PR[n]=['0']
        n=n+1
        
    #Processing COLUMN DATASET
    PC=[0,1,2,3,4,5,6,7,8]
    n=0
    while(n<=8):
        #Function block 2
        def sub_list(LST1,LST2):
            LST3=[X for X in LST1 if X not in LST2]
            #print("Function block 2 running",n,"times")
            return LST3
        DEFAULT=list(str(123456789))
        PC[n]=sub_list(DEFAULT,C[n])
        if(len(PC[n])==0):
           PC[n]=['0']
        n=n+1

    #---------------------------------------------------------------------------------

    #Processing ROW-COLUMN DATASET
    A_RC=[0,1,2,3,4,5,6,7,8]

    A_RC[0]=['0','1','2','3','4','5','6','7','8']
    A_RC[1]=['0','1','2','3','4','5','6','7','8']
    A_RC[2]=['0','1','2','3','4','5','6','7','8']
    A_RC[3]=['0','1','2','3','4','5','6','7','8']
    A_RC[4]=['0','1','2','3','4','5','6','7','8']
    A_RC[5]=['0','1','2','3','4','5','6','7','8']
    A_RC[6]=['0','1','2','3','4','5','6','7','8']
    A_RC[7]=['0','1','2','3','4','5','6','7','8']
    A_RC[8]=['0','1','2','3','4','5','6','7','8']

    #print("printing A_RC value",A_RC)#unwanted

    #new block
    r2=0

    while(r2<9):#for n blocks
        #print("r2-------------------------------------------------------",r2) #check
        if(r2==0):
            n=0
            m=0
            x1=0;
            x2=2;
            y1=0;
            y2=2;
            o1=0;
            o2=0;
        elif(r2==1):
            n=0
            m=3
            x1=0;
            x2=2;
            y1=3;
            y2=5;
            o1=0;
            o2=3;
        elif(r2==2):
            n=0
            m=6
            x1=0;
            x2=2;
            y1=6;
            y2=8;
            o1=0;
            o2=6;
        elif(r2==3): #Node 2
            n=3
            m=0
            x1=3;
            x2=5;
            y1=0;
            y2=2;
            o1=0;
            o2=0;
        elif(r2==4):
            n=3
            m=3
            x1=3;
            x2=5;
            y1=3;
            y2=5;
            o1=0;
            o2=3;
        elif(r2==5):
            n=3
            m=6
            x1=3;
            x2=5;
            y1=6;
            y2=8;
            o1=0;
            o2=6;
        elif(r2==6): #Node 3
            n=6
            m=0
            x1=6;
            x2=8;
            y1=0;
            y2=2;
            o1=0;
            o2=0;
        elif(r2==7):
            n=6
            m=3
            x1=6;
            x2=8;
            y1=3;
            y2=5;
            o1=0;
            o2=3;
        elif(r2==8):
            n=6
            m=6
            x1=6;
            x2=8;
            y1=6;
            y2=8;
            o1=0;
            o2=6;
        else:
            #To prevent unwanted interruption
            n=10
            m=10
            x1=0;
            x2=0;
            y1=0;
            y2=0;
            o1=10;
            o2=10;
        
        a=0;
        while(x1<=n<=x2):
        
            while(y1<=m<=y2):
                #print("R------------------------",n,"C---------------------",m)#check
                
                if(r2==r2 and B[r2][a]=='0'):
                    #a=0;
        
                        #-------------------
                    #print(r2,a)
                    #Function block 1
                    def add_list(LST1,LST2,LST3):
                        LST4=LST1 + LST2
                        LST5=[X for X in LST3 if X in LST4]
                        #print("Function block 1 running",a,n,m,"times")#checking
                        #print("LST5",LST5)#checking
                        return LST5
                        
                    DEFAULT=list(str(123456789))
                    A_RC[r2][a]=add_list(PR[n],PC[m],DEFAULT)
                    #print("A_RC",A_RC)#checking

                else:
                    A_RC[r2][a]=B[r2][a]

                        #------------------------------------------------------------------------------
                        
    #--------------------------------------------------------------------------------------------------
                a=a+1   #determining block value position
                m=m+1
                
            m=o2;
            n=n+1
            
        n=o1;
            
        r2=r2+1 #reset for next block 
    #-------------------------------------------------------------------------------------------------

    #Processing BLOCK DATASET
    PB=[0,1,2,3,4,5,6,7,8]
    n=0
    while(n<=8):
        #Function block 3
        def sub_list(LST1,LST2):
            LST3=[X for X in LST1 if X not in LST2]
            #print("Function block 3 running",n,"times")
            return LST3
        DEFAULT=list(str(123456789))
        PB[n]=sub_list(DEFAULT,B[n])
        if(len(PB[n])==0):
           PB[n]=['0']
        n=n+1

    #Generating Hash Value of each Blocks
    HASH_B=[0,1,2,3,4,5,6,7,8]

    HASH_B[0]=[0,1,2,3,4,5,6,7,8]
    HASH_B[1]=[0,1,2,3,4,5,6,7,8]
    HASH_B[2]=[0,1,2,3,4,5,6,7,8]
    HASH_B[3]=[0,1,2,3,4,5,6,7,8]
    HASH_B[4]=[0,1,2,3,4,5,6,7,8]
    HASH_B[5]=[0,1,2,3,4,5,6,7,8]
    HASH_B[6]=[0,1,2,3,4,5,6,7,8]
    HASH_B[7]=[0,1,2,3,4,5,6,7,8]
    HASH_B[8]=[0,1,2,3,4,5,6,7,8]

    n=0;
    while(n<=8):
        m=-1
        while(m<=7):
            m=m+1
            if(B[n][m]=='0'):
                #Function block 4
                def same_list(LST1,LST2,LST3):
                    LST5=[X for X in LST1 if X in LST2]
                    LST6=[X for X in LST5 if X in LST3]
                    #LST7=[X for X in LST6 if X in LST4]
                    
                    #print(n,"Function block 4 running",m,"times")
                    return LST6
                DEFAULT=list(str(123456789))
                HASH_B[n][m]=same_list(DEFAULT,PB[n],A_RC[n][m])
            else:
                HASH_B[n][m]=B[n][m]
            if(len(HASH_B[n][m])==1):#---------------------<<<<<entering finded values>>>>>>------------------------
                HASH_B[n][m]=HASH_B[n][m][0]
        n=n+1
#---------------------------------------------------------------------------------------------------------------------    
    I=[0,1,2,3,4,5,6,7,8]

    I[0]=[HASH_B[0][0],HASH_B[0][1],HASH_B[0][2],HASH_B[1][0],HASH_B[1][1],HASH_B[1][2],HASH_B[2][0],HASH_B[2][1],HASH_B[2][2]]
    I[1]=[HASH_B[0][3],HASH_B[0][4],HASH_B[0][5],HASH_B[1][3],HASH_B[1][4],HASH_B[1][5],HASH_B[2][3],HASH_B[2][4],HASH_B[2][5]]
    I[2]=[HASH_B[0][6],HASH_B[0][7],HASH_B[0][8],HASH_B[1][6],HASH_B[1][7],HASH_B[1][8],HASH_B[2][6],HASH_B[2][7],HASH_B[2][8]]
    I[3]=[HASH_B[3][0],HASH_B[3][1],HASH_B[3][2],HASH_B[4][0],HASH_B[4][1],HASH_B[4][2],HASH_B[5][0],HASH_B[5][1],HASH_B[5][2]]
    I[4]=[HASH_B[3][3],HASH_B[3][4],HASH_B[3][5],HASH_B[4][3],HASH_B[4][4],HASH_B[4][5],HASH_B[5][3],HASH_B[5][4],HASH_B[5][5]]
    I[5]=[HASH_B[3][6],HASH_B[3][7],HASH_B[3][8],HASH_B[4][6],HASH_B[4][7],HASH_B[4][8],HASH_B[5][6],HASH_B[5][7],HASH_B[5][8]]
    I[6]=[HASH_B[6][0],HASH_B[6][1],HASH_B[6][2],HASH_B[7][0],HASH_B[7][1],HASH_B[7][2],HASH_B[8][0],HASH_B[8][1],HASH_B[8][2]]
    I[7]=[HASH_B[6][3],HASH_B[6][4],HASH_B[6][5],HASH_B[7][3],HASH_B[7][4],HASH_B[7][5],HASH_B[8][3],HASH_B[8][4],HASH_B[8][5]]
    I[8]=[HASH_B[6][6],HASH_B[6][7],HASH_B[6][8],HASH_B[7][6],HASH_B[7][7],HASH_B[7][8],HASH_B[8][6],HASH_B[8][7],HASH_B[8][8]]

    #print("print I",I)
    #print("print R",R)
#------------------------------------------------------------------------------------------------------------------
    n=0

    while(n<=8):
        m=0
        while(m<=8):


            if(len(I[n][m])!=1):

                def same_list(LST1,LST2):
                    LST3=[X for X in LST1 if X in LST2]
                    #print(n,"Function block 4 running",m,"times")
                    return LST3
                R[n][m]=same_list(PR[n],I[n][m])
            else:
                R[n][m]=I[n][m]
            m=m+1
        n=n+1

    #print("print R",R)

    r1=r1+1


print("final value is",HASH_B)
