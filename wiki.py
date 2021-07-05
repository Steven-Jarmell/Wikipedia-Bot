import discord
import wikipedia
from wikipedia.exceptions import DisambiguationError, HTTPTimeoutError, PageError, RedirectError, WikipediaException

class MyClient(discord.Client):

    async def on_ready(self): #Lets user know the bot is up and running

        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message): #Waits for message

        if message.author == client.user: #Prevents the bot from taking any action from its own messages
            return
        
        if message.content == '_wiki-commands': # Command list for user
            await message.channel.send('_wiki (input) : Produces the first two sentences of whatever you enter in \n' +
                                       '_wiki-setlang (input) : Sets language to whatever you choose' +
                                       '_wiki-random : Produces a random wikipedia page and a summary of it'
                                        )

        elif message.content.startswith('_wiki-setlang'): # Lets user change languages
            language = message.content[14:]
            # Loop to let user know if their language input was accepted
            try:
                wikipedia.set_lang(language) 
                await message.channel.send('Language switched to ' + wikipedia.languages().get(language))
            
            except:
                await message.channel.send('Please enter a valid language abbreviation\n' +
                                           'For all language abbreviations, go to https://git.io/JciVp')

        elif message.content == '_wiki-random': # Displays a random article
            while True: # On the off chance an exception occurs such as a disambiguation error
                try:    # This will just loop and find a different article
                    random_page = wikipedia.random()
                    summary = wikipedia.summary(random_page, 2)
                    page_title = random_page.title()
                    await message.channel.send('The random article selected is titled: ' + page_title + '\n' +
                                        'Here is a summary: ' + summary )
                    break
                except:
                    continue

        elif message.content.startswith('_wiki'): # Main search function
            search = message.content[5:] + '"\"'
            try: # Catches all the types of errors that the Wikipedia API can cause
                summary = wikipedia.summary(search, 2)
                await message.channel.send(summary)

            except DisambiguationError as ex:
                await message.channel.send(ex)

            except HTTPTimeoutError as ex:
                await message.channel.send(ex) 

            except RedirectError as ex:
                await message.channel.send(ex)

            except PageError as ex:
                await message.channel.send(ex)

            except WikipediaException as ex:
                await message.channel.send(ex)
            # Handles an unknown exception that might occur
            except Exception as ex:
                await message.channel.send(ex)                  

client = MyClient() # Creates Client

client.run('YOUR TOKEN HERE')