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
_ex = ""

#x is list of input variables content.
x = list()
for i in range(0, len(variables_lis)) :
    x.append(0)

for i in range(0, 2**len(variables_lis)) :
    
    _ex = input_expression
    binary_number = bin(i)
    binary_number = binary_number[2:]
    
    for index in range(0, len(binary_number)) :
        x[(len(x)-1)-index] = int(binary_number[(len(binary_number)-1)-index])

    for index, variable in enumerate(variables_lis) :
        _ex = _ex.replace("%" + variable, str(x[index]))

    if(eval(_ex) == True) :
        output_message = "set : {} = {} =====> {} =====> expression satisfied ✓".format(variables_lis,x,_ex)
        break


print("output : {}".format(output_message))