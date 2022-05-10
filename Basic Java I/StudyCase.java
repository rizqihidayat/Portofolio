public class StudyCase {
        public static void main(String[] args){
            int x;
            x = Integer.parseInt(args[0]);

            int y;
            y = Integer.parseInt(args[1]);
            
            int a = x*y;
            System.out.println(a);

            if( a % 2 == 0){
            System.out.println("Genap");
            }else{
            System.out.println("Ganjil");
            }
            
            int z;
            z = Integer.parseInt(args[2]);
            int b = x*y*z;
            System.out.println(b);

            if( b % 2 == 0){
            System.out.println("Genap");
            }else{
            System.out.println("Ganjil");
            }
    }
}