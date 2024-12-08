def is_valid(isbn):
    isbn = [l.lower() for l in isbn if l != '-']
    if len(isbn) != 10 or not all(i.isdigit() for i in isbn[0:9]):
        return False
    if not (isbn[-1].isdigit() or isbn[-1] == 'x'):
        return False
    if 'x' in isbn[-1]:
        isbn[-1] = 10
    isbn = [int(i) for i in isbn]
    multiples = [i for i in range(1, 11)][::-1]
    return (sum([multiples[i]*isbn[i] for i in range(len(isbn))]) % 11) == 0

#is_valid("3-598-21507-A")
