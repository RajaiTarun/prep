import json

# ---------- helpers ----------
def mcq(q, opts, ans, why, code=None):
    return {"t": "mcq", "q": q, "code": code, "opts": opts, "ans": ans, "why": why}

def out(q, code, ans, why):
    return {"t": "out", "q": q, "code": code, "ans": ans, "why": why}

def item(text, core=True, tag=None):
    return {"x": text, "c": core, "tag": tag}

# ---------- quiz banks ----------
Q = {}

Q["d1a"] = [
    mcq("HR asks: 'Hyderabad or Bengaluru, and why?' Which answer works best?",
        ["I already study at IIIT Hyderabad and my friends are here, so Hyderabad.",
         "Hyderabad, because the work there is closest to what I want to do (name it from the PPT), and two professional reasons.",
         "Either is fine, I'm flexible."],
        1, "Seniors said: decide in advance, give professional reasons, never personal ones like hometown or friends. 'Flexible' sounds unprepared, and you can't change it later (Nikhil)."),
    mcq("'Why MathWorks?' Which answer would a manager remember?",
        ["Big company, great culture, good work-life balance.",
         "Engineers and scientists depend on MATLAB and Simulink for real work. I like building tools other people rely on, like MerchFlow, which I built after talking to its users. And EDG trains new engineers across the product.",
         "The package is good and the brand is great on a resume."],
        1, "The answer has to be specific to MathWorks and tied to your own story. Option A fits every company, and option C is about you, not them."),
    mcq("'What do you understand about EDG?' What is the safest way to answer?",
        ["Repeat the PPT slides word for word.",
         "Say the PPT point, explain what it means in practice, then say why it suits you.",
         "Say you'll learn about it after joining."],
        1, "Anubhav was asked what the PPT points 'actually mean'. Repeating slides fails the first follow-up question."),
]
Q["d1b"] = [
    mcq("'Tell me about yourself.' Pick the right shape.",
        ["Start from your school and go year by year in detail.",
         "Read your resume aloud, line by line.",
         "90 seconds: B.E. IT, then GATE and PGEE, then M.Tech at IIIT-H, the systems you built, and why MathWorks EDG."],
        2, "Short story with a direction that ends at MathWorks. The year-by-year timeline comes only when they ask for it, and they will (Anubhav, Sanchit)."),
    mcq("'Why did you take GATE twice?'",
        ["'The first rank wasn't good enough.' Then stop.",
         "Give the honest reason, what you changed in your preparation, and the result (97.24 percentile, PGEE AIR 114).",
         "Change the topic."],
        1, "HR asks 'why?' about every decision. A setback with what you changed and a measurable result becomes a strength story."),
    mcq("'Why not a PhD?'",
        ["'A PhD is boring.'",
         "'Maybe in two years.'",
         "'I enjoy building products people use. EDG lets me learn that at scale, and industry is where I want to grow now.'"],
        2, "Option B tells them you might leave soon. Option A sounds dismissive."),
    mcq("'What if you get a better offer?'",
        ["'I'd take the better offer.'",
         "Give an honest preference with reasons tied to the work, EDG and the values, not the package.",
         "'I haven't thought about it.'"],
        1, "Sanchit was cross-questioned on exactly this."),
]

Q["d2a"] = [
    out("What does this print?",
        'struct B {\n  B() { f(); }\n  virtual void f() { cout << "B"; }\n};\nstruct D : B {\n  void f() override { cout << "D"; }\n};\nint main() { D d; d.f(); }',
        "BD",
        "Inside B's constructor the object is still only a B, because the vptr points to B's vtable at that moment. A virtual call in a constructor never reaches the derived class."),
    out("What does this print on a 64-bit machine?",
        "struct A {};\nstruct V { virtual void f() {} };\nint main() { cout << sizeof(A) << \" \" << sizeof(V); }",
        "1 8",
        "An empty class takes 1 byte so every object has its own address. One virtual function adds a hidden vptr (8 bytes); the vtable itself is one per class, not per object."),
    out("What does this print?",
        'struct B { virtual void f() { cout << "B"; } };\nstruct D : B { void f() { cout << "D"; } };\nvoid g(B b)  { b.f(); }\nvoid h(B& b) { b.f(); }\nint main() { D d; g(d); h(d); }',
        "BD",
        "g takes B by value, so the D part is sliced off (object slicing). h takes a reference, so dynamic dispatch works."),
    mcq("B has a NON-virtual destructor. `B* p = new D; delete p;` What happens?",
        ["Only ~B runs: undefined behaviour, and D's resources leak", "~D then ~B run", "Compile error"],
        0, "Make the base destructor virtual and the output becomes ~D~B. (Checked: with a virtual destructor it prints ~D~B.)"),
    mcq("Which statement is TRUE in C++?",
        ["An abstract class cannot have a constructor",
         "A pure virtual destructor must still have a body",
         "A pure virtual function can never have a definition",
         "C++ has an `interface` keyword"],
        1, "Derived destructors always call the base destructor, so it needs a body. Abstract classes can have constructors (to set up members), and a pure virtual function may have a definition. A C++ 'interface' is just a class with only pure virtual functions plus a virtual destructor."),
]
Q["d2b"] = [
    out("What does this print?",
        'struct T {\n  T() { cout << "c"; }\n  T(const T&) { cout << "C"; }\n  T& operator=(const T&) { cout << "="; return *this; }\n};\nint main() { T a; T b = a; T c; c = a; }',
        "cCc=",
        "`T b = a;` creates a new object, so it calls the copy constructor, not operator=. operator= runs only on an object that already exists."),
    mcq("A class owns `int* data` (new in constructor, delete in destructor) and has NO copy constructor. `Buf a; Buf b = a;` At the end of scope:",
        ["Works fine", "Double free / crash: both objects delete the same pointer", "Compile error"],
        1, "The default copy is shallow. This is the Rule of Three: if you write a destructor, also write the copy constructor and copy assignment (deep copy), or `= delete` them."),
    mcq("You wrote only `Point(int x, int y)`. Then `Point arr[5];`",
        ["Compiles, 5 zero points", "Error: no default constructor", "Compiles with garbage values"],
        1, "Once you write any constructor, the compiler stops generating the default one. Arrays of objects need it. This answers Sneha's 'why do we need a default constructor?'"),
    mcq("What does `Widget(const Widget&) = delete;` do?",
        ["Makes Widget non-copyable (like unique_ptr)", "Deletes the object", "Makes copies faster"],
        0, "`= delete` removes a function the compiler would otherwise generate. unique_ptr does exactly this with its copy operations."),
]
Q["d2c"] = [
    out("What does this print?",
        "struct S {\n  static int n;\n  S() { ++n; }  ~S() { --n; }\n};\nint S::n = 0;\nint main() {\n  S a;\n  { S b, c; cout << S::n; }\n  cout << S::n;\n}",
        "31",
        "One static counter is shared by all objects. b and c are destroyed at the closing brace, so the count drops back to 1. The static member must be defined outside the class (int S::n = 0;)."),
    out("C++17. What does this print?",
        "int x = 1;\nauto f = [x]() mutable { return ++x; };\ncout << f() << f() << x;",
        "231",
        "[x] captures a COPY. mutable lets the lambda change its own copy, which persists between calls (it's a member of the functor class the compiler makes). The outer x stays 1."),
    mcq("`const int* p;` and `int* const q = &x;` Which line compiles?",
        ["*p = 5;", "p = &y;", "q = &y;"],
        1, "Read right to left: p is a pointer to a const int (the pointer can move, the value is read-only). q is a const pointer to int (the value can change, the pointer can't move)."),
    mcq("Which is TRUE about friend?",
        ["Friendship is inherited", "Friendship is mutual", "A friend can access the private members of the class that declared it", "A friend function is a member function"],
        2, "Friendship is given, not taken: not inherited, not mutual, and a friend is not a member (no `this`)."),
    mcq("`auto make() { int n = 5; return [&] { return n; }; }` Calling the returned lambda gives:",
        ["5", "Undefined behaviour: a dangling reference to n", "Compile error"],
        1, "[&] captures by reference. n dies when make() returns. Capture by value [=] here."),
]

Q["d3a"] = [
    out("C++17. What does this print?",
        "int a[] = {10, 20, 30};\nint* p = a;\ncout << *p++ << \" \" << *p << \" \";\ncout << ++*p << \" \" << a[1];",
        "10 20 21 21",
        "*p++ reads 10, then moves p to a[1]. *p is 20. ++*p increments the VALUE a[1] to 21. Postfix ++ binds tighter than *; prefix ++ and * associate right to left."),
    out("What does this print?",
        "int a[5] = {1, 2, 3, 4, 5};\nint* p = (int*)(&a + 1);\ncout << *(p - 1);",
        "5",
        "&a is a pointer to the whole array (int(*)[5]), so &a + 1 jumps 5 ints ahead, just past the end. p - 1 is the last element."),
    out("What does this print on 64-bit?",
        "void f(int a[]) { cout << sizeof(a); }\nint main() { int a[10]; cout << sizeof(a) << \" \"; f(a); }",
        "40 8",
        "An array decays to a pointer when it is passed to a function, so inside f, sizeof gives the pointer size. That is why C functions take a separate length."),
    out("What does this print?",
        'char s[] = "abc";\ncout << sizeof(s) << strlen(s);',
        "43",
        "sizeof counts the '\\0' terminator; strlen does not."),
]
Q["d3b"] = [
    out("What does this print (typical 64-bit)?",
        "struct S { char c; int i; char d; };\nstruct R { int i; char c; char d; };\ncout << sizeof(S) << \" \" << sizeof(R);",
        "12 8",
        "Padding aligns int to 4 bytes. Ordering members from large to small cuts the padding."),
    mcq("Which is TRUE about new vs malloc?",
        ["Both call constructors", "new calls the constructor and throws std::bad_alloc on failure; malloc only gets raw bytes and returns NULL", "malloc is type-safe"],
        1, "Also: new returns a typed pointer, malloc returns void*. Pair new with delete and malloc with free, never mixed."),
    out("What does this print?",
        "int a = 5;\nint& r = a;\nint* p = &r;\n*p = 7;\nr++;\ncout << a;",
        "8",
        "A reference is another name for a. &r is the address of a. Both changes land on a."),
    mcq("Your C Vector is full on push_back. Why double the capacity instead of adding 1?",
        ["Saves memory", "Makes push_back amortised O(1); adding 1 makes it O(n) every time", "realloc requires it"],
        1, "Doubling means copies happen rarely: n pushes cost O(n) in total. Know this line for Nikhil's Vector-in-C question."),
]
Q["d3c"] = [
    out("What does this print?",
        "cout << (0.1 + 0.2 == 0.3) << \" \";\nfloat f = 0.1;\ncout << (f == 0.1);",
        "0 0",
        "0.1 can't be stored exactly in binary (IEEE 754). The float and double roundings differ too. Compare with a tolerance: fabs(a - b) < 1e-9."),
    out("What does this print?",
        "unsigned int x = -1;\ncout << (x > 0) << \" \" << x;",
        "1 4294967295",
        "-1 in two's complement is all 1 bits. Read as unsigned, that is the maximum 32-bit value."),
    out("What does this print?",
        'int r = printf("hi");\nprintf("%d", r);',
        "hi2",
        "printf returns the number of characters printed."),
    mcq("Two objects hold shared_ptr to each other. What happens when both go out of scope?",
        ["Both are freed", "Memory leak: the ref counts never reach 0", "Crash"],
        1, "That's a cycle. Make one direction a weak_ptr: it observes without owning."),
    mcq("`unique_ptr<int> a = make_unique<int>(5); auto b = a;`",
        ["Compiles, both own it", "Compile error: the copy is deleted. Use auto b = std::move(a);", "Runtime error"],
        1, "unique_ptr is move-only: one owner at a time."),
]

Q["d4a"] = [
    mcq("'Tell me about a conflict with a teammate.' Strongest answer:",
        ["'My teammate was lazy, so I did all the work.'",
         "'We disagreed on a design choice. I suggested we test both on a small case. The data favoured one, we went with it, and I learnt to bring evidence early.'",
         "'I've never had a conflict.'"],
        1, "No blaming, a concrete action from you, and a learning at the end. 'Never had one' sounds dishonest."),
    mcq("'Your biggest weakness?' Which SHAPE is right? (Use your own real weakness.)",
        ["'I'm a perfectionist.'",
         "A real weakness, a concrete step you are taking, and evidence that it's working.",
         "'I don't have any.'"],
        1, "Interviewers insisted on TWO weaknesses (Anubhav), so have two of this shape."),
    mcq("Which RESULT line is strongest?",
        ["'It went well.'", "'Fixed it, verified with 50 concurrent requests, zero requests over the limit after.'", "'My professor was happy.'"],
        1, "Results with numbers and proof. Your resume already has them: 50 concurrent requests, 58-item checklist, 40% faster, 0 records lost."),
]
Q["d4b"] = [
    mcq("A customer's technical query comes in while your project deadline is close. Best response:",
        ["Ignore it until the deadline",
         "Acknowledge the customer, judge urgency and impact, time-box it, and tell your lead early if it risks the deadline",
         "Drop the project work"],
        1, "Vanshika was asked this exact situation. They want prioritising plus communication."),
    mcq("A bug on a platform you don't know (say, MATLAB):",
        ["Ask a senior immediately",
         "Reproduce it small, read the docs, isolate, try a fix, then ask with what you already tried",
         "Say it's not your area"],
        1, "Aashima was asked this. Tie it to your POSIX shell story: you learned system calls from man pages."),
    mcq("Explain caching to a non-technical HR person:",
        ["'Redis is an in-memory key-value store with TTL eviction.'",
         "'Like keeping answers you already looked up in a notebook so you don't search again. The hard part is crossing an answer out when it changes.'"],
        1, "HRs are not technical; they want real-world analogies (Nikhil)."),
]

Q["d5a"] = [
    out("How many times is 'hi' printed?",
        'fork(); fork(); fork();\nprintf("hi\\n");',
        "8",
        "Each fork doubles the processes: 2^3 = 8."),
    out("How many times is 'x' printed?",
        'if (fork() && fork()) fork();\nprintf("x\\n");',
        "4",
        "First child gets 0, so && short-circuits: it prints once. The parent forks again: that child gets 0 (prints once), and the parent forks a third time (2 prints). Total 4."),
    out("How many times is 'y' printed?",
        'fork() || fork();\nprintf("y\\n");',
        "3",
        "The parent gets a non-zero value, so || short-circuits. The child gets 0, so it runs the second fork, making 2. Total 3."),
    out("Output? (stdout is the terminal, so it is line-buffered)",
        'printf("A");\nfork();\nprintf("B\\n");',
        "AB\nAB",
        "'A' is still sitting in the stdout buffer when fork copies the process, so both processes print it. A great follow-up question: fix it with fflush(stdout) before fork."),
]
Q["d5b"] = [
    mcq("In your pipe code, the parent forgets to close the pipe's write end. `ls | grep a`:",
        ["Works normally", "grep hangs forever waiting for EOF", "ls crashes"],
        1, "EOF only comes when EVERY write end is closed. This is the #1 bug in pipe code, so say it before they ask."),
    mcq("execvp succeeds. A printf on the next line:",
        ["Runs after the command finishes", "Never runs: the process image was replaced", "Runs in the parent"],
        1, "That's why the shell forks first: the child calls exec, and the shell (the parent) survives."),
    mcq("Why does your Ctrl+C handler only set a flag?",
        ["Faster", "printf and malloc aren't async-signal-safe; calling them inside a handler can deadlock or corrupt state", "Signals can't call functions"],
        1, "This is the line from your resume they will poke at."),
    mcq("`dup2(fd, 1); printf(\"hi\");` Where does 'hi' go?",
        ["Terminal", "The file fd points to", "Both"],
        1, "dup2 makes fd 1 (stdout) a copy of fd. That's how your shell does `> out.txt`. dup picks the lowest free fd; dup2 lets you choose the target."),
    mcq("A child exits and the parent never calls wait. The child is:",
        ["Orphan", "Zombie", "Daemon"],
        1, "Zombie = dead, but its exit status is still waiting to be collected. Orphan = the parent died first (adopted by init). Your JobController reaps zombies with waitpid(WNOHANG) on SIGCHLD."),
]
Q["d5c"] = [
    mcq("Key difference between a mutex and a semaphore:",
        ["None", "A mutex has an owner (only the locker unlocks it); a semaphore is a counter any thread can signal", "Semaphores are only for processes"],
        1, "A binary semaphore looks like a mutex but has no ownership."),
    mcq("You always lock A then B in every thread. Which deadlock condition did you break?",
        ["Mutual exclusion", "Hold and wait", "Circular wait", "No preemption"],
        2, "Lock ordering prevents a cycle. Know all 4 conditions."),
    mcq("What do threads of one process share?",
        ["Everything including stacks", "Heap, globals and code; each thread has its own stack and registers", "Nothing"],
        1, "That's why threads need locks and processes need IPC (like your pipes)."),
    mcq("A page fault means:",
        ["The program crashed", "The page isn't in RAM yet; the OS loads it and the instruction retries", "Disk failure"],
        1, "Usually normal (demand paging). A segfault is an INVALID access."),
]

Q["d6a"] = [
    mcq("Redis lock: why store a unique random token as the value of `SET lock:item NX PX 30000`?",
        ["Speed", "So you delete the lock only if it's still yours, in case it expired and someone else took it", "Redis requires a value"],
        1, "Release with check-and-delete done atomically (a Lua script)."),
    mcq("Client retries POST /orders after a timeout, with the same idempotency key:",
        ["A second order is created", "The server finds the key and returns the stored result: no duplicate", "Error 500"],
        1, "That's your resume line: retried requests don't create duplicate orders."),
    mcq("Two checkouts read stock = 1 at the same time (READ COMMITTED) and both decrement. Best fix?",
        ["Add a cache", "`UPDATE items SET stock = stock - 1 WHERE id = ? AND stock > 0` and check the rows affected (or SELECT ... FOR UPDATE)", "Retry later"],
        1, "A lost update. An atomic conditional update makes the database the referee. Your Redis lock solves the same race one layer up."),
    mcq("Cache-aside on a stock change. The right order:",
        ["Update the cache, then the DB", "Write the DB, then delete the cache key", "Only update the cache"],
        1, "Deleting (not updating) avoids racing writers. This is your stale-stock fix, including on checkout and rollback."),
]
Q["d6b"] = [
    out("Node.js: what is the order?",
        "console.log(1);\nsetTimeout(() => console.log(2), 0);\nPromise.resolve().then(() => console.log(3));\nconsole.log(4);",
        "1 4 3 2",
        "Synchronous code first, then microtasks (promises), then the timer queue. Aryan was asked about the event loop."),
    mcq("A RabbitMQ consumer crashes after sending the email but before ack. Then:",
        ["Message lost", "Message is redelivered, so the handler must be idempotent", "Queue blocks"],
        1, "At-least-once delivery. Retries go to a dead-letter queue after N failures."),
    mcq("Can the server revoke a JWT before it expires?",
        ["Yes, JWTs have a revoke field", "Not by itself; use short expiry + refresh tokens, or a denylist", "Only the client can"],
        1, "Stateless means no server lookup. Know this trade-off for your gateway."),
]
Q["d6c"] = [
    mcq("Raft with 3 nodes. One node dies. Then two die.",
        ["Works both times", "With 1 down it still elects (2 of 3 is a majority); with 2 down it stops", "Stops at 1 down"],
        1, "A majority (quorum) is needed. This is why you used 3 nodes."),
    mcq("Why do consumers read only up to the commit watermark?",
        ["Speed", "Records not yet on every in-sync replica could vanish after a leader failover", "Disk limits"],
        1, "That's how '0 acknowledged records lost' holds."),
    mcq("During a network partition your log refuses writes without a quorum. In CAP terms it's:",
        ["AP", "CP", "CA"],
        1, "Consistency over availability. Kashif was asked about CAP."),
    mcq("A real limitation of gRPC vs REST:",
        ["Slower", "Browsers can't call native gRPC directly (they need gRPC-Web or a proxy), and binary payloads are harder to debug", "No streaming"],
        1, "Vanshika was asked gRPC benefits AND limits."),
]

Q["d7a"] = [
    mcq("Find the duplicate in n+1 numbers in 1..n, O(1) space, array unchanged:", ["Sort", "Hash set", "Floyd's cycle detection on indices", "XOR"], 2, "LeetCode 287 (Sanchit). Treat value as next index; the duplicate is the cycle's entry."),
    mcq("Next greater element for every item:", ["Two loops", "Monotonic stack", "Heap"], 1, "O(n) (Piyush)."),
    mcq("Middle of a linked list in one pass:", ["Count, then walk", "Slow + fast pointers", "Recursion"], 1, "The fractional n/k variant moves slow once every k steps (Piyush)."),
    mcq("A stack that also gives min in O(1):", ["Sort on every push", "Keep a second stack (or pairs) of current mins", "Heap"], 1, "LeetCode 155 (Anubhav: stack private, functions public)."),
]
Q["d7b"] = [
    mcq("Quickselect for kth smallest: average and worst case?", ["O(n log n) / O(n log n)", "O(n) / O(n^2)", "O(log n) / O(n)"], 1, "Random pivot keeps the average at O(n) (Kashif)."),
    mcq("Median of two sorted arrays, optimal:", ["Merge, O(m+n)", "Binary search on the partition, O(log min(m,n))"], 1, "Start with the merge idea, then go optimal (Vanshika)."),
    mcq("Set Matrix Zeroes in O(1) extra space:", ["Copy the matrix", "Use the first row and column as markers (+ one flag)", "Recursion"], 1, "LeetCode 73 (Aashrey)."),
]
Q["d7c"] = [
    mcq("Why is heap insert O(log n)?", ["It sorts", "A complete binary tree has height log n, and sift-up moves at most one level per step", "Hashing"], 1, "'Tell me all you know about heap' (Vanshika)."),
    mcq("Building a heap from an unsorted array (heapify):", ["O(n log n)", "O(n)", "O(log n)"], 1, "Most nodes are near the bottom and sift down very little. A classic follow-up."),
    mcq("Puzzle (Digvijay): 50 red + 50 blue balls, 2 buckets. Pick a bucket at random, then a ball. Best split?",
        ["25 red + 25 blue in each", "1 red alone in one bucket; 49 red + 50 blue in the other", "All reds in one bucket"],
        1, "P = 1/2 x 1 + 1/2 x 49/99 = about 74.7%. Explain WHY: one bucket becomes a guaranteed win."),
    mcq("LCA edge case: p is an ancestor of q.", ["Returns the root", "Returns p", "Undefined"], 1, "Aryan's interviewer focused on edge cases."),
]

import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extra import X
for k, v in X.items():
    Q.setdefault(k, []).extend(v)

# ---------- days ----------
NONTECH = "Non-tech"
TECH = "Tech"

days = [
 {"id": "d1", "n": 1, "date": "Sat 21 Nov", "kind": NONTECH, "title": "MathWorks and you",
  "why": "Start where you lose most marks: HR and managerial. Today is half a day, from 1 PM.",
  "blocks": [
    {"time": "1:00 - 3:00 PM", "name": "Know MathWorks, EDG and your location", "items": [
      item("Read mathworks.com: what MATLAB and Simulink do, which industries use them. Write 3 products you can name."),
      item("Read the MathWorks core values. Write each in one line, plus one story of yours that fits it."),
      item("EDG: careers page + search. Write 5 lines: what it is, the training, domains, why it fits you (correct it after the PPT)."),
      item("Decide Hyderabad or Bengaluru. Write 2 professional reasons."),
      item("Read MathWorks' guide 'Interviewing at MathWorks as a Student'.", False),
    ], "quiz": "d1a", "quizName": "Pick the stronger answer"},
    {"time": "3:30 - 6:00 PM", "name": "Your journey, in your words", "items": [
      item("Write 'Tell me about yourself' (90 sec). Record it twice on your phone."),
      item("Year-by-year timeline from Class 10: marks, GATE 2024 and 2025, GATE DA, PGEE AIR 114, CGPAs. A one-line 'why' for each decision."),
      item("Motivation answers: why M.Tech, why not PhD, why not abroad, why MathWorks, what if you get a better offer."),
      item("Write 4 questions to ask them (2-3 technical about MATLAB / MathWorks, 1 about EDG).", False),
    ], "quiz": "d1b", "quizName": "Answer makeover",
     "game": "Why x 3: for every decision on your timeline, ask yourself 'why?' three times in a row. If you stall on the third, rewrite that line."},
  ],
  "talk": "Say 'Tell me about yourself' and 'Why MathWorks?' out loud, timed."},

 {"id": "d2", "n": 2, "date": "Sun 22 Nov", "kind": TECH, "title": "OOPS day",
  "why": "The deepest part of every MathWorks tech round. Piyush: 'very thorough on OOPS, specially abstract and interface'.",
  "blocks": [
    {"time": "9:00 - 11:30 AM", "name": "Polymorphism inside out", "items": [
      item("Abstract class vs interface; pure virtual; an abstract class CAN have a constructor; a pure virtual destructor needs a body."),
      item("Draw the vtable and vptr on paper: one vtable per class, one vptr per object, the effect on sizeof, a virtual call inside a constructor."),
      item("Why there is no virtual constructor; when the destructor must be virtual."),
      item("Video #17 dynamic_cast (safe downcast, needs a polymorphic base).", False, "Video"),
    ], "quiz": "d2a", "quizName": "Output arena: virtual"},
    {"time": "12:00 - 1:30 PM", "name": "Constructors and the special members", "items": [
      item("The 6 special members, = default, = delete, Rule of 3 / 5, when the default constructor disappears."),
      item("Notepad, no IDE: a String class with constructor, copy constructor, operator= (self-assignment check, deep copy) and destructor."),
      item("Can a constructor be overridden? Can a destructor be overloaded? Why is a default constructor needed?", False),
    ], "quiz": "d2b", "quizName": "Copy or assign?"},
    {"time": "3:00 - 5:30 PM", "name": "Your list: static, friend, const, lambdas, struct", "items": [
      item("static members and functions (object counter), friend function and friend class rules."),
      item("const: const member functions, mutable, const int* vs int* const vs const int* const."),
      item("Lambdas = functors made by the compiler: [=] vs [&], mutable. Watch video #39 Functor.", True, "Video"),
      item("C struct vs C++ struct; access specifiers + the public / protected / private inheritance table.", False),
      item("namespace std: 5-minute revision of #60.", False),
    ], "quiz": "d2c", "quizName": "Trap hunt"},
  ],
  "talk": "Explain the vtable to a non-tech friend in 60 sec. Then story 1: a conflict with a teammate (Kafka project)."},

 {"id": "d3", "n": 3, "date": "Mon 23 Nov", "kind": TECH, "title": "Pointers and memory day",
  "why": "Snippet output and debugging questions are mostly pointers (Piyush, Aashima, Aryan), and Nikhil had to write a Vector in C.",
  "blocks": [
    {"time": "9:00 - 11:30 AM", "name": "Pointer output drills", "items": [
      item("*p++, ++*p, *++p, (*p)++; array vs &array; sizeof of an array inside a function."),
      item("25 pointer output questions on paper (GfG / IndiaBix). Trace each line before checking."),
      item("Videos #24 (argument evaluation order), #27 (comma operator), #66 (pre vs post increment).", False, "Video"),
    ], "quiz": "d3a", "quizName": "Output arena: pointers"},
    {"time": "12:00 - 1:30 PM", "name": "Memory, by hand", "items": [
      item("malloc / calloc / realloc / free vs new / delete: constructor calls, NULL vs bad_alloc."),
      item("Notepad: copy a 2D array from stack to heap with malloc, and free it correctly (Anubhav)."),
      item("Notepad: Vector in C with push_back, pop_back, erase using realloc (Nikhil)."),
      item("Function pointers and struct padding: quick revision.", False),
    ], "quiz": "d3b", "quizName": "Memory quiz"},
    {"time": "3:00 - 5:30 PM", "name": "Smart pointers and how things work", "items": [
      item("Notepad: your own unique_ptr (move-only) and shared_ptr (ref count, copy constructor, operator=, destructor)."),
      item("Say RAII in 30 seconds (use your notebook page)."),
      item("How printf works: va_list, va_start, va_arg, va_end, then a buffered write().", False),
      item("How int and float are stored: two's complement, IEEE 754.", False),
    ], "quiz": "d3c", "quizName": "Ownership quiz"},
  ],
  "talk": "Explain smart pointers in 30 sec. Then story 4: the rate-limiter race condition bug."},

 {"id": "d4", "n": 4, "date": "Tue 24 Nov", "kind": NONTECH, "title": "Stories day",
  "why": "Two of the three rounds are behavioural, and many peers were rejected in HR. Generic answers fail; stories pass.",
  "blocks": [
    {"time": "9:00 - 11:30 AM", "name": "Build 11 STAR stories", "items": [
      item("Write each as Situation, Task, Action (what YOU did), Result (with a number). Max 90 sec each."),
      item("1 Conflict (Kafka team) - 2 Leadership (MerchFlow, approaching clubs) - 3 Customer focus (user interviews) - 4 Hard bug (rate limiter) - 5 Last-minute change (stale stock)."),
      item("6 Deadlines + one real miss - 7 Learning fast (POSIX syscalls) - 8 Explaining tech to non-tech - 9 Setback (GATE) - 10 Critical feedback - 11 Motivating a team / stress."),
    ], "quiz": "d4a", "quizName": "Spot the weak story"},
    {"time": "12:00 - 1:30 PM", "name": "Traits and manager situations", "items": [
      item("2 strengths with proof, 2 REAL weaknesses with fixes, what friends and professors would say (good and bad)."),
      item("Manager situations: project + customer queries together; how you prioritise; an unfamiliar platform like MATLAB; explaining tech to non-tech; a non-technical teammate."),
      item("'No internship' answer (steer to projects); PPO / commitment answer.", False),
    ], "quiz": "d4b", "quizName": "What would you do?"},
    {"time": "3:00 - 5:30 PM", "name": "Mock HR interview #1", "items": [
      item("A friend plays HR for 40 min using the Question Bank tab. After EVERY answer they ask 'why?' or 'give an example'."),
      item("Record it. Mark your 3 weakest answers and rewrite them."),
      item("Rapid fire: 20 questions in 20 minutes, no pauses.", False),
    ], "game": "Score your mock out of 5, one point each: no generic answer - every answer under 2 min - steady pace - a number in every result - no long silent pauses."},
  ],
  "talk": "Say your 2 strengths and 2 weaknesses. Then story 2: leadership."},

 {"id": "d5", "n": 5, "date": "Wed 25 Nov", "kind": TECH, "title": "OS + your POSIX shell",
  "why": "One theme: OS and your shell project are the same topic. Anubhav was asked to write pipe code because POSIX was on his resume; Sanchit got dup/dup2 and fork counting.",
  "blocks": [
    {"time": "9:00 - 11:30 AM", "name": "Processes and pipes", "items": [
      item("fork / exec / wait / waitpid; zombie vs orphan; process vs thread; fork counting (GfG fork practice)."),
      item("Notepad: a pipe between two commands in C (pipe, fork twice, dup2, close unused ends, waitpid)."),
      item("dup vs dup2, the fd table, I/O redirection.", False),
    ], "quiz": "d5a", "quizName": "Fork counter"},
    {"time": "12:00 - 1:30 PM", "name": "Your shell at L3 depth", "items": [
      item("Walk through `ls | grep a > out.txt &` end to end, out loud."),
      item("Signals: why the Ctrl+C handler only sets a flag, Ctrl+Z / SIGTSTP, process groups, SIGCHLD reaping."),
      item("Prepare 2-min, 5-min and 20-min versions of the project."),
      item("Bounded deque history (why O(1)), the OOP module split.", False),
    ], "quiz": "d5b", "quizName": "Shell debugger"},
    {"time": "3:00 - 5:30 PM", "name": "Sync and memory", "items": [
      item("Mutex vs semaphore, locks, the 4 deadlock conditions + prevention, race conditions (link to your rate limiter)."),
      item("Virtual memory, paging, page faults; how a program runs (compile, link, load)."),
      item("What threads share vs what processes share.", False),
    ], "quiz": "d5c", "quizName": "OS rapid fire"},
  ],
  "talk": "POSIX shell 2-min version. Then story 7: learning something fast."},

 {"id": "d6", "n": 6, "date": "Thu 26 Nov", "kind": TECH, "title": "Projects day: MerchFlow + Kafka log",
  "why": "Managerial rounds are resume-heavy, and Nikhil said to prepare 20 minutes per project. Your 'Familiar' tech is covered here, at the depth in the Resume depth tab.",
  "blocks": [
    {"time": "9:00 - 11:30 AM", "name": "MerchFlow (checkout at L3)", "items": [
      item("Draw the HLD: 5 services, Postgres, Mongo, Redis, RabbitMQ. Walk through one order end to end."),
      item("Checkout: Redis lock (SET NX PX + unique token), idempotency keys, Saga compensation. Why each."),
      item("Why Postgres vs Mongo; transactions, isolation, the oversell race and its fix."),
      item("Cache invalidation + how you measured 40%; rate limiter race + fix; JWT / RBAC / the access-control bug.", False),
    ], "quiz": "d6a", "quizName": "Checkout under fire"},
    {"time": "12:00 - 1:30 PM", "name": "Familiar tech at the right depth", "items": [
      item("Node.js: single thread, event loop, async/await, why Node for an I/O-heavy gateway (Aryan was asked)."),
      item("RabbitMQ: ack, retry, dead-letter queue, why not Kafka for notifications."),
      item("Express middleware chain, REST verbs and idempotency, MongoDB document model.", False),
      item("Code Strategy + Observer in C++ (the warning-stack question).", False),
    ], "quiz": "d6b", "quizName": "Event-loop puzzle"},
    {"time": "3:00 - 5:30 PM", "name": "Kafka-style event log (L2)", "items": [
      item("Partitions, append-only log, offsets; leader-follower replication, commit watermark, in-sync replicas."),
      item("Raft election (terms, votes, majority), split brain + leader epochs, idempotent producer."),
      item("CAP placement; gRPC benefits and limits (Vanshika); YOUR part vs your teammate's."),
      item("LLD: design classes for the student-rank system (Kashif). SQL: join, GROUP BY, nth highest salary.", False),
    ], "quiz": "d6c", "quizName": "Distributed quiz"},
  ],
  "talk": "MerchFlow 2-min version + Kafka 2-min version. Then story 3: customer focus."},

 {"id": "d7", "n": 7, "date": "Fri 27 Nov", "kind": TECH, "title": "DSA day",
  "why": "Only problems seniors were actually asked, written fully on paper, brute force first then optimal, thinking aloud.",
  "blocks": [
    {"time": "9:00 - 11:30 AM", "name": "Linked lists and stacks", "items": [
      item("Reverse a list (iterative + recursive); LC 92; middle / fractional node; LC 141 + 142; LC 287."),
      item("LC 155 Min Stack (class-based); next greater element; a popular stack question (valid parentheses)."),
    ], "quiz": "d7a", "quizName": "Name the pattern in 10 seconds"},
    {"time": "12:00 - 1:30 PM", "name": "Arrays and classes", "items": [
      item("LC 73 Set Matrix Zeroes; kth smallest (quickselect); min / max / median of 2 sorted arrays; student ranks (getNthRank)."),
      item("Notepad: a Linked List class (constructor from an array + reverse)."),
    ], "quiz": "d7b", "quizName": "Complexity check"},
    {"time": "3:00 - 5:30 PM", "name": "Trees, heap, backtracking", "items": [
      item("LCA (LC 236 / 235); binary tree to BST without extra space; heap ops + why O(log n); LC 215."),
      item("Rat in a maze; Word Search (LC 79)."),
      item("Pick ONE favourite DS (linked list) and know everything: ops, complexity, implementation, real uses.", False),
    ], "quiz": "d7c", "quizName": "Heap + puzzle"},
  ],
  "talk": "Your favourite data structure in 2 min. Then your location answer and the 4 questions you'll ask them."},

 {"id": "d8", "n": 8, "date": "Sat 28 Nov", "kind": NONTECH, "title": "Dress rehearsal (light day)",
  "why": "No new topics. Mock all three rounds, fix gaps, use the buffer for anything an exam pushed out, sleep early.",
  "blocks": [
    {"time": "9:00 - 11:30 AM", "name": "Tech mock + buffer", "items": [
      item("60-min tech mock on notepad: 2 OOPS outputs, 1 pointer snippet, 1 class to implement, 1 DSA, 10 min of resume."),
      item("Buffer: finish any items skipped on exam days."),
    ]},
    {"time": "12:00 - 1:30 PM", "name": "Manager + HR mocks", "items": [
      item("30-min manager mock (resume deep-dive + situations) and 30-min HR mock with a friend."),
      item("Fix the 3 weakest answers."),
    ]},
    {"time": "3:00 - 5:00 PM", "name": "Cheat sheet + calm", "items": [
      item("1-page cheat sheet: Tell me about yourself, EDG, location + reasons, 2 + 2 traits, 4 questions to ask."),
      item("Your notebook's Interview Revision page in practice mode."),
      item("Laptop, charger, ID, internet (if online). Sleep by 11 PM."),
    ], "quiz": "d8c", "quizName": "Confidence round"},
  ],
  "talk": "Final 'Tell me about yourself' + EDG in 60 sec. Then stop studying."},
]

depth = [
 ["POSIX shell (C++)", "L3", "Must", "Day 5", "fork / exec / pipe / dup2 / waitpid / sigaction, pipe code in C, signals, zombies. Overlaps with OS, so it's double value."],
 ["MerchFlow", "L2, checkout at L3", "Must", "Day 6", "HLD drawing, one order end to end, Redis lock + idempotency + Saga in depth, why each database."],
 ["Kafka-style event log", "L2, your part at L3", "Must", "Day 6", "Partitions, replication + watermark, Raft, leader epochs, idempotent producer, CAP, gRPC. Know exactly what YOU built."],
 ["C++ (proficient)", "L3", "Must", "Days 2-3", "OOPS, pointers, memory, smart pointers, special members. Write code without an IDE."],
 ["SQL (proficient)", "L2", "Should", "Day 6 extra", "Write a join, GROUP BY / HAVING, nth highest salary; indexes; transactions."],
 ["JavaScript / Node.js (familiar)", "L2", "Should", "Day 6", "Single thread, event loop, promises vs setTimeout order, async/await, why Node for the gateway. Skip prototypes and V8 internals."],
 ["Express / REST (familiar)", "L1", "Should", "Day 6 extra", "Middleware chain (JWT, RBAC, rate limit), verbs, status codes, which methods are idempotent."],
 ["PostgreSQL (familiar)", "L2", "Should", "Day 6", "ACID, isolation levels, the lost-update race, SELECT ... FOR UPDATE, indexes."],
 ["MongoDB (familiar)", "L1", "Should", "Day 6 extra", "Document model and why it suits a catalog with varying attributes. Skip aggregation pipelines."],
 ["Redis (familiar)", "L2", "Must", "Day 6", "Cache-aside + invalidation, TTL, SET NX PX lock with a token, INCR for rate limiting, single-threaded."],
 ["RabbitMQ (familiar)", "L1-L2", "Should", "Day 6", "Queue, ack, redelivery, dead-letter queue, why async for notifications, vs Kafka."],
 ["Design patterns", "L2, Strategy + Observer at L3", "Must", "Day 6 extra", "Where each pattern sits in MerchFlow; code Strategy for the warning-stack question."],
 ["LLD / HLD", "L2", "Should", "Day 6", "Draw MerchFlow's HLD, the shell's class diagram, one small LLD (student ranks)."],
 ["Coursework (Agentic AI etc.)", "L1", "If time", "Day 8 buffer", "A 2-minute summary per course, only in case they ask. DSA / OS / DBMS / DS are covered by the days above."],
 ["Java, Python, Docker, Kubernetes", "Skip", "Skip", "-", "Not on your resume. If asked, say so honestly. Seniors got snippets in every language they named."],
]

from topics import T
TQ, TT = {}, {}
for key, (title, qs) in T.items():
    res = []
    for q in qs:
        if isinstance(q, tuple):
            _, k, i = q
            res.append(Q[k][i])
        else:
            res.append(q)
    TQ[key] = res; TT[key] = title
for d in days:
    for bi, b in enumerate(d["blocks"]):
        b.pop("quiz", None); b.pop("quizName", None)
        for ii, it in enumerate(b["items"]):
            k = f"{d['id']}-{bi}-{ii}"
            if k in TQ: it["quiz"] = k
missing = [k for k in TQ if not any(it.get("quiz") == k for d in days for b in d["blocks"] for it in b["items"])]
assert not missing, missing
data = {"days": days, "quiz": TQ, "titles": TT, "depth": depth}
js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

html = open(os.path.join(HERE, "template.html"), encoding="utf-8").read().replace("__DATA__", js)
open(os.path.join(HERE, "..", "index.html"), "w", encoding="utf-8").write(html)
print("ok", len(html))
