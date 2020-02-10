//
//  SelfDrivingCar.swift
//  Classes and Objects
//
//  Created by Andy Gray on 11/12/2018.
//  Copyright © 2018 Andy Gray. All rights reserved.
//

import Foundation

class SelfDrivingCar : Car
{
    var destination : String?
    
    override func drive()
    {
        super.drive()
        
        if let userSetDestination = destination
        {
            print("driving towards \(userSetDestination)")
        }
        
        
    }
}
