# Extra quiz content, merged into Q by build.py
def mcq(q, opts, ans, why, code=None):
    return {"t": "mcq", "q": q, "code": code, "opts": opts, "ans": ans, "why": why}
def out(q, code, ans, why):
    return {"t": "out", "q": q, "code": code, "ans": ans, "why": why}
def bug(q, code, ans, why):
    return {"t": "bug", "q": q, "code": code, "ans": ans, "why": why}
def chain(q, steps):
    return {"t": "chain", "q": q, "steps": [{"q": a, "a": b} for a, b in steps]}

X = {}

X["d1a"] = [
    mcq("Interviewer: 'Name a MathWorks product other than MATLAB.'",
        ["Mathematica", "Simulink", "LabVIEW"], 1,
        "Mathematica is Wolfram's and LabVIEW is NI's. Saying a competitor's product as theirs is an instant red flag."),
    mcq("'What do you know about MathWorks?' Best order for your answer:",
        ["Salary, location, perks", "Products, then the customers and their workflows, then how you'd grow there", "Company history year by year"], 1,
        "Aashrey's order: Product, then Customer, then Career growth. It shows you know what they build and who uses it."),
    mcq("The PPT is in the morning and your interview is after lunch. What's the best use of the PPT?",
        ["Skip it to revise DSA", "Write down the EDG points, its domains and key phrases, plus one question to ask", "Just listen"], 1,
        "Nearly every report says HR/managerial questions come straight from the PPT, and Viral was rejected after HR."),
    chain("Location follow-ups (they keep pushing):", [
        ("Why Hyderabad?", "Two professional reasons tied to the work there (from the website / PPT)."),
        ("What if we place you in Bengaluru instead?", "Stay calm and positive: you prefer Hyderabad for those reasons, but the role and learning matter most to you."),
        ("Which department in Hyderabad interests you most, and why?", "Name one from the PPT list and link it to your systems work (shell, distributed log)."),
    ]),
    chain("'Why MathWorks?' follow-ups:", [
        ("Why MathWorks?", "Engineers and scientists rely on its products; you like building tools others depend on (MerchFlow); EDG training."),
        ("Where else have you applied?", "Be honest and short. Say MathWorks is your top preference and why."),
        ("Why should we pick you over the others?", "3 points matched to the role, each with proof: C++ and systems depth (shell, Raft), you talk to users first (MerchFlow), you verify your work (58-item QA, fault-injection tests)."),
    ]),
]
X["d1b"] = [
    chain("'Tell me about yourself' follow-ups:", [
        ("Tell me about yourself.", "Your 90-second story ending at MathWorks EDG."),
        ("Why IT in B.E. and not CS?", "An honest reason, plus how you built CS depth anyway (GATE CS 97.24 percentile, systems projects)."),
        ("Why M.Tech at IIIT Hyderabad?", "Depth in systems and distributed systems; strong labs and courses; PGEE AIR 114."),
        ("What did M.Tech teach you that B.E. didn't?", "One concrete example: designing a fault-tolerant system (Raft, leader epochs) and testing it with fault injection."),
    ]),
    mcq("HR asks for your 10th marks and you don't remember the exact number.",
        ["Make up a number", "Know them before the interview; if unsure, give an honest approximate", "Say it's not important"], 1,
        "They asked Anubhav for percentages and ranks for every year. Write them on your Day 1 timeline."),
    mcq("You get an HR question you have no prepared answer for.",
        ["Start talking immediately and hope", "Take a short pause, say 'Let me think for a second', then answer in a simple structure with one example", "Say 'I don't know'"], 1,
        "A 2-second pause is fine. Piyush warned against long pauses that look like over-thinking, not short ones."),
    chain("'Why not PhD?' follow-ups:", [
        ("Why not a PhD?", "You enjoy building products people use; industry is where you want to grow now."),
        ("Your CGPA is good, your professors may want you. Still no?", "Respect for research, but your strengths and interest are in engineering products. Stay consistent."),
        ("Where do you see yourself in 5 years?", "Strong engineer at MathWorks, owning a component, mentoring juniors, understanding customers deeply."),
    ]),
    mcq("How long should 'Tell me about yourself' be?", ["15 seconds", "60-90 seconds", "5 minutes"], 1,
        "Long enough to give a story with direction; short enough that they ask follow-ups, which you've prepared."),
]

X["d2a"] = [
    out("What does this print?",
        'struct B { void f(int) { cout << "Bi"; } };\nstruct D : B { void f(double) { cout << "Dd"; } };\nint main() { D d; d.f(1); }',
        "Dd", "Name hiding: D::f hides every B::f, even with a different signature, so overloading doesn't cross scopes. Fix: `using B::f;` inside D. (Video #76.)"),
    out("What does this print? (A classic trap.)",
        'struct B { virtual void f(int x = 1) { cout << "B" << x; } };\nstruct D : B { void f(int x = 2) override { cout << "D" << x; } };\nint main() { B* p = new D; p->f(); }',
        "D1", "The function is chosen at run time (D), but default arguments are chosen at compile time from the static type (B). Never change default args in overrides."),
    out("What does this print?",
        "struct B { virtual ~B() {} };\nstruct D : B {};\nstruct E : B {};\nint main() { B* p = new E; cout << (dynamic_cast<D*>(p) == nullptr); }",
        "1", "dynamic_cast checks the real type at run time and returns nullptr for a wrong pointer cast (a reference cast throws bad_cast). It needs at least one virtual function in the base."),
    out("A class has TWO virtual functions. sizeof on 64-bit?",
        "struct V { virtual void f() {} virtual void g() {} };\ncout << sizeof(V);",
        "8", "Still one vptr per object. More virtual functions only make the class's vtable longer."),
    out("Virtual inheritance: what does this print?",
        'struct A { A() { cout << "A"; } };\nstruct B : virtual A { B() { cout << "B"; } };\nstruct C : virtual A { C() { cout << "C"; } };\nstruct D : B, C { D() { cout << "D"; } };\nint main() { D d; }',
        "ABCD", "One shared A. Without `virtual` it prints ABACD: two copies of A, and calling an A member through D becomes ambiguous. That's the diamond problem."),
    mcq("`class Shape { public: virtual double area() = 0; };` then `Shape s;`", ["Compiles", "Compile error: can't create an abstract class", "Runtime error"], 1,
        "You can still have Shape* and Shape& pointing to derived objects. That's the point of an interface."),
    chain("vtable follow-ups (Nikhil, Sneha were asked):", [
        ("How does a virtual function call actually work?", "Object's vptr, then the class vtable, then the function pointer at a fixed slot, then call it."),
        ("When is the vptr set?", "In each constructor: the base constructor sets it to the base vtable, then the derived constructor overwrites it. That's why a virtual call inside a constructor doesn't reach the derived class."),
        ("What's the cost of virtual functions?", "One vptr per object, one extra indirection per call, and usually no inlining."),
    ]),
]
X["d2b"] = [
    out("Order of construction and destruction:",
        'struct M { M() { cout << "M"; } ~M() { cout << "m"; } };\nstruct B { B() { cout << "B"; } ~B() { cout << "b"; } };\nstruct D : B { M m; D() { cout << "D"; } ~D() { cout << "d"; } };\nint main() { D d; }',
        "BMDdmb", "Base first, then members in declaration order, then the constructor body. Destruction is the exact reverse."),
    mcq("What's wrong here?", ["Nothing", "a is initialised FIRST (declaration order), from b which is still garbage", "Compile error"], 1,
        "Members are initialised in the order they are declared, not the order in the initializer list. Compilers warn (-Wreorder).",
        code="struct S {\n  int a; int b;\n  S(int x) : b(x), a(b + 1) {}\n};"),
    bug("Find the bug in this copy assignment:",
        "String& operator=(const String& o) {\n  delete[] data;\n  data = new char[strlen(o.data) + 1];\n  strcpy(data, o.data);\n  return *this;\n}",
        "Self-assignment: `s = s;` deletes its own data first, then copies from freed memory.",
        "Add `if (this == &o) return *this;` or use copy-and-swap. Also, if new throws, the object is left with a dangling pointer, which copy-and-swap fixes too."),
    mcq("Why must a copy constructor take its argument by reference?", ["Speed only", "Passing by value would itself call the copy constructor, which recurses forever, so the compiler rejects it", "Style rule"], 1,
        "Video #58. Take it as `const T&` so temporaries can bind too."),
    mcq("`explicit Meters(int m);` then `Meters d = 5;`", ["Compiles", "Compile error: explicit blocks implicit conversion", "d is 0"], 1,
        "`Meters d(5);` still works. explicit stops surprising conversions."),
    mcq("When does the move constructor run?", ["`T b = a;` with a still used later", "`v.push_back(std::move(s));` or returning a local by value", "Never automatically"], 1,
        "std::move only casts to an rvalue; the move constructor steals the resources. Returned locals are often moved, or elided entirely (RVO)."),
    chain("Rule of 3 / 5 / 0 follow-ups (Digvijay):", [
        ("What is the Rule of Three?", "If you need a custom destructor, copy constructor or copy assignment, you need all three: the class owns a resource."),
        ("What does the Rule of Five add?", "Move constructor and move assignment, so owning classes can transfer resources cheaply."),
        ("What is the Rule of Zero?", "Let members manage resources (vector, string, unique_ptr) so you write none of the five."),
    ]),
]
X["d2c"] = [
    out("What does this print?",
        "int f() { static int c = 0; return ++c; }\nint main() { cout << f() << f() << f(); }",
        "123", "A static local is initialised once and lives for the whole program."),
    mcq("A static member function CANNOT:", ["Be called without an object", "Access non-static members directly (it has no `this`)", "Access static members"], 1,
        "Call it as ClassName::f(). It's like a free function inside the class's scope."),
    mcq("A const member function calls a non-const member function. Result?", ["Works", "Compile error: `this` is const inside a const function", "Undefined behaviour"], 1,
        "const-correctness spreads: const functions may call only const functions (unless the member is mutable)."),
    mcq("A good use of `mutable`:", ["Make everything changeable", "A cache or hit counter updated inside a const getter", "Thread safety"], 1,
        "The object stays logically const while an internal detail changes."),
    out("What does this print?",
        "int x = 1;\nauto f = [&] { return x * 10; };\nx = 5;\ncout << f();",
        "50", "[&] reads x when the lambda RUNS, not when it was made. With [=] it would print 10."),
    out("What does this print?",
        "struct Add {\n  int n;\n  int operator()(int x) const { return x + n; }\n};\nint main() { Add a{3}; cout << a(4); }",
        "7", "A functor is an object with operator(). A lambda [n](int x){ return x + n; } compiles into exactly this class."),
    mcq("struct vs class in C++:", ["struct can't have functions", "Only the default access differs: struct is public (members and inheritance), class is private", "struct can't inherit"], 1,
        "In C, a struct can't have member functions or access specifiers; in C++ it can."),
    mcq("`class D : protected B` - B's public members become in D:", ["public", "protected", "private"], 1,
        "Public inheritance keeps them public; protected makes them protected; private makes them private. Private members of B are never accessible in D."),
    chain("friend follow-ups:", [
        ("Doesn't friend break encapsulation?", "It widens access in a controlled way: the class itself decides who its friends are."),
        ("When is friend actually justified?", "Overloading operator<< for your class: it must be a non-member, but needs the private data."),
        ("Is friendship inherited or mutual?", "Neither."),
    ]),
]

X["d3a"] = [
    out("What does this print?", "int a[] = {1, 2, 3, 4};\nint* p = a + 1;\ncout << p[1] << *(p - 1) << 1[a];", "312",
        "p[1] is *(p+1) = 3. 1[a] is *(1+a) = 2, because indexing is just pointer addition, so it's commutative."),
    out("What does this print?", "int x = 10;\nint* p = &x;\nint** pp = &p;\n**pp = 20;\ncout << x;", "20", "pp points to p, which points to x."),
    out("What does this print?", 'const char* s = "hello";\ncout << *(s + 1) << s + 3;', "elo",
        "*(s+1) is the char 'e'. s+3 is a char pointer, so cout prints the string from there: \"lo\"."),
    out("What does this print?", "int a[3][2] = {1, 2, 3, 4, 5, 6};\ncout << *(*(a + 1) + 1) << \" \" << sizeof(a[0]);", "4 8",
        "a+1 is row 1 {3,4}; +1 moves to 4. a[0] is a whole row of 2 ints = 8 bytes."),
    out("C++17. What does this print?", "int a = 5, *p = &a;\ncout << (*p)++ << a;", "56",
        "(*p)++ returns the old value 5, then a becomes 6. C++17 evaluates << left to right."),
    out("What does this print?", "int x = (1, 2, 3);\ncout << x;", "3", "The comma operator evaluates left to right and gives the last value. (Video #27.)"),
    out("What does this print?", "int a[5];\ncout << (&a[4] - &a[1]);", "3", "Pointer subtraction counts ELEMENTS, not bytes (the type is ptrdiff_t)."),
    mcq("Is `i = i++ + ++i;` well-defined?", ["Yes, it's 12 for i = 5", "No: undefined behaviour (i modified twice without sequencing)", "Compile error"], 1,
        "Say 'undefined behaviour' with confidence. Guessing a number is the wrong answer here."),
]
X["d3b"] = [
    bug("Find the bug:", "int* f() {\n  int x = 10;\n  return &x;\n}", "Returns the address of a local variable: a dangling pointer once f returns.",
        "Return by value, use static, or allocate on the heap (and document who frees it)."),
    bug("Find the bug:", "int* p = malloc(10 * sizeof(int));\np = realloc(p, 20 * sizeof(int));", "If realloc fails it returns NULL, p is overwritten, and the original block leaks.",
        "Use a temp: `int* t = realloc(p, ...); if (!t) { /* handle */ } else p = t;`. You'll need this in your Vector in C."),
    bug("Find the bug:", "int* p = new int[10];\n// ...\ndelete p;", "Memory from new[] must be released with delete[]; plain delete is undefined behaviour.",
        "new pairs with delete, new[] with delete[], malloc with free. Never mix them."),
    mcq("calloc vs malloc:", ["Same thing", "calloc zero-fills and takes (count, size), checking for multiplication overflow; malloc leaves memory uninitialised", "malloc zero-fills"], 1,
        "That's also why malloc is faster (video #56)."),
    out("What does this print?", "int add(int a, int b) { return a + b; }\nint mul(int a, int b) { return a * b; }\nint (*ops[])(int, int) = {add, mul};\ncout << ops[1](3, 4) << ops[0](3, 4);", "127",
        "An array of function pointers, the idea behind dispatch tables and callbacks."),
    mcq("`int (*f)(int)` vs `int *f(int)`:", ["Same", "The first is a pointer to a function returning int; the second is a function returning int*", "Both are pointers"], 1,
        "The parentheses bind * to the name first. Read declarations from the name outward."),
    out("sizeof on typical 64-bit?", "struct T { char c; double d; char e; };\ncout << sizeof(T);", "24",
        "c (1) + 7 padding + d (8) + e (1) + 7 tail padding, so arrays of T stay aligned. Put the double first and it drops to 16."),
    chain("Vector-in-C follow-ups (Nikhil):", [
        ("What fields does your Vector struct hold?", "int* data, size_t size, size_t capacity."),
        ("How does push_back grow?", "When size == capacity, realloc to 2 x capacity (amortised O(1)), with a temp pointer for failure."),
        ("What does erase(i) cost?", "O(n): shift every element after i left by one (memmove)."),
    ]),
]
X["d3c"] = [
    out("What does this print?", "auto a = make_unique<int>(5);\nauto b = std::move(a);\ncout << (a == nullptr) << *b;", "15",
        "After the move, a is empty and b owns the int."),
    out("What does this print?", "auto a = make_shared<int>(1);\nauto b = a;\n{ auto c = a; cout << a.use_count(); }\ncout << a.use_count();", "32",
        "a, b and c share one control block. c dies at the brace, so the count drops to 2."),
    mcq("Why prefer make_shared over shared_ptr<T>(new T)?", ["Same thing", "One allocation for the object and control block together, and no leak if something throws mid-expression", "It's thread-safe"], 1,
        "Say 'one allocation' first. That is the follow-up they expect."),
    mcq("weak_ptr::lock() returns:", ["A raw pointer", "A shared_ptr: empty if the object is already gone", "A bool"], 1,
        "That's how a weak_ptr safely 'uses' an object it doesn't own."),
    mcq("Why does `printf(\"%d\", 3.5)` print garbage?", ["Rounding", "printf can't see argument types; it reads an int where a double was passed (undefined behaviour)", "Overflow"], 1,
        "Variadic args carry no type info, so the format string drives va_arg. That's the core of 'how printf works'."),
    out("What does this print?", "cout << (int)3.99 << (int)-3.99;", "3-3", "Casting to int truncates toward zero, not floor."),
    out("What does this print?", "float x = 16777217;\ncout << (x == 16777216);", "1",
        "A float has a 24-bit mantissa, so above 2^24 it can't store every integer. 16777217 rounds to 16777216."),
    out("What does this print?", "unsigned char c = 255;\nc++;\ncout << (int)c;", "0", "Unsigned overflow wraps around (well-defined). Signed overflow is undefined behaviour."),
    chain("Smart pointer follow-ups (Digvijay, Sanchit):", [
        ("Implement a shared_ptr. Where does the reference count live?", "In a separate heap control block shared by all copies, not inside the object, so any type works."),
        ("What do copy constructor, operator= and destructor do?", "Copy: share the pointer, ++count. Assign: release the old one (--count, delete at 0), then share the new one (check self-assignment). Destructor: --count, delete the object and block at 0."),
        ("Is shared_ptr thread-safe?", "The count is atomic, so copies in different threads are safe. Access to the pointed object is not."),
    ]),
]

X["d4a"] = [
    mcq("In a STAR story, which part should be the longest?", ["Situation", "Task", "Action", "Result"], 2,
        "Interviewers judge what YOU did. Keep Situation to 1-2 lines."),
    mcq("'I' or 'we' in your stories?", ["Always 'we', to be humble", "'We' for team context, 'I' for your own actions and decisions", "Always 'I'"], 1,
        "Too much 'we' hides your contribution; all 'I' sounds like you ignore the team."),
    mcq("'Tell me about a failure.' The ending that works:", ["'But it wasn't my fault.'", "What you learnt and what you now do differently, with proof", "'It worked out in the end anyway.'"], 1,
        "Anubhav was asked about a missed deadline and then 'what would you do differently?'"),
    mcq("You've never had a formal leadership title. A leadership question comes:", ["Say you haven't led", "Use initiative without a title: you started MerchFlow by talking to clubs and drove it", "Make up a role"], 1,
        "Leadership = influence plus ownership. A title isn't required."),
    chain("Conflict-story follow-ups (they dig deep):", [
        ("Tell me about a conflict with a teammate.", "Your Kafka project story in STAR."),
        ("What exactly did your teammate say, and what did you say?", "Recall specifics. Vague answers get exposed here."),
        ("What would you do differently?", "One honest improvement, e.g. agree on design criteria before arguing about solutions."),
        ("How is your relationship with them now?", "Good, and you still work together. Shows maturity."),
    ]),
]
X["d4b"] = [
    mcq("'Why should we hire you?'", ["'I'm hard-working and a quick learner.'", "3 points matched to the role, each with proof from your work", "'Because I need this job.'"], 1,
        "Don't look desperate (Sneha). Proof beats adjectives."),
    mcq("A non-technical person joins your team.", ["Do their work for them", "Give tasks that match their strengths, explain with analogies, check in often", "Ask for them to be moved"], 1,
        "Piyush was asked exactly this."),
    mcq("HR asks your salary expectation in campus hiring.", ["Name a high number", "Say you're open and go with the standard campus offer; the role and learning matter most", "Refuse to answer"], 1,
        "In campus hiring the CTC is fixed. Negotiating looks out of place."),
    chain("Customer-query follow-ups (Vanshika's managerial round):", [
        ("You must do project work AND answer customers' technical queries. How?", "Acknowledge fast, judge urgency and impact, time-box, keep your lead informed."),
        ("The customer is angry and actually wrong.", "Listen fully, acknowledge the frustration, show the evidence politely, offer a path forward."),
        ("You don't know the answer to their question.", "Don't guess: say you'll find out by a specific time, research and ask the team, then follow up as promised."),
    ]),
    chain("Weakness follow-ups (Anubhav was pushed for two):", [
        ("What's your weakness?", "Weakness #1, the step you're taking, the evidence."),
        ("Give me another one.", "Weakness #2, ready. Never 'I can't think of another'."),
        ("How do you know you're improving?", "A measurable sign, e.g. your estimates are now within a day on recent tasks."),
    ]),
]

X["d5a"] = [
    out("stdout is a pipe/file (fully buffered). How many dashes?", 'for (int i = 0; i < 2; i++) {\n  fork();\n  printf("-");\n}', "8",
        "3 processes are created (4 total), but the buffered dashes are copied into children at each fork. That gives 8, not 6."),
    out("Same loop, but `printf(\"-\\n\")` on a TERMINAL (line-buffered). How many dashes?", 'for (int i = 0; i < 2; i++) {\n  fork();\n  printf("-\\n");\n}', "6",
        "Each line is flushed right away: 2 prints in the first iteration and 4 in the second. Verified both ways; the difference is buffering."),
    out("What does this print?", 'int x = 5;\nif (fork() == 0) { x++; printf("%d\\n", x); }\nelse { wait(NULL); printf("%d\\n", x); }', "6\n5",
        "After fork, parent and child have SEPARATE copies of memory (copy-on-write). The child's x++ doesn't touch the parent's x."),
    mcq("fork() returns:", ["The child's PID to both", "0 in the child, the child's PID in the parent, -1 on failure", "1 in the child"], 1,
        "This is how your ProcessExecutor tells which branch it's in."),
    mcq("execvp vs execv:", ["Same", "The p searches PATH for the program; v means the args come as an argv array", "p means pipe"], 1,
        "Your shell uses execvp so `ls` works without /bin/ls."),
]
X["d5b"] = [
    mcq("Why must `cd` be a shell built-in?", ["Speed", "A child's chdir changes only the child's directory, so the shell itself must call chdir", "cd isn't a real program"], 1,
        "A favourite follow-up for anyone with a shell on their resume. Same logic for exit."),
    mcq("For an N-stage pipeline, how many pipes and forks?", ["N pipes, N forks", "N-1 pipes, N forks", "N forks, 1 pipe"], 1,
        "One pipe between each pair of neighbours, one child per command. The parent closes all pipe fds and waits."),
    mcq("Ctrl+Z on a running command in your shell:", ["Kills it", "The terminal sends SIGTSTP; the shell ignores it, the child's default action stops it", "Nothing"], 1,
        "Your resume line: 'the shell ignores Ctrl+Z while the child does not'."),
    mcq("Why a deque for the 20-command history?", ["Sorted order", "O(1) push at the back and O(1) eviction from the front", "Less memory than an array"], 1,
        "A circular buffer would also work. Mention it as an alternative."),
    chain("POSIX shell project follow-ups:", [
        ("Walk me through what happens when I type `ls | grep a > out.txt &`.", "Parse into 2 commands, a pipe, a redirection and a background flag; pipe(); fork twice; dup2 wiring; open out.txt and dup2 onto fd 1 for grep; execvp; parent closes fds and doesn't wait (background)."),
        ("How do you avoid zombies for background jobs?", "SIGCHLD handler sets a flag; the main loop reaps with waitpid(-1, &st, WNOHANG) in a loop."),
        ("What was the hardest bug?", "Have one real one, e.g. a hang from an unclosed pipe write end."),
    ]),
]
X["d5c"] = [
    mcq("Why is `counter++` from two threads a race?", ["It isn't", "It's read-modify-write (load, add, store), and the threads can interleave and lose updates", "The CPU is too slow"], 1,
        "Fix with a mutex or std::atomic. Your rate-limiter bug was the same pattern in Redis."),
    mcq("A pool allows 3 DB connections at once. Semaphore initial value?", ["0", "1", "3"], 2,
        "A counting semaphore: wait() takes one, signal() gives one back."),
    mcq("Typical process memory layout, low to high address:", ["Stack, heap, data, text", "Text (code), data, bss, heap (grows up), ..., stack (grows down)", "Heap, stack, text"], 1,
        "Globals in data/bss, locals on the stack, malloc/new on the heap. Your notebook's memory-layout page covers this."),
    mcq("What is thrashing?", ["The CPU overheating", "Too little RAM for the working sets, so the OS spends its time swapping pages instead of running programs", "A deadlock"], 1,
        "Fix: fewer processes or more memory."),
    mcq("What does the linker do?", ["Turns code into assembly", "Combines object files and libraries and resolves symbol references into one executable", "Loads the program into RAM"], 1,
        "The loader is the OS part that maps the executable into memory."),
    chain("Deadlock follow-ups:", [
        ("Give a real deadlock example.", "Thread 1 holds lock A and waits for B; thread 2 holds B and waits for A."),
        ("How do you prevent it?", "Global lock ordering, or try-lock with timeout and back off."),
        ("Was your rate-limiter bug a deadlock?", "No, a race condition (lost updates on a counter), fixed with an atomic operation. Know the difference."),
    ]),
]

X["d6a"] = [
    mcq("Your Saga's compensation step (restore stock) itself fails. What then?", ["Ignore it", "Retry it (it must be idempotent), and alert or queue it for manual fixing after N failures", "Roll back the payment by hand"], 1,
        "Compensations are retried until they succeed; that's why they must be idempotent."),
    mcq("'Isn't microservices overkill for a college project?'", ["Defend it no matter what", "Agree it's heavier: you chose it to learn independent scaling and failure isolation, and know a monolith would be simpler at this size", "Say everyone uses microservices"], 1,
        "An honest trade-off scores higher than a defensive answer."),
    mcq("PostgreSQL's default isolation level:", ["Serializable", "Read Committed", "Read Uncommitted"], 1,
        "That's why the lost-update race on stock exists by default."),
    mcq("The trade-off of adding an index:", ["None", "Faster reads, slower writes and more storage", "Faster writes"], 1, "Every insert or update must also update the index."),
    chain("Checkout follow-ups (MerchFlow):", [
        ("Two users buy the last item in the same millisecond. What happens?", "Only one gets the per-item Redis lock; the other waits or fails; stock is re-checked inside the lock."),
        ("What if Redis goes down?", "First say honestly what your code does today. Then the better design: fall back to the DB's atomic conditional update, or fail checkout safely. Never oversell."),
        ("Payment succeeds but the order service crashes before saving.", "The idempotency key plus the Saga log let a retry finish the order without charging twice."),
    ]),
]
X["d6b"] = [
    out("Node.js: what is the order?", "async function f() {\n  console.log(1);\n  await null;\n  console.log(2);\n}\nf();\nconsole.log(3);", "1 3 2",
        "An async function runs synchronously until the first await; the rest goes to the microtask queue."),
    mcq("A CPU-heavy loop runs inside an Express handler. What happens?", ["Only that request slows", "The whole event loop blocks: every request waits", "Node spreads it over cores"], 1,
        "Move CPU work to worker threads or another service. Node suits I/O-heavy work like your gateway."),
    mcq("Which HTTP methods are idempotent?", ["POST and PATCH", "GET, PUT and DELETE", "Only GET"], 1,
        "POST isn't, which is exactly why your checkout needed idempotency keys."),
    mcq("401 vs 403:", ["Same", "401 = not authenticated (no or bad token); 403 = authenticated but not allowed", "403 = server error"], 1,
        "Your RBAC check at the gateway returns 403."),
    mcq("You want to swap the rate-limiting algorithm at run time without touching the caller. Pattern?", ["Observer", "Strategy", "Builder"], 1,
        "Strategy swaps the algorithm. Observer notifies listeners (email + SMS on order placed). Factory creates objects; Builder assembles a complex one step by step."),
]
X["d6c"] = [
    mcq("Why are Raft election timeouts randomised?", ["Security", "So nodes rarely time out together and split the vote", "Speed"], 1, "A split vote means no majority, so another round."),
    mcq("Kafka-style log ordering guarantee:", ["Total order across the topic", "Order only within a partition", "No ordering"], 1, "Same key goes to the same partition, which keeps per-key order."),
    mcq("Benefit of consistent hashing when adding a broker:", ["None", "Only about 1/N of keys move instead of almost all", "Faster hashing"], 1, "With hash % N, changing N moves most keys."),
    mcq("A correct 'second highest salary' query:", ["SELECT MAX(salary) FROM emp", "SELECT MAX(salary) FROM emp WHERE salary < (SELECT MAX(salary) FROM emp)", "SELECT salary FROM emp LIMIT 2"], 1,
        "For nth: DENSE_RANK() OVER (ORDER BY salary DESC), or ORDER BY salary DESC LIMIT 1 OFFSET n-1 on DISTINCT salaries."),
    mcq("WHERE vs HAVING:", ["Same", "WHERE filters rows before grouping; HAVING filters groups after GROUP BY", "HAVING is faster"], 1, "COUNT(*) > 5 must go in HAVING."),
    chain("Kafka project follow-ups:", [
        ("Explain your project to a non-technical HR person.", "A shared, numbered notebook that several machines keep identical copies of, so nothing is lost if one breaks."),
        ("What was the hardest part?", "One real thing, e.g. getting leader fencing right after a paused leader came back."),
        ("What would you change?", "One honest improvement, e.g. log compaction or batching for throughput."),
    ]),
]

X["d7a"] = [
    mcq("Recursive linked-list reversal: extra space?", ["O(1)", "O(n) call stack", "O(log n)"], 1, "Iterative is O(1). Say both when asked for both approaches (Aashrey)."),
    mcq("Why use a dummy node in LeetCode 92?", ["Speed", "It handles reversing from position 1 without special-casing the head", "Required by C++"], 1, "Dummy nodes remove head edge cases."),
    mcq("After Floyd's pointers meet, how do you find the cycle's start?", ["Count the nodes", "Reset one pointer to the head; move both one step at a time; where they meet is the start", "It's the meeting point"], 1,
        "Prove it if asked: the distance from the head = the distance from the meeting point (mod the cycle length)."),
    mcq("Valid parentheses uses:", ["Queue", "Stack", "Heap"], 1, "Push openers; on a closer, the top must match."),
]
X["d7b"] = [
    mcq("Kth largest with a min-heap of size k: time?", ["O(n log n)", "O(n log k)", "O(k)"], 1, "Better than sorting when k is small; quickselect is O(n) average."),
    mcq("Word Search (LC 79) time, grid m x n, word length L:", ["O(mn)", "O(mn x 4^L)", "O(L)"], 1, "Each cell starts a DFS that branches up to 4 ways (3 after the first step)."),
    mcq("Rat in a maze: why un-mark a cell when backtracking?", ["Memory", "So other paths can still use it", "Speed"], 1, "Mark, recurse, unmark. That's the backtracking template."),
    mcq("LCA in a BST vs a general binary tree:", ["Same algorithm", "BST: walk down by comparing values, O(h); general tree: recursive search, O(n)", "BST needs extra space"], 1, "Mention both: interviewers like it."),
]
X["d7c"] = [
    mcq("Puzzle: 8 balls, one heavier, a balance scale. Minimum weighings?", ["3", "2", "1"], 1,
        "Weigh 3 vs 3. If equal, weigh the remaining 2. If not, take the heavier 3 and weigh 1 vs 1."),
    mcq("Puzzle: 25 horses, 5 tracks, no timer. Minimum races for the top 3?", ["6", "7", "10"], 1,
        "5 group races, 1 race of the winners, 1 final race of the 5 remaining candidates."),
    mcq("Puzzle: 3 switches outside a room, 3 bulbs inside, you can enter once. How?", ["Impossible", "Switch 1 on for 10 min, then off; switch 2 on; enter: lit = 2, warm = 1, cold = 3", "Guess"], 1,
        "Uses a second property (heat). Interviewers want your reasoning, not just the trick."),
    mcq("Puzzle: 2 eggs, 100 floors. Minimum drops in the worst case?", ["10", "14", "50"], 1,
        "Drop from 14, 27, 39, ... (gaps shrink by 1), since 14+13+...+1 = 105 >= 100."),
]

X["d8c"] = [
    mcq("Final check: a virtual call inside a base constructor goes to:", ["Derived", "Base", "Undefined"], 1, "The vptr still points to the base vtable during the base constructor."),
    mcq("Final check: an unclosed pipe write end causes:", ["A crash", "The reader hangs waiting for EOF", "Nothing"], 1, "Say it before they ask."),
    mcq("Final check: 'Why Hyderabad?' must contain:", ["Friends and family", "Two professional reasons", "'Anywhere is fine'"], 1, "Decided in advance, and can't change later."),
    mcq("Final check: answer shape for every HR question:", ["Short yes/no", "STAR with a real example and a number", "A 5-minute speech"], 1, "No generic answers."),
    mcq("Final check: you're stuck in the tech round. You:", ["Go silent", "Think aloud, try a smaller case, ask for a hint", "Give up"], 1, "Asking for a hint is fine (Aashima)."),
    mcq("Final check: before you write code, you:", ["Start typing immediately", "Clarify inputs, say brute force then optimal with complexity, then code", "Ask for the answer"], 1, "Aashrey and Sanchit."),
]
