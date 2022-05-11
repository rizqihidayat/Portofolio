public class Academician {
    private String name;
    private int age;
    public int getAge(){
    return age;
    }
    public String getName(){
    return name;
    }
    public void setAge(int newAge){
    this.age = newAge;
    }
    public void setName(String newName){
    this.name = newName;
    }

    void studentsubject(String name, int age, String subject) {
        System.out.println(name  + age + subject);
      }
    
}