# Java面试题

## 一个".java"源文件中是否可以包括多个类?

可以，但只能有一个public类，而且如果有public类的话，这个文件的名字要和这个类的名字一样。

## 源文件javac出多个class文件出来是怎么回事?

```java
public class A {
}

class B {
}

class C {
}
```

这样每个class会是一个.class文件。

```java
public class A {
    class B {
    }
}
```

这会产生两个.class文件，一个A.class，一个A$B.class。

```java
public class A {
    void xxx() {
        button.addActionLisener(new ActionListener() {
            ...
        });
    }
}
```

使用匿名类，这也会产生多个.class，一个A.class，一个A$1.class。

## 什么是匿名类？

```
new 父类构造器(参数列表)|实现接口() {
        //匿名内部类的类体部分  
    }
```

- 使用匿名内部类时，我们必须是继承一个类或者实现一个接口，但是两者不可兼得，同时也只能继承一个类或者实现一个接口。
- 匿名内部类中是不能定义构造函数的。
- 匿名内部类中不能存在任何的静态成员变量和静态方法。
- 匿名内部类为局部内部类，所以局部内部类的所有限制同样对匿名内部类生效。
- 匿名内部类不能是抽象的，它必须要实现继承的类或者实现的接口的所有抽象方法。

## `switch case`中`switch`后的变量类型可以是什么？

- 可以转换为int的类型。
- String类型。
- 枚举类型。

## `char`型变量与汉字。

java中的一个`char`占2个字节。java采用unicode，2个字节来表示一个字符，如`java char x = '编'`。

`java String.getBytes(encoding)`方法是获取指定编码的`byte`数组表示，通常gbk/gb2312是2个字节，utf-8是3个字节。如果不指定`encoding`则取系统默认的`encoding`。

## 使用final关键字修饰一个变量时，是引用不能变，还是引用的对象不能变？

使用final关键字修饰一个变量时，是指引用变量不能变，引用变量所指向的对象中的内容 还是可以改变的。

## Overload和Override的区别。

Overload是重载的意思，Override是覆盖的意思，也就是重写。

## 构造器Constructor是否可被override?

构造器Constructor不能被继承，因此不能重写Override，但可以被重载Overload。

## Java抽象类（abstract class）和类（class）的区别？

- 抽象类不能实例化；
- 抽象类允许有abstract方法；
- 抽象类的非抽象子类必须实现abstract方法。

## java接口与抽象类如何合作?

- 接口可以继承接口。抽象类可以实现（implements）接口，抽象类是可继承实体类，但前提是实体类必须有明确的构造函数。
- 一个java抽象类实现一个接口时，可以不实现接口中所有的方法，但抽象类的子类必须实现。

## java中实现多态的机制是什么？

靠的是父类或接口定义的引用变量可以指向子类或具体实现类的实例对象，而程序调用的方法在运行期才动态绑定，就是引用变量所指向的具体实例对象的方法，也就是内存里正在运行的那个对象的方法，而不是引用变量的类型中定义的方法。

## Java实现了闭包吗？

Java实现了闭包，但仅实现了值捕获，没有实现引用捕获。

## `String s = new String("xyz")`创建了几个String Object?

两个或一个，`"xyz"`对应一个对象，这个对象放在字符串常量缓冲区，常量`"xyz"`不管出现多少遍，都是缓冲区中的那一个。`New String`每写一遍，就创建一个新的对象，它一句那个常量`"xyz"`对象的内容来创建出一个新String对象。如果以前就用过`"xyz"`，这句代表就不会创建`"xyz"`自己了，直接从缓冲区拿。

```java
public class Main {
    public static void main(String[] args) {
        String a = new String("abc");
        String b = "abc";
        System.out.println("abc" == a);//false
        System.out.println("abc" == b);//true
        System.out.println(a == b);//false
    }
}
```

```java
public String(String original) {
    this.value = original.value;
    this.hash = original.hash;
}
```

## try-catch-finally-return的执行顺序

### try块中没有抛出异常，try、catch和finally块中都有return语句

```java
public static int NoException() {
    int i = 10;
    try {
        System.out.println("i in try block is：" + i);
        return --i;
    } catch (Exception e) {
        --i;
        System.out.println("i in catch - form try block is：" + i);
        return --i;
    } finally {
        System.out.println("i in finally - from try or catch block is：" + i);
        return --i;
    }
}
```

运行结果：

```
=============NoException==================
i in try block is：10
i in finally - from try or catch block is：9
8
===============================
```

执行顺序：执行try块，执行到return语句时，先执行return的语句，--i，但是不返回到main方法，执行finally块，遇到finally块中的return语句，执行--i，并将值返回到main方法，这里就不会再回去返回try块中计算得到的值。结论：try-catch-finally都有return语句时，没有异常时，返回值是finally中的return返回的。

### try块中没有抛出异常，仅try和catch中有return语句

```java
public static int NoException1() {
    int i = 10;
    try {
        System.out.println("i in try block is：" + i);
        return --i;
    } catch (Exception e) {
        --i;
        System.out.println("i in catch - form try block is：" + i);
        return --i;
    } finally {
        System.out.println("i in finally - from try or catch block is：" + i);
        --i;
        System.out.println("i in finally block is：" + i);
        //return --i;
    }
}
```

运行结果：

```
=============NoException1==================
i in try block is：10
i in finally - from try or catch block is：9
i in finally block is：8
9
===============================
```

执行顺序：try中执行完return的语句后，不返回，执行finally块，finally块执行结束后，返回到try块中，返回i在try块中最后的值。结论：try-catch都有return语句时，没有异常时，返回值是try中的return返回的。

### try块中抛出异常，try、catch和finally中都有return语句

```java
public static int WithException() {
    int i = 10;
    try {
        System.out.println("i in try block is：" + i);
        i = i / 0;
        return --i;
    } catch (Exception e) {
        System.out.println("i in catch - form try block is：" + i);
        --i;
        System.out.println("i in catch block is：" + i);
        return --i;
    } finally {
        System.out.println("i in finally - from try or catch block is--" + i);
        --i;
        System.out.println("i in finally block is--" + i);
        return --i;
    }
}
```

执行结果：

```
=============WithException==================
i in try block is：10
i in catch - form try block is：10
i in catch block is：9
i in finally - from try or catch block is--8
i in finally block is--7
6
===============================
```

执行顺序：抛出异常后，执行catch块，在catch块的return的--i执行完后，并不直接返回而是执行finally，因finally中有return语句，所以，执行，返回结果6。结论：try块中抛出异常，try、catch和finally中都有return语句，返回值是finally中的return。

### try块中抛出异常，try和catch中都有return语句

```java
public static int WithException1() {
    int i = 10;
    try {
        System.out.println("i in try block is：" + i);
        i = i / 0;
        return --i;
    } catch (Exception e) {
        System.out.println("i in catch - form try block is：" + i);
        return --i;
    } finally {

        System.out.println("i in finally - from try or catch block is：" + i);
        --i;
        System.out.println("i in finally block is：" + i);
        //return i;
    }
}
```

执行结果：

```
=============WithException1==================
i in try block is：10
i in catch - form try block is：10
i in finally - from try or catch block is：9
i in finally block is：8
9
===============================
```

执行顺序：抛出异常后，执行catch块，执行完finally语句后，依旧返回catch中的执行return语句后的值，而不是finally中修改的值。结论：返回的catch中return值。

### try、catch中都出现异常，在finally中有返回

```java
public static int WithException2() {
    int i = 10;
    try {
        System.out.println("i in try block is：" + i);
        i = i / 0;
        return --i;
    } catch (Exception e) {
        System.out.println("i in catch - form try block is：" + i);
        int j = i / 0;
        return --i;
    } finally {

        System.out.println("i in finally - from try or catch block is：" + i);
        --i;
        --i;
        System.out.println("i in finally block is：" + i);
        return --i;
    }
}
```

执行结果：

```
=============WithException2==================
i in try block is：10
i in catch - form try block is：10
i in finally - from try or catch block is：10
i in finally block is：8
7
===============================
```

执行顺序：try块中出现异常到catch，catch中出现异常到finally，finally中执行到return语句返回，不检查异常。 结论：返回finally中return值。

### 只在函数最后出现return语句

```java
public static int WithException3() {
    int i = 10;
    try {
        System.out.println("i in try block is：" + i);
        i = i / 0;
        //return --i;
    } catch (Exception e) {
        System.out.println("i in catch - form try block is：" + i);
        //int j = i/0;
        //return --i;
    } finally {
        System.out.println("i in finally - from try or catch block is：" + i);
        --i;
        --i;
        System.out.println("i in finally block is：" + i);
        //return --i;
    }
    return --i;
}
```

执行结果：

```
=============WithException3==================
i in try block is：10
i in catch - form try block is：10
i in finally - from try or catch block is：10
i in finally block is：8
7
===============================
```

## 当一个线程进入一个对象的一个synchronized方法后，其它线程是否可进入此对象的其它方法?

1. 其他方法前是否加了`synchronized`关键字，如果没加，则能。
2. 如果这个方法内部调用了`wait()`，则可以进入其他`synchronized`方法。
3. 如果其他个方法都加了`synchronized`关键字，并且内部没有调用`wait()`，则不能。
4. 如果其他方法是static，它用的同步锁是当前类的字节码，与非静态的方法不能同步，因为非静态的方法用的是`this`。

## ArrayList和Vector的区别

1. 同步性：Vector是线程安全的，也就是说是它的方法之间是线程同步的，而ArrayList是线程序不安全的，它的方法之间是线程不同步的。如果只有一个线程会访问到集合，那最好是使用ArrayList，因为它不考虑线程安全，效率会高些；如果有多个线程会访问到集合，那最好是使用Vector，因为不需要我们自己再去考虑和编写线程安全的代码。
2. 数据增长：ArrayList与Vector都有一个初始的容量大小，当存储进它们里面的元素的个数超过了容量时，就需要增加ArrayList与Vector的存储空间，每次要增加存储空间时，不是只增加一个存储单元，而是增加多个存储单元，每次增加的存储单元的个数在内存空间利用与程序效率之间要取得一定的平衡。Vector默认增长为原来两倍，而ArrayList的增长策略在文档中没有明确规定（从源代码看到的是增长为原来的1.5倍）。ArrayList与Vector都可以设置初始的空间大小，Vector还可以设置增长的空间大小，而ArrayList没有提供设置增长空间的方法。

## HashMap和Hashtable的区别

1. HashMap是Hashtable的轻量级实现（非线程安全的实现），他们都完成了Map接口，主要区别在于HashMap允许空（`null`）键值（key），由于非线程安全，在只有一个线程访问的情况下，效率要高于Hashtable。
2. HashMap允许将null作为一个entry的key或者value，而Hashtable不允许。
3. HashMap把Hashtable的contains方法去掉了，改成containsvalue和containsKey。因为contains方法容易让人引起误解。
4. Hashtable继承自Dictionary类，而HashMap是Java1.2引进的Map interface的一个实现。
5. 最大的不同是，Hashtable的方法是Synchronize的，而HashMap不是，在多个线程访问Hashtable时，不需要自己为它的方法实现同步，而HashMap就必须为之提供外同步。
6. Hashtable和HashMap采用的hash/rehash算法都大概一样，所以性能不会有很大的差异。

## List，Set，Map是否继承自Collection接口?

List，Set是，Map不是

## Collection和 Collections的区别。

Collection是集合类的上级接口，继承与他的接口主要有Set和List。

Collections是针对集合类的一个帮助类，他提供一系列静态方法实现对各种集合的搜索、排序、线程安全化等操作。

## java中有几种类型的流？JDK为每种类型的流提供了一些抽象类以供继承，请说出他们分别是哪些类？

字节流，字符流。字节流继承于`InputStream`/`OutputStream`，字符流继承于`InputStreamReader`/`OutputStreamWriter`。在java.io包中还有许多其他的流，主要是为了提高性能和使用方便。

## 描述一下JVM加载class文件的原理机制?

JVM中类的装载是由ClassLoader和它的子类来实现的，Java ClassLoader是一个重要的Java运行时系统组件。它负责在运行时查找和装入类文件的类。

## 能不能自己写个类，也叫java.lang.String？

可以，但在应用的时候，需要用自己的类加载器去加载，否则，系统的类加载器永远只是去加载re.jar包中的那个`java.lang.String`。

## 自旋锁、阻塞锁、可重入锁、悲观锁、乐观锁、读写锁、偏向所、轻量级锁、重量级锁、锁膨胀、对象锁和类锁

### 自旋锁

自旋锁可以使线程在没有取得锁的时候，不被挂起，而转去执行一个空循环，（即所谓的自旋，就是自己执行空循环），若在若干个空循环后，线程如果可以获得锁，则继续执行。若线程依然不能获得锁，才会被挂起。

使用自旋锁后，线程被挂起的几率相对减少，线程执行的连贯性相对加强。因此，对于那些锁竞争不是很激烈，锁占用时间很短的并发线程，具有一定的积极意义，但对于锁竞争激烈，单线程锁占用很长时间的并发程序，自旋锁在自旋等待后，往往毅然无法获得对应的锁，不仅仅白白浪费了CPU时间，最终还是免不了被挂起的操作，反而浪费了系统的资源。

在JDK1.6中，Java虚拟机提供-XX:+UseSpinning参数来开启自旋锁，使用-XX:PreBlockSpin参数来设置自旋锁等待的次数。

在JDK1.7开始，自旋锁的参数被取消，虚拟机不再支持由用户配置自旋锁，自旋锁总是会执行，自旋锁次数也由虚拟机自动调整。

可能引起的问题：

- 过多占据CPU时间：如果锁的当前持有者长时间不释放该锁，那么等待者将长时间的占据cpu时间片，导致CPU资源的浪费，因此可以设定一个时间，当锁持有者超过这个时间不释放锁时，等待者会放弃CPU时间片阻塞；

- 死锁问题：试想一下，有一个线程连续两次试图获得自旋锁（比如在递归程序中），第一次这个线程获得了该锁，当第二次试图加锁的时候，检测到锁已被占用（其实是被自己占用），那么这时，线程会一直等待自己释放该锁，而不能继续执行，这样就引起了死锁。因此递归程序使用自旋锁应该遵循以下原则：递归程序决不能在持有自旋锁时调用它自己，也决不能在递归调用时试图获得相同的自旋锁。

### 阻塞锁

让线程进入阻塞状态进行等待，当获得相应的信号（唤醒，时间）时，才可以进入线程的准备就绪状态，准备就绪状态的所有线程，通过竞争，进入运行状态。

JAVA中，能够进入/退出、阻塞状态或包含阻塞锁的方法有，synchronized关键字（其中的重量锁），ReentrantLock，Object.wait()/notify()。

### 可重入锁

可重入锁，也叫做递归锁，指的是同一线程外层函数获得锁之后，内层递归函数仍然有获取该锁的代码，但不受影响。

在JAVA环境下ReentrantLock和synchronized都是可重入锁

下面是使用实例

```java
public class Test implements Runnable {

    public synchronized void get() {
        System.out.println(Thread.currentThread().getId());
        set();
    }

    public synchronized void set() {
        System.out.println(Thread.currentThread().getId());
    }

    @Override
    public void run() {
        get();
    }

    public static void main(String[] args) {
        Test ss = new Test();
        new Thread(ss).start();
        new Thread(ss).start();
        new Thread(ss).start();
    }
}
```

```java
public class Test implements Runnable {
    ReentrantLock lock = new ReentrantLock();

    public void get() {
        lock.lock();
        System.out.println(Thread.currentThread().getId());
        set();
        lock.unlock();
    }

    public void set() {
        lock.lock();
        System.out.println(Thread.currentThread().getId());
        lock.unlock();
    }

    @Override
    public void run() {
        get();
    }

    public static void main(String[] args) {
        Test ss = new Test();
        new Thread(ss).start();
        new Thread(ss).start();
        new Thread(ss).start();
    }
}
```

两个例子最后的结果都是正确的，即同一个线程id被连续输出两次。

结果如下：

```
Threadid: 8

Threadid: 8

Threadid: 10

Threadid: 10

Threadid: 9

Threadid: 9
```

可重入锁最大的作用是避免死锁

我们以自旋锁作为例子，

```java
public class SpinLock {
    private AtomicReference<Thread> owner = new AtomicReference<>();

    public void lock() {
        Thread current = Thread.currentThread();
        while (!owner.compareAndSet(null, current)) {
        }
    }

    public void unlock() {
        Thread current = Thread.currentThread();
        owner.compareAndSet(current, null);
    }
}
```

对于自旋锁来说：

1. 若有同一线程两调用lock()，会导致第二次调用lock位置进行自旋，产生了死锁

说明这个锁并不是可重入的。（在lock函数内，应验证线程是否为已经获得锁的线程）

1. 若1问题已经解决，当unlock()第一次调用时，就已经将锁释放了。实际上不应释放锁。

（采用计数次进行统计）

修改之后，如下：

```java
public class SpinLock1 {
    private AtomicReference<Thread> owner = new AtomicReference<>();
    private int count = 0;

    public void lock() {
        Thread current = Thread.currentThread();
        if (current == owner.get()) {
            count++;
            return;
        }
        while (!owner.compareAndSet(null, current)) {
        }
    }

    public void unlock() {
        Thread current = Thread.currentThread();
        if (current == owner.get()) {
            if (count != 0) {
                count--;
            } else {
                owner.compareAndSet(current, null);
            }
        }
    }
}
```

该自旋锁即为可重入锁。

### 悲观锁和乐观锁

- 悲观锁（Pessimistic Lock）：顾名思义就是很悲观，每次去拿数据的时候都认为别人会修改，所以每次在拿数据的时候都会上锁，这样别人想拿这个数据就会block直到它拿到锁。传统的关系型数据库里边就用到了很多这种锁机制，比如行锁，表锁等，读锁，写锁等，都是在做操作之前先上锁。独占锁是悲观锁的一种实现

- 乐观锁（Optimistic Lock）：顾名思义，就是很乐观，每次去拿数据的时候都认为别人不会修改，所以不会上锁，但是在更新的时候会判断一下在此期间别人有没有去更新这个数据，可以使用版本号等机制。乐观锁适用于多读的应用类型，这样可以提高吞吐量，像数据库如果提供类似于write_condition机制的其实都是提供的乐观锁。使用CAS来保证，保证这个操作的原子性

两种锁各有优缺点，不可认为一种好于另一种，像乐观锁适用于写比较少的情况下，即冲突真的很少发生的时候，这样可以省去了锁的开销，加大了系统的整个吞吐量。但如果经常产生冲突，上层应用会不断的进行retry，这样反倒是降低了性能，所以这种情况下用悲观锁就比较合适。

### 轮询锁和定时锁

由tryLock实现，与无条件获取锁模式相比，它们具有更完善的错误恢复机制。可避免死锁的发生：

boolean tryLock()：仅在调用时锁为空闲状态才获取该锁。如果锁可用，则获取锁，并立即返回值true。如果锁不可用，则此方法将立即返回值false。

boolean tryLock(long time, TimeUnit unit) throws InterruptedException：

如果锁在给定的等待时间内空闲，并且当前线程未被中断，则获取锁。

如果锁可用，则此方法将立即返回值true。如果锁不可用，出于线程调度目的，将禁用当前线程，并且在发生以下三种情况之一前，该线程将一直处于休眠状态：

锁由当前线程获得；或者

其他某个线程中断当前线程，并且支持对锁获取的中断；或者

已超过指定的等待时间

如果获得了锁，则返回值true。

如果当前线程：

在进入此方法时已经设置了该线程的中断状态；或者

在获取锁时被中断，并且支持对锁获取的中断，

则将抛出InterruptedException，并会清除当前线程的已中断状态。

如果超过了指定的等待时间，则将返回值false。如果time小于等于0，该方法将完全不等待。

### 显示锁和内置锁

显示锁用Lock来定义、内置锁用syschronized。

内置锁：每个java对象都可以用做一个实现同步的锁，这些锁成为内置锁。线程进入同步代码块或方法的时候会自动获得该锁，在退出同步代码块或方法时会释放该锁。获得内置锁的唯一途径就是进入这个锁的保护的同步代码块或方法。

内置锁是互斥锁。

### 读-写锁

Lock接口以及对象，使用它，很优雅的控制了竞争资源的安全访问，但是这种锁不区分读写，称这种锁为普通锁。为了提高性能，Java提供了读写锁，在读的地方使用读锁，在写的地方使用写锁，灵活控制，如果没有写锁的情况下，读是无阻塞的，在一定程度上提高了程序的执行效率。

Java中读写锁有个接口java.util.concurrent.locks.ReadWriteLock，也有具体的实现ReentrantReadWriteLock，详细的API可以查看JavaAPI文档。

ReentrantReadWriteLock和ReentrantLock不是继承关系，但都是基于AbstractQueuedSynchronizer来实现。

lock方法是基于CAS来实现的

ReadWriteLock中暴露了两个Lock对象：

在读写锁的加锁策略中，允许多个读操作同时进行，但每次只允许一个写操作。读写锁是一种性能优化的策略。

RentrantReadWriteLock在构造时也可以选择是一个非公平的锁（默认）还是公平的锁。

### 对象锁和类锁

java的对象锁和类锁在锁的概念上基本上和内置锁是一致的，但是，两个锁实际是有很大的区别的，对象锁是用于对象实例方法，或者一个对象实例上的，类锁是用于类的静态方法或者一个类的class对象上的。

类的对象实例可以有很多个，但是每个类只有一个class对象，所以不同对象实例的对象锁是互不干扰的，但是每个类只有一个类锁。但是有一点必须注意的是，其实类锁只是一个概念上的东西，并不是真实存在的，它只是用来帮助我们理解锁定实例方法和静态方法的区别的.

synchronized只是一个内置锁的加锁机制，当某个方法加上synchronized关键字后，就表明要获得该内置锁才能执行，并不能阻止其他线程访问不需要获得该内置锁的方法。

调用对象wait()方法时，会释放持有的对象锁，以便于调用notify方法使用。notify()调用之后，会等到notify所在的线程执行完之后再释放锁

### 锁粗化（Lock Coarsening）：

锁粗化的概念应该比较好理解，就是将多次连接在一起的加锁、解锁操作合并为一次，将多个连续的锁扩展成一个范围更大的锁。举个例子：

```java
public class StringBufferTest {
    StringBuffer stringBuffer = new StringBuffer();

    public void append() {
        stringBuffer.append("a");
        stringBuffer.append("b");
        stringBuffer.append("c");
    }
}
```

这里每次调用stringBuffer.append方法都需要加锁和解锁，如果虚拟机检测到有一系列连串的对同一个对象加锁和解锁操作，就会将其合并成一次范围更大的加锁和解锁操作，即在第一次append方法时进行加锁，最后一次append方法结束后进行解锁。

### 互斥锁

互斥锁，指的是一次最多只能有一个线程持有的锁。如Java的Lock

15 无锁状态-》偏向锁-》轻量级锁-》重量级锁。锁膨胀

锁的状态总共有四种：无锁状态、偏向锁、轻量级锁和重量级锁。随着锁的竞争，锁可以从偏向锁升级到轻量级锁，再升级的重量级锁（但是锁的升级是单向的，也就是说只能从低到高升级，不会出现锁的降级）。JDK 1.6中默认是开启偏向锁和轻量级锁的，

锁膨胀：从轻量锁膨胀到重量级锁是在轻量级锁解锁过程发生的。

重量级锁：Synchronized是通过对象内部的一个叫做监视器锁（monitor）来实现的。但是监视器锁本质又是依赖于底层的操作系统的Mutex Lock来实现的。而操作系统实现线程之间的切换这就需要从用户态转换到核心态，这个成本非常高，状态之间的转换需要相对比较长的时间，这就是为什么Synchronized效率低的原因。因此，这种依赖于操作系统Mutex Lock所实现的锁我们称之为"重量级锁"。

轻量级锁："轻量级"是相对于使用操作系统互斥量来实现的传统锁而言的。但是，首先需要强调一点的是，轻量级锁并不是用来代替重量级锁的，它的本意是在没有多线程竞争的前提下，减少传统的重量级锁使用产生的性能消耗。在解释轻量级锁的执行过程之前，先明白一点，轻量级锁所适应的场景是线程交替执行同步块的情况，如果存在同一时间访问同一锁的情况，就会导致轻量级锁膨胀为重量级锁。

偏向锁：引入偏向锁是为了在无多线程竞争的情况下尽量减少不必要的轻量级锁执行路径，因为轻量级锁的获取及释放依赖多次CAS原子指令，而偏向锁只需要在置换ThreadID的时候依赖一次CAS原子指令（由于一旦出现多线程竞争的情况就必须撤销偏向锁，所以偏向锁的撤销操作的性能损耗必须小于节省下来的CAS原子指令的性能消耗）。上面说过，轻量级锁是为了在线程交替执行同步块时提高性能，而偏向锁则是在只有一个线程执行同步块时进一步提高性能。

无锁状态：在代码进入同步块的时候，如果同步对象锁状态为无锁状态。

## Java中反射的作用是什么?

JAVA反射机制是在运行时，对于任意一个类，都能够知道这个类的所有属性和方法；对于任意一个对象，都能够调用它的任意一个方法；这种动态获取的信息以及动态调用对象的方法的功能称为java语言的反射机制。Java反射机制主要提供了以下功能：

1. 在运行时判断任意一个对象所属的类；
2. 在运行时构造任意一个类的对象；
3. 在运行时判断任意一个类所具有的成员变量和方法；
4. 在运行时调用任意一个对象的方法；生成动态代理。

## 成员变量、局部变量、静态变量的区别

|  属性  |   成员变量  |      局部变量     |    静态变量   |
| :--: | :-----: | :-----------: | :-------: |
| 定义位置 | 在类中，方法外 | 方法中，或者方法的形式参数 |  在类中，方法外  |
| 初始化值 | 有默认初始化值 | 无，先定义，赋值后才能使用 |  有默认初始化值  |
| 调用方式 |   对象调用  |      ---      | 对象调用，类名调用 |
| 存储位置 |    堆中   |       栈中      |    方法区    |
| 生命周期 |  与对象共存亡 |     与方法共存亡    |   与类共存亡   |
|  别名  |   实例变量  |      ---      |    类变量    |

## 谈谈你对StrongReference、WeakReference和SoftReference的认识

- 强引用（StrongReference）：就是在代码中普遍存在的，类似`Object obj = new Object()`这类的引用，只要强引用还存在，GC永远不会回收掉被引用的对象。
- 软引用（SoftReference）：用来描述一些还有用但非必须的对象。对于软引用关联着的对象，在系统将要发生内存溢出异常时，将会把这些对象列入回收范围之中进行第二次回收。如果这次回收还没有足够的内存，才会抛出内存溢出异常。
- 弱引用（WeakReference）：也是用来描述非必须对象的，但是它的强度比软引用更弱一些，被弱引用关联的对象只能生存到了下一次GC发生之前。当GC工作时，无论当时内存是否足够，都会回收只被弱引用关联的对象。
- 虚引用（PhantomReference）：虚引用也称幽灵引用或者幻影引用，它是最弱的一种引用关系。一个对象是否有虚引用的存在，完全不会对其生存时间构成影响，也无法通过虚引用来取得一个对象实例。为一个对象设置虚引用的唯一目的就是在这个对象被GC回收是收到一个系统通知。

## ==与`equals()`的区别？

- ==判断两个对象的地址是否相等（对于基本类型判断值是否相等）。
- `equals()`会寻找自身或最近的父类实现，调用其`equals()`。
- 若无任何父类实现`equals()`，则会调用Object的`equals()`，其与==相同。

## `equals()`与`hashCode()`的区别？

- `equals()`仅在显示调用`equals()`时使用，而`hashCode()`在如散列表中会自动调用，以判断是否为同一对象。
- 重写`equals()`时必须重写`hashCode()`，否则会造成不可预料的后果。

## Java集合框架示意图

### 集合框架概览

| Collection class | Allow duplicate | Ordered | Sorted | Thread-safe |
| :--------------: | :-------------: | :-----: | :----: | :---------: |
|     ArrayList    |       Yes       |   Yes   |   No   |      No     |
|    LinkedList    |       Yes       |   Yes   |   No   |      No     |
|      Vector      |       Yes       |   Yes   |   No   |     Yes     |
|      HashSet     |        No       |    No   |   No   |      No     |
|   LinkedHashSet  |        No       |   Yes   |   No   |      No     |
|      TreeSet     |        No       |   Yes   |   Yes  |      No     |
|      HashMap     |        No       |    No   |   No   |      No     |
|   LinkedHashMap  |        No       |   Yes   |   No   |      No     |
|     Hashtable    |        No       |    No   |   No   |     Yes     |
|      TreeMap     |        No       |   Yes   |   Yes  |      No     |

![collections framework overview][collections_framework_overview]

### List

![List API class diagram][list_api_class_diagram]

### Set

![Set API class diagram][set_api_class_diagram]

### Map

![Map API class diagram][map_api_class_diagram]

### Queue

![Queue API class diagram][queue_api_class_diagram]

## Error和Exception的区别

Error类和Exception类的父类都是throwable类，他们的区别是：

- Error类一般是指与虚拟机相关的问题，如系统崩溃，虚拟机错误，内存空间不足，方法调用栈溢等。对于这类错误的导致的应用程序中断，仅靠程序本身无法恢复和和预防，遇到这样的错误，建议让程序终止。
- Exception类表示程序可以处理的异常，可以捕获且可能恢复。遇到这类异常，应该尽可能处理异常，使程序恢复运行，而不应该随意终止异常。

## 线程的状态转换关系

![Thread Life Cycle][thread_life_cycle]

## 用户线程（User Thread）与守护线程（Daemon Thread）

- JVM中存在两种线程：用户线程和守护线程
- 当线程中只剩下守护线程时JVM就会退出，反之还有任意一个用户线程在，JVM都不会退出。
- `thread.setDaemon(true)`必须在`thread.start()`之前设置，否则会抛出IllegalThreadStateException异常。
- 在守护线程中产生的线程也是守护线程。

## 如何理解volatile以及Java内存模型？

当程序在运行过程中，会将运算需要的数据从主存复制一份到CPU的高速缓存当中，那么CPU进行计算时就可以直接从它的高速缓存读取数据和向其中写入数据，当运算结束之后，再将高速缓存中的数据刷新到主存当中。由此会出现缓存一致性问题，如下图所示。 ![Cache Consistency][cache_consistency]

以就出现了缓存一致性协议。最出名的就是Intel 的MESI协议，MESI协议保证了每个缓存中使用的共享变量的副本是一致的。它核心的思想是：当CPU写数据时，如果发现操作的变量是共享变量，即在其他CPU中也存在该变量的副本，会发出信号通知其他CPU将该变量的缓存行置为无效状态，因此当其他CPU需要读取这个变量时，发现自己缓存中缓存该变量的缓存行是无效的，那么它就会从内存重新读取。

如在单例模式中使用双重检验加锁的方法就易出现问题

```java
public class Singleton {
    private volatile static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

因`instance = new Singleton();`并不是一个原子操作，其可以分解为：

1. 为对象分配内存；
2. 调用对应的构造做对象的初始化操作；
3. 将引用INSTANCE指向新分配的空间。

在Java内存模型中，在不改变程序运行结果的前提下，为尽可能地提高并行度，允许编译器和处理器对指令进行重排序，虽然重排序过程不会影响到单线程程序的执行，但却会影响到多线程并发执行的正确性。例如此处2依赖于1，3依赖于1。第二步与第三步是独立无依赖的，是可以被优化重排序的。这样在多线程环境下就会出现问题。

由此引入volatile关键字：

- 保证了不同线程对这个变量进行操作时的可见性，即一个线程修改了某个变量的值，这新值对其他线程来说是立即可见的。
- 禁止进行指令重排序。

volatile重排序规则表：

|   是否能重排序   | 后普通读／写 | 后volatile读 | 后volatile写 |
| :--------: | :----: | :--------: | :--------: |
|   先普通读／写   |   Yes  |     Yes    |     No     |
| 先volatile读 |   No   |     No     |     No     |
| 先volatile写 |   Yes  |     No     |     No     |

为了实现volatile的内存语义，编译器在生成字节码时，会在指令序列中插入内存屏障来禁止特定类型的处理器重排序。对于编译器来说，发现一个最优布置来最小化插入屏障的总数几乎不可能，为此，JMM采取保守策略。下面是基于保守策略的JMM内存屏障插入策略：

- 在每个volatile写操作的前面插入一个StoreStore屏障。
- 在每个volatile写操作的后面插入一个StoreLoad屏障。
- 在每个volatile读操作的后面插入一个LoadLoad屏障。
- 在每个volatile读操作的后面插入一个LoadStore屏障。

**LoadLoad屏障**

序列：Load1, LoadLoad, Load2

确保Load1所要读入的数据能够在被Load2和后续的load指令访问前读入。通常能执行预加载指令或/和支持乱序处理的处理器中需要显式声明Loadload屏障，因为在这些处理器中正在等待的加载指令能够绕过正在等待存储的指令。 而对于总是能保证处理顺序的处理器上，设置该屏障相当于无操作。

**StoreStore屏障**

序列：Store1, StoreStore, Store2

确保Store1的数据在Store2以及后续Store指令操作相关数据之前对其它处理器可见（例如向主存刷新数据）。通常情况下，如果处理器不能保证从写缓冲或/和缓存向其它处理器和主存中按顺序刷新数据，那么它需要使用StoreStore屏障。

**LoadStore屏障**

序列： Load1, LoadStore, Store2

确保Load1的数据在Store2和后续Store指令被刷新之前读取。在等待Store指令可以越过loads指令的乱序处理器上需要使用LoadStore屏障。

**StoreLoad屏障**

序列: Store1, StoreLoad, Load2

确保Store1的数据在被Load2和后续的Load指令读取之前对其他处理器可见。StoreLoad屏障可以防止一个后续的load指令 不正确的使用了Store1的数据，而不是另一个处理器在相同内存位置写入一个新数据。

## Java中的BIO，NIO，AIO分别是什么?

### BIO（synchronous Blocking IO，同步阻塞IO）

如Apache，Tomcat。服务器实现模式为一个连接一个线程，即客户端有连接请求时服务器端就需要启动一个线程进行处理，如果这个连接不做任何事情会造成不必要的线程开销，当然可以通过线程池机制改善。

BIO方式适用于连接数目比较小且固定的架构，这种方式对服务器资源要求比较高，并发局限于应用中，JDK1.4以前的唯一选择，但程序直观简单易理解。

### NIO（synchronous Non blocking IO，同步非阻塞IO）

如Nginx，Netty。服务器实现模式为一个请求一个线程，即客户端发送的连接请求都会注册到多路复用器上，多路复用器轮询到连接有I/O请求时才启动一个线程进行处理。

NIO方式适用于连接数目多且连接比较短（轻操作）的架构，比如聊天服务器，并发局限于应用中，编程比较复杂，JDK1.4开始支持。

### AIO（Asynchronous non blocking IO，异步非阻塞IO）

还不是特别成熟。服务器实现模式为一个有效请求一个线程，客户端的I/O请求都是由OS先完成了再通知服务器应用去启动线程进行处理，

AIO方式使用于连接数目多且连接比较长（重操作）的架构，比如相册服务器，充分调用OS参与并发操作，编程比较复杂，JDK7开始支持。

## Serializable接口和序列化与反序列化

- Serializable接口没有任何方法
- 一个类只要实现了Serializable接口，即可被序列化
- 实现Serializable接口的类，在序列化时不能有不可被序列化的成员变量
- 通过ObjectOutputStream和ObjectInputStream对对象进行序列化及反序列化
- 虚拟机是否允许反序列化，不仅取决于类路径和功能代码是否一致，一个非常重要的一点是两个类的序列化 ID 是否一致（即`private static final long serialVersionUID`）
- transient关键字的作用是控制变量的序列化，在变量声明前加上该关键字，可以阻止该变量被序列化到文件中；在被反序列化后，transient变量的值被设为初始值。
- 在序列化过程中，如果被序列化的类中定义了`writeObject()`和`readObject()`方法，虚拟机就会试图调用对象类里的`writeObject()`和`readObject()`方法，进行用户自定义的序列化和反序列化。如果没有这样的方法，则默认调用是ObjectOutputStream的`defaultWriteObject()`方法以及ObjectInputStream的`defaultReadObject()`方法。

序列化算法一般会按步骤做如下事情：

- 将对象实例相关的类元数据输出。
- 递归地输出类的超类描述直到不再有超类。
- 类元数据完了以后，开始从最顶层的超类开始输出对象实例的实际数据值。
- 从上至下递归输出实例的数据。

## ArrayList的`subList()`方法注意事项

`subList()`方法接口为

```java
List<E> subList(int fromIndex, int toIndex);
```

其返回的是原List从\[fromIndex,toIndex)之间的一部分的视图（如ArrayList的内部类SubList），实际依赖于原List，且对subList的修改也会作用到原List中。

ArrayList的`subList()`结果不可以强制转换为ArrayList（否则会抛出ClassCastException异常）。

```java
SubList(AbstractList<E> parent, int offset, int fromIndex, int toIndex) {
    this.parent = parent;
    this.parentOffset = fromIndex;
    this.offset = offset + fromIndex;
    this.size = toIndex - fromIndex;
    this.modCount = ArrayList.this.modCount;
}
```

## Arrays的`asList()`方法注意事项

`Arrays.asList()`可将数组转换为集合，但转换得到的集合不能使用如`add()`、`remove()`和`clear()`等方法（否则会抛出UnsupportedOperationException异常）。

原因是`asList()`返回的是Arrays的内部类ArrayList，使用到的是适配器模式，并未实现集合的某些修改方法。

```java
public static <T> List<T> asList(T... a) {
    return new ArrayList<>(a);
}
```

```java
ArrayList(E[] array) {
    if (array==null)
        throw new NullPointerException();
    a = array;
}
```

## Comparator注意事项

Comparator要满足自反性、传递性和对称性，否则会抛出IllegalArgumentException。

- 自反性：x，y的比较结果和y，x的比较结果相反。
- 传递性：x > y，y > z，则x > z。
- 对称性：x = y，则x，z的比较结果和y，z比较结果相同。

## HashMap多线程下死循环问题

多线程`put()`时触发`resize()`，进而导致新建Entry数组，并将之前数组中每个链表都重新hash到新的数组中；由于多线程下Entry数组私有，但Entry链表中的元素共享，且由于采用头插法hash到新的链表数组中，导致链表出现环。

而当`get()`到此环，而`get()`的hash值又与此环的任何元素都不相等时，则出现死循环。

[疫苗：Java HashMap的死循环 | | 酷 壳 - CoolShell][hashmap coolshell]

## 什么是ConcurrentHashMap

ConcurrentHashMap 类中包含两个静态内部类 HashEntry 和 Segment。HashEntry 用来封装映射表的键 / 值对；Segment 用来充当锁的角色，每个 Segment 对象守护整个散列映射表的若干个桶。每个桶是由若干个 HashEntry 对象链接起来的链表。一个 ConcurrentHashMap 实例中包含由若干个 Segment 对象组成的数组。

Segment 类继承于 ReentrantLock 类，从而使得 Segment 对象能充当锁的角色。每个 Segment 对象用来守护其（成员对象 table 中）包含的若干个桶。

## Map类集合k／V能否存储null值的情况

|        集合类        | Key允许为null | Value允许为null |    Super    |   说明  |
| :---------------: | :--------: | :----------: | :---------: | :---: |
|     Hashtable     |     No     |      No      |  Dictionary |  线程安全 |
| ConcurrentHashMap |     No     |      No      | AbstractMap | 分段锁技术 |
|      TreeMap      |     No     |      Yes     | AbstractMap | 线程不安全 |
|      HashMap      |     Yes    |      Yes     | AbstractMap | 线程不安全 |

## SimpleDataFormat线程安全吗？

SimpleDataFormat线程不安全，一般不要定义为static变量，如果定义为static则必须加锁，或者使用DataUtils工具类。

## Timer可以用来并行处理定时任务吗？

一个Timer对象仅有一个线程，如果向Timer提交多个TimerTask，且某个TimerTask很耗时，则其他TimerTask即使到了执行时间，也仍会等待之前的task执行完毕；甚至，如果某个TimerTask抛出异常导致线程终止，则其后的TimerTask将不会执行。

## 可以在多线程下使用Random吗？

Random是线程安全的（由AtomicLong实现），但在多线程时可能遇到效率问题。Random的seed是AtomicLong类型，其使用CAS（compare-and-set）操作来更新；CAS在资源高度竞争时表现会变得很糟糕。

ThreadLocalRandom克服了如上Random的缺陷。

## `Thread.join()`是如何实现的？

`join()`方法是通过`wait()`实现的。当当前线程调用`otherThread.join()`时，当前线程会获得对象otherThread的锁，调用该对象的`wait()`方法开始等待；直到otherThread唤醒当前线程。而当otherThread退出时，会在native方法中调`notifyAll()`从而唤醒当前线程，当前线程继续运行。

## GC中可回收对象的判定方法

### 引用计数法

给对象中添加一个引用计数器，每当有一个地方引用它时，计数器值就加1；当引用失效时，计数器值就减1；任何时刻计数器为0的对象就是不可能再被使用的。

其优点是简单，高效；缺点是很难处理循环引用。

### 可达性分析算法

通过一系列称为“GC Roots”的对象作为起始点，从这些节点开始向下搜索，搜索所走过的路径称为引用链（Reference Chain），当一个对象到GC roots没有任何引用链相连（用图论的话来说，就是从GC Roots到这个对象不可达）时，则证明此对象是不可用的。

可作为GC Roots的对象包括：

- 虚拟机栈（栈帧中的本地变量表）中引用的对象。
- 方法区中类静态属性引用的对象。
- 方法区中常量引用的对象。
- 本地方法栈中JNI（即一般说的Native方法）引用的对象。

## 垃圾收集算法

### 标记——清除算法

标记——清除算法分为“标记”和“清除”两个阶段：首先标记出所有需要回收的对象，在标记完成后统一回收所有被标记的对象（标记过程即使用可回收对象的判定方法）。

主要有两方面的不足：

- 效率问题，标记和清除两个过程的效率都不高。
- 空间问题，标记清除之后会产生大量不连续的内存碎片，空间碎片太多可能会导致以后在程序运行过程中需要分配较大对象时，无法找到足够的连续内存而不得不提前触发另一次垃圾收集动作。

### 复制算法

复制算法将可用内存容量划分为大小相等的两块，每次只使用其中的一块。当这一块的内存用完了，就将还存活着的对象复制到另一块上，然后把已使用过的内存空间一次性清理掉。这样使得每次都是对整个半区进行内存回收，内存分配时也就不用考虑内存碎片等复杂情况，只要移动堆顶指针，按序分配内存即可，实现简单，运行高效。

主要的不足是将内存缩小为了原来的一半，代价较高。

### 标记——整理算法

标记——整理算法的标记过程仍然与标记——清除算法一样，但后续步骤不是直接对可回收对象进行清理，而是让所有存活的对象都向一端移动，然后直接清理掉端边界以外的内存。

### 分代收集算法

分代收集算法，即：分代分配，分代回收。对象将根据存活的时间被分为：年轻代（Young Generation）、年老代（Old Generation）、永久代（Permanent Generation，也就是方法区）。

#### 年轻代

年轻代可以分为3个区域：Eden区和两个存活区（Survivor 0 、Survivor 1）。

1. 绝大多数刚创建的对象会被分配在Eden区，其中的大多数对象很快就会消亡。Eden区是连续的内存空间，因此在其上分配内存极快；
2. 最初一次，当Eden区满的时候，执行Minor GC，将消亡的对象清理掉，并将剩余的对象复制到一个存活区Survivor0（此时，Survivor1是空白的，两个Survivor总有一个是空白的）；
3. 下次Eden区满了，再执行一次Minor GC，将消亡的对象清理掉，将存活的对象复制到Survivor1中，然后清空Eden区；
4. 将Survivor0中消亡的对象清理掉，将其中可以晋级的对象晋级到Old区，将存活的对象也复制到Survivor1区，然后清空Survivor0区；
5. 当两个存活区切换了几次（HotSpot虚拟机默认15次，用-XX:MaxTenuringThreshold控制，大于该值进入老年代，但这只是个最大值，并不代表一定是这个值）之后，仍然存活的对象（其实只有一小部分，比如，我们自己定义的对象），将被复制到老年代。

这种垃圾回收的方式就是复制算法。由于绝大部分的对象都是短命的，甚至存活不到Survivor中，所以，Eden区与Survivor的比例较大，HotSpot默认是 8:1，即分别占新生代的80%，10%，10%。如果一次回收中，Survivor + Eden中存活下来的内存超过了10%，则需要将一部分对象分配到老年代。

#### 年老代

对象如果在年轻代存活了足够长的时间而没有被清理掉（即在几次Young GC后存活了下来），则会被复制到年老代，年老代的空间一般比年轻代大，能存放更多的对象，在年老代上发生的GC次数也比年轻代少。当年老代内存不足时，将执行Major GC，也叫 Full GC。

年老代的垃圾回收方式是标记——整理算法。

#### 永久代

永久代的回收并不是必须的。

其回收有两种：常量池中的常量和无用的类信息。常量的回收很简单，没有引用了就可以被回收。对于无用的类进行回收，必须保证3点：

- 类的所有实例都已经被回收；
- 加载类的ClassLoader已经被回收；
- 类对象的Class对象没有被引用（即没有通过反射引用该类的地方）。

## Java是值传递还是引用传递？

Java中方法参数传递方式是按值传递。

- 如果参数是基本类型，传递的是基本类型的字面量值的拷贝。
- 如果参数是引用类型，传递的是该参量所引用的对象在堆中地址值的拷贝。

## 线程同步的方法

- 同步方法：synchronized关键字修饰的方法。
- 同步代码块：synchronized关键字修饰的语句块。
- volatile关键字。
- 可重入锁： ReentrantLock类是可重入、互斥、实现了Lock接口的锁。
- ThreadLocal。

## Java创建线程的方式

### 继承Thread类创建线程类

1. 定义Thread类的子类，并重写该类的`run()`方法，该`run()`方法的方法体就代表了线程要完成的任务。因此把`run()`方法称为执行体。
2. 创建Thread子类的实例，即创建了线程对象。
3. 调用线程对象的`start()`方法来启动该线程。

### 通过Runnable接口创建线程类

1. 定义runnable接口的实现类，并重写该接口的`run()`方法，该`run()`方法的方法体同样是该线程的线程执行体。
2. 创建Runnable实现类的实例，并依此实例作为Thread的target来创建Thread对象，该Thread对象才是真正的线程对象。
3. 调用线程对象的`start()`方法来启动该线程。

### 通过Callable和Future创建线程

1. 创建Callable接口的实现类，并实现`call()`方法，该`call()`方法将作为线程执行体，并且有返回值。

2. 创建Callable实现类的实例，使用FutureTask类来包装Callable对象，该FutureTask对象封装了该Callable对象的`call()`方法的返回值。

3. 使用FutureTask对象作为Thread对象的target创建并启动新线程。

4. 调用FutureTask对象的`get()`方法来获得子线程执行结束后的返回值。

## 线程池原理

java.uitl.concurrent.ThreadPoolExecutor类是线程池中最核心的一个类，其构造函数为

```java
public ThreadPoolExecutor(int corePoolSize,
                            int maximumPoolSize,
                            long keepAliveTime,
                            TimeUnit unit,
                            BlockingQueue<Runnable> workQueue,
                            ThreadFactory threadFactory,
                            RejectedExecutionHandler handler)
```

- `corePoolSize`：核心池大小，默认情况下线程不会超过核心大小。
- `maximumPoolSize`： 最大线程数，当达到一定负载时，线程数会超过核心数，但始终小于最大线程数。当负载较轻会回收线程至核心池数量。
- `keepAliveTime`：表示线程没有任务执行时，的存活时间。默认情况，当线程数大于核心小于最大数量时才会启用；如果调用allowCoreThreadTimeOut(boolean)方法，线程数下界为0。
- `unit`：`keepAliveTime`的时间单位。
- `workQueue`：阻塞队列，用来存储等待执行的任务。
  - ArrayBlockingQueue：基于数组的先进先出，创建时必须指定大小。
  - PriorityBlockingQueue：优先级队列。
  - LinkedBlockingQueue：基于链表的队列，默认长度为Integer.MAX_VALUE。
  - SynchronousQueue：不保存任务，直接创建新线程。
- `threadFactory`：线程工厂。
- `handler`：对拒绝任务的处理策略，四种参数。
  - AbortPolicy：丢弃任务并抛异常。
  - DiscardPolicy：丢弃任务不抛异常。
  - DiscardOldestPolicy：丢弃最前面的任务。
  - CallerRunsPolicy：交由调用线程处理。

运行流程：

1. 接收到任务。
2. 判断已存在线程数是否大于等于核心线程数，如果不是，则创建新线程执行任务；否则转3。
3. 判断任务队列是否有界，如果不是，将任务加入队列中；否则转4。
4. 判断任务队列是否已满，如果不是，将任务加入队列中；否则转5。
5. 判断已存在线程数是否等于最大线程数，如果不是，则创建新线程执行任务；否则转6。
6. 拒绝该任务。

## 类与类加载器的关系

对于任意一个类，都需要由加载它的类加载器和这个类本身一同确立其在Java虚拟机中的唯一性；每个类加载器，都拥有一个独立的类名称空间。

比较两个类是否“相等”，只有在这两个类是由同一个类加载器加载的前提下才有意义。否则，即使这两个类来源于同一个Class文件，被同一个虚拟机加载，只要加载它们的类加载器不同，那这两个类就必定不相等。

这里所指的“相等”，包括代表类的Class对象的`equals()`方法、`isAssignableFrom()`方法、`isInstance()`方法的返回结果，也包括使用`instanceof`关键字做对象所属关系判定等情况。

## 双亲委派模型

从Java虚拟机角度来看，只存在两种类加载器：

- 启动类加载器（Bootstrap ClassLoader）：这个类加载器使用C++语言实现，是虚拟机自身的一部分。
- 所有其他类加载器：这些类加载器都由Java语言实现，独立于虚拟机外部，并且全都继承自抽象类java.lang.ClassLoader。

从Java开发人员角度来看，绝大多数Java程序都会用到以下3种系统提供的类加载器：

- 启动类加载器（Bootstrap ClassLoader）：负责将存放在&lt;JAVA_HOME>/lib目录中的，或者被-Xbootclasspath参数所指定的路径中的，并且是虚拟机识别的（仅按文件名识别，如rt.jar）类库加载到虚拟机内存中。启动类加载器无法被Java程序直接引用。
- 扩展类加载器（Extension ClassLoader）：由sun.misc.Launcher$ExtClassLoader实现，负责加载&lt;JAVA_HOME>/lib/ext目录中的，或者被java.ext.dirs系统变量所指定的路径中的所有类库。开发者可以直接使用扩展类加载器。
- 应用程序类加载器（Application ClassLoader）：由sun.misc.Launcher$AppClassLoader实现，由于这个类加载器是ClassLoader中的`getSystemClassLoader()`方法的返回值，所以一般也称它为系统类加载器。负责加载用户类路径（ClassPath)上所指定的类库。开发者可以直接使用这个类加载器，如果应用程序中没有自定义过自己的类加载器，一般情况下这个就是程序中默认的类加载器。

![Parents Delegation Model][parents_delegation_model]

```java
protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
    synchronized (getClassLoadingLock(name)) {
        // First, check if the class has already been loaded
        Class<?> c = findLoadedClass(name);
        if (c == null) {
            try {
                if (parent != null) {
                    c = parent.loadClass(name, false);
                } else {
                    c = findBootstrapClassOrNull(name);
                }
            } catch (ClassNotFoundException e) {
                // ClassNotFoundException thrown if class not found
                // from the non-null parent class loader
            }

            if (c == null) {
                // If still not found, then invoke findClass in order
                // to find the class.
                c = findClass(name);
            }
        }
        if (resolve) {
            resolveClass(c);
        }
        return c;
    }
}
```

双亲委派模型的工作过程是：如果一个类加载器收到了类加载请求，它首先不会自己去尝试加载这个类，而是把这个请求委派给父类加载器去完成，每一个层次的类加载器都是如此。因此，所有的加载请求最终都应该传送到顶层的启动类加载器中，只有当父类加载器反馈自己无法完成这个加载请求时，子类加载器才会尝试自己去加载。

## 如何自定义类加载器

继承ClassLoader类，实现`findClass()`方法，调用父类的`defineClass()`方法，返回加载后的类。

需要被加载的类：

```java
package com.example.tomcat;

public class Foo {

	public void sayHi() {
		System.out.println("hello world");
	}
}
```

自定义类加载器：

```java
package com.example.tomcat;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;

public class MyClassLoader extends ClassLoader {
    //类加载器的名称
    private String name;
    //类存放的路径
    private String classpath = "/demo/target/classes/com/example/tomcat/";
    
    MyClassLoader(String name) {
        this.name = name;
    }

    MyClassLoader(ClassLoader parent, String name) {
        super(parent);
        this.name = name;
    }

    /**
     * 重写findClass方法
     */
    @Override
    public Class<?> findClass(String name) {
        byte[] data = loadClassData(name);
        return this.defineClass(name, data, 0, data.length);
    }

    public byte[] loadClassData(String name) {
        try {
            name = name.replace(".", "//");
            FileInputStream is = new FileInputStream(new File(classpath + name + ".class"));
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            int b = 0;
            while ((b = is.read()) != -1) {
                baos.write(b);
            }
            return baos.toByteArray();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public static void main(String args[]) throws Exception {
        MyClassLoader my = new MyClassLoader("myLoader");
        Class<?> loadClass = my.loadClass("com.example.tomcat.Foo");
        Foo cast = (Foo) loadClass.newInstance();
        cast.sayHi();
    }
}
```

## 类的生命周期

- 加载（Loading）
- 连接（Linking）
  - 验证（Verification）
  - 准备（Preparation）
  - 解析（Resolution）
- 初始化（Initialization）
- 使用（Using）
- 卸载（Unloading）

## 类初始化的时机

- 遇到new、getstatic、putstatic或invokestatic这4条字节码指令时，如果类没有进行过初始化，则需先触发其初始化。生成这4条指令的最常见的Java代码场景是：
  - 使用new关键字实例化对象的时候
  - 读取或设置一个类的静态字段的时候
  - 调用一个类的静态方法的时候
- 使用java.lang.reflect包的方法对类进行反射调用的时候，如果类没有进行过初始化，则需先触发其初始化。
- 当初始化一个类的时候，如果发现其父类还没有进行过初始化，则需先触发其父类的初始化。
- 当虚拟机启动时，用户需要指定一个要执行的主类（包含`main()`方法的那个类），虚拟机会先初始化这个主类。

## 类的加载过程

### 加载

1. 通过一个类的全限定名来获取定义此类的二进制字节流。
2. 将这个字节流所代表的静态存储结构转换为方法区的运行时数据结构。
3. 在内存中生成一个代表这个类的java.lang.Class对象，作为方法区这个类的各种数据的访问入口。

### 连接

#### 验证

验证的目的是为了确保Class文件的字节流中包含的信息符合当前虚拟机的要求，并且不会危害虚拟机自身的安全。验证阶段大致完成4个阶段的检验动作：文件格式验证、元数据验证、字节码验证、符号引用验证。

##### 文件格式验证

即验证字节流是否符合Class文件格式的规范，并且能被当前版本的虚拟机处理。主要包括以下验证点：

- 是否以魔术0xCAFEBABE开头。
- 主、次版本号是否在当前虚拟机处理范围之内。
- 常量池的常量中是否有不被支持的常量类型（检查常亮tag标识）。
- 指向常亮的各种索引值中是否有指向不存在的常量或不符合类型的常量。
- CONSTANT_Uft8_info型的常量中是否有不符合UTF8编码的数据。
- Class文件中各个部分及文件本身是否有被删除或附加的其他信息。
- ……

##### 元数据验证

即对字节码描述的信息进行语义分析，以保证其描述的信息符合Java语言规范的要求。这个阶段可能包括以下验证点：

- 这个类是否有父类（除了java.lang.Object之外，所有的类都应该有父类）。
- 这个类的父类是否继承了不允许被继承的类（被final修饰的类）。
- 如果这个类不是抽象类，是否实现了其父类或接口之中要求实现的所有方法。
- 类中的字段、方法是否与父类产生矛盾（如覆盖了父类的final字段，或出现不符合规则的方法重载，如方法参数一致，但返回值类型不同）。
- ……

##### 字节码验证

即通过数据流河控制流分析，确定程序语义是合法的、符合逻辑的。这个阶段将对类的方法体进行校验分析，保证被校验类的方法在运行时不会做出危害虚拟机安全的事件，如：

- 保证任意时刻操作数栈的数据类型与指令代码序列都能配合工作，例如不会出现类似在操作栈放置了一个int类型的数据，使用时却按long类型来加载入本地变量表中。
- 保证跳转指令不会跳转到方法体以外的字节码指令上。
- 保证方法体中的类型转换是有效的，例如不能把父类对象赋值给子类数据类型。

##### 符号引用验证

即对类自身以外（常量池中的各种符号引用）的信息进行匹配性校验。发生在虚拟机将符号引用转化为直接引用的时候，通常包括以下几个验证点：

- 符号引用中通过字符串描述的全限定名是否能找到对应的类。
- 在指定类中是否存在符合方法的字段描述符以及简单名称所描述的方法和字段。
- 符号引用中的类、字段、方法的访问性（private、protected、public、default）是否可以被当前类访问。
- ……

#### 准备

准备阶段是正式为类变量分配内存并设置类变量初始值的阶段，这些变量使用的内存都将在方法区中进行分配。这时候进行内存分配的仅包括类变量（被static修饰的变量），而不包括示例变量。

#### 解析

解析阶段是虚拟机将常量池内的符号引用替换为直接引用的过程。解析动作主要针对类或接口、字段、类方法、接口方法、方法类型、方法句柄和调用点限定符7类符号引用进行。

### 初始化

初始化阶段，根据程序员通过程序制定的主观计划去初始化类变量和其他资源。即初始化阶段是执行类构造器`<clinit>()`方法的过程。

- `<clinit>()`方法是由编译器自动收集类中的所有类变量的赋值动作和静态语句块（static {}块）中语句合并产生。编译器收集的顺序是由语句在源文件中出现的顺序所决定的，静态语句块中只能访问到定义在静态语句块之前的变量，定义在它之后的变量，在前面的静态语句块可以赋值，但不能访问。
- `<clinit>()`方法与类的构造函数（或者说实例构造器`<init>()`方法）不同，它不需要显式地调用父类构造器，虚拟机会保证在子类的`<clinit>()`方法执行之前，父类`<clinit>()`方法已经执行完毕。
- 由于父类的`<clinit>()`方法先执行，也就意味着父类中定义的静态语句块要优先于子类的变量赋值操作。
- `<clinit>()`方法对于类或接口来说并不是必须的，如果一个类中没有静态语句块，也没有对变量的赋值操作，那么编译器可以不为这个类生成`<clinit>()`方法。
- 接口中不能使用静态语句块，但仍然有变量初始化的赋值操作，因此接口与类一样都会生成`<clinit>()`方法。但接口与类不同的是，执行接口的`<clinit>()`方法不需要先执行父接口的`<clinit>()`方法。只有当父接口中定义的变量使用时，父接口才会初始化。另外，接口的实现类在初始化时也一样不会执行接口的`<clinit>()`方法。
- 虚拟机会保证一个类的`<clinit>()`方法在多线程环境中被正确的加锁、同步，如果多个线程同时去初始化一个类，那么只有一个线程去执行这个类的`<clinit>()`方法，其他线程都需要阻塞等待，直到活动线程执行`<clinit>()`方法完毕。

## 符号引用和直接引用的区别

- 符号引用（Symbolic References）：符号引用以一组符号来描述所引用的目标，符号可以是任意形式的字面量，只要使用时能无歧义地定位到目标即可。符号饮用与虚拟机实现的内存布局无关，引用的目标并不一定已经加载到内存中。
- 直接引用（Direct References）：直接引用可以时直接指向目标的指针、相对偏移量或是一个能间接定位到目标的句柄。直接引用是和虚拟机实现内存布局相关的，同一个符号引用在不同虚拟机实例上翻译出来的直接引用一般不会相同。

## 如何理解平台无关性

虚拟机和字节码存储格式是实现语言无关性的基础。Java虚拟机不和包括Java在内的任何语言绑定，它只与“Class文件”这种特定的二进制文件格式所关联，Class文件中包含了Java虚拟机指令集和符号表以及若干其它辅助信息。任何一门功能性语言都可以表示为一个能被Java虚拟机所接受的有效的Class文件。

## 运行时数据区域

Java虚拟机在执行Java程序过程中会把内存区域划分为若干个不同的数据区域，这些区域各有各自的用途、创建和销毁时间。有的区域随着虚拟机进程的启动而存在，有些区域则依赖用户线程的启动和结束而建立和销毁。

![Java Runtime Data Areas][java_runtime_data_areas]

### 程序计数器（Program Counter Register）

程序计数器占用较小的内存空间，可以看做是当前线程所执行的字节码的行号指示器，由于Java虚拟机的多线程是通过线程轮流切换并分配处理器执行时间的方式来实现的，在任何一个确定的时刻，一个处理器（对于多核处理器来说就是一个内核）都只会执行一条线程中的指令。因此，为了线程切换后能够恢复到正确的执行位置，每条线程都需要有一个独立的程序计数器。

如果线程正在执行Java方法，则计数器记录的是正在执行的虚拟机字节码指令的地址；如果正在执行的是Native方法，则这个计数器则为空。

### Java虚拟机栈（Java Virtual Machine Stacks）

虚拟机栈也是线程私有，而且生命周期与线程相同，每个Java方法在执行的时候都会创建一个栈帧（Stack Frame）用于存储局部变量表、操作数栈、动态链接、方法出口等信息。

Java虚拟机规范中，对该区域规定了两种异常情况：

- 如果线程请求的栈深度大于虚拟机所允许的深度，讲抛出StackOverflowError异常；
- 虚拟机栈可以动态拓展，当扩展时无法申请到足够的内存，就会抛出OutOfMemoryError异常。

### 本地方法栈（Native Method Stack）

本地方法栈的作用与虚拟机栈作用是非常类似的。虚拟机栈为虚拟机执行Java方法（也就是字节码）服务，而本地方法栈则为虚拟机使用到的Native方法服务。

### Java堆（Java Heap）

对大多数应用来说，Java堆（Heap）是Java虚拟机所管理的内存中最大的一块，Java堆是被所有线程共享的一块内存区域，在虚拟机启动时创建。该内存区域唯一的目的就是存放对象实例，Java对象实例以及数组都在堆上分配（随着JIT编译器发展等技术成熟，所有对象分配在堆上也渐渐不是那么“绝对”了）。

根据Java虚拟机规范的规定，Java堆可以处于物理上不连续的内存空间中，只要逻辑上是连续的即可，就像我们的磁盘空间一样（或者说，像链表一样虽然内存上不一定连续，但逻辑上是连续）。

### 方法区（Method Area）

方法区与Java堆一样，是各个线程共享的内存区域，用于存储已被虚拟机加载的类信息、常量、静态变量、即时编译器编译后的代码等数据。

### 运行时常量池（Runtime Constant Pool）

运行时常量池是方法区的一部分。Class文件中除了有关类的版本、字段、方法、接口等描述信息外，还有一项信息是常量池，用于存放编译期生成的各种字面量和符号引用，这部分内容将在类加载后进入方法区的运行时常量池中存放。

运行时常量池相对于Class文件常量池的另一个重要特征是具备动态性，Java语言并非不要求常量一定只有编译期才能产生，也就是并非预置入Class文件中常量池的内容才能进入方法区运行时常量池，运行期间也可以将新的常量池放入池中。

[cache_consistency]: cache_consistency.jpeg

[collections_framework_overview]: collections_framework_overview.png

[list_api_class_diagram]: List_API_class_diagram.png

[map_api_class_diagram]: Map_API_class_diagram.png

[queue_api_class_diagram]: Queue_API_class_diagram.png

[set_api_class_diagram]: Set_API_class_diagram.png

[thread_life_cycle]: thread_life_cycle.png

[hashmap coolshell]: http://coolshell.cn/articles/9606.html

[parents_delegation_model]: parents_delegation_model.png

[java_runtime_data_areas]: java_runtime_data_areas.png
