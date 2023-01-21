## 1. Interfering with the Built-in Functions ##

a_list = [1, 8, 10, 9, 7]
print(max(a_list))

def max(list):
    a_string = "No max value returned"
    return a_string

max_val_test_0 = max(a_list)
print(max_val_test_0)
del max

## 3. Default Arguments ##

def open_dataset(file_name='AppleStore.csv'):
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data

apps_data=open_dataset()

## 4. The Official Python Documentation ##

one_decimal=round(3.43,1)
two_decimals=round(0.231,2)
five_decimals=round(921.22252,5)

## 5. Multiple Return Statements ##

def open_dataset(file_name='AppleStore.csv',headers=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    if headers == False:
        data.pop(0)
    
    return data


apps_data = open_dataset(headers=False)

## 6. Returning Multiple Variables ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        
        return data[1:]
    else:
        data = data[:1]
        return data[0]

header = open_dataset(header=False)
apps_data=open_dataset()

## 7. More About Tuples ##

def open_dataset(file_name='AppleStore.csv'):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    

    h = data[1:]
    data = data[:1]
    a = data[0]
        
    return a, h

header, apps_data = open_dataset() 

## 9. Scopes — Global and Local ##

e = 'mathematical constant'
a_sum = 1000
length = 50