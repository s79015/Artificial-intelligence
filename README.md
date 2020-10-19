# Artificial-intelligence

Imagine an auction of paintings by four famous artists: Picasso, Van Gogh, Rembrandt and Da Vinci. In an
auction room the auctioneer presents each piece to be sold, and all bidders then write their bids for the item
on a secret sealed note that is handed to the auctioneer. The auctioneer then declares the highest bidder the
winner, takes a payment (equal to their bid or to that of the second-highest bidder, depending on the auction),
and starts the next round with a new item. If there is a target collection of paintings to buy, the rst bidder
to buy this bundle of goods terminates the auction and wins. Otherwise, the auction continues until either
everyone runs out of money or there are no more items to sell. If there is no target bundle, the bidder with the
paintings of the highest total value is the winner.
The objective is to implement strategies for a Python 3 bidding bot that will participate in such an auction.

2 The Auction
The auction runs in the following way. An Auctioneer initialises a room full of bots, then sets up the auction.
This involves giving each bot the same budget to spend, setting the sequence of items to be sold, and setting
the rules of the auction such as how the overall winner of the game will be decided.
The Auctioneer will then announce an item type to be bid upon, and ask the bots for bids. Your Bot will
use the information that the Auctioneer gives it to determine an amount to bid. Once all bots have bid, the
Auctioneer will declare the highest bidder the winner, who will then be charged (but not necessarily the amount
they bid, see below) and receives the item. If the bids draw, then the winner is chosen at random from the
drawn bidders.

For each game, there is at most one winner. The auction will continue until either there are no more items to sell
or if there is a set winning condition, e.g., a bidder managed to acquire the target collection of artists' paintings
needed, in which case they are declared the winner. If there is no target collection as a winning condition then
the auction will end once all the paintings are sold, and the bidder who ends with the highest total value of
items is the winner.
Note that, however, whilst the highest bidder will always win, the auction may be set up so the highest bidder
does not pay their own bid. It can be set up so that the highest bidder is only charged the second-highest bid
(see winner pays).
You will write your strategies in your Bot. Your Bot will be tested in a series of dierent auctions against Bots
of varying diculty and number. Finally, your Bots will be tested against each other in a tournament.
There are two types of games that will be played:
 Value Game:
Highest total value at the end wins, the highest bidder pays the second-highest bid. Picasso is
worth 4, Van Gogh worth 6, Rembrandt worth 8 and Da Vinci worth 12
 Collection Game:
First to collect a given bundle of painting types, the highest bidder pays their own bid. For
example, the collection bundle could be 3 paintings of any artist and 1 of any other artist.
Note that for all games in this tournament, the auction size (number of paintings up for auction) will be 200
and the starting budget for every bidder is 1001.


3 Implementation
Provided to you are two main Python 3 les to run the auctions: auctioneer.py and arena.py. We also
provide you with some example bots in the bots folder, random bot.py, flat bot 10.py and u1234321.py.
3.1 auctioneer.py
auctioneer.py contains the denition for the Auctioneer class, which sets up and runs the auction. We will
use this exact same le while marking your bots, so DO NOT CHANGE ANY OF THE CODE IN THIS FILE.
It has the following arguments:
 game type(string): Either \value" or \collection" for the 2 game types. Value games are won by the bot
with the highest value of paintings after all rounds. Collection games are won when a bot manages to
collect a full set of paintings as specied in the target collection.
 room(list of modules): A \room" is a list of bots that will play the auction. The bots are module objects.
There is an example of how to import them at the top of the auctioneer.py le, and how to pass them to
the Auctioneer as a list at the bottom of the auctioneer.py le. There are also examples in the arena.py
le.
 painting order(list of strings): A list of the sequence of painting types that will be auctioned in each of
the rounds. If this is set to None then a random order will be used.
 target collection(list of integers): For collection type games, the winning bot is the rst to win a
collection of paintings. This is given as a list. For example, [4,2] means that the winner is the rst bot
to collect 4 paintings of one artist and 2 of another artist. The specic artist is not important. So 4 Da
Vincis and 2 Rembrandts would win, as would 4 Picassos and 2 Van Goghs.
 slowdown(
oat): How long to wait at each round of the auction. If you set this to zero the auctions will
run fast.
 verbose(boolean): Whether the auctioneer prints updates to the terminal or not.
 output csv file(string): The auctioneer automatically logs the result of every round in an auction. This
defaults to 'data/auctioneer log.csv', but you can specify a dierent lename.
When the auctioneer is initialised it will automatically set up the auction and all the bots in the room with the
initialise bots() method.
The method run auction() will run the auction until it is completed.
It is not necessary to know how the Auctioneer class works to do well on the coursework. But if you are
interested there are more details in the README.md le.

3.2 arena.py
The arena.py le is provided as a convenient way to run auctions. This includes some methods that show
examples of how to run auctions. This is given to you as an example, so please feel free to change any of the
code here and experiment.
You might want to run an auction slowly, with a full print out to the terminal of the auction's progress, as
shown in run basic auction(). This will be useful to see how your bot is performing live. Or you might want
to run lots of auctions quickly, as shown in run lots of auctions().
2

3.3 bots
In the bots folder we included a few bots for you to practice with. We have given you 3 bots. bots/u1234321.py
is a good starting point for your own bot, with everything commented clearly. bots/flat bot 10.py and
bots/random bot.py are example bots that should be easy to beat.
