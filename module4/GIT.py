def palindrome(string):
    return string[::-1] == string

while True:
    string = input("¬ведите слово: ")
    if string == "stop":
        break
    if palindrome(string):
        print("True")
    else:
        print("False")