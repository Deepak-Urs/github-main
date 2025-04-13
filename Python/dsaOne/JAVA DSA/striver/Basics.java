class BankAcc {
    private double balance;

    public BankAcc() {
        this.balance = 0;
    }

    public BankAcc(double __balance) {
        this.balance = __balance;
    }

    public void setBalance(double newBalance) {
        this.balance = newBalance;
    }

    public void printBalance() {
        System.out.println(this.balance);
    }

}

public class Basics {
    public static void main(String[] args) {
        BankAcc t1 = new BankAcc();
        t1.printBalance();

        BankAcc t2 = new BankAcc(100.0);
        t2.setBalance(100.0);
        t2.printBalance();
    }
}