public class DoublePoint {
    /*
    Returns the number of binary digits that can be printed from single point percision.
     */
    public static float calcDoublePoint(){
        double one = 1;
        double seps = 1;
        double appone = one + seps;
        for( int ipow = 1; ipow <= 1000; ipow++){

            seps = seps / 2;
            appone = 1 + seps;
            if (Math.abs(appone) == 1){
                return ipow;
            }
        }
        System.out.print("Did not make it after 1000 iterations");
        return 0;
    }

    public static void main(String[] args){
        double numBinaryDigits = calcDoublePoint();
        System.out.println("The number of binary digits that can be printed is " + calcDoublePoint());
        System.out.println("The smallest number this corresponds to is " + Math.pow(2,-numBinaryDigits));
    }
}
