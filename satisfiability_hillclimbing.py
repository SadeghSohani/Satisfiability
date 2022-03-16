import random

#read file and counting the number of variables.
with open('input.txt','r') as file :
    input_expression = file.read().replace('\n', '')
print("input : {}".format(input_expression).replace('%',''))
#-----------------------------------------------------------------------------------

#make a list for input variables.
variables_lis = list()
for index,chr in enumerate(input_expression) :
    if(chr == '%' and not variables_lis.__contains__(input_expression[index+1])) :
        variables_lis.append(input_expression[index+1])
#-----------------------------------------------------------------------------------

#random init values.
init_vals = list()
for i in range(0, len(variables_lis)) :
    init_vals.append(random.randint(0, 1))
print("variables list are = {}".format(variables_lis))
print("first init values are = {}".format(init_vals))
#-----------------------------------------------------------------------------------

#check that if list can satisfi the expression, return true.this is solution function.
def solution(inputs,variables_list) :
    _ex = input_expression
    for index, variable in enumerate(variables_list) :
        _ex = _ex.replace("%" + variable, str(inputs[index]))
    if(eval(_ex) == True) :
        return True
    else :
        return False
#-----------------------------------------------------------------------------------

#this is score function.
def scoring(inputs, variables_list) :
    _ex = input_expression
    for index, variable in enumerate(variables_list) :
        _ex = _ex.replace("%" + variable, str(inputs[index]))
    _ex = _ex.split('and')
    counter = 0
    for clouse in _ex :
        if(eval(clouse.strip())) :
            counter = counter + 1
    return counter
#-----------------------------------------------------------------------------------

#this is hill climbing cnf satisfiability function.
def hc_cnf_satisfiability(init_vals, variables_list, limit) :
    
    if(solution(init_vals, variables_list)) :
        return "solution is {}".format(init_vals)
    else :
        s = list()
        s.extend(init_vals)
        for i in range(0,limit) :
            this_state_score = scoring(s, variables_list)
            #print(this_state_score)
            for index, value in enumerate(s) :
                s1 = list()
                s1.extend(s)
                if(s1[index]) :
                    s1[index] = 0
                else :
                    s1[index] = 1
                if(solution(s1, variables_list)) :
                    return "solution is {}".format(s1)
                elif(scoring(s1,variables_list) >= this_state_score) :
                    s.clear()
                    s.extend(s1)
                    break
                elif(index == len(s)-1) :
                    return "no solution found, last state (local maximum) is {}".format(s)
            if(i == limit - 1) :
                return "hill climbing is in a loop, no solution founded!, last state is {}".format(s)
            
print(hc_cnf_satisfiability(init_vals, variables_lis, 1000))

#input examples :
"(%x or %z) and (not %z or %y or %w) and (%y or %z) and (%x or not %z)"            
"(%x or %y) and (%w or not %l) and (not %z or not %r)"