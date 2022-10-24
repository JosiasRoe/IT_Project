# This example requires the 'message_content' intent.

import discord #discord.py module
import pickle
from pathlib import Path #För att sätta filväg


def pull_data_pickel(sida, post_id): # Hämtar datan för en post genom argumenten: facebooksidan och tiden den postades
    postname_pickle = str(sida) + str(post_id) + 'post.pkl' #genererar unikt filnamn med facebooksida och tiden den postades
    file = Path(".") / "Pickle" / postname_pickle #sätter rätt filväg
    with open(file,'rb') as sidorpickle:
        post = pickle.load(sidorpickle)
    return post

def print_data(post): #printar datan från en post
    #print()
    return(f"{post['text']} \n {post['post_text']} \n {post['post_url']} \n {post['time']} \n {post['link']} \n")
    

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        #await message.author.send("hello user") #Sends private message to user.
        prefix = "!" #Prefix for the commands

        if message.content.startswith(prefix):
            command = message.content[len(prefix):] #removes the lenght of the prefix to get the command sent by the user.
            isAdmin = [role.name == "Partyledare" for role in message.author.roles] #checks if the user has the Admin role.

            #if command == "Hello" and isAdmin:
                #await message.channel.send("Hello Partyledare!")

            if command == "help": #Checks if the command is help
                await message.channel.send("I hope this helps: (this is the new prompt) \n"
                                            "```\n"
                                            "This is a list of all the commands:\n\n"
                                            "help - This is the help command\n"
                                            "stats - All the servers stats only available for admins\n"
                                            "notifications - Manage your notifications\n"
                                            "```")
                                        
            elif command == "event": #Checks if the command is event
                await message.channel.send(print_data(pull_data_pickel("IT-Klubbverk", 399825645201318)))
                
            else:
                await message.channel.send("This command doesn't exist")


             

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTAzMDQ2NDQxODc0MTQ5NzkxNg.GEYE03.EIzxCuFmoIXPa0Vk8g0mJP2M0WiRzSVm1If3HQ')