import re
def arithmetic_arranger(problems,display = False):
  s = 0
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""

  sign = ""
  number1 = 0
  number2 = 0
  result = 0

  if len(problems) > 5:
      return ("Error: Too many problems.")
  
  else:
      for i in problems:
          if "/" in i or "*" in i:
              return ("Error: Operator must be '+' or '-'.")
          else:
              if re.search('[a-zA-Z]', i) != None:
                  return ("Error: Numbers must only contain digits.")
              else:
                  s = i
                  t=re.findall(r'\b\d+\b',s)
  
                  number1 = int(t[0])
                  number2 = int(t[1])
  
                  if len(str(number1)) > 4 or len(str(number2)) > 4:
                      return ("Error: Numbers cannot be more than four digits.")
                  else:
                      
                  #addition
                    if "+" in i:
                      
                      sign="+"
                      result = number1+number2
                      
                    elif "-" in i:
                      sign="-"
                      result = number1-number2
                    
                    num = max(number1,number2)
                    l=len(str(num))+2
  
                    line1+=str(number1).rjust(l)
                    line2+=sign
                    line2+=str(number2).rjust(l-1)
                    line3+=str("-"*l).rjust(l)
                    line4+=str(result).rjust(l)
  
                    if i != problems[-1]:
                      line1+="    "
                      line2+="    "
                      line3+="    "
                      line4+="    "
                    else:
                      break


  calculation = line1+"\n"+line2+"\n"+line3+"\n"+line4
  output =  ar = line1+"\n"+line2+"\n"+line3

  if display:
    return calculation
  else:
    return output
