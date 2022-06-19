''' tanu is a fraud by nature
tanu wrote a python fucntion to prinmt a multiplicatiuon table of a given number and put one of the valus (randomly generated)as wrong
tanu did this to fool his classmates and them commit a mistake in a test oyu cannot tolerate this! so you d3ecided to decide to uase your python skills to counter tnu actions by writing python program
that validates tanu's multiplication table
your function should be able tpo find the wrong values in the Tanu's table and expose tanu as a fraud'

note:  tanu function returns a list of numbers like this:

tanu function input:
tanu multiplication(6)


tanu function return this output:
[6,12,26,.....60]   here 26 is the mistake in this


you have to write a function is correct (Table,number)and returns the index where tanu's function is wrong and print it to the screen if the tbale is correct'
your function return is none '''

import random
def tanumultiplication(number):
    wrong = random.randint(0, 9)
    table = [i*number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(1, 10)
    return table

def iscoorect(table,number):
    for i in range(1, 11):
        if table[i-1] != i * number:
            return i-1
    return None

if __name__ == '__main__':
    number = int(input("Enter a number: "))
    mytable = tanumultiplication(number)
    print(mytable)
    wrongIndex = iscoorect(mytable,number)
    print(f"The table is wrong at the index {wrongIndex} or you can that at position {wrongIndex+1}")


