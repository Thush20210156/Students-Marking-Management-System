def student_version():



    try:
        Pass=int(input('Please enter your credits at pass: '))
        if Pass not in range(0,121,20):
            print('Out of range')
            exit()#Python pool website https://www.pythonpool.com/python-exit/
        defer=int(input('Please enter your credits at defer: '))
        if defer not in range(0,121,20):
            print('Out of range')
            exit()
        fail=int(input('Please enter your credits at fail: '))
        if fail not in range(0,121,20):
            print('Out of range')
            exit()

        
    except ValueError:
        print('Integer required..!')
        exit()






    if Pass==120:
        print('Progress')
        exit()
    elif Pass==100:
        print('Progress(module trailer)')
        exit()
    elif Pass<=80 and fail<=60:
        print('Do not progress-module retriever')
        exit()
    elif 80<=fail<=120:
        print('Exclude')
        exit()
    elif (Pass+defer+fail)!=120:
        print('Total incorrect....!!!')
        exit()

student_version()



