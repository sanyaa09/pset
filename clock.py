
def clock(time):
    nums=["twelve","one", "two", "three", "four", 
       "five", "six", "seven", "eight", "nine", 
       "ten", "eleven", "twelve", "thirteen", 
       "fourteen", "fifteen", "sixteen", "seventeen", 
       "eighteen", "nineteen", "twenty", "twenty one", 
       "twenty two", "twenty three", "twenty four", 
       "twenty five", "twenty six", "twenty seven", 
       "twenty eight", "twenty nine"]


    if time.find(':')== -1:
         print("Null")
         return 

    h,m=time.split(':')      



    if h.isnumeric() and m.isnumeric() and len(h)==2 and len(m)==2:
      if int(h)>=13:
      	   h=int(h)-12

      
	       
      if int(m) == 0:
           print(nums[int(h)]+ "o' clock\n")
  
      elif int(m) == 1: 
             print("one minute past " +nums[int(h)] +" o'clock")
  
      elif int(m) == 59:
             print("one minute to" + nums[int(h)%12+1] +" o'clock") 
  
      elif int(m) == 15:
             print("quarter past " +nums[int(h)]  +" o'clock" ) 

      elif int(m) == 30: 
             print("half past " +nums[int(h)] +" o'clock")
 
      elif int(m) == 45: 
             print("quarter to" + nums[int(h)%12+1] +" o'clock")
  
      elif int(m) <= 30:
             print(nums[int(m)]+" minutes past " +nums[int(h)] +" o'clock")
  
      elif int(m) > 30:
             print(nums[60-int(m)]+" minutes to  " + nums[(int(h)%12)+1] +" o'clock")


x=input("Enter time:")

clock(x)





