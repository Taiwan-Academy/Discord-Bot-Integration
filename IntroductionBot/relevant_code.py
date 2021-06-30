async def join_verify(ctx):

    # Welcome page
    Welcome_page = discord.Embed(
        title = "Welcome join this Discord Channel",
        description = "Please answer the following answer to verify your role",
        colour = discord.Colour.orange()
    )
    message = await ctx.author.send(embed = Welcome_page)

    await message.add_reaction("\U0001F44D")
    await message.add_reaction("\U0001F44E")
    accept = False



    while True:
        # However, in the DM, user is the bot
        reaction, user = await client.wait_for('reaction_add', check = check)
        if str(reaction) =="\U0001F44D":
            accept = True
            break
        else:
            await user.send("Sorry you cannot join us!")

            break

    await message.delete()

    ## Degree select page
    degree_page = discord.Embed(
        title = "Please select wheter you're bachelor, master, phd",
        description = "Select bat if you're bachelor, horse if you're master, select duck if you're doctor",
        colour = discord.Colour.orange()
    )
    message = await ctx.author.send(embed = degree_page)
    def check(reaction, user):
        return user != message.author

    bachelor= "🦇"
    master = "🐴"
    doc="🦆"
    await message.add_reaction(bachelor)
    await message.add_reaction(master)
    await message.add_reaction(doc)
    
    
    status = -1
    role_name = 'TEST_users'
    while True:
            # However, in the DM, user is the bot
            reaction, user = await client.wait_for('reaction_add', check = check)
            if str(reaction) =="🦇":
                print("user {} is a bachelor".format(user))
                role_name = "bachelor"
                break
            elif str(reaction) =="🐴":
                print('user {} is master'.format(user))
                status = 1
                role_name = "master"
                break

            elif str(reaction) =="🦆":
                print('user {} is doctor'.format(user))
                role_name = "phd"
                status = 2
                break
    await asyncio.sleep(5)

    # KEY, add_role 要是 member
    # need extra find member, now 
    await add_role(ctx.author, role_name)
    await message.delete()
