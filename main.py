import os
import discord
import random

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$help':
        embedVar = discord.Embed(title="CritR Bot Command List.",
                                 color=0x00ff00)
        embedVar.add_field(
            name=
            "**Harmless/Funny Critical Fumble Tables.** *(Not Functional Yet)*",
            value=
            "Magic (Spell): **$magic f** \nMelee Weapon: **$melee f** \nNatural Weapon: **$natural f** \nRange Weapon: **$range f** \nThrown Weapon: **$thrown f**",
            inline=False)
        embedVar.add_field(
            name="**Standard Critical Fumble Tables.**",
            value=
            "Magic (Spell): **$magic** \nMelee Weapon: **$melee** \nNatural Weapon: **$natural** \nRange Weapon: **$range** \nThrown Weapon: **$thrown**",
            inline=False)
        embedVar.add_field(
            name="**Hard Critical Fumble Tables.**",
            value=
            "Magic (Cantrip and Spell): **$magic h** \nMelee Weapon: **$melee h** \nNatural Weapon: **$natural h** \nRange Weapon: **$range h** \nThrown Weapon: **$thrown h**",
            inline=False)
        embedVar.add_field(
            name="**Display Standard Odds Tables**",
            value=
            "Magic (Spell): **$magic table** \nMelee Weapon: **$melee table** \nNatural Weapon: **$natural table** \nRange Weapon: **$range table** \nThrown Weapon: **$thrown table**",
            inline=False)
        embedVar.add_field(
            name="**Display Hard Odds Tables**",
            value=
            "Magic (Cantrip and Spell): **$magic table h** \nMelee Weapon: **$melee table h** \nNatural Weapon: **$natural table h** \nRange Weapon: **$range table h** \nThrown Weapon: **$thrown table h**",
            inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$magic':
        from tables import magic_fails
        from opening import open_statement
        o_state = random.choice(open_statement)
        m_fail = random.choice(magic_fails)
        embedVar = discord.Embed(title="Magic Critical Fail.")
        embedVar.add_field(name='Standard Table',
                           value=f"{o_state} {m_fail}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$magic h':
        from tables import magic_h_fails
        from opening import open_statement
        o_state = random.choice(open_statement)
        m_fail = random.choice(magic_h_fails)
        embedVar = discord.Embed(title="Magic Critical Fail.")
        embedVar.add_field(name='Hard Table',
                           value=f"{o_state} {m_fail}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$magic table':
        from tables_ex import magic_fails
        embedVar = discord.Embed(title="Magic (Spells) Critical Fail Table.")
        embedVar.add_field(name='Standard Table',
                           value=f"{magic_fails}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$magic table h':
        from tables_ex import magic_h_fails
        embedVar = discord.Embed(
            title="Magic (Cantrips and Spells) Critical Fail Table.")
        embedVar.add_field(name='Hard Table',
                           value=f"{magic_h_fails}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$melee':
        from tables import melee_fails
        from opening import open_statement
        o_state = random.choice(open_statement)
        m_fail = random.choice(melee_fails)
        embedVar = discord.Embed(title="Melee Critical Fail.")
        embedVar.add_field(name='Standard Table',
                           value=f"{o_state} {m_fail}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$melee h':
        from tables import melee_h_fails
        from opening import open_statement
        o_state = random.choice(open_statement)
        m_fail = random.choice(melee_h_fails)
        embedVar = discord.Embed(title="Melee Critical Fail.")
        embedVar.add_field(name='Hard Table',
                           value=f"{o_state} {m_fail}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$melee table':
        from tables_ex import melee_fails
        embedVar = discord.Embed(title="Melee Critical Fail Table.")
        embedVar.add_field(name='Standard Table',
                           value=f"{melee_fails}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$melee table h':
        from tables_ex import melee_h_fails
        embedVar = discord.Embed(title="Melee Critical Fail Table.")
        embedVar.add_field(name='Hard Table',
                           value=f"{melee_fails}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$thrown':
        from tables import thrown_fails
        from opening import open_statement
        o_state = random.choice(open_statement)
        t_fail = random.choice(thrown_fails)
        embedVar = discord.Embed(title="Thrown Critical Fail.")
        embedVar.add_field(name='Standard Table',
                           value=f"{o_state} {t_fail}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$thrown h':
        from tables import thrown_fails
        from opening import open_statement
        o_state = random.choice(open_statement)
        t_fail = random.choice(thrown_fails)
        embedVar = discord.Embed(title="Thrown Critical Fail.")
        embedVar.add_field(name='Hard Table',
                           value=f"{o_state} {t_fail}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$thrown table':
        from tables_ex import thrown_fails
        embedVar = discord.Embed(title="Thrown Weapon Critical Fail Table.")
        embedVar.add_field(name='Standard Table',
                           value=f"{thrown_fails}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$thrown table h':
        from tables_ex import thrown_fails
        embedVar = discord.Embed(title="Thrown Weapon Critical Fail Table.")
        embedVar.add_field(name='Hard Table',
                           value=f"{thrown_fails}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$natural':
        from tables import nat_fails
        from opening import open_statement
        o_state = random.choice(open_statement)
        n_fail = random.choice(nat_fails)
        embedVar = discord.Embed(title="Natural Weapon Critical Fail.")
        embedVar.add_field(name='Standard Table',
                           value=f"{o_state} {n_fail}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$natural h':
        from tables import nat_fails
        from opening import open_statement
        o_state = random.choice(open_statement)
        n_fail = random.choice(nat_fails)
        embedVar = discord.Embed(title="Natural Weapon Critical Fail.")
        embedVar.add_field(name='Hard Table',
                           value=f"{o_state} {n_fail}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$natural table':
        from tables_ex import nat_fails
        embedVar = discord.Embed(title="Natural Critical Fail Table.")
        embedVar.add_field(name='Standard Table',
                           value=f"{nat_fails}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$natural table h':
        from tables_ex import nat_fails
        embedVar = discord.Embed(title="Natural Critical Fail Table.")
        embedVar.add_field(name='Hard Table',
                           value=f"{nat_fails}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$range':
        from tables import range_fails
        from opening import open_statement
        o_state = random.choice(open_statement)
        r_fail = random.choice(range_fails)
        embedVar = discord.Embed(title="Range Weapon Critical Fail.")
        embedVar.add_field(name='Standard Table',
                           value=f"{o_state} {r_fail}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$range h':
        from tables import range_fails
        from opening import open_statement
        o_state = random.choice(open_statement)
        r_fail = random.choice(range_fails)
        embedVar = discord.Embed(title="Range Weapon Critical Fail.")
        embedVar.add_field(name='Hard Table',
                           value=f"{o_state} {r_fail}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$range table':
        from tables_ex import range_fails
        embedVar = discord.Embed(title="Range Critical Fail Table.")
        embedVar.add_field(name='Standard Table',
                           value=f"{range_fails}",
                           inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == '$range table h':
        from tables_ex import range_fails
        embedVar = discord.Embed(title="Range Critical Fail Table.")
        embedVar.add_field(name='Hard Table',
                           value=f"{range_fails}",
                           inline=False)
        await message.channel.send(embed=embedVar)


#Not Connected to a Discord Bot. Needs a token to connect.
my_secret = os.environ['TOKEN']
client.run(my_secret)
