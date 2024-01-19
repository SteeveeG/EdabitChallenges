# Link to Challenge: https://edabit.com/challenge/ehyZvt6AJF4rKFfXT
def uncensor(sentence="", vowels=""):
    for v in vowels:
        sentence = sentence.replace('*', v, 1)
    print(sentence)


uncensor('Wh*r* d*d my v*w*ls g*?', 'eeioeo')
uncensor('abcd', '')
uncensor('*PP*RC*S*', 'UEAE')
uncensor('Ch**s*, Gr*mm*t -- ch**s*', 'eeeoieee')
uncensor('*l*ph*nt', 'Eea')