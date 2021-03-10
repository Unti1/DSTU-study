from collections import Counter

form = '(a+c)*b(a+d)*b(a+c)*'
f_form = form
# sim_val = list(f)
oper = []
val = ''
max_ind = len(form)

# Выборка выражений со скобками
while (form.find('(') >= 0)or(form.find(')') >= 0)or(form.find('*') >= 0):
    start_index = form.find('(')
    end_index = form.find(')')
    zvezd_index = form.find('*')
    
    if zvezd_index == end_index + 1:
        oper.append(form[start_index:zvezd_index+1])
        form = form[zvezd_index+1:]
    elif zvezd_index <= end_index:
        offset = end_index - zvezd_index + 2 
        oper.append(form[start_index : zvezd_index + offset])
        form = form[zvezd_index + offset :]
        print(form)
    else:
        oper.append(form[start_index:end_index+1])
        form = form[end_index+1:]
    
    if len(form) == 1:
        form = ''

form = f_form
print(oper)

# Вычет повторяющихся формул для подсчета внескобочных символов
counter = Counter(oper)
for i in oper:
    if counter[i] != 1:
        oper.remove(i)
        counter = Counter(oper)

#дописать
s = oper
for op in s:
    non_form = form.split(op)
    for i in non_form:
        if i != '':
            form = i

for i in non_form:
    if '' in non_form:
        non_form.remove('')

print(non_form)
