    s = s.lower()

   
    # letters = set('abcdefghijklmnopqrstuvwxyz')
    # digits = set('0123456789')
    
    letters = set(chr(i) for i in range(ord('a'), ord('z') + 1))
    digits = set(chr(i) for i in range(ord('0'), ord('9') + 1))

   
    chars = set(s)

  
    miss_letters = letters - chars
    miss_digits = digits - chars

    result = ''.join(sorted(miss_letters)) + ''.join(sorted(miss_digits))
    print(result)