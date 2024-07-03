
def consonant(strval):

    vowels = 'aeiouAEIOU'
    
    for char in strval:
        
        if char.isalpha and char not in vowels:
            
            yield char
        

def main():
    strval = 'Python Programming'
    mygen = consonant(strval)

    rlst = list(mygen)
    print(len(rlst))
    for v in rlst:
        print(v, end=' ')
    print()


if __name__ == '__main__':
    main()
