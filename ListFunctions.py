lucky_numbers = [4,8,15,16,23,42]
friends = ["Moipone", "Yolisa", "Olebogeng"]
#friends.extend(lucky_numbers) #this would combine data of lucky numbers function with friends
friends.append("Thato")#this adds an item at the end of the list
friends.insert(1,"Floyd")#This would add foly to index 1 on my friends list
friends.remove("Floyd")#This would remove Floyd from my friends list
friends.pop()#This would remove the last item in my friends's list which in this case would take Thato out
print(friends.index("Olebogeng"))#this checks and outputs Olebogeng's position in the list of friends
print(friends.count("Moipone"))#This counts and outputs the number Moipone appears in my friends list
print(friends.sort())#this sorts the list in order
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

print(friends)