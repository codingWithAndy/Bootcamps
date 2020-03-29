//
//  Car.swift
//  Classes and Objects
//
//  Created by Andy Gray on 11/12/2018.
//  Copyright © 2018 Andy Gray. All rights reserved.
//

import Foundation

enum CarType
{
    case Sedan
    case Coupe
    case Hatchback
}

class Car
{
    
    var colour = "Black"
    var numberOfSeats : Int = 5
    var typeOfCar : CarType = .Coupe
    
    init()
    {
        
    }
    
    convenience init(customColour : String)
    {
        self.init()
        colour = customColour
    }
    
    func drive()
    {
        print("Car is moving")
    }
    
    func 
}
