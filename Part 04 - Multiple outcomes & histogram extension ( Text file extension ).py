
print('Staff version with histogram (Text File) \n')

#assigning variables
cr_pass = int(0)
cr_defer = int(0)
cr_fail = int(0)

progress_st = []
trailer_st = []
retriever_st = []
exclude_st = []

progress_input = {}

progression_data = []

#list of inputs a user can give
input_range = [0,20,40,60,80,100,120]

def main():
    progress_outcome = str()
    """Getting the user input for credits, validating the user inputs and display the progress outcome"""
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
        #calculating and displaying the progression outcome
        if cr_pass == 120:
            progress_outcome = 'Progress'
            progress_st.append('*')
            
        elif cr_pass == 100:
            progress_outcome = 'Progress (module trailer)'
            trailer_st.append('*')
            
        elif cr_pass == 80 or cr_pass == 60:
            progress_outcome = 'Module retriever'
            retriever_st.append('*')
            
        elif cr_pass == 40:
            if cr_fail == 80:
                progress_outcome = 'Exclude'
                exclude_st.append('*')
            else:
                progress_outcome = 'Module retriever'
                retriever_st.append('*')
                
        elif cr_pass == 20:
            if cr_fail == 80 or cr_fail == 100:
                progress_outcome = 'Exclude'
                exclude_st.append('*')
            else:
                progress_outcome = 'Module retriever'
                retriever_st.append('*')
                
        elif cr_pass == 0:
            if cr_fail == 80 or cr_fail == 100 or cr_fail == 120:
                progress_outcome = 'Exclude'
                exclude_st.append('*')
            else:
                progress_outcome = 'Module retriever'
                retriever_st.append('*')

        #storing input progression data in a text file
        temp_inputs = ()
        temp_inputs = f'{progress_outcome} - {cr_pass}, {cr_defer}, {cr_fail}'

        f = open('progression_data.txt', 'a')
        f.write(f'{temp_inputs}\n')
        f.close()
                
    except AssertionError:
        print('Total Incorrect')
                            
    print(progress_outcome,'\n')


main()

#getting an input from the user to enter multiple outcomes or to quit
while True:
    
    answer = str(input('would you like to enter a another set of data?\nEnter \'y\' for yes or \'q\' to quit and view results:')).lower()
    if answer == 'y':

        main()
            
    elif answer == 'q':

        total_count = len(progress_st) + len(trailer_st) + len(retriever_st) + len(exclude_st)

        #horizontal histogram
        print('\n'+'_'*60)

        print('\nHorizontal Histogram')
        print('Progress', len(progress_st),'  :',*progress_st)
        print('Trailer', len(trailer_st),'   :',*trailer_st)
        print('Retriever', len(retriever_st),' :',*retriever_st)
        print('Exclude', len(exclude_st),'   :',*exclude_st,'\n')

        print(total_count, ' outcomes in total')

        print('\n'+'_'*60)

        #vertical histogram
        len_list = [ len(progress_st), len(trailer_st), len(retriever_st), len(exclude_st)]

        print('\nProgress',len(progress_st),' | Trailing',len(trailer_st),' | Retriever',len(retriever_st),' | Excluded',len(exclude_st))
        
        for i in range(max(len_list)):
            try:
                print(f'   {progress_st[i]}             ', end="")
            except IndexError:
                print(f'                 ', end="")
            try:
                print(f'{trailer_st[i]}              ', end="")
            except IndexError:
                print(f'               ', end="")
            try:
                print(f'{retriever_st[i]}              ', end="")
            except IndexError:
                print(f'               ', end="")
            try:
                print(f'{exclude_st[i]}\t')
            except IndexError:
                print(f' \t')

        #input progression data
        print()        
        f = open('progression_data.txt', 'r')
        for i in f:
            print (i, end='')

        break

    else:
        print('Invalid option!\n')
        continue
   


















 
