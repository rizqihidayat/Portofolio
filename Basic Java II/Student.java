public class Student extends Academician {
    public String grade;

    public void info(String args[]){
        System.out.println(super.getName());
        System.out.println(super.getAge());
    }
    
    public void studentsubject(String subject) {
        System.out.println("I am a Student"); 
    }

}