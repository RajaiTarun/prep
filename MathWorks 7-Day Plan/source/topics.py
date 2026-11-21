# Per-topic quizzes. R(k, i) reuses an existing question from the old block quizzes.
def mcq(q, opts, ans, why, code=None):
    return {"t": "mcq", "q": q, "code": code, "opts": opts, "ans": ans, "why": why}
def out(q, code, ans, why):
    return {"t": "out", "q": q, "code": code, "ans": ans, "why": why}
def bug(q, code, ans, why):
    return {"t": "bug", "q": q, "code": code, "ans": ans, "why": why}
def chain(q, steps):
    return {"t": "chain", "q": q, "steps": [{"q": a, "a": b} for a, b in steps]}
def R(k, i):
    return ("ref", k, i)

T = {}  # key: "d<day>-<block>-<item>" -> (title, [questions])

# ================= DAY 1 =================
T["d1-0-0"] = ("MathWorks products", [
    R("d1a", 3), R("d1a", 4),
    mcq("Where is MathWorks headquartered?", ["Seattle, Washington", "Natick, Massachusetts", "Austin, Texas"], 1, "Natick, Massachusetts. Founded in 1984, privately held. Small facts like this show you did your homework."),
    mcq("What does the name MATLAB come from?", ["Math Laboratory", "MATrix LABoratory", "Machine Learning Lab"], 1, "Matrix laboratory: it started as an easy way to use matrix libraries. A nice one-liner for 'what do you know about us?'"),
    mcq("Simulink is mainly used for:", ["Writing web apps", "Block-diagram modelling and simulation of dynamic systems (model-based design)", "Database management"], 1, "Engineers model a system (a car's braking control, say), simulate it, and can generate embedded C code from the model."),
    mcq("Which industries are big MATLAB / Simulink users?", ["Only universities", "Automotive, aerospace, communications, finance and academia", "Only finance"], 1, "Mentioning automotive and aerospace shows you understand that the users are engineers doing critical work."),
    mcq("Polyspace (a MathWorks product) does:", ["Video editing", "Static analysis to find run-time errors in C/C++ code", "Cloud hosting"], 1, "A great link to your interest in C++ correctness. You can say it in a 'why MathWorks' answer."),
    mcq("A manager asks 'Why would C++ skills matter at MathWorks?' Best angle:", ["'C++ is popular.'", "Performance-critical engines behind high-level tools need C/C++; seniors were told C++ is the preferred interview language there.", "'I don't know.'"], 1, "Tie it to their products and to Nikhil's review (C++ preferred, Java being moved away from)."),
    mcq("You mix up a product during the interview. Best recovery:", ["Pretend you didn't", "Correct yourself quickly and move on", "Change topic"], 1, "Honesty is valued (Anubhav: 'interviewers tend to know')."),
])
T["d1-0-1"] = ("Using MathWorks' core values", [
    mcq("How should you use the core values in an interview?", ["Recite them as a list", "Weave one into a story: show the value through what you did", "Ignore them"], 1, "Aashrey: read the core values and integrate them into your stories."),
    mcq("You tell your MerchFlow user-interview story. Which value is it the clearest proof of?", ["Customer focus / listening to users", "Cost cutting", "Speed only"], 0, "Check the exact wording on their site, then name it after the story, in one line."),
    mcq("Best place to mention a value:", ["Start of every answer", "One line at the end of a story, linking what you did to the value", "Only if asked 'what are our values?'"], 1, "Show first, then name it once. Forced repetition sounds rehearsed."),
    mcq("HR asks 'Which of our values do you relate to most?'", ["'All of them.'", "Pick ONE, give a real story that shows it, and say why it matters to you", "'I haven't read them.'"], 1, "One value with proof beats a list."),
    mcq("Your rate-limiter fix (verified with 50 concurrent requests) best shows:", ["Quality and ownership of your work", "Sales skill", "Creativity only"], 0, "Pick the value from their page that's closest to quality / doing things right."),
    mcq("A value you can't connect to any real story:", ["Invent a story", "Don't force it; use the values you can prove", "Mention it anyway"], 1, "Invented stories collapse under 'tell me more'."),
])
T["d1-0-2"] = ("The EDG program", [
    R("d1a", 2), R("d1a", 5),
    mcq("'Why EDG instead of joining a team directly?' Strongest answer:", ["'It's the only option.'", "Structured training plus exposure across the product and its customers before you specialise, which suits a new grad", "'It's easier.'"], 1, "Confirm the exact training details from the PPT and use their words."),
    mcq("Seniors were asked how they'd handle BOTH project work and customers' technical queries. What does that tell you about EDG?", ["Nothing", "Customer-facing technical work is part of the role, so customer-focus stories matter", "It's a sales job"], 1, "Vanshika's managerial question. Prepare your MerchFlow user story for it."),
    mcq("You're unsure about a detail of EDG's domains in the interview.", ["Make it up confidently", "Say what you know from the PPT and that you'd like to learn more, then ask a question", "Say you didn't attend"], 1, "Never invent facts about their program."),
    chain("EDG follow-ups:", [
        ("What is EDG, in your own words?", "2-3 lines from the PPT, in your own words, plus what it means for a new engineer."),
        ("Which domain interests you most?", "One domain from the PPT list, linked to your systems / C++ work."),
        ("Why should we put you in that domain?", "Proof from your projects: the shell, the distributed log, MerchFlow's checkout."),
    ]),
    mcq("A good question to ASK about EDG:", ["'How many leaves do I get?'", "'What does an EDG engineer typically work on in the first months, and how do they move to a team?'", "'Can I skip EDG?'"], 1, "Shows interest in growth, not perks."),
])
T["d1-0-3"] = ("Location choice", [
    R("d1a", 0), R("d1a", 6), R("d8c", 2),
    mcq("Can you change your location choice after the interview?", ["Yes, any time", "No: seniors said decide carefully, you can't change it later", "Only after a year"], 1, "Nikhil's review."),
    mcq("You study at IIIT Hyderabad. Should that be your reason for Hyderabad?", ["Yes, it's the main reason", "No: keep it out (or at most a footnote); lead with professional reasons", "Only if asked"], 1, "It counts as a personal reason, which seniors said to avoid."),
    mcq("They show you departments in both offices and ask you to choose areas of interest.", ["Pick randomly", "Pick ones that connect to your resume (systems, C++, distributed) and say why", "Say 'any'"], 1, "Anubhav was shown the department list."),
    mcq("'Would you relocate if the business needs it?'", ["'No.'", "'Yes. The role and learning matter most, though I prefer X for the reasons I gave.'", "'Maybe.'"], 1, "Flexible but consistent."),
])

T["d1-1-0"] = ("Tell me about yourself", [
    R("d1b", 0), R("d1b", 4), R("d1b", 8),
    mcq("How should 'Tell me about yourself' END?", ["With your hobbies", "With why you're here: what draws you to MathWorks EDG", "With your CGPA"], 1, "End with a hook into the next question."),
    mcq("Hobbies in your intro:", ["List several", "Skip, or one line only if it shows something relevant", "Spend most of the time there"], 1, "Keep the 90 seconds for your story."),
    mcq("Same question in the manager round vs HR round:", ["Identical answer", "Same story; the manager version leans more on projects and design work", "Totally different stories"], 1, "Consistent facts, adjusted emphasis."),
    mcq("What to avoid in the intro:", ["A clear arc", "Reading out every number on your resume", "Ending at MathWorks"], 1, "Pick 2-3 numbers that matter (GATE 97.24 percentile, PGEE AIR 114)."),
    mcq("Best way to practise it:", ["Read it silently", "Record yourself twice, listen, cut what drags", "Memorise word for word"], 1, "Word-for-word memorising sounds robotic; know the beats instead."),
])
T["d1-1-1"] = ("Your timeline and decisions", [
    R("d1b", 1), R("d1b", 5), R("d1b", 6),
    chain("GATE follow-ups:", [
        ("You qualified GATE CS in 2024. Why write it again?", "Your honest reason (a better rank for the institute you wanted) and what you changed in preparation."),
        ("What exactly did you change?", "Concrete: a schedule, mock tests, revising weak subjects. Have specifics."),
        ("What did that teach you?", "One lesson that also applies to work, e.g. measuring progress, not just putting in hours."),
    ]),
    mcq("'Why IT in B.E. and not CS?'", ["'Bad luck.'", "Honest reason + how you built CS depth anyway (GATE CS, systems projects)", "Avoid it"], 1, "Every 'why' needs an honest reason plus what you did about it."),
    mcq("'How did you manage GATE prep with your B.E. final year?'", ["'I skipped classes.'", "A real routine and priority system, with one example", "'It was easy.'"], 1, "A hidden time-management question."),
    mcq("You told HR one reason for M.Tech and the manager a different one. Risk?", ["None", "Looks inconsistent; rounds compare notes", "It shows flexibility"], 1, "Write your 'why' lines once on Day 1 and stick to them."),
    mcq("Anubhav was asked about every year from class 10 with percentages and ranks. Your preparation:", ["Wing it", "A one-page timeline with exact numbers and a 'why' for each step", "Only prepare the last 2 years"], 1, "This is the Day 1, 4-6 PM task."),
])
T["d1-1-2"] = ("Motivation answers", [
    R("d1a", 1), R("d1b", 2), R("d1b", 3), R("d1b", 7), R("d1a", 7),
    mcq("'Why not go abroad?'", ["'Too expensive.'", "A positive reason to be here: the role, EDG training, growth at MathWorks", "'My family won't allow it.'"], 1, "Asked to Aashima. Avoid money or family as the only reason."),
    mcq("'Why M.Tech and not a job after B.E.?'", ["'I didn't get a job.'", "Depth in systems and distributed systems, with your shell and Raft projects as proof", "'Everyone does M.Tech.'"], 1, "Asked in many reports (Vanshika, Viral, Aashima, Sanchit)."),
    mcq("'Have you applied elsewhere?'", ["'No' (when untrue)", "Honest and short, then why MathWorks is your top choice", "List every company"], 1, "Honesty, then commitment."),
])
T["d1-1-3"] = ("Questions to ask them", [
    mcq("Best technical question for the manager:", ["'What's the salary?'", "'How does the team test MATLAB across releases and platforms?'", "'Do you work weekends?'"], 1, "Aashrey: managers like a technical discussion about MATLAB / MathWorks."),
    mcq("How many questions should you prepare?", ["0", "2-3 technical for the manager, 1 for HR", "10"], 1, "Ask 1-2 in the room, depending on time."),
    mcq("A question to avoid in the interview:", ["About the team's tech stack", "About leave policy and salary", "About EDG training"], 1, "Campus CTC is fixed. Perk questions signal the wrong priorities."),
    mcq("Piyush's tip at the end of each round:", ["Leave quickly", "Ask for feedback and ask a question that adds value", "Ask about the next round's questions"], 1, "Ask something like 'Is there anything I could have explained better?'"),
    mcq("'Do you have any questions for us?' You say 'No'.", ["Fine", "A missed chance to show curiosity", "Shows confidence"], 1, "Always have one."),
    mcq("A good question for HR:", ["'Can I change location later?'", "'What do new engineers who do well in EDG have in common?'", "'How strict is attendance?'"], 1, "Shows you want to succeed there."),
])

# ================= DAY 2 =================
T["d2-0-0"] = ("Abstract class, interface, pure virtual", [
    R("d2a", 4), R("d2a", 10),
    out("What does this print?", 'struct Shape {\n  Shape() { cout << "S"; }\n  virtual double area() = 0;\n  virtual ~Shape() {}\n};\nstruct Sq : Shape {\n  Sq() { cout << "Q"; }\n  double area() override { return 4; }\n};\nint main() { Sq s; cout << s.area(); }', "SQ4", "An abstract class CAN have a constructor; it runs when a derived object is built."),
    out("A pure virtual function WITH a definition. What prints?", 'struct B { virtual void f() = 0; };\nvoid B::f() { cout << "Bf"; }\nstruct D : B {\n  void f() override { B::f(); cout << "Df"; }\n};\nint main() { D d; d.f(); }', "BfDf", "A pure virtual function can have a body. Derived classes must still override it, and may call the base version explicitly."),
    out("Pure virtual destructor. What prints?", 'struct B { virtual ~B() = 0; };\nB::~B() { cout << "~B"; }\nstruct D : B { ~D() { cout << "~D"; } };\nint main() { B* p = new D; delete p; }', "~D~B", "A pure virtual destructor makes the class abstract but still needs a body, because ~D always calls ~B. Without the body: linker error."),
    mcq("D inherits from abstract B but does NOT override B's pure virtual function. Then:", ["D is concrete", "D is abstract too: you can't create a D", "Compile error in B"], 1, "Abstractness is inherited until every pure virtual function is overridden."),
    mcq("Can an abstract class have data members and normal member functions?", ["No", "Yes: only one pure virtual function is needed to make it abstract", "Only static ones"], 1, "That's the difference from an 'interface', which has only pure virtual functions."),
    mcq("Piyush: 'be very thorough on abstract and interface'. The one-line difference:", ["Same thing", "An interface has only pure virtual functions (+ a virtual destructor) and no state; an abstract class can mix state, implemented functions and pure virtuals", "An interface can be instantiated"], 1, "C++ has no interface keyword. Java does; say so if they ask about Java."),
])
T["d2-0-1"] = ("vtable, vptr and dynamic dispatch", [
    R("d2a", 0), R("d2a", 1), R("d2a", 8), R("d2a", 2), R("d2a", 11),
    out("What does this print?", 'struct B {\n  void f() { cout << "B"; }\n  virtual void g() { cout << "Bg"; }\n};\nstruct D : B {\n  void f() { cout << "D"; }\n  void g() override { cout << "Dg"; }\n};\nint main() { B* p = new D; p->f(); p->g(); }', "BDg", "Only virtual calls go through the vtable. f is non-virtual, so the pointer's static type (B) decides."),
    mcq("3 classes in a hierarchy, each with virtual functions. How many vtables?", ["1", "3 (one per class)", "One per object"], 1, "One vtable per class; one vptr per object."),
    mcq("Can a static member function be virtual?", ["Yes", "No: it has no `this`, so there's no object (or vptr) to dispatch on", "Only in abstract classes"], 1, "Virtual dispatch needs an object."),
    mcq("Where does the vptr usually live?", ["In the vtable", "Inside each object (typically at the start)", "In a global table"], 1, "That's why sizeof grows by 8 bytes on 64-bit."),
])
T["d2-0-2"] = ("Virtual constructor and destructor", [
    R("d2a", 3), R("d2a", 6), R("d2a", 5),
    mcq("Why can't a constructor be virtual?", ["Syntax limit only", "Virtual dispatch needs a vptr, which doesn't exist until construction, and you must know the exact type to construct", "It slows things down"], 1, "Sanchit had an output question on this."),
    mcq("How do you 'virtually construct' a copy of an object through a base pointer?", ["You can't", "A virtual clone() function that each class overrides to return new Derived(*this)", "Use memcpy"], 1, "The 'virtual constructor' idiom, also a Factory-like pattern."),
    mcq("When must a destructor be virtual?", ["Always", "When a derived object may be deleted through a base pointer (rule of thumb: the class has any virtual function)", "Never"], 1, "Otherwise only ~Base runs: undefined behaviour and leaks."),
    out("Virtual call inside destructors. What prints?", 'struct B {\n  virtual void f() { cout << "B"; }\n  virtual ~B() { f(); }\n};\nstruct D : B {\n  void f() override { cout << "D"; }\n  ~D() { f(); }\n};\nint main() { B* p = new D; delete p; }', "DB", "~D runs first (calls D::f). By the time ~B runs, the D part is gone, so f resolves to B::f."),
    mcq("A destructor throws during stack unwinding. What happens?", ["Exception is ignored", "std::terminate: the program aborts", "The other exception is replaced"], 1, "Destructors are noexcept by default. Never throw from them."),
    mcq("Base destructor is virtual. Is the derived destructor automatically virtual?", ["No", "Yes, even without the keyword", "Only with override"], 1, "Virtual-ness is inherited for destructors too."),
])
T["d2-0-3"] = ("dynamic_cast and the other casts", [
    R("d2a", 7),
    out("What does this print?", "struct B { virtual ~B() {} };\nstruct D : B { int x = 7; };\nint main() {\n  B* p = new D;\n  if (D* d = dynamic_cast<D*>(p)) cout << d->x;\n}", "7", "The real object is a D, so the downcast succeeds."),
    mcq("dynamic_cast to a REFERENCE fails. What happens?", ["Returns nullptr", "Throws std::bad_cast", "Undefined behaviour"], 1, "References can't be null, so it throws."),
    mcq("dynamic_cast on a class with NO virtual functions:", ["Works", "Compile error: the base must be polymorphic", "Returns nullptr"], 1, "It needs run-time type info, which comes with the vtable."),
    mcq("static_cast downcast to the WRONG type:", ["Returns nullptr", "Compiles, no check: undefined behaviour when used", "Throws"], 1, "static_cast trusts you. Use dynamic_cast when you're not sure."),
    mcq("const_cast is for:", ["Converting int to double", "Adding or removing const (modifying a really-const object is still undefined behaviour)", "Downcasting"], 1, "Typical legit use: calling an old C API that takes char* but doesn't modify it."),
    mcq("reinterpret_cast is for:", ["Safe downcasts", "Low-level reinterpretation of bits, e.g. a pointer to an integer address", "Removing const"], 1, "Least safe cast. Know that it exists and why it's rare."),
    mcq("Your code uses many dynamic_casts to choose behaviour. What would an interviewer say?", ["Great design", "A design smell: prefer virtual functions so each class carries its own behaviour", "It's fastest"], 1, "Polymorphism beats type-switching."),
])

T["d2-1-0"] = ("Special members, Rule of 3 / 5", [
    R("d2b", 0), R("d2b", 1), R("d2b", 3), R("d2b", 9), R("d2b", 10),
    mcq("The 6 special member functions:", ["Constructor, destructor, getter, setter, operator==, print", "Default constructor, destructor, copy constructor, copy assignment, move constructor, move assignment", "Only constructor and destructor"], 1, "Digvijay was asked which functions the compiler makes by default."),
    mcq("You declare a copy constructor yourself. Is a move constructor generated?", ["Yes", "No: moves then fall back to copies", "Only in C++20"], 1, "Declaring any of copy / move / destructor suppresses the implicit move operations."),
    out("What does this print?", 'struct T {\n  T() { cout << "d"; }\n  T(const T&) { cout << "c"; }\n  T(T&&) { cout << "m"; }\n};\nint main() { T a; T b = std::move(a); T c = b; }', "dmc", "std::move(a) makes an rvalue, so the move constructor runs. b is an lvalue, so c is copied."),
])
T["d2-1-1"] = ("Write a String class (no IDE)", [
    R("d2b", 6), R("d2b", 7),
    bug("Find the bug:", "String(const char* s) {\n  data = new char[strlen(s)];\n  strcpy(data, s);\n}", "Off by one: no room for the '\\0' terminator, so strcpy writes past the end.", "Allocate strlen(s) + 1."),
    bug("Find the bug:", "~String() { delete data; }", "data came from new[], so it must be delete[] data.", "Mismatched new[] / delete is undefined behaviour."),
    mcq("Why does operator= return String&?", ["Required syntax", "To allow chaining like a = b = c (and avoid an extra copy)", "Speed only"], 1, "Video #40."),
    mcq("Copy-and-swap's main benefit:", ["Fewer lines only", "Strong exception safety and automatic self-assignment handling", "No destructor needed"], 1, "Take the parameter by value (the copy), swap with *this, and let the old data die with the parameter."),
    out("Deep copy check. What prints?", "struct S {\n  int* p;\n  S(int v) : p(new int(v)) {}\n  S(const S& o) : p(new int(*o.p)) {}\n  ~S() { delete p; }\n};\nint main() { S a(1); S b = a; *b.p = 9; cout << *a.p << *b.p; }", "19", "The copy constructor allocates new memory, so changing b doesn't touch a."),
    chain("'Write a String class' follow-ups:", [
        ("What members does it need?", "char* data (and size_t len); constructor from const char*, destructor."),
        ("Write the copy constructor.", "Allocate len + 1, copy the characters: a deep copy."),
        ("Write operator=.", "Self-assignment check, allocate the new buffer first, copy, delete the old one, return *this."),
        ("Add a move constructor.", "Steal other.data, set other.data = nullptr so its destructor is safe."),
    ]),
])
T["d2-1-2"] = ("Constructor and destructor rules", [
    R("d2b", 2), R("d2b", 4), R("d2b", 5), R("d2b", 8),
    mcq("Can a constructor be overridden?", ["Yes", "No: constructors aren't inherited or virtual, so they can't be overridden (only overloaded)", "Only in abstract classes"], 1, "Sneha was asked this."),
    mcq("Can a destructor be overloaded?", ["Yes", "No: exactly one destructor, no parameters", "Only with templates"], 1, "Also asked to Sneha."),
    mcq("Can a constructor be private?", ["No", "Yes: e.g. a Singleton or a factory function controls creation", "Only in structs"], 1, "Classic follow-up after 'can constructors be overridden?'"),
    mcq("Where is a member initializer list REQUIRED?", ["Never", "For const members, reference members, members with no default constructor, and base classes needing arguments", "Only for pointers"], 1, "Video #22."),
    mcq("`Point() : Point(0, 0) {}` is:", ["Recursion", "Constructor delegation (C++11)", "A compile error"], 1, "Video #29."),
])

T["d2-2-0"] = ("static and friend", [
    R("d2c", 0), R("d2c", 5), R("d2c", 6), R("d2c", 3), R("d2c", 13),
    out("sizeof with a static member (int is 4 bytes):", "struct A { static int n; int x; };\nint A::n;\nint main() { cout << sizeof(A); }", "4", "Static data members live outside objects, so they don't add to sizeof (video #81)."),
    mcq("You declare `static int n;` in a class but never define it. Using it gives:", ["0", "A linker error (undefined reference)", "A compile error in the header"], 1, "Define it in one .cpp: `int A::n = 0;` (or `inline static` in C++17). Video #57."),
    mcq("Classic legit use of a friend function:", ["Speed", "Overloading operator<< for your class", "Replacing inheritance"], 1, "operator<< must be a non-member (the left side is ostream) but needs your private data."),
    mcq("Is initialisation of a function-local static thread-safe in C++11?", ["No", "Yes: the compiler guarantees one-time initialisation", "Only with a mutex"], 1, "That's why the 'Meyers singleton' is safe."),
    mcq("A static member function accessing a non-static member through an object passed in:", ["Not allowed", "Allowed: `obj.x` is fine; only the implicit `this` is missing", "Undefined behaviour"], 1, "It's like a free function with private access."),
])
T["d2-2-1"] = ("const and mutable", [
    R("d2c", 2), R("d2c", 7), R("d2c", 8),
    mcq("`const int* const p;`", ["Both pointer and value can change", "Neither the pointer nor the value can change", "Only the value can change"], 1, "Read right to left: const pointer to const int."),
    mcq("A const object can call:", ["Any member function", "Only const member functions", "No member functions"], 1, "const objects need const functions (or mutable members)."),
    mcq("Why can `void f(const string& s)` accept f(\"hi\") but `void g(string& s)` can't?", ["It's a bug", "A temporary can bind to a const reference but not to a non-const one", "Only literals are special"], 1, "That's why parameters are usually const T&."),
    out("Overloading on const. What prints?", "struct C {\n  int f() { return 1; }\n  int f() const { return 2; }\n};\nint main() { C a; const C b; cout << a.f() << b.f(); }", "12", "The object's const-ness chooses the overload."),
    mcq("Nikhil was asked about 'immutability'. In C++, an immutable class is one where:", ["All members are public", "All members are set in the constructor and never change (const members / no setters)", "It uses mutable"], 1, "Mention: thread-safe to share and easy to reason about."),
])
T["d2-2-2"] = ("Lambdas and functors", [
    R("d2c", 1), R("d2c", 4), R("d2c", 9), R("d2c", 10),
    out("What does this print?", "int x = 1;\nauto f = [=] { return x * 10; };\nx = 5;\ncout << f();", "10", "[=] copies x when the lambda is CREATED. Compare with [&], which gives 50."),
    out("What does this print?", "vector<int> v = {5, 1, 4};\nsort(v.begin(), v.end(), [](int a, int b) { return a > b; });\ncout << v[0] << v[2];", "51", "A lambda as a comparator: descending order, so 5 4 1."),
    mcq("A lambda with NO captures can convert to:", ["Nothing", "A plain function pointer", "A std::string"], 1, "Captures become members, so only capture-less lambdas fit in a function pointer."),
    mcq("`[this]` captures:", ["A copy of the object", "The object's pointer, so members are used by reference (careful with lifetime)", "Nothing"], 1, "Dangerous if the lambda outlives the object."),
    mcq("`[](auto x) { return x * 2; }` is:", ["Invalid", "A generic lambda: its operator() is a template", "Only for ints"], 1, "C++14 feature."),
])
T["d2-2-3"] = ("struct, access specifiers and inheritance modes", [
    R("d2c", 11), R("d2c", 12), R("d2a", 9),
    mcq("`class D : B {};` with no keyword. The inheritance is:", ["public", "private (class default)", "protected"], 1, "With `struct D : B` the default is public."),
    mcq("A protected member is accessible from:", ["Anywhere", "The class itself and its derived classes, not from outside", "Only the class itself"], 1, "Sneha was asked private vs public vs protected."),
    mcq("Private inheritance models:", ["is-a", "implemented-in-terms-of (usually composition is better)", "has-many"], 1, "Public inheritance = is-a."),
    out("What does this print?", "struct P { int x; };\nint main() {\n  P p{3};\n  P* q = &p;\n  cout << p.x << q->x << (*q).x;\n}", "333", "-> is shorthand for (*q).; use . on objects and -> on pointers."),
    mcq("C struct vs C++ struct:", ["Identical", "A C++ struct can have member functions, access specifiers, constructors and inheritance; a C struct holds data only", "C structs can inherit"], 1, "In C you also need the `struct` keyword in declarations (unless typedef'd)."),
])
T["d2-2-4"] = ("namespace std and scope", [
    mcq("Why is `using namespace std;` bad in a header?", ["It's slower", "Every file including the header gets all of std dumped in: name clashes", "It doesn't compile"], 1, "Video #60."),
    mcq("`using namespace std; int count = 0;` then using `count` in a function:", ["Always fine", "Can become ambiguous with std::count", "Compile error always"], 1, "A real-world clash example to quote."),
    mcq("Better alternatives:", ["None", "`std::` prefix, or `using std::cout;` for specific names", "#define"], 1, "Fine in a .cpp or a small scope; never in headers."),
    out("What does this print?", "int x = 1;\nnamespace N { int x = 2; }\nint main() {\n  int x = 3;\n  cout << x << ::x << N::x;\n}", "312", "Local x, then ::x for the global one, then N::x."),
    mcq("An anonymous namespace `namespace { int helper; }` gives:", ["Global visibility", "Internal linkage: visible only in that .cpp file", "A compile error"], 1, "The modern replacement for `static` at file scope."),
    mcq("Why does `cout << s` work for a std::string without writing std:: for operator<<?", ["Magic", "Argument-dependent lookup (ADL): functions are also searched in the arguments' namespaces", "It's a keyword"], 1, "Bonus depth if they push."),
])

# ================= DAY 3 =================
T["d3-0-0"] = ("Pointer precedence", [
    R("d3a", 0), R("d3a", 8), R("d3a", 11),
    out("What does this print?", "int a[] = {10, 20, 30};\nint* p = a;\ncout << *++p << \" \" << *p;", "20 20", "*++p moves p first, then reads."),
    out("What does this print?", "int a[] = {10, 20, 30};\nint* p = a;\nint x = ++*p;\ncout << x << a[0];", "1111", "++*p increments the value a[0] to 11."),
    out("What does this print?", "int a[] = {1, 2, 3};\nint* p = a;\n*p++ = 9;\ncout << a[0] << *p;", "92", "Writes 9 to a[0], then p moves to a[1]."),
    mcq("`*p++` parses as:", ["(*p)++", "*(p++)", "++(*p)"], 1, "Postfix ++ binds tighter than unary *."),
    mcq("`int* p, q;` declares:", ["Two pointers", "p is a pointer; q is a plain int", "Compile error"], 1, "The * belongs to the name. A classic output-question trap."),
])
T["d3-0-1"] = ("Pointer output practice", [
    R("d3a", 1), R("d3a", 2), R("d3a", 3), R("d3a", 4), R("d3a", 5), R("d3a", 6), R("d3a", 7), R("d3a", 10),
    mcq("`char* s = \"abc\"; s[0] = 'x';`", ["Prints xbc", "Undefined behaviour: string literals are read-only (usually a crash)", "Compile error in C"], 1, "Use `char s[] = \"abc\";` to get a modifiable copy."),
])
T["d3-0-2"] = ("Evaluation order, comma, pre/post increment", [
    R("d3a", 9),
    out("What does this print?", "int i = 5;\nint j = (i++, i++, i);\ncout << j << i;", "77", "The comma operator sequences left to right: i becomes 6, then 7, then j = 7."),
    out("C++17. What does this print?", "int i = 1;\ncout << (i++ + 10) << i;", "112", "i++ yields 1, so 11. In C++17, << evaluates left to right, so i is 2 next."),
    out("What does this print?", "int x;\nx = 1, 2;\ncout << x;", "1", "The = operator binds tighter than the comma: (x = 1), 2."),
    mcq("In `f(i++, i++)`, which argument is evaluated first?", ["Left", "Unspecified (and before C++17 even undefined for this)", "Right"], 1, "Video #24. Never depend on argument order."),
    mcq("Why prefer ++it over it++ for iterators?", ["No difference", "it++ must copy the old value to return it; ++it doesn't", "++it is safer"], 1, "Video #66: for ints the compiler optimises it; for class types it matters."),
    mcq("`printf(\"%d %d\", i, i++);` in C:", ["Prints i then i", "Undefined behaviour: i read and modified without sequencing", "Always prints 5 5"], 1, "Say 'undefined behaviour', don't guess numbers."),
    mcq("A legit everyday use of the comma operator:", ["Never", "for (i = 0, j = n - 1; i < j; i++, j--)", "Returning two values"], 1, "Two-pointer loops."),
])

T["d3-1-0"] = ("malloc / new and friends", [
    R("d3b", 1), R("d3b", 7), R("d3b", 6),
    mcq("How do you make new return nullptr instead of throwing?", ["You can't", "`new (std::nothrow) T`", "Wrap in if"], 1, "Default new throws std::bad_alloc."),
    mcq("realloc() on memory from new:", ["Fine", "Undefined behaviour: realloc only for malloc / calloc memory", "Works for arrays"], 1, "Never mix allocators."),
    mcq("free(NULL):", ["Crash", "Safe: does nothing", "Undefined behaviour"], 1, "Same for delete nullptr."),
    mcq("Does free() call the object's destructor?", ["Yes", "No: only delete calls destructors", "Only for structs"], 1, "Another reason not to malloc C++ objects."),
    mcq("Placement new `new (buf) T()` does:", ["Allocates twice", "Constructs a T in memory you already have (no allocation)", "Deletes buf"], 1, "Video #52. std::vector uses it internally."),
    mcq("malloc vs calloc speed:", ["calloc faster", "malloc faster: calloc also zeroes the memory", "Same"], 1, "Video #56."),
])
T["d3-1-1"] = ("2D array from stack to heap (Anubhav)", [
    chain("Write it: copy a 2D array from stack to heap.", [
        ("Allocate the heap structure.", "int** m = malloc(R * sizeof(int*)); then for each row m[i] = malloc(C * sizeof(int)); check each for NULL."),
        ("Copy the data.", "for each row: memcpy(m[i], a[i], C * sizeof(int)); (or a nested loop)."),
        ("Free it correctly.", "free(m[i]) for every row first, then free(m)."),
    ]),
    bug("Find the bug:", "int** m = malloc(r * sizeof(int));", "Should be sizeof(int*): on 64-bit a pointer is 8 bytes, an int is 4, so the row-pointer array is too small.", "Idiom: `malloc(r * sizeof *m)` always gets it right."),
    mcq("A contiguous alternative to int**:", ["Not possible", "`int (*p)[C] = malloc(R * sizeof *p);` one block, indexed p[i][j]", "Use a struct"], 1, "One malloc, one free, cache-friendly."),
    mcq("Freeing int** rows in the wrong order (free(m) first):", ["Fine", "You lose the row pointers, so the rows leak (or you read freed memory)", "Faster"], 1, "Free inside-out."),
    out("sizeof check (int = 4 bytes):", "int a[2][3];\ncout << sizeof(a) << \" \" << sizeof(a[0]) << \" \" << sizeof(a[0][0]);", "24 12 4", "Whole array, one row, one element."),
    out("Row-major layout. What prints?", "int a[2][3] = {{1, 2, 3}, {4, 5, 6}};\nint* p = &a[0][0];\ncout << p[4];", "5", "Rows are stored one after another: 1 2 3 4 5 6."),
    mcq("Passing a stack 2D array to a function needs:", ["Nothing", "The column size in the parameter: void f(int a[][3], int rows)", "A pointer to pointer"], 1, "int a[2][3] does NOT convert to int**."),
    mcq("memcpy vs memmove for copying separate arrays:", ["memmove only", "memcpy is fine (no overlap); memmove is for overlapping regions", "Neither"], 1, "You'll need memmove in Vector erase."),
])
T["d3-1-2"] = ("Vector in C (Nikhil)", [
    R("d3b", 3), R("d3b", 5), R("d3b", 11),
    mcq("pop_back on an empty vector:", ["Returns garbage", "Check size first and report an error (return code or assert)", "Shrinks capacity"], 1, "Edge cases are what they watch for."),
    mcq("Should capacity ever shrink?", ["Never", "Optionally when size drops to a quarter of capacity (halve then), to avoid thrashing", "After every pop"], 1, "Shrinking at half causes grow/shrink ping-pong."),
    mcq("erase(i) should shift elements with:", ["memcpy", "memmove (source and destination overlap)", "strcpy"], 1, "memcpy with overlap is undefined behaviour."),
    mcq("In C++ std::vector, which operation can invalidate ALL iterators?", ["Reading", "push_back that triggers a reallocation", "size()"], 1, "Natural follow-up after your C version."),
    mcq("Time of push_back, pop_back, erase(i), get(i) in your Vector:", ["All O(1)", "Amortised O(1), O(1), O(n), O(1)", "All O(n)"], 1, "Say these without thinking."),
])
T["d3-1-3"] = ("Function pointers and struct padding", [
    R("d3b", 8), R("d3b", 9), R("d3b", 0), R("d3b", 10),
    out("What does this print?", "int apply(int (*f)(int), int x) { return f(x); }\nint sq(int x) { return x * x; }\nint main() { cout << apply(sq, 5); }", "25", "Passing a function as a callback. Piyush got debugging questions on function pointers."),
    mcq("Why does padding exist?", ["Compiler bug", "So members sit at aligned addresses, which the CPU reads faster (or requires)", "Security"], 1, "Videos #1 and #77."),
    mcq("`#pragma pack(1)` does:", ["Nothing", "Removes padding: smaller struct, but possibly slower unaligned access", "Adds padding"], 1, "Used for file formats and network packets."),
    mcq("qsort's comparator has type:", ["int(int, int)", "int (*)(const void*, const void*)", "bool(int, int)"], 1, "Function pointers plus void pointers together."),
])

T["d3-2-0"] = ("Smart pointers (write your own)", [
    R("d3c", 0), R("d3c", 1), R("d3c", 3), R("d3c", 4), R("d3c", 7), R("d3c", 8), R("d3c", 13),
    mcq("sizeof(unique_ptr<int>) with the default deleter:", ["16", "Same as a raw pointer (8 on 64-bit)", "24"], 1, "Zero-overhead, which is why it's the default choice."),
    mcq("Returning a unique_ptr from a function by value:", ["Compile error (no copy)", "Fine: the return value is moved automatically", "Undefined behaviour"], 1, "Factories return unique_ptr."),
    mcq("Two shared_ptrs created separately from the SAME raw pointer:", ["Share one count", "Two control blocks: double delete", "Fine"], 1, "Create the first one from new (or make_shared), then copy it."),
])
T["d3-2-1"] = ("RAII", [
    mcq("RAII in one line:", ["A garbage collector", "Tie a resource's lifetime to an object: acquire in the constructor, release in the destructor", "A design pattern for threads"], 1, "Your notebook has the full page."),
    out("What does this print?", 'struct R {\n  R() { cout << "open "; }\n  ~R() { cout << "close "; }\n};\nvoid f() { R r; throw 1; }\nint main() {\n  try { f(); } catch (int) { cout << "caught"; }\n}', "open close caught", "Destructors run during stack unwinding, before the catch. That's why RAII is exception-safe."),
    mcq("Why is RAII safer than manual delete?", ["It isn't", "Early returns and exceptions can skip a manual delete; a destructor always runs", "It's faster"], 1, "The core argument."),
    mcq("Which is an RAII type?", ["int*", "std::lock_guard (unlocks the mutex in its destructor)", "malloc"], 1, "Also: std::fstream, std::vector, unique_ptr."),
    mcq("RAII vs garbage collection:", ["Same", "RAII releases deterministically at scope end and works for any resource (files, locks), not just memory", "GC is always better"], 1, "Why C++ needs no GC."),
    mcq("Should a destructor throw?", ["Yes", "No: if it throws during unwinding, std::terminate runs", "Only for files"], 1, "Ties to Day 2."),
    mcq("What does RAII stand for?", ["Run-time Allocation Is Immediate", "Resource Acquisition Is Initialization", "Reference And Instance Isolation"], 1, "A confusing name; 'scope-bound resource management' is clearer."),
    mcq("A function opens a FILE* with fopen and has 3 return paths. RAII fix:", ["fclose before every return", "Wrap it in a class (or unique_ptr with a custom deleter) that fcloses in the destructor", "Use goto"], 1, "Show you can apply RAII beyond memory."),
])
T["d3-2-2"] = ("How printf works (variadic functions)", [
    R("d3c", 9), R("d3c", 2),
    mcq("The order of the variadic macros:", ["va_arg, va_start, va_end", "va_start, then va_arg for each argument, then va_end", "va_end first"], 1, "va_list holds the position in the argument list."),
    mcq("Why does printf need the format string?", ["Style", "Variadic arguments carry no type or count info, so the format tells it what to read", "Speed"], 1, "The core of 'how is printf implemented'."),
    mcq("printf output didn't appear before a crash. Why?", ["printf failed", "stdout is buffered; the buffer wasn't flushed", "The OS deleted it"], 1, "fflush(stdout) or end lines with \\n on a terminal. Links to the fork buffering question."),
    mcq("Passing a char or float through `...`:", ["Passed as is", "Promoted: char/short to int, float to double", "Not allowed"], 1, "That's why %f works for both float and double in printf."),
    out("What does this print?", 'printf("%5.2f|", 3.14159);', " 3.14|", "Width 5, 2 decimals, right-aligned with a leading space."),
    mcq("C++'s type-safe alternative to C varargs:", ["Macros", "Variadic templates (and iostreams / std::format)", "void*"], 1, "Mention it as a modern touch."),
])
T["d3-2-3"] = ("How int and float are stored", [
    R("d3c", 5), R("d3c", 6), R("d3c", 10), R("d3c", 11), R("d3c", 12),
    mcq("-1 in 8-bit two's complement:", ["10000001", "11111111", "01111111"], 1, "Invert the bits of 1 and add 1."),
    mcq("IEEE 754 single precision (float) layout:", ["1 sign, 8 exponent, 23 mantissa bits", "1 sign, 11 exponent, 52 mantissa", "16 / 16"], 0, "Double: 1, 11, 52."),
    out("On a little-endian machine (x86), what prints?", "int x = 1;\nchar* c = (char*)&x;\ncout << (int)*c;", "1", "Little-endian stores the least significant byte first (video #10)."),
])

# ================= DAY 4 =================
T["d4-0-0"] = ("STAR structure", [
    R("d4a", 2), R("d4a", 3), R("d4a", 4),
    mcq("STAR stands for:", ["Start, Talk, Answer, Repeat", "Situation, Task, Action, Result", "Skill, Team, Aim, Review"], 1, "Sanchit: answers were expected in STAR."),
    mcq("Ideal story length:", ["15 seconds", "60-90 seconds, then let them dig", "5 minutes"], 1, "Short enough to invite follow-ups you've prepared for."),
    mcq("The interviewer cuts in mid-story with a question.", ["Finish your story first", "Answer their question directly; they're steering", "Ignore it"], 1, "Interruptions are interest, not rudeness."),
    mcq("Can you reuse one story for two different questions?", ["Never", "Yes, with a different emphasis, but don't lean on one story for everything", "Always use one story"], 1, "11 stories give you range."),
    mcq("The single best upgrade to most results:", ["A longer sentence", "A number or concrete proof", "A quote from your boss"], 1, "Your resume has numbers ready."),
])
T["d4-0-1"] = ("Stories 1-5", [
    R("d4a", 0), R("d4a", 6), R("d4a", 7),
    mcq("Story 3 (customer focus, MerchFlow). The strongest ending:", ["'And the app was cool.'", "What changed for users (no wrong sizes, slot alerts) and that you'd work the same way with MathWorks customers", "'My friends liked it.'"], 1, "Link to EDG's customer work."),
    mcq("Story 4 (rate-limiter race). Emphasise:", ["How hard it was", "How you found it, proved the fix (50 concurrent requests) and prevented a repeat", "Blame the library"], 1, "Process beats drama."),
    mcq("Story 5 (stale stock, a last-minute change). Emphasise:", ["Panic", "How you re-prioritised, what you changed (invalidate on checkout and rollback) and how you communicated", "That it wasn't your fault"], 1, "Vanshika was asked about last-minute changes."),
    chain("Leadership follow-ups:", [
        ("Tell me about a time you showed leadership.", "MerchFlow: you found the problem, talked to clubs and drove the build."),
        ("How did you get others to agree?", "Showed the data from user conversations and a working demo."),
        ("What would you do differently as a leader?", "One honest improvement, e.g. involve users earlier in testing."),
    ]),
    mcq("A story in which everything went perfectly:", ["Best kind", "Weak: interviewers want a challenge and how you handled it", "Fine for HR"], 1, "Show the obstacle."),
])
T["d4-0-2"] = ("Stories 6-11", [
    R("d4a", 5),
    mcq("Story 6, a missed deadline. The right tone:", ["Blame circumstances", "Own it, explain what you changed, show it hasn't repeated", "Say it never happened"], 1, "Anubhav: 'What would you have done differently?'"),
    mcq("Story 7, learning fast (POSIX syscalls). Show:", ["That it was easy", "Your method: man pages, small experiments, isolate, test, then ask", "How many hours you spent"], 1, "Reusable for the 'unfamiliar MATLAB bug' question."),
    mcq("Story 9, a setback (GATE). Avoid:", ["Showing what you changed", "Sounding bitter or blaming the exam", "A result number"], 1, "End on growth: 97.24 percentile, PGEE AIR 114."),
    mcq("Story 10, critical feedback. A strong answer includes:", ["Why the feedback was wrong", "The feedback in their words, what you changed, and proof it worked", "Only the feedback"], 1, "Aashrey and Digvijay were asked this."),
    mcq("Story 11, stress. A strong answer has:", ["'I don't get stressed.'", "Concrete habits (planning, breaks, breaking work down) and one real example", "'I work all night.'"], 1, "Vanshika and Piyush were asked."),
    mcq("Motivating a demotivated teammate:", ["Do their work", "Understand why, find a part they enjoy, set a small shared goal, recognise progress", "Report them"], 1, "Piyush was asked."),
    chain("Explaining tech to a non-technical person:", [
        ("Explain your distributed event log to me as if I'm not technical.", "A numbered register that several machines copy, so nothing is lost if one breaks."),
        ("Why do you need several copies?", "Machines fail; with copies, another one takes over."),
        ("How do they agree who's in charge?", "They vote; whoever gets the majority leads (that's Raft)."),
    ]),
])
T["d4-1-0"] = ("Strengths, weaknesses, how others see you", [
    R("d4a", 1), R("d4b", 7), R("d4b", 3),
    mcq("A strength without proof:", ["Fine", "Weak: always back it with an example", "Better than a long answer"], 1, "Proof beats adjectives."),
    mcq("'What would your friends say is your negative side?'", ["'Nothing.'", "A real, mild flaw consistent with your stated weakness, plus how you manage it", "A serious flaw"], 1, "Aashima was asked both positive and negative."),
    mcq("'What makes you unique?'", ["'I'm hard-working.'", "A specific combination with proof: systems depth plus talking to users plus verifying your work", "'Nothing much.'"], 1, "Specific beats generic."),
    mcq("Your strength in HR was 'thoroughness'; in the manager round you say 'speed'. Risk?", ["None", "Inconsistent: they compare notes", "Shows range"], 1, "Same 2 + 2 in every round."),
])
T["d4-1-1"] = ("Manager situations", [
    R("d4b", 0), R("d4b", 1), R("d4b", 2), R("d4b", 4), R("d4b", 6),
    mcq("Three urgent tasks land at once:", ["Do them in arrival order", "Rank by impact and deadline, agree priorities with your lead, communicate trade-offs", "Work overtime on all"], 1, "Show a method, not heroics."),
    mcq("You disagree with your manager's technical decision:", ["Comply silently", "Raise it privately with data; if they still decide otherwise, commit and support it", "Escalate immediately"], 1, "'Disagree and commit.'"),
    mcq("'How will this role differ from college?'", ["'Not much.'", "Real customers, code reviews and quality bars, team-scale work, fixed deadlines", "'More money.'"], 1, "Piyush was asked."),
])
T["d4-1-2"] = ("No internship, PPO, salary", [
    R("d4b", 5),
    mcq("'Why no internship?'", ["Make excuses", "Say plainly, then show what you built instead (MerchFlow, team Kafka project)", "Avoid the question"], 1, "Confident, not defensive."),
    mcq("'What did you do in your summers?'", ["'Nothing.'", "Projects and preparation, with one concrete outcome", "'Watched movies.'"], 1, "Show you used the time."),
    mcq("A PPO-related scenario question:", ["Give different answers to HR and manager", "Be clear and consistent about your commitment", "Refuse to answer"], 1, "Aashima had a PPO discussion."),
    mcq("'Would you join if you got another offer later?'", ["'Depends on the money.'", "Honest commitment with reasons tied to MathWorks", "'Probably not.'"], 1, "Same as the better-offer question."),
])
T["d4-2-2"] = ("Rapid fire HR", [
    chain("Rapid fire: answer each in under 30 seconds.", [
        ("One word that describes you?", "One word plus a 1-line proof."),
        ("Your biggest achievement?", "PGEE AIR 114 / GATE 97.24 percentile, or a project result, with why it mattered."),
        ("A failure?", "Short STAR with the learning."),
        ("Why should we hire you?", "3 points with proof."),
        ("Where in 5 years?", "Strong engineer at MathWorks, owning a component."),
        ("Team player or individual?", "Both, with a 1-line example of each."),
        ("Handle pressure?", "Your habit plus a 1-line example."),
        ("What motivates you?", "Building things people rely on."),
        ("Any questions?", "Yes: one prepared question."),
    ]),
])

# ================= DAY 5 =================
T["d5-0-0"] = ("fork / exec / wait", [
    R("d5a", 0), R("d5a", 1), R("d5a", 2), R("d5a", 3), R("d5a", 4), R("d5a", 5), R("d5a", 6), R("d5a", 7), R("d5a", 8),
    mcq("After fork, is the parent's memory copied immediately?", ["Yes, fully", "No: copy-on-write; pages are copied only when one process writes", "Shared forever"], 1, "Why fork is cheap even for big processes."),
])
T["d5-0-1"] = ("Pipe code in C", [
    R("d5b", 0), R("d5b", 6),
    mcq("After pipe(fd):", ["fd[0] write, fd[1] read", "fd[0] is the read end, fd[1] the write end", "Both read and write"], 1, "Remember: 0 like stdin (read), 1 like stdout (write)."),
    mcq("Writing to a pipe whose read ends are all closed:", ["Blocks forever", "SIGPIPE (write fails with EPIPE if ignored)", "Data is saved"], 1, "Why `yes | head` stops."),
    mcq("The pipe buffer is full:", ["Data is lost", "The writer blocks until the reader reads", "The OS grows it forever"], 1, "Pipes give natural back-pressure."),
    mcq("In the child that runs `ls` (left side):", ["dup2(fd[0], 0)", "dup2(fd[1], 1), then close both fd[0] and fd[1], then execvp", "Nothing"], 1, "Close the originals after dup2."),
    mcq("Who calls waitpid?", ["The children", "The parent, for both children (after closing its pipe ends)", "Nobody"], 1, "Otherwise zombies."),
    chain("Write it: `ls | wc -l` in C.", [
        ("Step 1?", "int fd[2]; pipe(fd);"),
        ("First child?", "fork; in the child: dup2(fd[1], 1); close(fd[0]); close(fd[1]); execlp(\"ls\", \"ls\", NULL); then exit(1) if exec fails."),
        ("Second child?", "fork; in the child: dup2(fd[0], 0); close both; execlp(\"wc\", \"wc\", \"-l\", NULL)."),
        ("Parent?", "close(fd[0]); close(fd[1]); waitpid both children."),
    ]),
])
T["d5-0-2"] = ("dup, dup2, file descriptors, redirection", [
    R("d5b", 3),
    mcq("dup(fd) returns:", ["fd + 1", "The lowest-numbered free descriptor, pointing to the same open file", "Always 3"], 1, "dup2 lets you pick the number (Sanchit was asked the difference)."),
    mcq("Descriptors 0, 1 and 2 are:", ["Files 0-2", "stdin, stdout, stderr", "Reserved for the kernel"], 1, "Basic but always asked."),
    mcq("After fork, the child's file descriptors:", ["Are closed", "Are copies that share the same open file (and file offset)", "Must be reopened"], 1, "That's how a pipe connects parent and child."),
    mcq("`>` vs `>>` in your shell:", ["Same", "open with O_TRUNC vs O_APPEND", "Read vs write"], 1, "Then dup2 onto fd 1."),
    mcq("`< in.txt` is implemented by:", ["dup2(fd, 1)", "open in.txt and dup2(fd, 0)", "A pipe"], 1, "Same idea, other direction."),
    mcq("O_CLOEXEC on a descriptor means:", ["Close on exit", "Close it automatically on exec, so it doesn't leak into the new program", "Read-only"], 1, "Depth bonus."),
    mcq("dup2(fd, fd):", ["Error", "Does nothing and returns fd", "Closes fd"], 1, "An edge case interviewers like."),
])

T["d5-1-0"] = ("Your shell, end to end", [
    R("d5b", 1), R("d5b", 5), R("d5b", 4), R("d5b", 9),
    mcq("execvp fails in the child. What must the child do?", ["Continue the loop", "Print an error and exit(), or you'll have two shells running", "Call exec again"], 1, "A classic real bug."),
    mcq("For `cmd &`, the shell:", ["Waits", "Doesn't wait, records the job, and reaps it later on SIGCHLD", "Runs it in a thread"], 1, "JobController's job."),
    mcq("How do you get a command's exit code from waitpid?", ["The return value", "WIFEXITED(status) then WEXITSTATUS(status)", "errno"], 1, "That's what $? shows."),
    mcq("Why processes (fork) and not threads for running commands?", ["Speed", "Each command is a separate program needing its own address space; exec replaces the whole process", "Threads can't run code"], 1, "Show you understand the model."),
])
T["d5-1-1"] = ("Signals", [
    R("d5b", 2), R("d5b", 7),
    mcq("Which signal can NEVER be caught or ignored?", ["SIGINT", "SIGKILL (and SIGSTOP)", "SIGTERM"], 1, "kill -9."),
    mcq("Why use sigaction instead of signal()?", ["Shorter", "Portable, well-defined behaviour plus flags like SA_RESTART", "Faster"], 1, "Your resume says sigaction."),
    mcq("The type for a flag set in a handler:", ["int", "volatile sig_atomic_t", "bool"], 1, "Guarantees atomic, visible writes."),
    mcq("SIGCHLD is sent when:", ["The parent exits", "A child exits or stops", "A pipe breaks"], 1, "Your reaping trigger."),
    mcq("SA_RESTART does:", ["Restarts the program", "Restarts slow system calls (like read) interrupted by the handler instead of failing with EINTR", "Restarts the signal"], 1, "Know whether your shell sets it, and why."),
    mcq("Why does only the foreground job get Ctrl+C?", ["Luck", "The terminal sends signals to its foreground process group (set with tcsetpgrp)", "The shell forwards it"], 1, "Process groups and job control."),
])
T["d5-1-3"] = ("History deque and OOP design", [
    R("d5b", 8),
    mcq("Splitting the shell into ProcessExecutor, JobController, BuiltinEngine and HistoryManager follows:", ["DRY", "Single Responsibility: each class has one reason to change", "YAGNI"], 1, "Name the principle."),
    mcq("Why not std::vector for history with eviction from the front?", ["It can't store strings", "erase at the front is O(n); a deque pops the front in O(1)", "Too much memory"], 1, "Data-structure reasoning."),
    mcq("Saving history across sessions:", ["Not needed", "Load the file at start, write it on exit (or append each command)", "Store in an env var"], 1, "Mention the file location (e.g. in the home dir)."),
    mcq("An alternative to a deque:", ["Linked list only", "A fixed circular buffer of 20 slots", "A hash map"], 1, "Show you know options."),
    mcq("Why classes in your C++ shell rather than plain C functions?", ["Required by C++", "They encapsulate state (job table, history) with the functions that use it", "Speed"], 1, "Ties OOP to your project."),
])

T["d5-2-0"] = ("Synchronisation and deadlock", [
    R("d5c", 0), R("d5c", 1), R("d5c", 4), R("d5c", 5), R("d5c", 9),
    mcq("The 4 conditions for deadlock:", ["Speed, memory, CPU, disk", "Mutual exclusion, hold and wait, no preemption, circular wait", "Lock, unlock, wait, signal"], 1, "Break any one to prevent it."),
    mcq("Spinlock vs mutex:", ["Same", "A spinlock busy-waits (good for very short waits); a mutex sleeps", "A mutex busy-waits"], 1, "Depth bonus."),
    mcq("Why wait on a condition variable inside a while loop?", ["Style", "Spurious wakeups: re-check the condition after waking", "Speed"], 1, "Classic follow-up."),
    mcq("Banker's algorithm is for:", ["Detection", "Deadlock avoidance", "Scheduling"], 1, "Know the names: prevention, avoidance, detection."),
])
T["d5-2-1"] = ("Virtual memory and how a program runs", [
    R("d5c", 3), R("d5c", 6), R("d5c", 7), R("d5c", 8),
    mcq("Benefits of virtual memory:", ["Only speed", "Isolation between processes, more address space than RAM, easy sharing", "None"], 1, "Each process thinks it has the machine."),
    mcq("A TLB is:", ["A disk cache", "A cache of recent virtual-to-physical page translations", "A thread type"], 1, "Speeds up address translation."),
    mcq("Page fault vs segmentation fault:", ["Same", "Page fault: valid page not in RAM (normal); segfault: invalid access (the program is killed)", "Segfault is normal"], 1, "Video #74."),
    mcq("C++ build stages in order:", ["Link, compile, preprocess", "Preprocess, compile, assemble, link", "Compile, link, preprocess"], 1, "Video #2."),
])
T["d5-2-2"] = ("Threads vs processes", [
    R("d5c", 2),
    mcq("Which context switch is cheaper?", ["Process", "Thread (same address space, no page-table switch)", "Same"], 1, "A common follow-up."),
    mcq("One thread segfaults:", ["Only that thread dies", "The whole process dies", "Nothing"], 1, "Why processes give stronger isolation."),
    mcq("Ways processes communicate (IPC):", ["Global variables", "Pipes, shared memory, message queues, sockets, signals", "None"], 1, "Your shell uses pipes."),
    mcq("When choose processes over threads?", ["Never", "When isolation matters (one crash mustn't kill the rest)", "Always"], 1, "Browser tabs are a classic example."),
    mcq("fork() in a multithreaded program copies:", ["All threads", "Only the calling thread", "No threads"], 1, "Why you should exec soon after fork."),
    mcq("Each thread has its own:", ["Heap", "Stack and registers", "Code"], 1, "Ties to the memory layout."),
])

# ================= DAY 6 =================
T["d6-0-0"] = ("MerchFlow architecture (HLD)", [
    R("d6a", 5),
    mcq("What does your API Gateway do?", ["Stores orders", "Single entry point: routing, JWT auth, RBAC, rate limiting", "Sends emails"], 1, "Your resume lists all of these at the gateway."),
    mcq("Why does each service have its own database?", ["Fashion", "Loose coupling: services deploy and change independently", "Speed only"], 1, "And the price: no cross-service joins or transactions, hence the Saga."),
    mcq("Why is notification async via RabbitMQ?", ["Required", "So a slow notification service can't delay checkout", "Emails need queues"], 1, "Straight from your resume."),
    mcq("The gateway is a single point of failure. Fix?", ["Ignore", "Run several instances behind a load balancer", "Remove it"], 1, "Show you know the weakness."),
    mcq("The biggest cost of microservices you faced:", ["None", "Distributed transactions and data consistency", "Too few services"], 1, "Leads into the Saga."),
    chain("'Walk me through one order':", [
        ("A student clicks Buy. What happens first?", "The request hits the gateway: JWT check, RBAC, rate limit, then routing to the Order service."),
        ("Then?", "The Order service takes the per-item Redis lock, checks the idempotency key, reserves stock and saves the order in PostgreSQL (a transaction)."),
        ("Payment fails. Then?", "The Saga compensates: restore stock, invalidate the cache, mark the order failed."),
        ("Success?", "Publish an event to RabbitMQ; the Notification service sends the delivery-slot alert."),
    ]),
    mcq("How would you know a service is unhealthy in production?", ["You wouldn't", "Health checks, logs and metrics (latency, errors) with alerts", "Users complain"], 1, "Production thinking (Aashima)."),
])
T["d6-0-1"] = ("Checkout: lock, idempotency, Saga", [
    R("d6a", 0), R("d6a", 1), R("d6a", 4), R("d6a", 8),
    mcq("Why does the Redis lock have a TTL?", ["Speed", "So a crashed holder doesn't block the item forever", "Redis needs one"], 1, "Then the follow-up: what if work takes longer than the TTL?"),
    mcq("Who generates the idempotency key?", ["The server after saving", "The client, before the first attempt, and reuses it on retries", "The database"], 1, "Otherwise retries get new keys."),
    mcq("Saga choreography vs orchestration:", ["Same", "Choreography: services react to each other's events; orchestration: a coordinator tells each step what to do", "Orchestration has no coordinator"], 1, "Know which one you built."),
    mcq("Why not two-phase commit (2PC) across services?", ["It's newer", "It blocks while waiting, needs every participant up, and couples services tightly", "It's not ACID"], 1, "Why Sagas exist."),
    mcq("Why lock per item instead of one global checkout lock?", ["Simpler", "A global lock would serialise all checkouts; per-item only blocks buyers of the same item", "Redis limit"], 1, "Fine-grained locking for flash sales."),
])
T["d6-0-2"] = ("Databases and transactions", [
    R("d6a", 2), R("d6a", 6), R("d6a", 7),
    mcq("ACID stands for:", ["Atomic, Consistent, Isolated, Durable", "Available, Consistent, Indexed, Distributed", "Async, Cached, Isolated, Durable"], 0, "Sneha was asked ACID."),
    mcq("Why normalise a schema?", ["Speed always", "Remove duplicated data, which avoids update anomalies", "Fewer tables"], 1, "1NF atomic values, 2NF no partial dependency, 3NF no transitive dependency."),
    mcq("A dirty read is:", ["Reading deleted rows", "Reading another transaction's uncommitted changes", "A slow read"], 1, "Prevented at Read Committed and above."),
    mcq("`SELECT ... FOR UPDATE` does:", ["Updates rows", "Locks the selected rows until the transaction ends", "Creates an index"], 1, "One fix for the oversell race."),
    mcq("Why MongoDB for the catalog?", ["It's faster always", "Items have varying attributes; a flexible document schema fits them", "No reason"], 1, "Your resume's reason."),
])
T["d6-0-3"] = ("Cache, rate limiter, JWT", [
    R("d6a", 3), R("d6b", 2), R("d6b", 6),
    mcq("The role of a TTL on cached catalog entries:", ["None", "A safety net: even a missed invalidation expires eventually", "Speed"], 1, "Invalidation first, TTL as backup."),
    mcq("A race-free fixed-window rate limiter in Redis:", ["GET then SET", "INCR the counter (atomic), set EXPIRE on the first hit", "Store in the gateway's memory"], 1, "Your race came from read-then-write."),
    mcq("Token bucket vs fixed window:", ["Same", "Fixed windows allow bursts at the window edges; a token bucket smooths them", "Token bucket has no limit"], 1, "Know at least one trade-off."),
    mcq("The IDOR bug (users editing others' profiles). The proper fix:", ["Hide the button", "Check on the server that the token's user owns the resource", "Use POST"], 1, "Never trust client-side checks."),
    mcq("Is a JWT's payload secret?", ["Yes, it's encrypted", "No: it's only signed (base64), anyone can read it, so no secrets inside", "Only the header is visible"], 1, "Signed is not encrypted."),
])

T["d6-1-0"] = ("Node.js and the event loop", [
    R("d6b", 0), R("d6b", 3), R("d6b", 4),
    out("Node.js: what is the order?", "setTimeout(() => console.log('t'), 0);\nprocess.nextTick(() => console.log('n'));\nPromise.resolve().then(() => console.log('p'));\nconsole.log('s');", "s n p t", "Sync, then the nextTick queue, then promise microtasks, then timers."),
    mcq("Is Node.js entirely single-threaded?", ["Yes", "Your JS runs on one thread, but libuv uses a thread pool for file I/O, DNS and crypto", "No, fully multithreaded"], 1, "Aryan was asked if JS is single-threaded."),
    mcq("An unhandled promise rejection in modern Node:", ["Ignored", "Crashes the process by default", "Retried"], 1, "Always catch async errors."),
    mcq("async/await is:", ["A new thread", "Syntax on top of promises", "Blocking"], 1, "The function pauses at await without blocking the loop."),
    mcq("Why Node.js for the gateway?", ["Fastest CPU", "Good at many concurrent I/O-bound requests with little overhead", "Required by Express"], 1, "Name the trade-off: bad for CPU-heavy work."),
])
T["d6-1-1"] = ("RabbitMQ", [
    R("d6b", 1),
    mcq("RabbitMQ exchange types:", ["Only one", "Direct, fanout, topic (and headers)", "Kafka, Redis"], 1, "Fanout broadcasts; topic routes by pattern."),
    mcq("A dead-letter queue holds:", ["All messages", "Messages that failed too many times or expired, for inspection", "Deleted users"], 1, "So one bad message doesn't block the queue."),
    mcq("RabbitMQ vs Kafka:", ["Same", "RabbitMQ removes messages after ack (a work queue); Kafka keeps a log you can replay", "Kafka has no ordering"], 1, "Your two projects contrast nicely."),
    mcq("Consumer prefetch limits:", ["Queue size", "How many unacked messages a consumer holds at once", "Retries"], 1, "Spreads load fairly."),
    mcq("To survive a broker restart:", ["Nothing needed", "Durable queues + persistent messages", "Use more RAM"], 1, "Production detail."),
    mcq("Delivery guarantee with acks:", ["Exactly once", "At least once, so consumers must be idempotent", "At most once"], 1, "Ties to your idempotency keys."),
    mcq("Why not just call the Notification service over HTTP from checkout?", ["Same thing", "If it's slow or down, checkout would wait or fail; the queue decouples them", "HTTP can't send email"], 1, "Your resume's exact reason."),
])
T["d6-1-2"] = ("Express, REST, MongoDB", [
    R("d6b", 5),
    mcq("Express middleware order matters because:", ["It doesn't", "Each runs in sequence: auth must come before the route handler", "Alphabetical"], 1, "Your gateway: JWT, then RBAC, then rate limit, then route."),
    mcq("What does next() do in Express middleware?", ["Ends the response", "Passes control to the next middleware", "Restarts"], 1, "Forget it and the request hangs."),
    mcq("PUT vs PATCH:", ["Same", "PUT replaces the whole resource; PATCH changes some fields", "PATCH creates"], 1, "Basic REST."),
    mcq("Status code for a successful create:", ["200", "201 Created", "204"], 1, "And 429 for rate limiting."),
    mcq("REST is stateless means:", ["No database", "Each request carries everything needed (like the JWT); no server session", "No caching"], 1, "Why JWT fits."),
    mcq("MongoDB: embed vs reference:", ["Always embed", "Embed data read together and owned by the parent; reference shared or large data", "Always reference"], 1, "L1 depth is enough."),
    mcq("Rate-limited request response code:", ["403", "429 Too Many Requests", "500"], 1, "Small detail, big impression."),
])
T["d6-1-3"] = ("Design patterns", [
    R("d6b", 7),
    mcq("Notify email + SMS + app when an order is placed. Pattern?", ["Strategy", "Observer", "Builder"], 1, "Subscribers listen; the order service doesn't know them."),
    mcq("Creating different payment handlers from a type string. Pattern?", ["Observer", "Factory", "Command"], 1, "Hides construction details."),
    mcq("Building an Order with many optional fields step by step. Pattern?", ["Builder", "Singleton", "Strategy"], 0, "Avoids huge constructors."),
    mcq("Wrapping each operation as an object so it can be queued, logged or undone. Pattern?", ["Command", "Factory", "Observer"], 0, "Undo/redo and job queues."),
    mcq("Vanshika: 'warn before the stack reaches its limit without modifying the main code.' Best answer:", ["Edit push()", "Inject a policy / listener (Strategy or Observer) that push() calls; add new behaviour by adding a class", "Use a global flag"], 1, "Open/closed principle: open for extension, closed for modification."),
    mcq("SOLID's O means:", ["Object-oriented", "Open for extension, closed for modification", "Only one class"], 1, "Name-drop it with the stack example."),
    chain("Design the warning stack:", [
        ("Interface?", "class LimitPolicy { public: virtual void onPush(size_t size, size_t cap) = 0; virtual ~LimitPolicy() = default; };"),
        ("How does Stack use it?", "Stack holds a LimitPolicy* (or unique_ptr) set in the constructor; push() calls policy->onPush(size, cap)."),
        ("New behaviour later?", "Write a new policy class; Stack's code never changes."),
    ]),
])

T["d6-2-0"] = ("Partitions, replication, watermark", [
    R("d6c", 1), R("d6c", 5), R("d6c", 6),
    mcq("Why is an append-only log fast?", ["Compression", "Sequential disk writes, no in-place updates", "Uses RAM only"], 1, "Kafka's core design idea."),
    mcq("An offset is:", ["A timestamp", "A record's position in a partition's log", "A broker id"], 1, "Consumers track their offset."),
    mcq("A follower falls far behind. What happens to the ISR?", ["Nothing", "It's removed from the in-sync set until it catches up", "The leader stops"], 1, "So the watermark can keep moving."),
    mcq("A producer waiting for acks from all in-sync replicas gets:", ["Speed", "Durability: an acknowledged record is on every ISR", "Ordering"], 1, "Trade latency for safety."),
    mcq("In a consumer group:", ["Every consumer reads everything", "Each partition goes to exactly one consumer in the group", "One consumer per topic"], 1, "Parallelism = number of partitions."),
])
T["d6-2-1"] = ("Raft, leader epochs, idempotent producers", [
    R("d6c", 0), R("d6c", 4),
    mcq("A Raft term is:", ["A timeout", "A logical election period number; higher terms win", "A log entry"], 1, "Stale leaders see a higher term and step down."),
    mcq("An entry is committed in Raft when:", ["The leader writes it", "A majority of nodes have stored it", "All nodes have it"], 1, "Majority = quorum."),
    mcq("Split brain is:", ["A crash", "Two nodes both acting as leader at once", "A full disk"], 1, "What leader epochs prevent."),
    mcq("How do leader epochs fence a stale leader?", ["They don't", "Requests carry the epoch; brokers reject any with an epoch lower than the current one", "By IP"], 1, "Your resume line."),
    mcq("Idempotent producer dedup works by:", ["Hashing payloads", "(producer ID, sequence number) per partition; the broker drops repeats", "Timestamps"], 1, "Retries after timeouts don't duplicate."),
    mcq("Why an odd number of Raft nodes?", ["Tradition", "3 and 4 both tolerate 1 failure, so the 4th node adds cost without extra tolerance", "Required"], 1, "Majority math."),
])
T["d6-2-2"] = ("CAP, gRPC, your role", [
    R("d6c", 2), R("d6c", 3), R("d6c", 9),
    mcq("In CAP, partition tolerance is:", ["Optional", "Not optional in real networks, so you choose C or A during a partition", "Same as availability"], 1, "Kashif was asked about CAP."),
    mcq("Protocol Buffers give gRPC:", ["JSON readability", "Compact binary messages and a typed contract that generates client and server code", "Encryption"], 1, "A benefit Vanshika was asked about."),
    mcq("gRPC call types:", ["Only request-response", "Unary, server streaming, client streaming, bidirectional streaming", "Only streaming"], 1, "Mention streaming as a benefit."),
    mcq("gRPC runs on:", ["HTTP/1.0", "HTTP/2 (multiplexed streams on one connection)", "UDP"], 1, "Another benefit."),
    mcq("'What was YOUR part in the team project?'", ["'We did everything together.'", "Name the components you built and decisions you made, and credit your teammate's part", "'Mostly my teammate.'"], 1, "Be precise; they'll probe your part."),
])
T["d6-2-3"] = ("LLD and SQL", [
    R("d6c", 7), R("d6c", 8),
    mcq("LEFT JOIN returns:", ["Only matching rows", "All rows from the left table, with NULLs where the right has no match", "All rows from both"], 1, "Draw it if asked."),
    mcq("Kashif's student-rank system: good classes?", ["One class with everything", "Student (id, marks per subject), RankBoard (holds students, getFirstRank / getLastRank / getNthRank)", "Only functions"], 1, "Separate data from the ranking logic."),
    mcq("getNthRank called many times:", ["Sort on every call", "Sort once (O(n log n)), then answer each query in O(1); re-sort or use a balanced tree on updates", "Linear scan each time"], 1, "Think about query patterns."),
    mcq("Two students have equal marks. Ranks?", ["Random", "Define it: same rank (dense rank) or a tie-breaker; ask the interviewer", "Error"], 1, "Asking clarifying questions is a plus."),
    mcq("COUNT(*) vs COUNT(col):", ["Same", "COUNT(*) counts all rows; COUNT(col) skips NULLs in that column", "COUNT(col) is faster"], 1, "Classic SQL trap."),
    mcq("Index a column that is:", ["Never used", "Often used in WHERE, JOIN or ORDER BY", "Frequently updated only"], 1, "Ties to the index trade-off."),
])

# ================= DAY 7 =================
T["d7-0-0"] = ("Linked list problems", [
    R("d7a", 0), R("d7a", 2), R("d7a", 4), R("d7a", 5), R("d7a", 6),
    mcq("Iterative reverse uses which pointers?", ["One", "prev, curr, next", "head and tail only"], 1, "Save next, point curr->next to prev, then advance both."),
    mcq("Cycle detection with a hash set costs:", ["O(1) space", "O(n) space; Floyd's needs O(1)", "O(n^2) time"], 1, "Start with this, then go optimal (Sanchit)."),
    mcq("Merging two sorted lists:", ["O(n log n)", "O(m + n) time, O(1) extra space", "O(mn)"], 1, "Dummy node again."),
    mcq("Delete a node given only a pointer to it (not the tail):", ["Impossible", "Copy the next node's value into it, then unlink the next node", "Walk from the head"], 1, "A classic trick question."),
    mcq("Intersection point of two lists:", ["Nested loops only", "Two pointers that switch to the other list's head at the end; they meet at the intersection", "Sort both"], 1, "O(m + n), O(1) space."),
])
T["d7-0-1"] = ("Stack problems", [
    R("d7a", 1), R("d7a", 3), R("d7a", 7),
    mcq("Largest rectangle in a histogram:", ["O(n^2) only", "Monotonic stack, O(n)", "Heap"], 1, "Same pattern as next greater element."),
    mcq("Next greater element in a CIRCULAR array (LC 503):", ["Impossible", "Iterate 2n indices (i % n) with a monotonic stack", "Sort first"], 1, "Piyush's question family."),
    mcq("Implement a stack using queues: cost of push or pop:", ["Both O(1)", "One of them O(n) (rotate the queue)", "Both O(log n)"], 1, "Know the trade-off."),
    mcq("Evaluating a postfix expression uses:", ["Queue", "Stack", "Tree"], 1, "Push operands; on an operator pop two."),
    mcq("MinStack with O(1) min, simplest design:", ["Sort on push", "Store (value, currentMin) pairs, or a second stack of mins", "Scan on getMin"], 1, "Anubhav: stack private, functions public."),
])
T["d7-1-0"] = ("Array problems", [
    R("d7b", 0), R("d7b", 1), R("d7b", 2), R("d7b", 3),
    mcq("Kth smallest with a heap:", ["Min-heap of all", "Max-heap of size k: O(n log k)", "Sort only"], 1, "Mention both heap and quickselect."),
    mcq("Merging two sorted arrays:", ["O(n log n)", "Two pointers, O(m + n)", "O(mn)"], 1, "Step 1 of the median question."),
    mcq("Quickselect's partition step:", ["Merges halves", "Puts the pivot in its final sorted place, smaller left, larger right", "Builds a heap"], 1, "Lomuto or Hoare."),
    mcq("Kashif's getNthRank with ties:", ["Ignore ties", "Clarify the rule (dense rank or standard rank) before coding", "Return -1"], 1, "Clarifying questions score points."),
])
T["d7-1-1"] = ("Linked List class (no IDE)", [
    chain("Write a LinkedList class (Aashrey):", [
        ("Node and class members?", "struct Node { int val; Node* next; }; class LinkedList { Node* head = nullptr; ... };"),
        ("Constructor from a vector?", "Loop through the values, append each with a tail pointer: O(n)."),
        ("reverse()?", "Iterative prev / curr / next, then head = prev."),
        ("Destructor?", "Walk the list deleting each node."),
    ]),
    mcq("Your LinkedList has a destructor that deletes nodes. You also need:", ["Nothing else", "A copy constructor and copy assignment (deep copy), or `= delete` them: Rule of Three", "A virtual destructor"], 1, "Otherwise a copy causes a double free."),
    mcq("Appending in O(1) needs:", ["Nothing", "A tail pointer", "A doubly linked list"], 1, "Mention it before they ask."),
    mcq("In Python (Aashrey's version), the 'destructor' step:", ["Required", "Not needed: garbage collection frees nodes", "Use del on each"], 1, "Language differences show depth."),
    mcq("Testing your class on paper. Check:", ["Only a long list", "Empty list, one node, two nodes, then a normal case", "Only the normal case"], 1, "Edge cases first."),
    mcq("Interviewer: 'reverse it recursively too'. The base case:", ["head == nullptr || head->next == nullptr: return head", "When length is 2", "No base case"], 0, "Then reverse the rest and fix two pointers."),
])
T["d7-2-0"] = ("Trees and heaps", [
    R("d7c", 0), R("d7c", 1), R("d7c", 3), R("d7b", 6),
    mcq("A BST's inorder traversal gives:", ["Random order", "Sorted order", "Level order"], 1, "The key to many BST problems."),
    mcq("Heap stored in an array: children of index i:", ["i+1, i+2", "2i+1 and 2i+2 (parent (i-1)/2)", "i*2 only"], 1, "Write this without thinking."),
    mcq("Binary tree to BST (same structure): the core idea:", ["Rotate nodes", "Collect values, sort them, write them back with an inorder traversal", "Rebuild from scratch"], 1, "Asked to Aashima. Then discuss the 'without extra space' constraint with the interviewer."),
    mcq("C++ std::priority_queue by default is:", ["A min-heap", "A max-heap", "Sorted array"], 1, "Use greater<int> for a min-heap."),
])
T["d7-2-1"] = ("Backtracking", [
    R("d7b", 4), R("d7b", 5),
    mcq("The backtracking template:", ["Sort, search", "Choose, explore (recurse), un-choose", "Divide and merge"], 1, "Say it out loud before coding."),
    mcq("Rat in a maze: one path vs all paths:", ["Same code", "Stop at the first success, or record every path and keep exploring", "All paths is impossible"], 1, "Clarify which they want."),
    mcq("Word Search: marking visited without an extra matrix:", ["Impossible", "Temporarily overwrite board[i][j] with '#', then restore it", "Use a global set only"], 1, "Saves space."),
    mcq("Pruning means:", ["Deleting the tree", "Stopping early when a partial path can't succeed", "Sorting first"], 1, "Big speed win in backtracking."),
])
T["d7-2-2"] = ("Favourite data structure and puzzles", [
    R("d7c", 2), R("d7c", 4), R("d7c", 5), R("d7c", 6), R("d7c", 7),
    mcq("'What's your favourite data structure?' (they will grill you):", ["Name one you barely know", "Linked list (or heap): operations, complexities, implementation, real uses, trade-offs vs arrays", "Say 'all of them'"], 1, "Aashrey was grilled on his choice."),
    mcq("Linked list vs array, the key trade-off:", ["None", "O(1) insert/delete at a known node vs O(1) random access and cache-friendliness", "Arrays can't grow"], 1, "Real use: LRU cache = hash map + doubly linked list."),
    mcq("Puzzle: 100 doors, toggled on passes 1 to 100 (pass k toggles every kth door). How many open at the end?", ["50", "10 (the perfect squares)", "0"], 1, "A door is toggled once per divisor; only perfect squares have an odd number of divisors."),
])

# ================= DAY 8 =================
T["d8-2-1"] = ("Confidence round", [R("d8c", i) for i in range(6)])
