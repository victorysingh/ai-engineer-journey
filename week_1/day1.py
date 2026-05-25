# #patient=('john',20,'new_')
# #print(patient)
# # name=input('what is your name? ')
# # color=input('what is your favorite color? ')
# # print(name+'likes'+color )
# # weight=float(input('enter yout weight(in pounds)'))
# # print(weight*0.453592)
# # 
# # name='preet'
# # age=20
# # dream_company='google'
# # daily_study_hours=7
# # print(f'My name is {name} and i am {age} years old and my dream company to work is {dream_company}')
# name= input('enter name')
# lessons= 12
# is_member= False
# print(f' hello{name}! you have completed lessons:{lessons}/n you are this premium member:{is_member}')
# price_openAI_api_sub=1200
# token_used=3000
# tottal_cost=
# api_token=int(input('enter tokens'))
# if api_token<1000:
#     print('ok')
# elif  1000<api_token<5000:
#     print('warning')
# else:
#     print('limit exceeded')
# i=1
# for i  in range(11):
#     print('AI Lesson',i)
# tools =["openAI","langchain","python"]
# for tool in tools:
#     print(tool)
# docS=[a,b,c,d,e]
# for doc in docs:
#     print(doc)
# n= input('eneter stop,start or quit')
# while(1):
#     if (n=='stop'):
#         print('stop')
#         break
#     elif (n=='start'):
#         print('start')
#         break
#     else:
#         print('quit')
#         break
# else:
#     print('inaalid entry')    
# =[2,2,2,2,6]    
# for x_count in n:
#     print('xn'*x_count)
# words=[1,3,5,5,4,3,2,7,9]

# def caculate_tokens(words):
#     count=0
#     for n in words:
#         count+=n
#     return count*1.3
# n=caculate_tokens(words)    
# prin
# 
# 1. Store multiple AI agents in a list
# agents = [
#     {"name": "Alice", "specialty": "Coding", "status": "active"},
#     {"name": "Bob", "specialty": "Data Analysis", "status": "inactive"},
#     {"name": "Charlie", "specialty": "Copywriting", "status": "active"},
#     {"name": "Delta", "specialty": "Customer Support", "status": "active"}
# ]

# print("--- Active AI Agents ---")

# # 2. Loop through the list and print only the active agents
# for agent in agents:
#     if agent["status"] == "active":
#         print(f"Name: {agent['name']} | Specialty: {agent['specialty']}")
def motivate(name):
    return f"Keep going {name}! You can become an AI engineer."


name = input("Enter your name: ")
subject = input("Enter your subject: ")
hours = int(input("Enter study hours: "))

lessons = ["Python Basics", "Loops", "Functions"]


print(f"\nHello {name}!")
print(f"You are studying {subject} for {hours} hours today.\n")


if hours <= 2:

    print("Increase study time for faster progress.")

else:

    print("Great consistency!")


print("\nLessons Completed:")

for lesson in lessons:

    print(f"- {lesson}")


message = motivate(name)

print("\n" + message)
  
