# context.md: full context of the MathWorks prep chat

Contents:
1. What was asked and built
2. Key facts about the MathWorks process
3. Online assessment (OA)
4. All 12 interview reports, condensed per round
5. Senior reviews (word for word)
6. Candidate resume summary
7. Prep plan: rules, Part 1 (non-tech, 2 days), Part 2 (tech, 7 days)
8. CppNuts video watch order
9. Open items
10. Progress log and C++ gap analysis (latest)

---

## 1. What was asked and built (in order)
1. **Filter two Google Sheets down to MathWorks rows** and build one final workbook (a Claude Sheet) with the seniors' reviews added. Result: tabs Overview, Prep Plan, Interview Reports (12 reports: 9 from sheet 1, 3 from sheet 2), Question Bank (107 rows), Senior Reviews (39 points).
2. **Rebuild only the Prep Plan tab**, round by round, split into non-tech (2-day strategy) and tech (detailed plan), using the candidate's resume for likely questions. The other tabs were left untouched.
3. **Rank a CppNuts YouTube playlist** (82 videos, 13 already watched) into High / Medium / Low batches for MathWorks, in watch order.
4. **Turn that ranking into a Claude Doc.**
5. **Package everything** into CLAUDE.md + context.md as a zip (this file).

Links (private to the owner unless shared):
- Workbook: https://claude.ai/artifact/3fvsfyZtMUqdzjVQMYwgrh
- Video doc: https://claude.ai/artifact/DMsDF5QpF7TqU99fnCddGg

---

## 2. Key facts about the MathWorks process
| Item | Details | Source |
|---|---|---|
| Program | MathWorks campus hiring for the **EDG** program. Offices: Hyderabad and Bengaluru. | All reports |
| Shortlist | 59 students shortlisted, 12 selected (one campus). | Nikhil Saxena |
| Rounds | Technical, Managerial (Hiring / Engineering Manager), HR. **Order not fixed.** One technical round + two behavioural rounds; HR/managerial weighted equally with tech. | Piyush, Aashrey, Aashima, Kashif |
| Tech round content | Mostly OOPS and OS, C/C++ fundamentals (pointers, struct), snippet output / error finding, implementing classes, 1-3 DSA (LeetCode easy-medium). | Aashrey, Aashima, Nikhil, Sanchit |
| Coding format | Shared doc / Hackerrank / notepad, **not compiled**. Full code (Anubhav, Nikhil, Aashrey) or pseudocode (Vanshika, Aashima; Sanchit for lack of time). Language usually your choice; **C++ preferred, Java being moved away from**. | Senior reviews |
| Languages | Name and rate your languages, then get snippets in each one. At least 2 languages; **3 expected from Master's students**. | Piyush, Aashima, Aashrey |
| EDG / PPT | HR/managerial questions come straight from the PPT (what EDG is, its domains, why EDG, why MathWorks). 10 of 12 reports mention it. Attend it, take notes; read the website and core values. | Nearly all |
| Location | Hyderabad vs Bengaluru, with reasons. Decide in advance; professional reasons only (e.g. "systems"); **can't change later**. They may show departments in both offices. | Nikhil, Anubhav, Sanchit, Aryan |
| Outcomes | 12 reports: 8 Selected, 1 Rejected (Viral Shah, HR round only described), 3 not recorded. | Both sheets |
| Official resource | MathWorks guide "Interviewing at Mathworks as a Student". | Aashrey |
| DSA prep | Striver A2Z / ~450 sheet; LeetCode medium. Master one data structure (favourite DS gets grilled). InterviewBit lists are enough for HR/managerial. | Nikhil, Vanshika, Aashima, Aashrey, Sanchit |
| Communication | Think aloud (essential online), steady pace, a story for every behavioural answer, ask for hints and clarifications, be confident, don't look desperate. | Piyush, Vanshika, Aashima, Sneha |

---

## 3. Online assessment (OA)
- Structure: **2 DSA + ~30 MCQs** (frontend, OS, aptitude etc.).
- **Both DSA questions must be implemented in different languages.**
- Python was not offered this time, so mostly C++.
- Previous-year / other-college MCQs repeat a lot (Aashrey).

---

## 4. Interview reports (12), condensed

### Sheet 1: Interview_PG_2026
**Nikhil Saxena (Selected). Order: Managerial, Technical, HR**
- Managerial: about himself and how he sees MathWorks; HR-like.
- Technical (1.5 h+, no DSA, Hackerrank used as a notepad): many snippets to find errors / output / fixes; **implement a Vector class in C** (push_back, pop_back, erase); C++ friend, virtual table, dynamic dispatch, immutability, diamond problem; Java GC, reflection, interning, string pool; implement an algorithm described in text, in C.
- HR: a project you liked and worked on as a team (leads to leadership, conflict resolution, initiative). HR is non-technical: relate tech to real-world examples.
- Remarks: the company wants to hear about itself (read the website); answer plus something extra; fix code errors quickly; don't use GPT; PPT questions come in both managerial and HR; ask clarifying questions.

**Piyush Kumar (Selected). Order: Hiring Manager, Technical, HR**
- Manager: intro, knowledge of role/company, how this role differs from college and previous work.
- Technical: explain projects; rate your languages; factorial in C; next greater element; fractional (n/k)-th node of a linked list (slow/fast pointers); many debugging/output questions on **pointer arithmetic and function pointers**; abstract class, interface, virtual / pure virtual; 5 min of Java OOPS. "Will test you to your limit on language and OOPS."
- HR (in person, 15-20 min): journey from school; motivating a team; handling a non-tech teammate; high-pressure situation / stress; leadership.
- Remarks: attend the PPT; know at least 2 languages (C/C++, Java, Python, JS); ask for feedback after each round; avoid LLMs and autocomplete while practising (pen/paper or notepad coding); deep OOPS; round order not consistent.

**Aashrey Jain (Selected). Order: Technical, HR, Hiring Manager**
- Technical: pick 2 languages and rate them; pick heap or linked list (chose linked list); reverse a linked list recursively and iteratively; LeetCode 92; LeetCode 73 with the space-optimised version; implement a Linked List class in Python (constructor from a list + reverse). Hackerrank, no test runs.
- HR: full academic timeline, work experience, previous compensation; critical feedback from a manager; 2 good + 1 bad thing your manager would say; why leave the job for M.Tech; why MathWorks; location; PhD plans.
- Manager: like HR but with a technical context.
- Remarks: 1 tech + 2 behavioural rounds shows they value communication. Order: Product → Customer (workflows, pain points) → Career growth. Weave in MathWorks core values. Prepare 1 technical + 1 company question. See previous OA MCQs. Official guide: "Interviewing at Mathworks as a Student".

**Anubhav Mishra (Selected). Order: Technical, HR, Managerial**
- Technical: detailed resume walkthrough; copy a 2D array from stack to heap with malloc in C; **implement the pipe operator** (POSIX on his resume); MinStack class (stack private, functions public).
- HR (very exhaustive): family/upbringing; each gap year from 10th with percentages, JEE/GATE ranks and "why?" for every decision; IIIT-H experience; multiple assignments with tight deadlines; approaching a new problem (asked for specific examples); a missed deadline and what you'd do differently; internship work; 2 qualities + **2** improvement areas from a mentor (insisted on two); team conflict in detail; why not PhD; why MathWorks / EDG, and what the PPT points actually mean; brief on EDG; location + "why"; choose areas of interest across Hyderabad / Bengaluru departments.
- Managerial: short (he was tired); overlapped with HR; challenges moving UG → internship → PG → internship; location.

**Vanshika Singh (Selected). Order: Technical, Managerial, HR**
- Technical: gRPC specifics, limitations, benefits; implement a stack class that warns before reaching its limit without modifying the main code (strategy pattern); min, max and median of 2 sorted arrays; everything about heap and why O(log n); lambda functions; why "namespace std".
- Managerial: opinions not matching a team partner; understanding of EDG (PPT); leadership role; handling both project work and customer technical queries; prioritising; why M.Tech.
- HR: conflict with a teammate; explaining something technical to a non-technical person; stress and workload; a last-minute project change.

**Aashima Mathur (listed as "Ashima Mathur") (Selected). Order: Managerial, Technical, HR**
- Managerial: completely resume-based; real-life / work situations; all projects and internships in depth; challenges moving a project to production; EDG and location (PPT); PPO discussion.
- Technical: at least 3 languages expected (Master's); easy-medium DSA (binary tree to BST without extra space); snippet output / errors on pointers and OOPs in C++, Java, C; virtual and pure virtual functions, destructors; pointer precedence; polymorphism; Java GC, method overriding; resume.
- HR: examples for everything, with cross-questioning; what friends would say (good and bad), unique qualities, strengths, weaknesses; why MathWorks, why Masters, why not PhD, why not abroad; PPO scenario, location with reasons; deadlines, multiple projects, prioritising, pressure, conflict; Git/GitHub, client-facing roles; debugging an unfamiliar platform such as MATLAB.
- Remarks: pay attention to the PPT.

**Digvijay Singh Rathore (Selected). Order: Technical, HR, Managerial**
- Technical: git-clone project (merge conflicts, scaling, better compression); OOPS and why we need it; implement a class: default-generated functions, constructor and copy constructor, overload operator=; find the error in pointer code; smart pointers and implementing them; **puzzle**: 50 red + 50 blue balls in 2 buckets, maximise P(red) when a random bucket is picked and then a random ball.
- HR: intro, education gaps; critical feedback from a friend; leading a team; 2 likely feedback points from a mentor/professor; resolving a conflict; higher studies; EDG and its importance; location.
- Managerial: like HR; strengths and weaknesses; risks taken that didn't work out; EDG.

**Sanchit Kumar (Selected). Order: Technical, Managerial, HR**
- Technical: 4 OOPS output questions, correcting errors, step-by-step explanation (static functions, virtual destructor, virtual constructor); smart pointers; POSIX and MINI-GIT projects in detail; **dup vs dup2**, fork() syntax and output, process counting (GfG fork practice Q1); Linked List Cycle and Find the Duplicate Number, brute force to optimal (constant space); approach + pseudocode only because of time.
- Managerial: intro → industry experience in detail; strengths, weaknesses, personality, how you plan the day (STAR); InterviewBit HR questions are enough; PPT questions; why MathWorks.
- HR (most exhaustive): year-wise details from 10th; why a drop year, why M.Tech; EDG; why MathWorks vs better offers; Hyderabad or Bengaluru and why; practise beforehand.
- Remarks: they grill in managerial and HR; don't lose hope; keep the conversation engaging.

**Viral Shah (Rejected). HR only described**
- HR: intro; drop year and reasons; why Masters; why MathWorks; leading a team; conflicts and resolution; EDG questions straight from the PPT (what EDG is, its domains).
- Remarks: communication-heavy; relate answers to real-life examples; have one example per question type (teamwork, leadership); revise C/C++/OOPs; attend the PPT and take notes.

### Sheet 2: Interview Experiences
**Sneha Arora (result not recorded). Order: Managerial, Technical, HR**
- Managerial: typical questions, nothing from the resume; roles available, preferred location and why; resolving a conflict with a colleague or manager; a weakness your teachers told you to improve.
- Technical: React internship and why that tech stack; databases you know; RDBMS vs NoSQL; dot product of 2 vectors (explain every line); how a computer runs code; a DNS question; rat in a maze; threads vs processes; how int and float are stored; semaphores, mutex, locking mechanisms; ACID, normalisation, transaction types, rollback/commit; 4 pillars with code, virtual methods, abstract classes, virtual pointers, polymorphism types; compile vs run time; can a constructor be overridden; need for a default constructor; can a destructor be overloaded; friend class; private / public / protected; pointers and dynamic memory; project choice.
- HR: like round 1, basic situational questions.
- Remarks: be confident; don't look desperate.

**Aryan Verma (result not recorded). Order: HR, Technical, Engineering Manager**
- HR: intro; EDG (watch the PPT); strengths and weaknesses; conflict; internship learnings and projects; work done in the Bengaluru and Hyderabad offices; location preference.
- Technical (3 interviewers): languages (C, C++, JavaScript); what OOPs is and why; classes and objects; 4 pillars; output-based OOPs (runtime polymorphism, virtual inheritance); fix code with operator overloading; 2 C output questions (associativity, precedence, pointers); void pointers; **LCA in a tree (edge cases)**; is JS single-threaded; event loop; Node.js architecture; Python.
- Engineering Manager: internship, projects, behavioural; mindset, organising, collaborating.

**Kashif Zaidi (result not recorded). Order: Technical, HR, Managerial**
- Technical: Kth smallest (quickselect); a student-marks scenario with getFirstRank / getLastRank / getNthRank.
- HR: rounds come in random order; PPT questions; situational questions.
- Managerial: projects; Docker, Kafka, distributed systems; CAP theorem, hashing basics.

---

## 5. Senior reviews (word for word, as sent)

**Vanshika Singh**
1. They made me to write the code but there was no need to compile it . Just on the doc. We can pick the language
2. If the person taking the interview has idea on the tech stack of any project, they may ask specific questions otherwise you have the liberty to choose one and talk about it.
3. Striver - that's it ( they asked me very popular stack question)
4. For the HR and managerial, they want to listen to scenarios. What problems did you face working in a team, example of a conflict with team member and how did you resolve it.for the tech round they may ask a dsa, resume based , language specific question(whatever you tell them , be it C,python).
5. For managerial and hr, Don't give generic answers . Give an example(a story) for every answer. They want to assess your communication, team work skills, time management.

**Piyush Kumar**
For the managerial round, you must have a clear idea regarding the concept of EDG. You can search online about the same and it will also be covered in the ppt session
For the HR round, be a bit cautious a lot of my peers got rejected in this round.
Prepare general questions and appear confident. Try to speak in flow. Not too fast, not too slow ,but a steady pace. Do not give the interviewer the impression that you are thinking too much in between.
And for the technical round, I would say be very thorough on OOPS concepts, specially around abstract and interface. Also about special pointers(people were asked questions related to implementation and usage). Try to get a basic idea of how basic functions such as printf are implemented.
Mid level leetcode DSA questions are generally asked. It depends on the interviewer whether pseudocode or exact code is asked.
For me personally, the interviewer didn't go into projects, just asked me to explain why,what of the project and key challenges
In manager/hr round generally a common question was key challenging lefe experience and how you dealt with it. The manager round should be very good from your side.
FYI: No particular order in which rounds happens.
Overall suggestion for non-tech round be and appear confident.
One more additional point if the interviews are online, it is necessary that you think aloud in the technical round.

**Anubhav Mishra**
full code, I they allowed me to pick the language but its upto them
everything, specially hr round
depends a lot on luck, some people were asked word search also
common hr questions, how do you handle conflicts deadline as well as interpersonal, be prepared to justify all your decisions up until now why JEE why MTech, strength, weakness etc.
just be honest, dont try to cheat or game the system, interviewers tend to know that

**Nikhil Saxena**
The following can vary based on the interviewer but the general idea as of now is
1) C++ is the preferred language. We are moving away from Java so engineers would be asked to favor it less. You need to write entire code.
2) Resume is where they would start. I suggest you don't take it farther from your resume. Maybe the engineer knows more and then it becomes an ego game. Your projects won't be checked. You will be asked to explain them in and out (not code level, high level ideas). Whatever you say will be taken as it is. So do resume well, prepare so that you can speak on a project for 20 mins
3. Strivers sheet of 450 or so questions would be enough.
4) For managerial and HR, read about the EDG program in advance. They will ask you to choose between hyd and bglr. Decide beforehand along with reasons. I said i want hyderabad because of systems. Don't give personal reasons like my hometown is nearby or my friends are here etc
5) Decide your location carefully. You cant change it later. Keep talking during all the three rounds especially during the tech and managerial. HR rounds are typical HR rounds.

**Aashrey Jain**
1. So for DSA, they want the full code. I mean, first you explain your approach to them and discuss any tradeoffs, and once they ask you to implement, you'll have to write the full function. Programming languages they usually expect either C++ or Python, but I guess they didn't have the option for Python in the OA this time, so could be majorly C++ then
2. The tech round will have DSA and CS Fundamentals, resume is usually asked in the managerial round only. A little bit technical but mostly related to design decisions and tradeoffs etc
3. Leetcode medium should be sufficient, master one DS. They did ask me for my favourite one and grilled me thoroughly in that
Tech round will be DSA, CS Fundamentals and little bit of system design. Managerial is resume and project focused. I have work ex so the manager focused heavily on that
HR me just be confident and be prepared with common scenario based questions. Read about MathWorks Core Values from their website and try integrating them into your answers and stories
For the managerial round, prepare 2-3 technical questions to ask them. Managers really like it if you can have a technical discussion with them or ask something about Matlab or MathWorks
Nope, mostly OOPS and OS. And sometimes C/C++ fundamentals as well, like pointers and struct etc

**Aashima Mathur**
1. For the coding part they'll ask you to write the pseudo code. You can pick a language of your choice
2. They check cs fundamentals as well.
3. Dsa questions are medium level only. If you've done striver's a2z sheet, that should be enough
4. Prepare situational questions and basic hr type questions like why MTech etc. Go through all possible questions since this component is valued equally as the tech part here.
5. Just make sure you explain things well, for whatever you are asked. Try to mention examples wherever possible. If you are stuck anywhere ask for hints.
For us mostly os and oops were asked

---

## 6. Candidate resume summary (the plan was tailored to this; contact details left out)
- **M.Tech CS, IIIT Hyderabad** (Jul 2025 – Jul 2027), CGPA 8.59. **B.E. IT, Shantilal Shah Engineering College, Bhavnagar** (2021–2025), CGPA 8.11. Coursework: DSA, OS, DBMS, Distributed Systems, Autonomous Software Engineering (Agentic AI).
- **MerchFlow**: event-driven microservices (5 Node.js/Express services: API Gateway, User, Catalog, Order, Notification); started from interviews with club admins and students; PostgreSQL (orders, ACID), MongoDB (catalog), Redis (cache, locks), RabbitMQ (async notifications); anti-oversell checkout (per-item Redis lock, idempotency keys, Saga that restores stock); Redis catalog cache about 40% faster with invalidation on every stock write; Factory / Builder / Command / Strategy + Observer patterns; JWT, RBAC, rate limiting; 58-item QA checklist; fixed a rate-limiter race condition (50 concurrent requests) and an access-control bug.
- **POSIX shell in C++**: fork, execvp, pipe, dup2, waitpid, sigaction; N-stage pipelines, I/O redirection, background jobs; modules ProcessExecutor, JobController (zombie reaping), BuiltinEngine, HistoryManager; signal-safe Ctrl+C (flag only), Ctrl+Z handling; 20-command bounded deque history saved to a file.
- **Kafka-inspired distributed event log in C++17 + gRPC** (team of 2, Oct 2026 – present): partitions as append-only logs; 3-broker leader–follower replication with a commit watermark; 3-node Raft for leader election; leader epochs against split brain; idempotent producers; 28 GoogleTest + 6 fault-injection tests, 0 acknowledged records lost.
- Skills: **Proficient** C++, SQL. **Familiar** JavaScript, Node.js, Express, REST, PostgreSQL, MongoDB, Redis, RabbitMQ. OOD, design patterns, LLD/HLD, microservices.
- Achievements: Dean's List 2025–26 (top 20%); PGEE 2025 AIR 114; GATE CS 2025 97.24 percentile; also qualified GATE DA 2025 and GATE CS 2024.
- No internship on the resume. No gap year.

---

## 7. Prep plan (this replaced the old Prep Plan tab)

### Rules
- Technical, Managerial and HR carry **equal weight**, **each one eliminates**, and the **order is never fixed**: no round can make up for another.
- Part 1 = non-tech in 2 days. Part 2 = tech in 7 days (~6 h/day). If time is short: do Part 1 fully and the tech Days 1–4 first.

### 0. What each round tests
| Round | Tests | Format | How to clear |
|---|---|---|---|
| Technical | OOPS (deepest), pointers/memory, OS, snippet output/debugging, class from scratch, 1–3 easy-medium DSA, resume, sometimes a puzzle | 1–1.5 h, 1–3 interviewers, Hackerrank/doc/notepad, not compiled; full code or pseudocode; starts with "name and rate your languages" | Think aloud, approach + trade-offs first, syntax-correct code, explain outputs step by step, fix errors fast |
| Managerial | You and MathWorks, resume at design level, technical-context situations, EDG/PPT, location, prioritising | Hiring / Engineering Manager; often like HR; resume-heavy | Talk end to end on each project, a story per answer, ask 2–3 technical questions |
| HR | Communication, honesty, journey and "why", teamwork, conflict, leadership, stress, deadlines, strengths/weaknesses, why MathWorks/EDG, location | 15 min to very long; heavy cross-questioning; non-technical; many peers rejected | Steady pace, no generic answers, STAR, real-world analogies, stay engaged |

### PART 1: Non-tech (HR + Managerial), 2-day schedule
| When | Round | What | How | Done when |
|---|---|---|---|---|
| Day 1, 9–11 AM | HR+Mgr | Learn MathWorks + EDG | Website (MATLAB, Simulink, customers), core values, EDG page, "Interviewing at MathWorks as a Student"; 1-page note | Explain in 60 s what MathWorks builds, who its customers are, EDG + domains, every core value |
| Day 1, 11–12 | HR+Mgr | Decide Hyderabad vs Bengaluru | Work and departments per office; 2 professional reasons | One-line answer, no personal reasons (not "I already study in Hyderabad") |
| Day 1, 1–4 PM | HR+Mgr | Build the story bank | STAR bullets for 11 stories, real events only | Each tellable in about 90 s with a concrete result |
| Day 1, 4–6 PM | HR | Journey script | "Tell me about yourself" (90 s); year-wise timeline from Class 10 with marks, GATE 2024/25, GATE DA, PGEE AIR 114, CGPAs; "why" for every decision | Can answer "why?" twice for every decision |
| Day 1, 7–9 PM | HR | Motivation answers | Why M.Tech / not PhD / not abroad / MathWorks / better offer / EDG; tie to core values | 30–60 s each, specific to MathWorks |
| Day 2, 9–11 AM | HR+Mgr | Traits | 2 strengths with proof, 2 real weaknesses with fixes, what others would say, critical feedback | 2 + 2 ready, with examples |
| Day 2, 11–1 | Mgr | Resume walk-through | 2-, 5- and 20-minute versions per project; draw the architecture | 20 min per project without notes |
| Day 2, 2–3 PM | Mgr | Technical-context situations | Project work + customer queries; prioritising; debugging an unfamiliar platform like MATLAB; explaining tech to non-tech; non-tech teammate | One answer + example each |
| Day 2, 3–3:30 | Mgr+HR | Questions for them | 2–3 technical + 1 company/EDG question | 4 written questions |
| Day 2, 4–7 PM | HR+Mgr | 2 mock interviews out loud | A friend plays HR (45 min) and the manager (30 min), asks "why?" and "example?" after every answer; record | No generic answers, no blanks, under 2 min per answer |
| Day 2, 8–9 PM | HR+Mgr | Fix and polish | Rewrite the 3 weakest answers; re-read the EDG note | 1-page cheat sheet |
| Interview day | All | PPT + between rounds | Note EDG points from the morning PPT; answer + one extra point; ask for feedback after each round; keep energy | PPT notes in hand |

### Story bank (11 stories)
1. **Conflict with a teammate**: Kafka project (team of 2), a real design or work-split disagreement. Never blame the teammate.
2. **Leadership / initiative**: MerchFlow, approaching club admins on your own; plus any real lead role.
3. **Customer focus**: MerchFlow user interviews (wrong sizes, missed slots), linked to MathWorks values (Product → Customer → Career).
4. **Hard bug / ownership**: rate-limiter race condition (50 concurrent requests), access-control bug, 58-item QA checklist.
5. **Last-minute change**: the stale-stock cache fix (invalidate on checkout and rollback).
6. **Deadlines / many tasks**: coursework + Kafka project + Dean's List; plus one real missed deadline.
7. **Learning fast**: POSIX syscalls, or Raft + gRPC; steps: docs, experiments, isolate, test.
8. **Explaining tech to non-tech**: analogies (Redis = notebook of answers already looked up; event log = numbered register; Saga = cancel the bill and return the item).
9. **Setback / risk**: the GATE journey (2024 → 2025, 97.24 percentile) or another real one.
10. **Critical feedback**: a real professor / TA / partner comment and what changed.
11. **Motivating a team / stress**: team project, exam prep.

### Must-have answers (22)
1. Tell me about yourself: B.E. IT → GATE 97.24 percentile, PGEE AIR 114 → M.Tech IIIT-H (Dean's List) → systems builder who talks to users → MathWorks EDG. Under 90 s.
2. Year-wise timeline with marks and ranks; no gap year; why GATE twice.
3. Why M.Tech: depth in systems (the shell, Raft log). Avoid "didn't get a job".
4. Why not PhD: you like building used products. Don't hint at leaving.
5. Why not abroad.
6. Why MathWorks: engineers and scientists as users, core values, customer focus, C++ preferred there.
7. Better offer? Reasons are EDG, the work and the values, not the package.
8. EDG + domains + what each PPT point means (expect cross-questions).
9. Hyderabad vs Bengaluru: 2 professional reasons; know the departments.
10. What MathWorks does in each office.
11. 2 strengths with proof. 12. 2 real weaknesses with fixes (they insist on two). 13. What friends / professors would say. 14. Family, briefly.
15. No internship: say so plainly and steer to projects. 16. PPO / commitment: consistent answer.
17. Project + customer queries together. 18. Prioritising / planning the day. 19. Debugging an unfamiliar platform (MATLAB). 20. Git/GitHub, client-facing. 21. Role vs college life.
22. Questions to ask: how MathWorks tests MATLAB across releases and platforms; how C++ is used in the product; what an EDG engineer does in the first months; how EDG works with customers. Not salary.

### PART 2: Technical, 7 days
**How to answer (10 rules):** think aloud; approach before code; full syntax-correct code without an IDE; pseudocode when told; edge cases (LCA judged on them); explain outputs step by step; fix errors fast; ask clarifying questions and for hints; answer + one extra point; don't claim what you can't defend.

**Languages to name:** C++ (proficient, about 8/10), C (not on the resume but asked a lot: malloc, structs, function pointers, Vector, factorial), JavaScript/Node (familiar, about 5–6/10: event loop, single thread, async), SQL (proficient: joins, GROUP BY, nth highest salary, indexes). Don't claim Java / Python. Master's students were expected to know 3 → C++, C, JavaScript.

| Day | Topic | Cover |
|---|---|---|
| 1 | OOPS part 1 | 4 pillars with code, access specifiers, constructors (default, parameterised, copy), operator=, rule of 3/5, default-generated functions, static, friend, this, const / immutability |
| 1 | OOPS part 2 | compile vs run-time polymorphism, overloading vs overriding, virtual / pure virtual, abstract vs interface, vtable/vptr, virtual destructor, no virtual constructor, constructor override?, destructor overload?, diamond / virtual inheritance, object slicing; 20 output snippets |
| 2 | Pointers and memory | pointer arithmetic, *p++ precedence, arrays vs pointers, double / const / void / function pointers, dangling, stack vs heap, malloc family vs new/delete, leaks, struct padding, int/float storage; ~30 pointer output questions; 2D array stack→heap |
| 2 | Modern C++ | unique/shared/weak_ptr + implement one, RAII, move basics, lambdas, namespace std, templates, STL complexities, how printf works |
| 3 | From scratch | Vector in C, Stack + MinStack, warning stack (Strategy/Observer), Linked List class, String class, smart pointer; on notepad |
| 3 | Design patterns | Factory, Builder, Command, Strategy, Observer with C++ examples + where used in MerchFlow; SOLID |
| 4 | OS | process vs thread, fork/exec, wait/waitpid, zombie/orphan, pipe, dup vs dup2, file descriptors, signals/sigaction, async-signal safety, job control, mutex/semaphore, deadlock, virtual memory/paging, compile→link→load; fork-count problems; write the pipe code in C |
| 5 | DSA: linked list, stack, arrays | see the DSA list |
| 6 | DSA: trees, heap, backtracking + favourite DS + puzzle | see the DSA list; master linked list or heap |
| 7 | Resume deep-dive; DBMS / networking / distributed; mock | ACID, normalisation, transactions, indexing, RDBMS vs NoSQL, DNS, CAP, consistent hashing, Docker; 60-min mock |
| Daily | 30-min warm-up | 4–5 snippets + "tell me about yourself" + EDG summary |

**DSA asked at MathWorks:** reverse a linked list (iterative + recursive); LC 92; middle / fractional n/k-th node; LC 141/142 cycle; LC 287 duplicate (O(1) space); next greater element; LC 155 Min Stack; popular stack questions; LC 73 Set Matrix Zeroes (O(1) space); kth smallest (quickselect); min/max/median of 2 sorted arrays; dot product of 2 vectors; factorial in C; student rank functions; LCA (LC 236/235, edge cases); binary tree → BST without extra space; heap ops + why O(log n) + LC 215; rat in a maze; word search (LC 79); BFS/DFS basics; Striver A2Z medium.

**Resume questions to expect (37):**
- *MerchFlow*: walkthrough; microservices vs monolith; PostgreSQL vs MongoDB / RDBMS vs NoSQL; transactions, commit/rollback, isolation; the Redis lock (SET NX + TTL, holder crash); idempotency keys; Saga (choreography vs orchestration, failed compensation); RabbitMQ vs Kafka, lost messages; stale cache and how "40%" was measured; rate-limiter algorithm and race fix; JWT / RBAC / the access-control bug; design patterns in code; Node.js event loop; scaling to production (Docker).
- *POSIX shell*: what happens for `ls | grep a > out.txt &`; write pipe code in C; dup vs dup2 and redirection; fork process counting; execvp and why fork first; zombie vs orphan, SIGCHLD reaping; why the Ctrl+C handler only sets a flag, Ctrl+Z; bounded-deque history; OOP module split.
- *Kafka log*: topics / partitions / offsets; replication, watermark, ISR; Raft election and partitions; split brain and leader epochs; idempotent producers; CAP placement; gRPC vs REST; testing (28 GoogleTest + 6 fault-injection); your role vs your teammate's; partition hashing and consistent hashing.
- *Other*: SQL on paper; LLD class design (student ranks / parking lot); Agentic AI coursework summary; strong GATE/PGEE ranks raise the bar on fundamentals.

---

## 8. CppNuts video watch order (69 remaining out of 82)
Already watched (13): #2, 37, 36, 1, 77, 10, 3, 56, 52 (basics), 73, 74 (basics), 82, 79.

**HIGH (37 videos, about 3 h 27 min)**
- H1 OOPS pillars (10 min): 69 Class & Object, 68 Abstraction, 70 Data Hiding, 71 Encapsulation
- H2 Polymorphism / inheritance (26 min): 33 Static & Dynamic Binding, 51 Virtual Destructor, 32 Diamond Problem, 50 Object Slicing, 44 override, 76 Function Hiding
- H3 Constructors / copy (47 min): 58 Copy ctor takes reference, 72 Shallow vs Deep Copy, 40 Return reference in copy assignment, 25 Stop copying objects, 22 Where an initializer list is a must, 29 Constructor delegation, 49 explicit, 55 Size of empty class, 54 struct vs class
- H4 Pointers (1 h 9 min): 13 void pointer, 5 Function Pointers, 4 Reference vs Pointer, 20 When reference over pointer, 75 this pointer, 19 Return array, 18 Return 2D array
- H5 friend / static / operators (30 min): 7 friend, 57 Define static member in cpp, 81 Static member space, 12 Operator overloading, 62 Pre/post increment overload
- H6 vector / namespace / printf (25 min): 6 Vector internals, 45 Vector drawbacks, 46 Why vector, 60 using namespace std bad, 31 printf/scanf return value, 8 Own atoi

**MEDIUM (20 videos, about 2 h 4 min)**
- M1 Output tricks (20 min): 24 Parameter evaluation order, 27 Comma operator, 66 Pre vs post increment speed, 23 Returning reference, 59 Pass by reference
- M2 Modern C++ (23 min): 39 Functor, 38 auto, 41 decltype, 43 RVO/NRVO, 42 Return multiple values, 35 range-for vs foreach
- M3 Casts (51 min; if short on time, 17 and 14 only): 17 dynamic_cast, 14 static_cast, 15 const_cast, 16 reinterpret_cast
- M4 Bits (17 min): 64 Set/clear/toggle bit, 67 Count set bits
- M5 Class tricks (12 min): 48 Stop inheritance, 53 Call ctor/dtor explicitly, 61 Templates in headers

**LOW (12 videos, about 46 min)**: 9 enum vs enum class, 28 Best place for enum, 26 Static in templates, 30 Code bloating, 11 Stop taking address, 21 Function before main, 34 Assign object to int, 47 Same-class check, 78 Alternative operators, 80 VLA, 63 Bingo N times, 65 Must watch.

Fit with the plan: Day 1 = H1, H2, H3, H5; Day 2 = H4, H6; Medium in the daily warm-up.
**Not covered by the playlist** (study separately): smart pointers + implementing one, abstract class vs interface, lambdas, pointer arithmetic outputs, OS (fork, dup/dup2, pipe).

---

## 9. Open items
- Open question left in the video doc: should dynamic_cast move from Medium to High?
- Personal details the candidate must fill in themselves: a real missed deadline, critical feedback, 2 weaknesses, a teammate conflict, the location choice and reasons, 10th/12th marks.
- The links in this file are private to the original owner unless shared.
- Candidate still has to practise the notepad-coding items in section 10C and the OS items.

---

## 10. Progress log and C++ gap analysis (latest, 2026-11-21)

### Status
- CppNuts playlist: candidate finished **H1 to H6** (plus the 13 watched earlier).
- Next to study (their own list): **RAII, smart pointers, struct, pointer, lambdas, functor, static, friend, namespace std.** Some are already known and only need revision or more depth.
- Notes already written in `C++ Prep Notebook/` (HTML): RAII, Smart Pointers, C++ Foundations, GFG Questions, Interview Revision, Playlist tracker, Interview Strategy. The notebook's own "Abhi baaki hai" list says these are not in the playlist: STL (map, set, unordered_map, iterators), lambdas, move semantics / rvalue references, exceptions, multithreading, const / mutable / inline / storage classes.
- A PDF of the gap analysis was made: `MathWorks C++ Gaps and Study Plan.pdf`.

### A. Asked to seniors, not yet covered (source = Question Bank / senior reviews)
| # | Topic | What was asked | Asked to | Priority | Time |
|---|---|---|---|---|---|
| 1 | Abstract class vs interface, pure virtual | Difference; abstract class constructor; pure virtual destructor needs a body; pure virtual can have a definition; C++ "interface" = only pure virtuals + virtual destructor | Piyush, Aashima, Sneha (Piyush: "very thorough... abstract and interface") | High | 45 min |
| 2 | vtable / vptr / dynamic dispatch | How a virtual call resolves; one vtable per class, one vptr per object; effect on sizeof; virtual call inside a constructor; be able to draw it | Nikhil, Sneha | High | 30 min |
| 3 | Virtual constructor (why impossible) | Output-based: static functions, virtual destructor, virtual constructor | Sanchit | High | 10 min |
| 4 | Constructor / destructor rules | Can a constructor be overridden; can a destructor be overloaded; why a default constructor is needed | Sneha, Aashima | High | 15 min |
| 5 | Compiler-generated functions + rule of 3/5 + move | The 6 special functions, `= default`, `= delete`, overloading `operator=` | Digvijay | High | 45 min |
| 6 | const / immutability | const member functions, const objects, `mutable`, `const int*` vs `int* const` vs `const int* const` | Nikhil | High | 30 min |
| 7 | Pointer precedence output drills | `*p++`, `++*p`, `*++p`, `(*p)++`, array pointer arithmetic; add videos M1 #24, #27, #66 | Aashima, Aryan, Piyush | High | 1-1.5 h |
| 8 | Access specifiers + inheritance modes | private / protected / public and the inheritance-mode table | Sneha | Medium | 15 min |
| 9 | How printf works | Variadic functions: va_list, va_start, va_arg | Piyush (tip) | Medium | 20 min |
| 10 | How int and float are stored | Two's complement, IEEE 754, why 0.1 + 0.2 != 0.3 | Sneha | Medium | 20 min |

### B. Know them, but must write them on notepad (no IDE)
| Code | Asked to |
|---|---|
| Vector in C: push_back, pop_back, erase with realloc | Nikhil |
| Copy a 2D array from stack to heap with malloc | Anubhav |
| Own unique_ptr / shared_ptr (ref count, copy ctor, operator=, dtor) | Digvijay, Sanchit |
| Class with ctor, copy ctor, operator= (self-assignment check, deep copy) | Digvijay |
| MinStack class (stack private, functions public) | Anubhav |
| Stack that warns before its limit without changing main (Strategy) | Vanshika |
| Linked list class (ctor from array, reverse) | Aashrey |

### C. Not asked directly, but do not skip
1. **OS from the resume (High):** fork process counting, dup vs dup2, pipe code in C, zombie vs orphan, mutex vs semaphore, process vs thread (Sanchit, Anubhav; POSIX shell project makes it near certain).
2. **dynamic_cast + static_cast (Medium):** videos M3 #17 and #14. Moving dynamic_cast to High is still open.
3. **new/delete vs malloc/free (Medium):** constructor calls, type safety, failure behaviour (exception vs NULL).

### Safe to skip if short on time
Java (GC, string pool, reflection; the plan says not to claim Java); exceptions, std::thread, STL internals, templates in depth; the rest of Medium and all of Low videos.

### Notes on the candidate's upcoming list
- Namespace std: already covered in H6 (#60); 5 min revision.
- Lambdas + functor: study together (lambda = compiler-made functor, captures = members); `[=]` vs `[&]`, `mutable`.
- Struct: padding and struct vs class done; left: C struct vs C++ struct, `->` vs `.` in output questions.

**Suggested order:** finish own list, then A1 to A6 (about 3 h), then A7 (pointer output drills), then B (notepad coding), then C (OS).
