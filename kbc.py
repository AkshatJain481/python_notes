# There will be total 16 questions (16 levels)
import random
game_running = True
level1 = [" How to convert a string into a integer type in python? \n (a) parseint() \n (b) int() \n (c) covint() \n (d) none of the above"," Using which keyword in python you can show the type of a variable? \n (a) typeof() \n (b) ty() \n (c) type() \n (d) vartype()"," If \n a = \"1\" \n b = \"11\" \n then print(a+b) will give output in python:- \n (a) 111 \n (b) 12 \n (c) will give error \n (d) none of the above"]

level1_ans = ["b","c","a"]

level2 = [" If \n a = \"4\" \n b = \"2\" \n print(a**b) will give output in python:- \n (a) 16 \n (b) 8 \n (c) give error \n (d) 42"," If \n a = 4 \n b = 2 \n print(a**b) will give output in python:- \n (a) 16 \n (b) 8 \n (c) give error \n (d) 42", " Which of the following will calculate 'a' raised to the power 'b' assuming 'a' and 'b' have integer values assigned in them in python:- \n (a) a^b \n (b) a**b \n (c) importing math library then using pow(a,b) function \n (d) both (b) and (c)" ]

level2_ans = ["c","a","d"]

level3 = [" If \n a = \"Hello_World!\" \n print(a[:5]) will give output in python:- \n (a) Hello \n (b) Hello_World! \n (c) give error \n (d) none of the above ", " If \n a = \"Hello_World!\" \n print(a[-11:-5]) will give output in python:- \n (a) Hello \n (b) Hello_World! \n (c) give error \n (d) none of the above ", " If \n a = \"Hello_World!\" \n print(a[6:]) will give output in python:- \n (a) Hello \n (b) World! \n (c) give error \n (d) Hello_World! "]

level3_ans = ["a","d","b"]

level4 = [" If \n a = 5 \n b = 2 \n print(a//b) will give output in python:- \n (a) 4 \n (b) 2.5 \n (c) give error \n (d) 2 ", " If \n a = 5 \n b = 2 \n  \"print(a//b)\" will give error because:- \n (a) \"//\" is not a valid operation \n (b) Both or one variable is a string \n (c) It won't give any error \n (d) none of these ", " If \n a = 5 \n b = 2 \n printf(a//b) will give output in python:- \n (a) 4 \n (b) 2.5 \n (c) give error \n (d) 2 "]

level4_ans = ["d","c","c"]

level5 = [" If \n a = \"Hello_Everyone!!! \" \n print(a.rstrip(\"!\")) will give output in python:- \n (a) Hello_Everyone \n (b) Hello_Everyone!! \n (c) Hello_Everyone!!!! \n (d) none of the above ", " If \n a = \"Hello_Everyone\" \n print(a.replace(\"e\",\"a\")) will give output in python:- \n (a) Hallo_Evaryona \n (b) Hallo_Everyone \n (c) Hallo_avaryona \n (d) none of the above ", " If \n a = \"Hello_Everyone!!!!\" \n print(a.replace(\"!\",\"q\")) will give output in python:- \n (a) Hello_Everyoneqqqq \n (b) Hello_Everyoneq!!! \n (c) Hello_Everyone!!!q \n (d) none of the above "]

level5_ans = ["a","a","a"]

level6 = [" If \n a = \"Hello, hi, Hi, hey\" \n print(a.count(\"h\")) will give output in python:- \n (a) 2 \n (b) 4 \n (c) Error \n (d) none of the above ", " If \n a = \"Hello, hi, Hi, hey\" \n print(a.endswith(\"ey\")) will give output in python:- \n (a) True \n (b) False \n (c) Error \n (d) none of the above "," If \n a = \"Hello, hi, Hi, hey\" \n print(a.startwith(\"h\")) will give output in python:- \n (a) True \n (b) False \n (c) Error \n (d) none of the above "]

level6_ans = ["a","a","b"]

level7 = ["  "]

question_list = [level1,level2,level3,level4,level5,level6]

answer_list = [level1_ans,level2_ans,level3_ans,level4_ans,level5_ans,level6_ans]
Score =  0
Prize_money = None
i = 0
player_money = None
random_needed = True
while(game_running):
   match Score:
      case 0:
         Prize_money = "Prize Money:- 1000Rs"
         player_money = "Money Won:- 0rs"
      case 1:
         Prize_money = "Prize Money:- 2000Rs"
         player_money = "Money Won:- 1000rs"
      case 2:
         Prize_money = "Prize Money:- 3000Rs"
         player_money = "Money Won:- 2000rs"
      case 3:
         Prize_money = "Prize Money:- 5000Rs"
         player_money = "Money Won:- 3000rs"
      case 4:
         Prize_money = "Prize Money:- 10000Rs"
         player_money = "Money Won:- 5000rs"
      case 5:
         Prize_money = "Prize Money:- 20000Rs"
         player_money = "Money Won:- 10000rs"

   if(random_needed):
     random_index1 = random.randint(0,2)
   level = question_list[i]
   print(level[random_index1],"\n",Prize_money.center(142))
   print("\n",player_money.center(142))
   a = input("\nEnter answer from a-d:- ")
   if(a == "a" or a == "b" or a == "c" or a == "d"):
       b = question_list.index(level)
       ans = answer_list[b]
       random_needed = True
       if (ans[random_index1] == a):
          i = i + 1
          Score = Score + 1
          print("CORRECT!!".center(142))
          print(" ")
       else:
        print("WRONG ANSWER :( , Game over")
        print(player_money)
        game_running = False
   else:
      print("Invalid Input")
      random_needed = False 
      

      
   
  



    



