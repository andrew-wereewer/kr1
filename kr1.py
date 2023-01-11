print("КРЕСТИКИ/НОЛИКИ ") 
 
pole = list(range(1,10)) 
 
def izo_pole(pole): 
   print("-" * 13) 
   for i in range(3): 
      print("|", pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3], "|") 
      print("-" * 13) 
 
def take_input(chey_hod): 
   valid = False 
   while not valid: 
      hod = input("ХОД - " + chey_hod+"? ") 
      try: 
         hod = int(hod) 
      except: 
         print("ВВЕДИТЕ ЧИСЛО") 
         continue 
      if hod >= 1 and hod <= 9: 
         if(str(pole[hod-1]) not in "XO"): 
            pole[hod-1] = chey_hod 
            valid = True 
         else: 
            print("ЗАНЯТА") 
      else: 
        print("ВВЕДТЕ ЧИСЛО ОТ  до 9 ") 
 
def proverka(pole): 
   win_combo = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) 
   for each in win_combo: 
       if pole[each[0]] == pole[each[1]] == pole[each[2]]: 
          return pole[each[0]] 
   return False 
 
def main(pole): 
    a = 0 
    win = False 
    while not win: 
        izo_pole(pole) 
        if a % 2 == 0: 
           take_input("X") 
        else: 
           take_input("O") 
        a += 1 
        if a > 4: 
           tmp = proverka(pole) 
           if tmp: 
              print(tmp, "ПОБЕДА") 
              win = True 
              break 
        if a == 9: 
            print("НИЧЬЯ") 
            break 
    izo_pole(pole) 
	
main(pole)