def arithmetic_arranger(problems, resolved=False):
    # Error handling Is Okey
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        for i in problems:
            a = i.split()
            if not '-' in a and not '+' in a:
                return "Error: Operator must be '+' or '-'."
            elif len(a[0]) > 4 or len(a[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            elif a[0].isdigit() == False or a[2].isdigit() == False:
                return "Error: Numbers must only contain digits."
    
    final_bot = ''
    final_top = ''
    final_dots = ''
    problems_spaces = '    '
    if resolved:
        final_res = ''
    for problem in problems:
        array = problem.split() # split the array
        numTop = array[0] # array[0] Top Number
        simbol = array[1] # array[1] Simbol
        numBot = array[2] # array[2] Bottom Number
        dots = space = ''
        if len(numTop) > len(numBot):
            numTop = numTop.rjust(len(numTop)+2) 
            space =  space.rjust(len(numTop) - len(numBot) - 1)
            numBot = simbol + space + numBot 
        elif len(numBot) > len(numTop):
            numBot = simbol + ' ' + numBot 
            space = space.rjust(len(numBot) - len(numTop))
            numTop = space + numTop
        else:
            numBot = simbol + ' ' + numBot   
            space = space.rjust(len(numBot) - len(numTop))
            numTop = space + numTop
        if resolved:
            res = str(eval(array[0] + array[1] + array[2]))
            space = ''
            space = space.rjust(len(numBot) - len(res))
            res = space + res
            if(problem == problems[len(problems) - 1]):
                final_res += res 
            else:
                final_res += res + problems_spaces
        
        dots = dots.rjust(len(numBot),'-')
        if(problem == problems[len(problems) - 1]):
            final_bot += numBot
            final_top += numTop
            final_dots += dots
        else:
            final_bot += numBot + problems_spaces
            final_top += numTop + problems_spaces
            final_dots += dots + problems_spaces
    
    
    if resolved:
        #arranged_problems = '{}\n{}\n{}\n{}'.format(final_top,final_bot,final_dots,final_res)
        arranged_problems = final_top + '\n' + final_bot + '\n' + final_dots + '\n' + final_res
    else:
        #arranged_problems = '{}\n{}\n{}'.format(final_top,final_bot,final_dots)
        arranged_problems = final_top + '\n' + final_bot + '\n' + final_dots 

    return print(arranged_problems)

arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'])
