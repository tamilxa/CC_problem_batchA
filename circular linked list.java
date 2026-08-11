//circular linked list
import java.util.*;
public class Main {

    static class Node {
        int data;
        Node next;
        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }
    Node head = null;
    void insertFirst(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            newNode.next = head;
            return;
        }

        Node temp = head;
        while (temp.next != head) {
            temp = temp.next;
        }

        newNode.next = head;
        head = newNode;
        temp.next = head;
    }
    void insertLast(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            newNode.next = head;
            return;
        }

        Node temp = head;
        while (temp.next != head) {
            temp = temp.next;
        }

        temp.next = newNode;
        newNode.next = head;
    }
    void insertMiddle(int data, int key) {
        if (head == null)
            return;

        Node curr = head;

        do {
            if (curr.data == key) {
                Node newNode = new Node(data);
                newNode.next = curr.next;
                curr.next = newNode;
                return;
            }

            curr = curr.next;
        } while (curr != head);

        System.out.println("Not found.");
    }
    void deleteFirst() {
        if (head == null)
            return;

        if (head.next == head) {
            head = null;
            return;
        }

        Node last = head;

        while (last.next != head) {
            last = last.next;
        }

        head = head.next;
        last.next = head;
    }
    void deleteLast() {
        if (head == null)
            return;

        if (head.next == head) {
            head = null;
            return;
        }

        Node curr = head;
        Node prev = null;

        while (curr.next != head) {
            prev = curr;
            curr = curr.next;
        }

        prev.next = head;
    }
    void deleteMiddle(int key) {
        if (head == null)
            return;

        if (head.data == key) {
            deleteFirst();
            return;
        }

        Node curr = head.next;
        Node prev = head;

        while (curr != head) {
            if (curr.data == key) {
                prev.next = curr.next;
                return;
            }

            prev = curr;
            curr = curr.next;
        }

        System.out.println("Key not found.");
    }

    void display() {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }

        Node temp = head;

        do {
            System.out.print(temp.data + " ");
            temp = temp.next;
        } while (temp != head);

        System.out.println();
    }

    public static void main(String[] args) {

        Main m = new Main();

        m.insertFirst(2);
        m.insertFirst(3);
        m.insertLast(8);
        m.insertFirst(6);
        m.insertLast(20);
        m.insertLast(24);
         m.display();
        m.insertMiddle(5, 8);
        m.display();
        m.deleteMiddle(2);
        m.display();
        m.deleteFirst();
        m.display();
        m.deleteLast();
        m.display();
    }
}