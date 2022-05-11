public class StudentApp {
  public static void main(String args[]){
    Student data = new Student();
    data.setName("Rizqi");
    data.setAge(25);
    data.studentsubject("Matematika");
    System.out.println("Name : " + data.getName());
    System.out.println(" Age : "+ data.getAge());
  } 
}