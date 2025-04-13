class Test {
        int age;

        public void assignAge(int num) {
            age = num;
        }
}

public class Basics {
    public static void main(String[] args) {
        Test t1 = new Test();
        t1.assignAge(10);

        Test t2 = new Test();
        t2.assignAge(15);

        System.out.println(t1.age);
        System.out.println(t2.age);
    }
}