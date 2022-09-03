import java.util.Scanner;

public class Main {

    class Node
    {
        Node last;
        int data;
        Node next;
        Node(int d){data=d;}
    }

    class myStack
    {
        Node head;
        Node mid;
        int counter;
    }

    myStack createStack()
    {
        myStack ms = new myStack();
        ms.counter = 0;
        return ms;
    }


    void push(myStack ms, int new_data)
    {
        Node newNode = new Node(new_data);
        newNode.last = null;
        newNode.next = ms.head;
        ms.counter += 1;
        if(ms.counter == 1)
        {
            ms.mid=newNode;
        }
        else
        {
            ms.head.last = newNode;

            if((ms.counter % 2) != 0)
                ms.mid=ms.mid.last;
        }
        ms.head = newNode;
    }

    void print(myStack ms)
    {
        if(ms.counter == 0){
            System.out.println();
            return;
        }
        Node head = ms.head;
        for (int i=0; i<ms.counter; i++){
            if (head != null) {
                System.out.print(head.data + " ");
                head = head.next;
            }
        }
        System.out.println();
    }

    void pop(myStack ms)
    {
        if(ms.counter == 0)
        {
            return ;
        }

        Node head = ms.head;
        ms.head = head.next;
        if(ms.head != null)
            ms.head.last = null;
        ms.counter -= 1;
        if(ms.counter % 2 == 0)
            ms.mid=ms.mid.next;
    }

    void findMiddle(myStack ms)
    {
        if(ms.counter == 0)
        {
            System.out.println(-1);
            return;
        }
        System.out.println(ms.mid.data);
    }
    void removeMiddle(myStack ms)
    {
        if (ms.counter == 1) {
            ms.head = null;
            ms.mid = null;
            ms.counter -= 1;
        }
        else if(ms.counter == 2) {
            ms.head.next = null;
            ms.mid = ms.head;
            ms.counter -= 1;
        }
        else if(ms.counter >= 3) {
            if (ms.counter % 2 == 1) {
                Node current = ms.mid;
                ms.mid = ms.mid.next;
                ms.mid.last = current.last;
                current.last.next = ms.mid;
            }
            else{
                Node current = ms.mid;
                ms.mid = ms.mid.last;
                ms.mid.next = current.next;
                current.next.last = ms.mid;
            }
            ms.counter -= 1;

        }

    }

    public static void main(String[] args) {
        Main ins = new Main();
        myStack ms = ins.createStack();
        Scanner scan = new Scanner(System.in);
        while (true)
        {
            String x = scan.next();
            if(x.equals("finish"))
                break;
            if(x.equals("push"))
                ins.push(ms, scan.nextInt());
            if(x.equals("pop"))
                ins.pop(ms);
            if(x.equals("print"))
                ins.print(ms);
            if(x.equals("findMiddle"))
                ins.findMiddle(ms);
            if(x.equals("removeMiddle"))
                ins.removeMiddle(ms);
        }

    }
}
