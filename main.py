#python project for better carrear and job suggestion
carrear = {
    "engineer" : "good aptitude and ggod skill",
    "army officer" : "good physical health and analytical skill",
    "salary"     : "approx 60k to 70k "
    
    
}
good_carrear = {
    "polytechnic" : "good aptitude and good skill ",
    "doctor"  : "good knowledge in biology and aptitude",
    "farmist" :  "good knowlege in biology and aptitude "
}
medical = {
    "doctor" : "hardworking and focus",
    "lab assistant" : "good knowledge of biology and hardworking",
    "life science research" : "hardworking and focused and practical perfect"
}
enterprenur = {
    "shop owner" : "best selling skill and time management",
    "landlord"  : "best management skill",
    "salary"  : "approx 30k to 40k"
}

print("how many marks have you achieved")
totalmarks = int(input("enter your marks"))
mathmarks = int(input("enter your math marks :"))
biologymarks = int(input("enter your biology :")) 
if totalmarks>90 :
    if biologymarks>90 :
        print(medical)
        
    elif mathmarks>90 :    
        print(carrear)
    else :
        print("goverment exam preparation")
        
    
        
elif totalmarks>70 and totalmarks<80 :
  print(good_carrear)
  
else:
  print(enterprenur)
  
  
