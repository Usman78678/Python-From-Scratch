#Write a program to fill in a letter template given below with name and date

letter = ''' Dear <|Name|>, 
You are selected!
<|Date|> 
Congratulations! '''

print(letter.replace("<|Name|>", "Usman").replace("<|Date|>", "05-01-2026"))