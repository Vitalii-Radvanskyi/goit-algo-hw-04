def total_salary(path):
    path = Path(path)
    total = 0
    count = 0
    if not path.exists():
        raise FileNotFoundError
    with path.open(encoding='utf-8') as file:
        for line in file:
            try:
                name, salary = line.strip().split(',')
                total += int(salary)
                count +=1
            except ValueError:
                continue
    if count == 0:
        return 0, 0.0
    
    average = total/count
    return (total,average)


total, average = total_salary('salary.txt') # моя перевірка 
print(f'Загальна сума заробітньої платні: {total},\nСереднє значення заробітньої платні: {average}')



def get_cats_info(path):
    cats_info = []
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError
    with path.open(encoding='utf-8') as file:
        for line in file:
            try:
                cat_id, name, age =line.strip().split(',')
                cats_info.append({"cat_id":cat_id, "name":name, 'age':int(age)})
            except ValueError:
                continue
    return cats_info  


cats_list = get_cats_info('test.txt') # моя перевірка 
for line in cats_list:
    print(line)