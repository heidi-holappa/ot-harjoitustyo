# Task 2 - Monopoly class diagram - part 2
**Note:** this file is intended for personal learning and should not be reviewed as a part of the weekly tasks. I wanted to experiment on how the diagram would form, if I used more attributes and some methods. I also practiced using a different syntax (more pythonic, perhaps) in mermaid. 

As a novice it was my experience, that for now it is easier to visualize an idea for an application from a diagram with more details. I assume that with experience and skills the benefits of a more abstract diagram become more apparent. 

```mermaid
 classDiagram
     
    class Game
    Game: SquareStart.location
    Game: SquarePrison.location
    Game: initializeGame()

    class Board
    
    class Dice
    Dice: dice
    Dice: throwDice() 
    
    class Player
    Player: balance 
    Player: ownedProperties
    Player: ownedBuildings
    Player: ownedHotels
    Player: playerLocation
      
      
    class Square
    Square: superMethods()
    
    class Money
    Money: balance
      

    Game "1" --> "2..8" Player
    Game "1" --> "*" Dice
    Game "1" --> Board      
    Board "1" --> "*" Square
    Player "*" .. "*" Square
    Game "1" --> "1" Money

    Square "1" <|-- "1" SquareStart
    Square "1" <|-- "1" SquarePrison
    Square "1" <|-- "1" SquareChance
    Square "1" <|-- "1" SquareIncomeTax
    Square "*" <|-- "*" SquareProperty
    Square "*" <|-- "*" SquareStation
    Square "*" <|-- "*" SquareFacility
    Game "1" --> "1" SquarePrison
    Game "1" --> "1" SquareStart
    
    class SquareStart
    SquareStart: nextSquare
    SquareStart: someAction()
    
    class SquarePrison
    SquarePrison: nextSquare
    SquarePrison: someAction()
      
    class SquareChance
    SquareChance: nextSquare
    SquareChance: someAction()
    
    class SquareIncomeTax
    SquareIncomeTax: nextSquare
    SquareIncomeTax: someAction()
    
    class SquareProperty
    SquareProperty: propertyName
    SquareProperty: nextSquare
    SquareProperty: someAction()
    
    
    class SquareStation
    SquareStation: stationName
    SquareStation: nextSquare
    SquareStation: someAction()
    
    class SquareFacility
    SquareFacility: nextSquare
    SquareFacility: facilityName
    SquareFacility: someAction()
    

    SquareProperty "1" .. "1" Player
    SquareFacility "1" .. "1" Player
    SquareStation "1" .. "1" Player

    SquareIncomeTax "1" --> "*" Cards
    SquareChance "1" --> "*" Cards

    class Cards
    Cards: deckChance
    Cards: deckIncomeTax
    Cards: suffleDecks()
    Cards: drawCard(type)
```