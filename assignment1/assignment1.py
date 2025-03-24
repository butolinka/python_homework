# Write your code here.
def hello():
    return "Hello!"

print(hello())

def greet (name):
    return f"Hello, {name}!"
print(greet("Ivan"))

def calc(a, b, action="multiply"):
    try:
        if action == 'subtract':
            return a - b
        elif action == 'add':
            return a + b
        elif action == 'multiply':
            return a * b
        elif action == 'divide':
            return a / b
        elif action == 'modulo':
            return a % b
        elif action == 'intdivide':
            return a // b
        elif action == 'power':
            return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
print(calc(5,6, 'multiply'))

def data_type_conversion(value, type):
    try:
        if type == 'float':
            return float(value)
        elif type == 'int':
            return int(value)
        elif type == 'str':
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
print(data_type_conversion(2.0, "int"))


def grade(*args):
    
    try:
        averege=sum(args)/len(args)
        if averege>=90:
            return "A"
        elif averege>=80:
            return "B"
        elif averege>=70:
            return "C"
        elif averege>=60:
            return "D"
        elif averege<60:
            return "F"
    except TypeError:
        return "Invalid data was provided."
print(grade('three', 'blind', 'mice'))


def repeat(string, count):
    result=""
    for i in range(count):
        result+=string
    return result
print(repeat('up,',4))

def student_scores(position="best", **kwargs):
    if position == "best":
        max=0
        nameS=""
        for key, value in kwargs.items():
            if value>max:
                nameS=key
                max=value
        return nameS

    else:
        sum=0
        for key, value in kwargs.items():
            sum+=value
        averege=int(sum/len(kwargs))
        return averege
print(student_scores( Tom=75, Dick=89, Angela=91, Frank=50 ))



def titleize(string):
    words=[]
    words=string.split()
    exeptWord=["a","on","an" ,"the","of","and" ,"is","in"]

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in exeptWord:
            words[i] = word.capitalize()
    return " ".join(words)
print(titleize('a goga and a magoga'))


def hangman(secret, guess):
    guessedSecret=[]
    for i in secret:
        if i in guess:
            guessedSecret.append(i)
        else:
            guessedSecret.append("_")
    return "".join(guessedSecret)
print(hangman("difficulty","ic"))

def pig_latin(string):
    result = []
    vovel = 'aeuio'
    string=string.split(" ")
    for i in string:
        if i[0] in vovel:
            i = i+ 'ay'
        elif i[0]=="q" and i[1]=="u":
            i= i[2:]+"quay"
        elif i[0] not in vovel and i[1]=="q" and i[2]=="u":
            i=i[3:]+i[0]+i[1]+i[2]+"ay"
        elif i[0] and i[1] not in vovel:
            i=i[2:]+i[0]+i[1]+"ay"     
        else:
            i=i[1:]+i[0]+"ay"
        result.append(i)    
    return " ".join(result)
print(pig_latin("squere"))