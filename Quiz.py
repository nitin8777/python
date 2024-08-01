qustions=["Q)1 Who is the father of C language?","Q)2 Which of the following is not a valid C variable name?","Q)3 All keywords in C are in __?","Q)4 Which is valid C expression?"]

options=[" a) Steve Jobs\n b) James Gosling\n c) Dennis Ritchie\n d) Rasmus Lerdorf"," a) int number;\n b) float rate;\n c) int variable_count;\n d) int $main\n"," a) LowerCase letters\n b) UpperCase letters\n c) CamelCase letters\n d) None of the above"," a) int my_num = 100,000;\n b) int my_num = 100000;\n c) int my num = 1000;\n d) int $my_num = 10000;"]

answer=["c","d","a","b"]
count=0
print("welcom to the quiz\n\t")
for i in range (len(qustions)):
      print(qustions[i])
      print(options[i])
      ans=input("enter your answer: ")
      if(ans==answer[i]):  
        print("correct answer")
        print("\n")
        count=count+1
      else:
        print("wrong answer right answer is ",answer[i])
        print("\n")
          
if (count==4):
  print("congratulation you won the quiz")
else:
  print("you lose the quiz")
