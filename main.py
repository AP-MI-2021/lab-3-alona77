def show_menu():
    print("1. Citire lista")
    print("2. Det cea mai lunga secv cu prop ca sunt palindroame")
    print("3. Det cea mai lunga subsecv cu prop ca au acelasi nr de div")
    print("4. Det cea mai lunga subsecv cu propr ca toate sunt pare")
    print("5. Exit")

def read_list():
    lst = []
    lst_str = input ("Introduceti numerele prin spatiu:")
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def is_palindrome(n):
    """
    determina daca un nr este palindrom sau nu 
    """
    c = n 
    p = 0
    while n >= 1:
         p = p * 10 + n % 10
         n = n // 10
    if c == p :
        return True
    else:
        return False

def get_longest_all_palindromes(lst):
    """
    determina subsecventa cea mai lunga de palindroame
    """
    l = len(lst)
    result = []
    for i in range (l):
        for j in range (i,l):
            all_palindromes = True
            for num in lst[i:j+1]:
                if is_palindrome(num) == False:
                    all_palindromes = False
                    break
            if all_palindromes:
                if j-i+1 >len(result):
                    result = lst[i:j+1]
    return result



def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([121,35, 676, 181,]) == [676, 181]
    assert get_longest_all_palindromes([1, 56, 898, 101, 2]) == [898, 101, 2]
    assert get_longest_all_palindromes([56, 12, 22, 909]) == [22, 909]


def nr_div(n):
    """
    determina numarul de divizori ai unui nr
    """
    k = 0
    copy = n
    for i in range (1,copy+1):
        if copy % i == 0:
            k = k + 1
    return k

def get_longest_same_div_count(lst):
    """
    determina cea mai lunga subsecv de numere care au acelasi nr de divizori
    """
    l = len(lst)
    result = []
    for i in range (l):
        for j in range (i,l):
            k = nr_div(lst[i])
            same_div_count = True
            for num in lst[i:j+1]:
                if nr_div(num) != k :
                    same_div_count = False
                    break
            if same_div_count:
                if j-i+1 >len(result):
                    result = lst[i:j+1]
    return result

def test_get_longest_same_div_count():
    assert get_longest_same_div_count([12, 45, 7, 8]) == [12, 45]
    assert get_longest_same_div_count([6, 8, 10, 3, 13]) == [6, 8, 10]
    assert get_longest_same_div_count([14, 8, 7, 99]) == [14, 8]


def get_longest_all_even(lst):
    l = len(lst)
    result = []
    for i in range (l):
        for j in range (i,l):
            all_even = True
            for num in lst[i:j+1]:
                if num % 2 != 0:
                    all_even = False
                    break
            if all_even:
                if j-i+1 >len(result):
                    result = lst[i:j+1]
    return result

def test_get_longest_all_even():
    assert get_longest_all_even([2,4, 7, 9 ,13])== [2,4]
    assert get_longest_all_even([11, 12, 16, 8, 10])==[12, 16, 8, 10]
    assert get_longest_all_even([2, 7, 59, 13, 19]) == [2]


def main():
    lst=[]
    while True:
        show_menu()
        opt = int(input("Introduceti optiunea: "))
        if opt == 1 :
            lst = read_list()
        elif opt == 2:
            print("Cea mai lunga subsecv de palindroame este ",  get_longest_all_palindromes(lst))
        elif opt == 3:
            divizor= get_longest_same_div_count(lst)
            print("Cea mai lunga subsec de nr cu acelasi nr de div este  ", divizor)
        elif opt == 4:
            print("cea mai lunga subsecv de nr pare este", get_longest_all_even(lst))
        elif opt == 5:
            break
        else:
            print("Optiunea invalida")

if __name__ == '__main__':
    test_get_longest_all_palindromes()
    test_get_longest_same_div_count()
    test_get_longest_all_even()
    main ()

