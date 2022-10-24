# This example requires the 'message_content' intent.

import discord #discord.py module
import pickle
from pathlib import Path #För att sätta filväg
import os

def pull_data_pickel(sida, post_id): # Hämtar datan för en post genom argumenten: facebooksidan och tiden den postades
    postname_pickle = str(sida) + str(post_id) + '.pkl' #genererar unikt filnamn med facebooksida och tiden den postades
    file = Path(".") / "Pickle" / postname_pickle #sätter rätt filväg
    with open(file,'rb') as sidorpickle:
        post = pickle.load(sidorpickle)
    return post

def print_data(post): #printar datan från en post
    #print()
    return(f"{post['text']} \n För mer info, se här: {post['post_url']} \n\n Detta var postat: {post['time']} \n\n\n")
    
sidor =	{ #Här skriver vi alla sidor vi ska scrapea
    "IT-Klubbverk": "itklubbv",
    #"Norrlands nation": "norrlands.nation/events",
    #"Södermanlands-Nerikes Nation":"snerikes",
}

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

                for sida in sidor:

                    directory= Path(".") / "Pickle"
                    number_of_files = len(os.listdir(directory)) # your directory path
                    
                    for x in range(1, number_of_files):
                        await message.channel.send(print_data(pull_data_pickel(sida, x)))



            else:
                await message.channel.send("This command doesn't exist")


             

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('') #Lägg in token här!!