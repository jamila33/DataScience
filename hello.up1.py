

# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.

def is_odd (number: int) -> bool:
    """
    Skriv beskrivning här.
    """
    truel_or_false = number % 2 == 1
    return truel_or_false  



print(is_odd(5))  # Output: True
print(is_odd(10)) # Output: False


# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

from typing import List
from unittest import result

def sum_list(numbers: List[int]) -> int:
    """
    skriv beskrivning här.
    """
    return sum(numbers)

resultat = sum_list([10, 20, 30])
print(resultat)  # Output: 60




# Uppgift 3
# Hitta det största talet i en lista

from typing import List
def max_in_list(numbers: List[int]) -> int:
    """
    Skriv beskrivning här.
    """
    return max(numbers)
resultat = max_in_list([10, 20, 30, 40, 50])
print(resultat)  # Output: 50


# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.


from typing import List

from typing import List

def fibonacci(n: int) -> List[int]:
    """
    Skriv beskrivning här.
    """
    if n <= 0:
        return [] 
    elif n == 1:
        return [0]  
    elif n == 2:
        return [0, 1] 
    else: 
        fib_sequence = [0, 1]
        for i in range(2, n ):
             fib_sequence.append(fib_sequence[i-1]+fib_sequence[i-2] )
            
        
    return fib_sequence  
resultat = fibonacci(10)
print(resultat)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]




# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.


def filter_odd(numbers):
    """
    Skriv beskrivning här.
    """
    return [num for num in numbers if num % 2 == 0]
resultat = filter_odd([1, 2, 3, 4, 5, 6])
print(resultat)  # Output: [2, 4, 6]


# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.


def multiplication_table(n, limit):
    """
    Skriv beskrivning här.
    """
    return [n * i for i in range(1, limit + 1)]
resultat = multiplication_table(4, 6)
print(resultat)  # Output: [4, 8, 12, 16, 20, 24]



# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.



def validate_password(password: str) -> bool:
    """
    Skriv beskrivning här.
    """
    if len(password) < 8:
        return False  
    if not any(char.isdigit() for char in password):
        return False  
    return True  
def test_funktion():
    assert validate_password("jamila333") == True  
    assert validate_password("short") == False      
    assert validate_password("password1") == True   


    # Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.


def count_letters(string):
    """
    Skriv beskrivning här.
    """
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1  
        else:
            letter_count[letter] = 1  
    return letter_count
resultat = count_letters("jordgubbe")
print(resultat)  # Output: {'j': 1, 'o': 1, 'r': 1, 'e': 1, 'g': 1, 'u': 1, 'b': 2, 'e': 1}


# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).



def is_palindrome(string):
    """
    Skriv beskrivning här.
    """
    cleaned_string = string.lower().replace(" ", "")
    
    return cleaned_string == cleaned_string[::-1]
print(is_palindrome("Jag ska komma sen"))  # Output: True
print(is_palindrome("hello"))    # Output: False




# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.


def celsius_to_fahrenheit(celsius):
    """
    Skriv beskrivning här.
    """
    return (celsius * 9/5) + 32
print(celsius_to_fahrenheit(15))  
print(celsius_to_fahrenheit(30))  


# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.


from pydoc import text

def word_count(text):
    """
    antalet ord i den givna texten.
    """
    print("hello world")  # Output: 5
print(" Python   är   kul! ")  # Output: 3


word_count("   Ett   mellanslag   ")   # Returnerar 2 
word_count("Hej\tvärld\nny")           # Returnerar 3 


# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.


def test_create_student_register():
    """
    Testar funktionen create_student_register.
    """
    students_list = [("Lina", 29), ("Oskar", 32)]
    result = create_student_register(students_list)  
    assert result == {'Lina': 29, 'Oskar': 32}
    


