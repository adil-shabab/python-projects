from instabot import Bot


bot = Bot()
bot.login(username = 'adil___shabab_', password = 'HADIYABANU@3197' )   # to login
# bot.follow('cristiano')      # to follow
# bot.unfollow('cristiano')    # to unfollow


# bot.upload_photo('path',caption='i love python ')    # to post

bot.send_message('hello','pp_nihal_pp')    # to send message, we can also make a list of people to send message



# # # to get all followers
followers = bot.get_user_followers('adil___shabab_')
for follower in followers:
    print(bot.get_user_info(follower))
    
    
# # # to get all following people
following = bot.get_user_following('adil___shabab_')
for person in following:
    print(bot.get_user_following(person))