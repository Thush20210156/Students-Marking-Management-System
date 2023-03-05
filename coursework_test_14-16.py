print('Staff version with Histogram')
print()

y=0
q=0
total=0

progress=0
module_trailer=0
module_retriever=0
exclude=0



while True:
  try:
     marks_list=[]
     PASS=int(input('Enter your total PASS credit: '))
     marks_list.append(PASS)
     if PASS not in range(0,121,20):
       print('Out of range')
       exit()
     
       
     DEFFER=int(input('Enter your total DEFER credit: '))
     marks_list.append(DEFFER)
     if DEFFER not in range(0,121,20):
       print('Out of range')
       exit()
       
     FAIL=int(input('Enter your total FAIL credits: '))
     marks_list.append(FAIL)
     if FAIL not in range(0,121,20):
       print('Out of range')
       exit()
     
  

     if PASS==120:
        print('Progress')
        progress+=1
     elif PASS==100:
        print('Progress(module trailer)')
        module_trailer+=1
     elif PASS<=80 and FAIL<=60:
        print('Do not progress-module retriever')
        module_retriever+=1
     elif 80<=FAIL<=120:
        print('Exclude')
        exclude+=1
        print()
     print('Would you like to enter another set of data ?')
     prompt=str(input('Enter \'y\' for yes or \'q \'to quit and view results: '))
     print()
     if prompt=='y':
            continue
       
     elif prompt=='q':
            break
     else:
            print('Please enter y or q to continue..!')

  except ValueError:
         print('Please enter a valid integer..!')
print('-'*80)
print('Horizontal Histogram')
print('Progress ',progress,':','*'*progress)
print('Trailer  ',module_trailer,':','*'*module_trailer)
print('Retriever',module_retriever,':','*'*module_retriever)
print('Excluded ',exclude,':','*'*exclude)
print('-'*80)

line=0

print('Progress','Trailing','Retriever','Exclude')

while(progress!=0)or(module_trailer!=0)or(module_retriever!=0)or(exclude!=0):

    if(progress!=0):
        line='  *' 
        progress=progress-1
    else:
        line=" "*5
        

    if(module_trailer!=0):
        line=line+ ' '*10+  '*'
        module_trailer= module_trailer -1
    else:
        line=line+''*11

    if(module_retriever!=0):
        line=line +' '*10+'*'
        module_retriever=module_retriever-1
    else:
        line=line+' '*11

    if(exclude!=0):
        line=line+' '*10+'*'
        exclude=exclude-1
    else:
        line=line+' '*11
    print(line)
    break

print('-'*80)

if PASS==120:
            print('Progress- ',marks_list)
elif PASS==100:
            print('Progress(module trailer)- ',marks_list)
elif PASS<=80 and FAIL<=60:
            print('Do not progress-module retriever',marks_list)
elif 80<=FAIL<=120:
            print('Exclude',marks_list)
                
              
                
        
 
             





       
       

  

       

       
    
