import java.util.*;
public class newDeque { //addFirst
    Deque<String> deque new LinkedList<String>();
    deque.addFirst("a");
    deque.addFirst("b");
    deque.addFirst("c");
    System.out.println(deque);

    String str = deque.peekLast();
    System.out.println(str);
    System.out.println(deque);

    while(deque.size()>0){
        System.out.println(deque.pollFirst());
    }
    System.out.println(deque);

    //addLast
    Deque<String> deque new LinkedList<String>();
    deque.addLast("a");
    deque.addLast("b");
    deque.addLast("c");
    System.out.println(deque);

    String str = deque.peekFirst();
    System.out.println(str);
    System.out.println(deque);

    while(deque.size()>0){
        System.out.println(deque.pollLast());
    }
    System.out.println(deque);


}


