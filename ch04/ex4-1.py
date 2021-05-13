# 예제 4-1 리스트를 이용한 전화번호 검색

def find_phonenumber(phonebook, name):
    for n, p in phonebook:
        if n == name:
            return p
    return None

phonebook = [
    ("John Doe", "555-555-5555"),
    ("Albert Einstein", "212-555-5555"),
]
print("John Doe's phone number is", find_phonenumber(phonebook, "John Doe"))
