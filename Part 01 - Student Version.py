input_range = [0,20,40,60,80,100,120]

#getting user input for credits
while True:
    try:
        cr_pass = int(input('\nEnter your credits at pass: '))
        assert cr_pass in input_range
        cr_defer = int(input('Enter your credits at defer: '))
        assert cr_defer in input_range
        cr_fail = int(input('Enter your credits at fail: '))
        assert cr_fail in input_range
    except ValueError:
        print('Integer Required')
    except AssertionError:
            print('Out of Range')
    else:
        break

total = cr_pass + cr_defer + cr_fail

try:
    assert total == 120
    if cr_pass == 120:
        progress_outcome = 'Progress'
    elif cr_pass == 100:
        progress_outcome = 'Progress (module trailer)'
    elif cr_pass == 80 or cr_pass == 60:
        progress_outcome = 'Do not Progress – module retriever'
    elif cr_pass == 40:
        if cr_fail == 80:
            progress_outcome = 'Exclude'
        else:
            progress_outcome = 'Do not Progress – module retriever'
    elif cr_pass == 20:
        if cr_fail == 80 or cr_pass == 100:
            progress_outcome = 'Exclude'
        else:
            progress_outcome = 'Do not Progress – module retriever'
    elif cr_pass == 0:
        if cr_fail == 80 or cr_pass == 100 or cr_pass == 120:
            progress_outcome = 'Exclude'
        else:
            progress_outcome = 'Do not Progress – module retriever'
    print(progress_outcome)
    
except AssertionError:
    print('Total Incorrect')
    
            
