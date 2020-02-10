import Foundation

var width: Float = 1.5
var height: Float = 2.3

//1 bucket of paint = 1.5 space

var bucketsOfPaint: Int {
    get {
        let surfaceArea = width * height
//        let areaCoveredPerBucket: Float = 1.5 Video version
//        let numberOfBuckets = surfaceArea / areaCoveredPerBucket Video version
//        let roundedBuckets = ceilf(surfaceArea / 1.5) Video version
        
        return Int(ceilf(surfaceArea / 1.5)) //Video version: Int(roundedBuckets)
    }
    set {
        let areaCovered = Double(newValue) * 1.5
        print("This amount of paint can cover: \(areaCovered)")
    }
}


print(bucketsOfPaint)

bucketsOfPaint = 6




