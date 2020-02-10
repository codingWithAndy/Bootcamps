//
//  ViewController.swift
//  Magic 8 Ball
//
//  Created by Andy Gray on 01/12/2018.
//  Copyright © 2018 Andy Gray. All rights reserved.
//

import UIKit

class ViewController: UIViewController
{

    //Creating connections to the Outlets
    @IBOutlet weak var imageView: UIImageView!
    
    //Declaring Variables
    var randomBallNumber: Int = 0
    
    //Creating ball image Array
    let ballArray = ["ball1","ball2","ball3","ball4","ball5"]
    
    override func viewDidLoad()
    {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        magic8Output()
    }

    
    @IBAction func askButtonPressed(_ sender: UIButton)
    {
        magic8Output()
    }
    
    func magic8Output()
    {
        randomBallNumber = Int.random(in: 0 ... 4)
        
        imageView.image = UIImage(named: ballArray[randomBallNumber])
        
    }
    
    override func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
    {
        magic8Output()
    }
    
}

