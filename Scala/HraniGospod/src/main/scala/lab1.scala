import scala.collection.mutable.ArrayBuffer

object lab1 extends App{
    def func(x: Double): Double = 2*math.log10(x) - x/3 + 1 

    def main(a:Double = 0.1,b: Double = 1,e: Double = 0.001): ArrayBuffer[Double] = {
        var tempA: Double = a
        var tempB: Double = b
        var i = 0
        var x: Double = 0
        
        var array: ArrayBuffer[Double] = new ArrayBuffer[Double]()
        while (math.abs(tempB - tempA) > e){
            x = (tempA+tempB)/2
            println(x)
            if ((func(tempA)*func(x))<0){
                tempB = x
            }   else  {
                tempA = x
                i = i + 1
            }
        }
        array = ArrayBuffer(i,func(x),x)
        array
    }
    print(main())   
}