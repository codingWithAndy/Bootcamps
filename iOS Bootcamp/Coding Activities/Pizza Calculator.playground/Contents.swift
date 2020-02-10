import Foundation

let pizzaInInches : Int = 16
var numberOfPeople : Int = 12
let slicesPerPerson : Int = 4

var numberOfSlices : Int {
    get{
        return pizzaInInches - 4 //Just having this line of code and not the get is the short hand version.
    }
    
}

var numberOfPizza : Int {
    get {
        let numberOfPeopleFedPerPizza = numberOfSlices / slicesPerPerson
        
        return numberOfPeople / numberOfPeopleFedPerPizza
    }
    set {
        let totalSlices = numberOfSlices * newValue
        numberOfPeople = totalSlices / slicesPerPerson
        
    }
}

numberOfPizza = 6

print(numberOfPeople)
