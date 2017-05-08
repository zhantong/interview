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

 属性  |  成员变量   |     局部变量      |   静态变量
:--: | :-----: | :-----------: | :-------:
定义位置 | 在类中，方法外 | 方法中，或者方法的形式参数 |  在类中，方法外
初始化值 | 有默认初始化值 | 无，先定义，赋值后才能使用 |  有默认初始化值
调用方式 |  对象调用   |      ---      | 对象调用，类名调用
存储位置 |   堆中    |      栈中       |    方法区
生命周期 | 与对象共存亡  |    与方法共存亡     |   与类共存亡
 别名  |  实例变量   |      ---      |    类变量

## 谈谈你对StrongReference、WeakReference和SoftReference的认识

- 强引用（StrongReference）：就是在代码中普遍存在的，类似`Object obj = new Object()`这类的引用，只要强引用还存在，GC永远不会回收掉被引用的对象。
- 软引用（SoftReference）：用来描述一些还有用但非必须的对象。对于软引用关联着的对象，在系统将要发生内存溢出异常时，将会把这些对象列入回收范围之中进行第二次回收。如果这次回收还没有足够的内存，才会抛出内存溢出异常。在JDK 1.2之后，提供了SoftReference类来实习软引用。
- 弱引用（WeakReference）：也是用来描述非必须对象的，但是它的强度比软引用更弱一些，被弱引用关联的对象只能生存到了下一次GC发生之前。当GC工作时，无论当时内存是否足够，都会回收只被弱引用关联的对象。在JDK 1.2之后，提供了WeakReference类来实现弱引用。
- 虚引用（PhantomReference）：虚引用也称幽灵引用或者幻影引用，它是最弱的一种引用关系。一个对象是否有虚引用的存在，完全不会对其生存时间构成影响，也无法通过虚引用来取得一个对象实例。为一个对象设置虚引用的唯一目的就是在这个对象被GC回收是收到一个系统通知。在JDK 1.2之后提供了PhantomReference类来实现虚引用。 �在JDK 1.2之后提供了PhantomReference类来实现虚引用。

## String, StringBuffer, SrtingBuilder的区别

- String类对象为不可变对象，一旦你修改了String对象的值，隐形重新创建了一个新的对象，释放原String对象，StringBuffer、StringBuilder类对象为可修改对象，可以通过append()方法来修改值。
- String类对象的性能元不如StringBuffer类和StringBuilder类。
- StringBuffer是线程安全的可变字符序列，而StringBuilder是线程不安全的可变字符序列，但是在单线程中使用效率很高。
