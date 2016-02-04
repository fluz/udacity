# Write a Poker Program

Check what hand wins a game of poker

The rules of the hands in poker can be found in http://en.wikipedia.org/wiki/List_of_poker_hands

## Defining the ranks

1. Straight Flush : (8,11) -> ['JS','TS','9','8','7']
2. Four of kind: (7,14,12) -> ['AS','AH','AD','AC','QS']
3. Full House: (6,8,13) -> ['8S','8C','8H','KH','KS']
4. Flush: (5,[10,8,7.5,3]) -> ['TD','8D','7D','5D','3D']
5. Straiht: (4,11) -> ['JS','TH','9D','8C','7H']
6. Three of kind: (3,7,[7,7,7,5,2]) -> ['7D','7S','7C','5C','2C']
7. Two Pairs: (2,11,3,[13,11,11,3,3]) -> ['13H','11H','11C','3S','3C']
8. Pair: (1,2,[11,6,3,2,2]) -> ['11H','6C','3S','2C','2S']
9. Highest Card: (0,7,5,4,3,2) -> ['7H','5C','4S','3C','2C']
