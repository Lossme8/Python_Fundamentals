import private_and_protected

user = private_and_protected.User("WebDevMentors", "Youtube", "examplemail", "examplemobile")

user.displayName()
user.name = "Stupid"
user.displayName()
print(user._User__password)