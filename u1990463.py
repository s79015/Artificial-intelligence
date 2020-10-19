
import random
import math
class Bot(object):

	def __init__(self):
		self.name = "1990463" # Put your id number her. String or integer will both work
		# Add your own variables here, if you want to.

	def get_bid_game_type_collection(self, current_round, bots, game_type, winner_pays, artists_and_values, round_limit,
		starting_budget, painting_order, target_collection, my_bot_details, current_painting, winner_ids):
		"""Strategy for collection type games.

		Parameters:
		current_round(int): 			The current round of the auction game
		bots(dict): 					A dictionary holding the details of all of the bots in the auction
										Includes what paintings the other bots have won and their remaining budgets
		game_type(str): 				Will be "collection" for collection type games
		winner_pays(int):				Rank of bid that winner plays. 1 is 1st price auction. 2 is 2nd price auction.
		artists_and_values(dict):		A dictionary of the artist names and the painting value to the score (for value games)
		round_limit(int):				Total number of rounds in the game - will always be 200
		starting_budget(int):			How much budget each bot started with - will always be 1001
		painting_order(list str):		A list of the full painting order
		target_collection(list int):	A list of the type of collection required to win, for collection games - will always be [4,2]
										[5] means that you need 5 of any one type of painting
										[4,2] means you need 4 of one type of painting and 2 of another
										[3,3,1] means you need 3 of one tpye of painting, 3 of another, and 1 of another
		my_bot_details(dict):			Your bot details. Same as in the bots dict, but just your bot.
										Includes your current paintings, current score and current budget
		current_painting(str):			The artist of the current painting that is being bid on
		winner_ids(list str):			A list of the ids of the winners of each round so far

		Returns:
		int:Your bid. Return your bid for this round.
		"""

		# WRITE YOUR STRATEGY HERE FOR COLLECTION TYPE GAMES - FIRST TO COMPLETE A FULL COLLECTION


							   #info
		my_budget = my_bot_details["budget"]
		my_current_paintings=my_bot_details["paintings"]

		#print("my_bot_details", my_bot_details)
		#print("My budget", my_budget)
		#print("my_current_paintings", my_current_paintings)
		#print("len target collection", len(target_collection))

		#bid stadard
		def bid_standard(target_collection):
			bid_standard=1001/sum(target_collection)
			bid_standard=round(bid_standard)
			if bid_standard>=my_budget:
				bid_standard=my_budget

			return bid_standard

		#print("Bid standard",bid_standard(target_collection))
		#print("listOfElems",painting_order[current_round:])



						# Collection AIM function
		def collection_aim (my_current_paintings,painting_order,target_collection):
			#print("my_current_paintings",len(my_current_paintings))
			#res = all(x==0 for x in my_current_paintings.values())
			val=0
			for values in my_current_paintings.values():
				if values!=0:
					val+=1


			#print("val",val)
			 ## my current paintings empty
			if val==0:
				# my current paintings empty
				dictOfElems = dict()
				collection_aim=dict()
				findings=0
				keys_save=[]
				position_save=[]
				target_collection_sort=target_collection
				target_collection_sort.sort(reverse=True)
				position=0
				# Iterate over each element in list
				for elem in painting_order:
						# If element exists in the dict, then increment its value else add it in dict
						if elem in dictOfElems:
							dictOfElems[elem] += 1
						else:
							dictOfElems[elem] = 1

						for keys in dictOfElems.keys():
							if (dictOfElems[keys]>=target_collection_sort[position]) and (keys not in keys_save) and (position not in position_save):
								if dictOfElems[keys]>target_collection_sort[position]:
									collection_aim[keys]=target_collection_sort[position]
								else:
									collection_aim[keys]=dictOfElems[keys]

								findings+=1
								keys_save.append(keys)
								position_save.append(position)
								position+=1
								#print("findings",findings)
								#print("values",values)
								#print("position_save",position_save)
								#print("position",position)
								#print("keys_save",keys_save)
							if position==len(target_collection_sort):
								break
						if position==len(target_collection_sort):
							break

			if val>0: #if my current paintings are not empty
				dictOfElems = dict()
				collection_aim=dict()


				keys_save=[]
				position_save=[]
				target_collection_sort=target_collection
				target_collection_sort.sort(reverse=True)

				findings_aim=0
				position=0
				for keys,values in my_current_paintings.items():
					if values!=0:
						collection_aim[keys]=values


				#print("collection_aim_my_current",collection_aim)
				# Iterate over each element in list
				for elem in painting_order:
						# If element exists in the dict, then increment its value else add it in dict
						if elem in dictOfElems:
							dictOfElems[elem] += 1
						else:
							dictOfElems[elem] = 1

						for keys in dictOfElems.keys():

							if keys in collection_aim.keys():
								#print("keys",keys)
								if (collection_aim[keys]+dictOfElems[keys])>=target_collection_sort[position] and (keys not in keys_save) and (position not in position_save) :

									collection_aim[keys]=target_collection_sort[position]-collection_aim[keys]
									keys_save.append(keys)
									position_save.append(position)
									findings_aim+=1
									position+=1
									#print("collection_aim_my_current_if",collection_aim)
							if len(collection_aim)<len(target_collection) and (keys not in collection_aim.keys()):
								if (dictOfElems[keys]>=target_collection_sort[position]) and (keys not in keys_save) and (position not in position_save):

									collection_aim[keys]=target_collection_sort[position]
									keys_save.append(keys)
									position_save.append(position)
									position+=1

							if position==len(target_collection_sort):
								break

						if position==len(target_collection_sort) :
							break

			return collection_aim



		#print("current_round",current_round)


		collection_aim=collection_aim(my_current_paintings,painting_order[current_round:],target_collection)


		#print("Collection aim final",collection_aim)

		bid=0
				#    when need to bid
		for key in collection_aim.keys():
				if current_painting==key and collection_aim[key]!=0:
					bid=bid_standard(target_collection)
        #finish
		return bid



	def get_bid_game_type_value(self, current_round, bots, game_type, winner_pays, artists_and_values, round_limit,
		starting_budget, painting_order, target_collection, my_bot_details, current_painting, winner_ids):
		"""Strategy for value type games.

		Parameters:
		current_round(int): 			The current round of the auction game
		bots(dict): 					A dictionary holding the details of all of the bots in the auction
										Includes what paintings the other bots have won and their remaining budgets
		game_type(str): 				Will be either "collection" or "value", the two types of games we will play
		winner_pays(int):				rank of bid that winner plays. 1 is 1st price auction. 2 is 2nd price auction.
		artists_and_values(dict):		A dictionary of the artist names and the painting value to the score (for value games)
		round_limit(int):				Total number of rounds in the game
		starting_budget(int):			How much budget each bot started with
		painting_order(list str):		A list of the full painting order
		target_collection(list int):	A list of the type of collection required to win, for collection games
										[5] means that you need 5 of any one type of painting
										[4,2] means you need 4 of one type of painting and 2 of another
										[3,3,1] means you need 3 of one type of painting, 3 of another, and 1 of another
		my_bot_details(dict):			Your bot details. Same as in the bots dict, but just your bot.
										Includes your current paintings, current score and current budget
		current_painting(str):			The artist of the current painting that is being bid on
		winner_ids(list str):			A list of the ids of the winners of each round so far

		Returns:
		int:Your bid. Return your bid for this round.
		"""
		# WRITE YOUR STRATEGY HERE FOR VALUE GAMES - MOST VALUABLE PAINTINGS WON WINS

		# Here is an example of how to get the current painting's value
		current_painting_value = artists_and_values[current_painting]
		#print("The current painting's value is ", current_painting_value)

		# Here is an example of printing who won the last round
		if current_round>1:
			who_won_last_round = winner_ids[current_round-1]
			#print("The last round was won by ", who_won_last_round)

		# Play around with printing out other variables in the function,
		# to see what kind of inputs you have to work with
		my_budget = my_bot_details["budget"]

        # painting order
		def painting_orders(painting_order):
			dictOfElems=dict()
			for elem in painting_order:
				# If element exists in the dict, then increment its value else add it in dict
				if elem in dictOfElems:
					dictOfElems[elem] += 1
				else:
					dictOfElems[elem] = 1
			return dictOfElems

		painting_order_count=painting_orders(painting_order[current_round:])
		#print("painting_order_count",painting_order_count)
		#print("len(painting_order[current_round:]",len(painting_order[current_round:]))
		def total_sum_paintings(painting_order_count):
			total_sum_paintings=dict()
			total_sum_paintings=painting_order_count
			for key in 	total_sum_paintings.keys():
				if key=="Picasso":
					total_sum_paintings[key]=total_sum_paintings[key]*4
				if key=="Van Gogh":
					total_sum_paintings[key]=total_sum_paintings[key]*6
				if key=="Rembrandt":
					total_sum_paintings[key]=total_sum_paintings[key]*8
				if key=="Da Vinci":
					total_sum_paintings[key]=total_sum_paintings[key]*12
			overall=0
			for key in 	total_sum_paintings.keys():
				overall+=total_sum_paintings[key]
			return 	total_sum_paintings,overall

		total_sum_paintings,overall=total_sum_paintings(painting_order_count)
		#print("total_sum_paintings before len bots",total_sum_paintings)
		#print("overall ",overall)
		#print("bots",len(bots))
		for key in total_sum_paintings.keys():
			total_sum_paintings[key]=round((total_sum_paintings[key]))
			#total_sum_paintings[key]=total_sum_paintings[key]-total_sum_paintings[key]*0.1

		#overall=round(overall)
		#overall=overall-overall*0.1
		#print("total_sum_paintings ",total_sum_paintings)
		#print("overall ",overall)


		def percentage(part, whole):
  			return 100 * float(part)/float(whole)

		def percentage_of_paintings(total_sum_paintings,overall):
			percentage_of_paintings=dict()
			percentage_of_paintings=total_sum_paintings
			for key in 	percentage_of_paintings.keys():
				percentage_of_paintings[key]=percentage(percentage_of_paintings[key], overall)

			return 	percentage_of_paintings

		percentage_of_paintings=percentage_of_paintings(total_sum_paintings,overall)
		#print("percentage_of_paintings",percentage_of_paintings)

		def from_percentage(perc, budget):
  			return float(budget)*float(perc)/100

		def percentage_of_budget(percentage_of_paintings,budget):
			percentage_of_budget=dict()
			percentage_of_budget=percentage_of_paintings
			for key in 	percentage_of_budget.keys():
				percentage_of_budget[key]=from_percentage(percentage_of_budget[key], budget)

			return 	percentage_of_budget
		percentage_of_budget=percentage_of_budget(percentage_of_paintings,my_budget)
		#print("percentage_of_budget",percentage_of_budget)


		def koef (bots,my_budget):
			sum=0
			number_of_active_players=0
			for i in range (len(bots)):
				sum+=bots[i]["budget"]
				if bots[i]["budget"]>10:
					number_of_active_players+=1

			#print("sum_budget",sum)
			if my_budget==0:
				koef=1
			else:
				koef=my_budget/sum


			koef=1/koef
			if koef>number_of_active_players:
				koef=number_of_active_players
			return koef


		koef=koef (bots,my_budget)




		def bid_dict(percentage_of_budget,painting_order_count):
			bid_dict=dict()
			bid_dict=percentage_of_budget
			for key in 	bid_dict.keys():
				if painting_order_count[key]!=0:
					#print("bid_dict[key]",bid_dict[key])
					#print("painting_order_count[key]",painting_order_count[key])
					bid_dict[key]=float(bid_dict[key])/float(painting_order_count[key]) # not good
					#print("bid_dict[key]",bid_dict[key])
				else:
					bid_dict[key]==0
			return 	bid_dict

		painting_order_count=painting_orders(painting_order[current_round:]) #always save
		#print("painting_order_count",painting_order_count)
		bid_dict=bid_dict(percentage_of_budget,painting_order_count)
		#print("bid_dict",bid_dict)
		#bid stadard
		def bid(bid_dict):
			for key in bid_dict.keys():
				if current_painting==key and bid_dict[key]!=0:
					#print("bid_dict[key]",bid_dict[key])
					bid=bid_dict[key]*koef
					bid=round(bid)+1
					#print("bid*koef",bid)
			return bid

		bid=bid(bid_dict)
		#print("bid",bid)
		painting_price=dict()
		painting_price["Picasso"]=4
		painting_price["Van Gogh"]=6
		painting_price["Rembrandt"]=8
		painting_price["Da Vinci"]=12



		for key in painting_price:
			if current_painting==key and bid<painting_price[key]:
				bid=painting_price[key]
				bid=round(bid)+1
				#print("bid painting_price[key]+1",bid)
		if bid>my_budget:
			bid=my_budget
		if bid>my_budget and my_budget==0:
			bid=0

		#print("my_bot_details score",my_bot_details["score"])
		#print("my_budget",my_bot_details["budget"])
		#print("my_budget",my_budget)
		#print("bots_dict",bots)
		#print("koef",koef)
		#print("Bid",bid)
		return bid
