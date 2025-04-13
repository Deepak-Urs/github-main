class BankAcc {
    double balance;
    String accType;

    public BankAcc() {
        this.balance = 0;
        this.accType = "Savings";
    }

    public BankAcc(double __balance, String __accType) {
        this.balance = __balance;
        this.accType = __accType;
    }

    public void printBalance() {
        System.out.println(this.balance);
    }

    public void printAccountType() {
        System.out.println(this.accType);
    }

}

public class Basics {
    public static void main(String[] args) {
        BankAcc t1 = new BankAcc();
        t1.printBalance();
        t1.printAccountType();

        BankAcc t2 = new BankAcc(100.0, "Checking");
        t2.printBalance();
        t2.printAccountType();
    }
}