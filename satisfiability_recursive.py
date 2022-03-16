
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

#our algorithm.......
output_message = "input expression is unsatisfiable!!!"

#x is list of input variables content.
x = list()
for i in range(0, len(variables_lis)) :
    x.append(0)

def satisfi(level, variables_lis, x, input_expression) :

    _ex = input_expression
    for index, variable in enumerate(variables_lis) :
        _ex = _ex.replace("%" + variable, str(x[index]))

    if( eval(_ex) == True ) :
        print("output : set : {} = {} =====> {} =====> expression satisfied ✓".format(variables_lis,x,_ex))
    
    else :
        if(level < len(variables_lis)) :
            x[level] = 0
            satisfi(level + 1 , variables_lis, x, input_expression)
        if(level < len(variables_lis)) :
            x[level] = 1
            satisfi(level + 1 , variables_lis, x, input_expression) 
    

satisfi(0, variables_lis, x, input_expression)