object lab2 extends App {
    var lis = List(1,1,2,3,5,8) 
    println(lis.last)
    def 
    println(lis.length)
    def isPalindrome(list:List[Any]):Boolean = {
        val len = list.length;
        for(i <- 0 until len/2) {
            if(list(i) != list(len-i-1)) return false; 
            }
        return true;
    }
    println(isPalindrome(lis))
}