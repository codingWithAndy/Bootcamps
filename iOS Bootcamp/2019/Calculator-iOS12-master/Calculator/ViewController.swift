//
//  ViewController.swift
//  Calculator
//
//  Created by Angela Yu on 10/09/2018.
//  Copyright © 2018 London App Brewery. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var displayLabel: UILabel!
    
    
    
    @IBAction func calcButtonPressed(_ sender: UIButton)
    {
        
        //What should happen when a non-number button is pressed
        if let calcValue = sender.currentTitle
        {
            if calcValue == "AC"
            {
                displayLabel.text = "0"
                
            }
        }
    
    }

    
    @IBAction func numButtonPressed(_ sender: UIButton)
    {
        
        //What should happen when a number is entered into the keypad
        if let numValue = sender.currentTitle
        {
            
            if displayLabel.text == "0"
            {
                displayLabel.text = numValue
            }
            else if let currentValue = displayLabel.text
            {
                displayLabel.text = currentValue + numValue
            }
            
        }
    
    }

}

