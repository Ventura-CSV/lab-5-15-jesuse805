
def consonant(strval):
    vowelsP = 'aeiouAEIOU'
    for char in strval:
        if char.isalpha and char not in vowelsP:
            yield char
        

def main():
    strval = 'PythonProgramming'
    mygen = consonant(strval)

    rlst = list(mygen)
    print(len(rlst))
    for v in rlst:
        print(v, end=',')
    print()


if __name__ == '__main__':
    main()
