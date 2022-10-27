# This example requires the 'message_content' intent.

import discord #discord.py module
import pickle
from pathlib import Path #För att sätta filväg
import os

def pull_data_pickel(file): # Hämtar datan för en post genom argumenten: facebooksidan och tiden den postades
    file_path = Path(".") / "Pickle" / file #sätter rätt filväg
    with open(file_path,'rb') as sidorpickle:
        post = pickle.load(sidorpickle)
    return post

def print_data(post, sida): #printar datan från en post
    return(f"```{sida}:\n{post['text']} \n\nDetta var postat: {post['time']} \n``` För mer info, se här: {post['post_url']}")
    
sidor =	{ #Här skriver vi alla sidor vi ska scrapea
    "IT-Klubbverk": "itklubbv",
    "Norrlands nation": "norrlands.nation",
    "Södermanlands-Nerikes Nation":"snerikes",
}


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    async def on_message(self, message):
        
        prefix = "!" #Prefix for the commands

        if message.content.startswith(prefix):
            command = message.content[len(prefix):] #removes the lenght of the prefix to get the command sent by the user.
            isAdmin = [role.name == "Partyledare" for role in message.author.roles] #checks if the user has the Admin role.

            if command == "hello" and isAdmin:
                await message.channel.send("Hello Partyledare!")

            elif command == "help": #Checks if the command is help
                await message.channel.send("I hope this helps: (this is the new prompt) \n"
                                            "```\n"
                                            "This is a list of all the commands:\n\n"
                                            "help - This is the help command\n"
                                            "stats - All the servers stats only available for admins\n"
                                            "notifications - Manage your notifications\n"
                                            "event all\n"
                                            "event it\n"
                                            "event norrlands\n"
                                            "event snerikes\n"
                                            "```")
                                        
            elif command == "event all": #Checks if the command is event

                for sida in sidor:

                    directory= Path(".") / "Pickle" # directory path
                    
                    for file in os.listdir(directory):
                        if file.startswith(sida):
                            await message.channel.send(print_data(pull_data_pickel(file), sida))


            elif command == "event it": #Checks if the command is event it
                
                directory= Path(".") / "Pickle" # directory path
                n = 1
                for file in os.listdir(directory):
                    while n <= 5:
                        if file.startswith("IT-Klubbverk"):
                            await message.channel.send(print_data(pull_data_pickel(file), "IT-Klubbverk"))
                            n += 1
                            break
                        else:
                            break


            elif command == "event norrlands": #Checks if the command is event it

                directory= Path(".") / "Pickle" # directory path
                n = 1
                for file in os.listdir(directory):
                    while n <= 5:
                        if file.startswith("Norrlands nation"):
                            await message.channel.send(print_data(pull_data_pickel(file), "Norrlands nation"))
                            n += 1
                            break
                        else: 
                            break
            

            elif command == "event snerikes": #Checks if the command is event it

                directory= Path(".") / "Pickle" # directory path
                n = 1
                for file in os.listdir(directory):
                    while n <= 5:
                        if file.startswith("Södermanlands-Nerikes Nation"):
                            await message.channel.send(print_data(pull_data_pickel(file), "Södermanlands-Nerikes Nation"))
                            n += 1
                            break
                        else:
                            break


            else:
                await message.channel.send("This command doesn't exist")


             

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('') #Lägg in token här!!