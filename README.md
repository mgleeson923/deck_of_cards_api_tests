# deck_of_cards_api_tests
Automation using Pytest to play Blackjack using deckofcardsapi.com

Notes:
 - AC is a bit ambiguous. If this were a feature sent to me, I'd ask the following:
   - Is the dealer part of the two players specified? Or is it Dealer and 2 players?
   - Why are we dealing 3 cards to each player? Blackjack is started with two cards, then can increment from there
   - Should the cards be dealt alternating between players? Or should each player get their hand of cards at once?
 - Given time constraints, I had a lot of reused code. With more time, some Helper files would've been useful
 - Determining the value of the Ace gave me some issues. It's worth 1 or 10 depending on the current hand the player
   has, so you'd almost have to calculate both hand values with the Ace being worth 1 and worth 10 to determine
   if the player got Blackjack. Unfortunately I just didn't quite have the time to wrap that portion up, so I treated
   all Aces as 10s for simplicity's sake. 
 - With additional time, I'd add some extra assertions verifying things such as remaining card count, etc.
