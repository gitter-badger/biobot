from willie import module


# http://willie.dftba.net/docs/#willie.module.commands

@module.commands('play')
def games(bot, trigger):
	
	if not bot.memory.contains(trigger.nick):
		
		bot.reply("YOU ARE NOW playing game bio cave")
		bot.reply(locs["hackspace"]["msg"])
		bot.memory[trigger.nick] = {"location":"hackspace"}
		
	else:
		
		bot.reply("You are already playing")
		bot.say(locs["hackspace"]["msg"])

@module.nickname_commands('.*')	
@module.priority('low')	
def answer(bot, trigger):
		thing = trigger.group(1).split()[0] if trigger.group(1) else ""
				
		if trigger.nick in bot.memory:
			if "answer" in bot.memory[trigger.nick]:
				
				if bot.memory[trigger.nick]["answer"] == thing:
					bot.reply(locs[bot.memory[trigger.nick]["location"]]["saved"])
					del bot.memory[trigger.nick]["answer"]
					bot.memory[trigger.nick] = {"location":"hackspace"}
					bot.reply(locs["hackspace"]["msg"])
					bot.memory[trigger.nick] = {"location":"hackspace"}				
					
				else:
					bot.reply(thing + " is not the answer!!!!")
					bot.reply(locs[bot.memory[trigger.nick]["location"]]["killed"])
					bot.reply("game over!!!! start again")
					del bot.memory[trigger.nick]
					bot.reply(locs["hackspace"]["msg"])
					bot.memory[trigger.nick] = {"location":"hackspace"}

@module.nickname_commands('play','go','look','take','put','quit','answer','help','lick','punch')
def play(bot, trigger):
		action = trigger.group(1).split()[0] if trigger.group(1) else ""
		thing = trigger.group(2).split()[0] if trigger.group(2) else ""
	
		if trigger.sender == "tolland":
			bot.reply(trigger.group(1))
			bot.reply(thing)
		
		
		if not bot.memory.contains(trigger.nick):
		
			bot.reply("YOU ARE NOW playing game bio cave")
			bot.reply(locs["hackspace"]["msg"])
			bot.memory[trigger.nick] = {"location":"hackspace"}
		
		elif trigger.nick in bot.memory and "answer" in bot.memory[trigger.nick]:
			
				pass
				
		
		elif action == "" or action is None:
			bot.reply("what game would you like to play? you can play biocave, say \"?play end\" to biobot to end game")
			
			
		elif action == 'go':
			if thing in locs:
				if "go" in locs[thing]:

					bot.memory[trigger.nick] = {"location":thing}
					bot.reply(locs[thing]["go"])
					bot.reply(locs[thing]["msg"])
					
					if "death" in locs[thing]:
						
						bot.reply(locs[thing]["death"])
						bot.reply("game over!!!! start again")
						del bot.memory[trigger.nick]
						bot.reply(locs["hackspace"]["msg"])
						bot.memory[trigger.nick] = {"location":"hackspace"}
					
					if "question" in locs[thing]:
						
						bot.reply(locs[thing]["question"])
						bot.memory[trigger.nick]["answer"] = locs[thing]["answer"]
												
				else:
					bot.reply("can't go to "+thing)
					bot.reply("you are standing in the "+bot.memory[trigger.nick]["location"])
					
						
		elif action == 'look':
			if thing in locs:
				if "look" in locs[thing]:

					bot.reply(locs[thing]["look"])
					
				else:
					bot.reply("can't look at "+thing)
					bot.reply("you are standing in the "+bot.memory[trigger.nick]["location"])
					
			
		elif action == 'lick':
			if thing in locs:

				bot.reply("You lick the "+ thing)
				bot.reply("That was awkward. The "+thing+" tastes of metal shavings. The "+thing+" edges away and makes a run for it")
				bot.reply("you are standing in the "+bot.memory[trigger.nick]["location"])
					
			
		elif action == 'punch':
			#if thing in locs:

			bot.reply("You punch the "+ thing)
			bot.reply("The "+thing+" reports you to the trustees. YOu are banned for an appropriate period of time")
			bot.reply("you are standing in the "+bot.memory[trigger.nick]["location"])
					
						
		elif action == 'take':
			if thing in locs:
				if "take" in locs[thing]:

					bot.reply(locs[thing]["take"])

				else:
					bot.reply("can't take "+thing)
					bot.reply("you are standing in the "+bot.memory[trigger.nick]["location"])
			else:
				bot.reply("There is no "+thing+" object that can be taken")
			
			
		elif action == 'quit':
			if bot.memory.contains(trigger.nick):
				
				bot.reply("game ended")
				#bot.reply(locs["hackspace"]["msg"])
				del bot.memory[trigger.nick]
			else:
				
				bot.reply("you don't appear to be playing")
			
		elif action == 'help':
		
				
			bot.reply("fuck off asking for help in the hackspace... lost your fingers have you? google seems to work...")
		
				
		elif action == 'play':
			if not bot.memory.contains(trigger.nick):
				
				bot.reply("YOU ARE NOW playing game  bio cave")
				bot.reply(locs["hackspace"]["msg"])
				bot.memory[trigger.nick] = {"location":"hackspace"}
				
			else:
				
				bot.reply("already play playing game "+thing+ ", you are standing in the "+bot.memory[trigger.nick]["location"])
				
				bot.reply(locs["hackspace"]["msg"])



locs = dict(
hackspace = {"msg":"You are standing in the hackspace, you can see the biolab, the classroom, the workshop and a shed","go":"You go into the hackspace."}, 
	biolab = {"msg":"You are standing in the biolab, it smells bad. You can also see a trapdoor and a pipette","look":"The biolab is a stinking fetid pit. There is a trapdoor and some laboratory equipment","go":"You go into the biolab. You get sidetracked into a babble conversation. Your lifeforce is reduced by 50%"}, 
		trapdoor = {"msg":"You are in a dark hole in the ground.","look":"It's too dark to see.","go":"You go down into the depths. It is a utility access box, there is nothing here."},
		shed = {"msg":"You are in a shed.","look":"It's full of obsolete radio crap.","go":"You go into the shed. ","death":"tgreer beats you to death with a land rover tyre iron."},
		incubator = {"msg":"it is a binder incubator.","look":"It does hold temp well."}, 
			workshop = {"msg":"You are standing in the workshop, you can see a lathe and a robot with an arm","look":"you see a workshop, there are broken tools.","go":"You go into the workshop"}, 
				homeopathy = {"msg":"the kit contains some stuff","take":"you take the water","look":"some water and some leaflets with babble"}, 
					magic = {"msg": "the wand is made of wood","take":"you take the stick","look":"is a stick"},
						robot = {"msg": "it is a staubli robot arm", "go":"You walk over to the robot","death": "the robot arm rips off your head and stuffs it into the incubator","look":"it is a staubli robot arm. It looks pretty dangerous, I wouldn't go over there"},
						lathe = {"msg": "it is a chester centurian 3-in-1", "go":"You walk over to the lathe. It requires a key.","look":"It looks pretty interesting"}, classroom = {"go":"You go into the classroom, the doors swing shut behind you.","msg": "You are standing in a classroom. Suddenly a UAV copter  roars into life and makes to attack you. You have one chance, you see its control and you realise you must short the terminal with a 10K resistor.","look":"It is a classroom","question":"You grab for a resistor, the colour you need is black-brown-xxxx... What is the 3rd colour band you need?","answer":"orange","saved":"amazingly you find a 10K resistor with bands black brown orange, you run out of the classroom","killed":"you are killed by the UAV"},
							uav = {"msg": "it is a staubli robot arm", "go":"You walk over to the robot","death": "the robot arm rips off your head and stuffs it into the incubator","look":"It looks pretty dangerous, I wouldn't go over there"},
								pipette = {"msg": "it is a pipette", "death": "the biohackers kill you for stealing their pipette","look":"It is a gilson","take":"you steal the pipette"}
								)




# bot.reply(trigger.group(2))


# @module.nickname_command('hello!?')

# bot.memory.contains(key)

# bot.reply(url)
# bot.memory['last_seen_url'][trigger.sender] = url




# trigger.sender

