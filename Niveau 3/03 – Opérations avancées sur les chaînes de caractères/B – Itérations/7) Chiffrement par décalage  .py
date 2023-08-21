for page in range(2, int(input())+1):
   if page%2 == 0:
      decalage = -3*page
   else:
      decalage = 5*page
   for char in input():
      if char.isalpha():
         if char.islower():
            charNumber = (ord(char.upper())-65 + decalage) % 26
            char = chr(charNumber+65).lower()
         else:
            charNumber = (ord(char)-65 + decalage) % 26
            char = chr(charNumber+65)
      print(char, end="")
   print()