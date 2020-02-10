//
//  ViewController.swift
//  Dicee
//
//  Created by Andy Gray on 01/12/2018.
//  Copyright © 2018 Andy Gray. All rights reserved.
//

import UIKit

class ViewController: UIViewController
{
    
    //Declaring Variables
    var randomDiceIndex1: Int = 0
    var randomDiceIndex2: Int = 0
    
    //Dice Image Array
    let diceImageArray = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png",]

    //Linking up the Dice Images
    @IBOutlet weak var diceImageView1: UIImageView!
    @IBOutlet weak var diceImageView2: UIImageView!
    
    override func viewDidLoad()
    {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        //Calls dice Changing Function
        randomDice()
    }

    //Action to change the dice.
    @IBAction func rollButton(_ sender: UIButton)
    {
        //Calls dice Changing Function
        randomDice()
    }
    
    func randomDice()
    {
        
        //Generating Random Numbers
        randomDiceIndex1 = Int.random(in: 0 ... 5)
        randomDiceIndex2 = Int.random(in: 0 ... 5)
        
        diceImageView1.image = UIImage(named: diceImageArray[randomDiceIndex1])
        diceImageView2.image = UIImage(named: diceImageArray[randomDiceIndex2])
        
    }
    
    //Shake to change dice
    override func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
    {
        randomDice()
    }
    
}

