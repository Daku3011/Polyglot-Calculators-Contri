public class TZConverter {
    public static void main(String args[]) {
        if (args.length > 0) {
            String cityName = args[0];
            City city = new City(cityName);
            System.out.println(
                    "The time in "
                    + cityName 
                    + " is "
                    + city.getCurrentTime()
                    + " on " 
                    + city.getCurrentDate());
        } else {
            System.out.println("No arguments");
            System.out.println("Example:");
            System.out.println(Colors.YELLOW + "java TZConverter Moscow");
            System.out.println("java -cp bin/ TZConverter Moscow"
                    + Colors.NOCOLOR);
            return;
        }
    }
}
