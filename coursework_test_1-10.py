#Part 1-Main Version
#-Tests 1-10--Outcomes
print('-'*10,'PART 1-MAIN VERSION','-'*10)
print()
print('Tests 1-10 -Outcomes')
print()


def outcomes():
    PASS=int(input('Please enter your credits at pass: '))
    DEFFER=int(input('Please enter your credits at defer: '))
    FAIL=int(input('Please enter your credits at fail: '))

    if PASS==120:
        print('Progress')
    elif PASS==100:
        print('Progress(module trailer)')
    elif PASS<=80 and FAIL<=60:
        print('Do not progress-module retriever')
    elif 80<=FAIL<=120:
        print('Exclude')
outcomes()

#-Tests 11-13--Validation

print('Tests 11-13 -Validation ')
print()

def validation():
 total=0

while True:
    try:
        PASS=int(input('Please enter your credits at pass: '))
        if PASS not in range(0,121,20):
            print('Out of range')
            
        DEFFER=int(input('Please enter your credits at defer: '))
        if DEFFER not in range(0,121,20):
            print('Out of range')
            
        FAIL=int(input('Please enter your credits at fail: '))
        if FAIL not in range(0,121,20):
            print('Out of range')

        if PASS==120:
            print('Progress')
            
        elif PASS==100:
            print('Progress(module trailer)')
            
        elif PASS<=80 and FAIL<=60:
            print('Do not progress-module retriever')
            
        elif 80<=FAIL<=120:
            print('Exclude')


        elif PASS+DEFFER+FAIL!=120:
            print('Total incorrect....!!!')
            
    except ValueError:
        print('Required an integer.....!!!')
        break

validation()

#-Tests 14-15--loop
print('Tests 14-15 -Loops ')
print()

progress=0
module_trailer=0
module_retriever=0
exclude=0



def loops():
    

    credit_list=[]
    list=[]

    while True:
      try:
         
         PASS=int(input('Enter your total PASS credit: '))
         if PASS not in range(0,121,20):
           print('Out of range')
           exit()
         
          
         DEFFER=int(input('Enter your total DEFER credit: '))
         if DEFFER not in range(0,121,20):
           print('Out of range')
           exit()
           
         FAIL=int(input('Enter your total FAIL credits: '))
         if FAIL not in range(0,121,20):
           print('Out of range')
           exit()

      except ValueError:
          print('Please enter a valid integer..!')
          exit()
           
    

      
         
      if PASS==120:
            credit_list=['Progress:-', PASS,',' ,DEFFER,',' ,FAIL]
            list.append(credit_list)
            print('Progress')
            progress+=1
            
            
      elif PASS==100:
            print('Progress(module trailer)')
            credit_list=['Progress(module trailer:- ',PASS,',', DEFFER ,',',FAIL]
            list.append(credit_list)
            module_trailer+=1
        

      elif PASS<=80 and FAIL<=60:
            print('Do not progress-module retriever')
            credit_list=['Module retriever:-', PASS,',', DEFFER,',',FAIL]
            list.append(credit_list)
            module_retriever+=1

      elif 80<=FAIL<=120:
            print('Exclude')
            credit_list=['Exclude:-', PASS,',', DEFFER,',', FAIL]
            list.append(credit_list)
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

loops()

#-Test 16-Histogram
print('Test 16-Histograms')
print()



    

print('Horizontal Histogram')
print('Progress ',progress,':','*'*progress)
print('Trailer  ',module_trailer,':','*'*module_trailer)
print('Retriever',module_retriever,':','*'*module_retriever)
print('Excluded ',exclude,':','*'*exclude)
print()
print('-'*60)


#Part 2-Vertical histogram
#-Test 17-Vertical histogram
print('-'*10,'PART 2-VERTICAL HISTOGRAM','-'*10)
print()
print('Test 17-Vertical HIstogram')
print()

def vertical_histogram():
    
    RESULT_COMMENTS = ['Progress', 'Trailing', 'Retriever', 'Exclude']
    print(' '.join(RESULT_COMMENTS))
    for comment_list in range(max(progress, module_trailer, module_retriever, exclude)):
        print("  {0}        {1}       {2}       {3}".format(
            '*' if comment_list < progress else ' ',
            '*' if comment_list < module_trailer else ' ',
            '*' if comment_list < module_retriever else ' ',
            '*' if comment_list < exclude else ' '
        ))

    print('-'*60)
    
vertical_histogram()

#Part 3-List/Tuple/Directory(extension)
#-Test 18-List/Tuple/Directory(extension)
print('-'*10,'PART 3-List/Tuple/Directory(extension)','-'*10)
print()
print('Test 18-List/Tuple/Directory(extension)')
print()


def List():
    for r in list:

        for c in r:
            print(c,end='')
        print()
List()


#Part 4-Text File
#-Test 19-Text File
print('-'*10,'PART 4-Text File','-'*10)
print()
print('Test 18-Text File')
print()

def text_file():
    with open('PROGRESSION.txt', 'w') as filehandle:
        for list_elements in list:
            filehandle.write('%s\n' %list_elements)
text_file()













