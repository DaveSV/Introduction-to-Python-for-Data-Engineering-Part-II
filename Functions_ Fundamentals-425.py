## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

sum_manual = 0

for element in a_list:
    sum_manual += element

print(sum_manual)
print(sum(a_list))

## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}


for c_rating in ratings:
    
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
        
print(content_ratings)

## 3. Creating Our Own Functions ##

def square(a_number):
    squared_number = a_number * a_number
    return squared_number

squared_10 = square(10)
squared_16 = square(16)

## 4. The Structure of a Function ##

def add_10(a_number):
    added_number = a_number + 10
    return added_number

add_30 = add_10(30)
add_90 = add_10(90)

## 5. Parameters and Arguments ##

def square(a_number):
    # Variable assignment step omitted
    return a_number * a_number 

squared_6 = square(6)
squared_11 = square(11)

## 6. Extract Values From Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = []

def extract(column):
    content_ratings = []
    for row in apps_data[1:]:
        content_rating = row[column]
        content_ratings.append(content_rating)
    return content_ratings
        
genres = extract(11)
print(genres)

## 7. Creating Frequency Tables ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = []

def extract(column):
    content_ratings = []
    for row in apps_data[1:]:
        content_rating = row[column]
        content_ratings.append(content_rating)
    return content_ratings
        
def freq_table(freq):
    content_ratings_freq = {}
    for c_freq in freq:
        if c_freq in content_ratings_freq:
            content_ratings_freq[c_freq] += 1
        else:
            content_ratings_freq[c_freq] = 1
    return content_ratings_freq
    
genres = extract(11)
genres_ft = freq_table(genres)
print(genres_ft)

## 8. Writing a Single Function ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


        
def freq_table(freq):
    content_ratings_freq = {}
    for row in apps_data[1:]:
        c_freq = row[freq]
        if c_freq in content_ratings_freq:
            content_ratings_freq[c_freq] += 1
        else:
            content_ratings_freq[c_freq] = 1
    return content_ratings_freq
    
ratings_ft = freq_table(7)

print(ratings_ft)

## 9. Reusability and Multiple Parameters ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(index, dataset):
    frequency_table = {}
    
    for row in dataset[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

ratings_ft = freq_table(7,apps_data)
print(ratings_ft)

## 10. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_ratings_ft = freq_table(apps_data,10)
print(content_ratings_ft)
ratings_ft = freq_table(data_set=apps_data, index=7)
print(ratings_ft)
genres_ft = freq_table(index=11, data_set=apps_data)
print(genres_ft)

## 11. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    a_list = extract(data_set, index)
    sum_list = find_sum(a_list)
    len_list = find_length(a_list)
    mean_list = sum_list / len_list
    return mean_list

avg_price = mean(apps_data,4)
print(avg_price)

## 12. Debugging Functions ##

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    a_list = extract(data_set, index)
    sum_list = find_sum(a_list)
    len_list = find_length(a_list)
    mean_list = sum_list / len_list
    return mean_list

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)