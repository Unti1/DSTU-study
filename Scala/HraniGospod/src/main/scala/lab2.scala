object lab2 extends App {
    var lis = List(1,2,2,2,2,1) 
    println(lis.last)
    println(lis.length)
    def isPalindrome2(list:List[Any]):Boolean = {
        val len = list.length;
        for(i <- 0 until len/2) {
            if(list(i) != list(len-i-1)) return false; 
            }
        return true;
    }
    println(isPalindrome2(lis))
    println()
    println()
}