# CLAUDE.md: MathWorks EDG Interview Prep

This folder holds the context for preparing for **MathWorks campus interviews (EDG program, Hyderabad / Bengaluru)**.
Read `context.md` before answering anything. It holds the extracted data, the senior reviews, the prep plan and the video plan from the original chat.

## Git workflow (mandatory)
Remote: https://github.com/RajaiTarun/prep (branch `main`).
1. **After every `git pull` (or clone), first read `CLAUDE.md` and `context.md` in full** before doing anything else. They may have changed since your last session, and `context.md` section 10 holds the latest progress.
2. **Before every `git push`, update `CLAUDE.md` and `context.md` with the latest changes** made in the session (new files, new progress, new decisions, new gaps), then commit and push. Don't push without that update.
3. Keep `.DS_Store` and other junk out of the repo (see `.gitignore`).

## Files in this folder
- `CLAUDE.md`: this file (instructions).
- `context.md`: the full context from the original chat (source of truth). Section 10 is the running progress log; add new entries there.
- `C++ Prep Notebook/`: the candidate's own HTML study notes (open `index.html`): Interview Revision, CppNuts Playlist (with done/not-done tracking), Interview Strategy, C++ Foundations, GFG Questions, RAII, Smart Pointers, plus `notes.css`. Notes are written in Hinglish.
- `MathWorks C++ Gaps and Study Plan.pdf`: the C++ gap analysis (what seniors were asked that is not yet studied). Same content is in section 10 of `context.md`.
- `MathWorks Interview Prep.xlsx`: offline copy of the final workbook. Tabs: Overview, Prep Plan (round-wise, with Status dropdowns), Interview Reports (12), Question Bank (107), Senior Reviews (39), plus a helper "Dropdown options" tab. Read it with openpyxl or pandas when you need exact cell content.
- `CppNuts Playlist MathWorks Watch Order.pdf`: offline copy of the video watch-order doc (High / Medium / Low batches). The same content is in section 8 of `context.md`.
- `MathWorks 7-Day Plan/`: the final 7-day timetable (Sat 21 to Sat 28 Nov 2026, interview Sun 29 Nov). See section 11 of `context.md`.
  - `index.html`: open in a browser. Day picker, a daily schedule, 3 study blocks per day with tickable tasks (Core / Extra, plus an "Exam day: Core only" switch), a 9:30 PM Talk-aloud, a Resume-depth guide, and **67 per-topic quizzes (525 questions)** in a one-question-at-a-time player. Ticks and best scores are saved in that browser's localStorage only.
  - `MathWorks 7-Day Timetable.xlsx`: offline copy with tabs Week Overview (Done % formulas), Timetable Checklist (Done checkboxes), Quizzes (all 525, with Day / Block / Topic columns), Resume Depth.
  - `source/`: how to regenerate both. Edit `build.py` (days, tasks, depth table), `topics.py` (per-topic quizzes; `R(k, i)` reuses a question from `build.py` / `extra.py`), `extra.py` (older shared question bank) or `template.html` (page design). Then run `python3 source/build.py` (writes `index.html`) and `python3 source/make_xlsx.py` (needs openpyxl; writes the .xlsx). Every C/C++, fork() and Node.js output answer was compiled and run to verify it: re-verify any new or changed output question the same way.
- If the xlsx and context.md ever disagree, ask the user which one is newer.

## Who this is for
- A candidate preparing for MathWorks campus interviews: Technical, Managerial and HR rounds.
- The original plan was built around one candidate's resume (M.Tech CS, IIIT Hyderabad; projects MerchFlow, POSIX shell, Kafka-style event log). If you are a different candidate, swap in your own resume and redo the "resume questions" and "story bank" parts.

## Ground rules (from the data, do not drop these)
1. Technical, Managerial and HR carry **equal weight**, **every round eliminates**, and the **order is never fixed**. Prepare all three in parallel.
2. Non-tech (HR + Managerial) prep should fit in **2 days or less**. The tech plan is **7 days at about 6 hours a day**.
3. MathWorks tech rounds focus on **OOPS (deepest)**, **C/C++ pointers and memory**, **OS**, **output prediction and debugging**, **implementing a class from scratch** and **1-3 LeetCode easy-medium DSA**. Code is written **without an IDE and not compiled**.
4. HR and Managerial questions come **straight from the MathWorks PPT** (EDG, its domains, why MathWorks). Location (Hyderabad vs Bengaluru) needs **professional reasons**, decided in advance, and cannot be changed later.
5. Every behavioural answer needs a **real example (STAR)**. Generic answers fail.

## How to work in this folder
- Treat `context.md` as the source of truth. Don't invent interview questions: every question in it came from a real report or senior review, and its source is named.
- When adding prep material, keep the same structure: **round, then what to do, how to do it, done when, source, status**.
- Keep senior reviews word for word. Don't rewrite them.
- If the user shares a new interview report or review, add it to the right section of `context.md` and say where.
- Prefer tables for plans and checklists. Mark priority as High / Medium / Low.
- When suggesting study videos or problems, tie each one to a reported question or say it's general prep.

## Original sources (may need access from the owner)
- Interview sheet 1 (Interview_PG_2026): https://docs.google.com/spreadsheets/d/1c59kq0ThDH8v5TU2s4Tl16qI6H45JP21Ik00QjR8gb4/edit?usp=sharing (tabs: "Interview Info", "OA Info")
- Interview sheet 2 (Interview Experiences): https://docs.google.com/spreadsheets/d/1uiZ1c0rvVuZKAXz2501d5YZ6mghV8qhY86UN6ElqwOw/edit?usp=drivesdk (Sheet1; Sheet2 is empty)
- Final prep workbook (Claude Sheet, private to the owner unless shared): https://claude.ai/artifact/3fvsfyZtMUqdzjVQMYwgrh, with tabs Overview, Prep Plan, Interview Reports, Question Bank, Senior Reviews
- Video watch-order doc (Claude Doc, private unless shared): https://claude.ai/artifact/DMsDF5QpF7TqU99fnCddGg

## Re-extracting MathWorks rows from the Google Sheets
Shell access to docs.google.com may be blocked. The original extraction ran this in a browser tab that had the sheet open (same origin):

```js
// Run on a docs.google.com page of the sheet. Replace SHEET_ID and GID.
function parse(s){const rows=[];let row=[],f='',q=false;
  for(let i=0;i<s.length;i++){const c=s[i];
    if(q){if(c=='"'){if(s[i+1]=='"'){f+='"';i++}else q=false}else f+=c}
    else{if(c=='"')q=true;else if(c==','){row.push(f);f=''}
      else if(c=='\n'){row.push(f.replace(/\r$/,''));rows.push(row);row=[];f=''}
      else f+=c}}
  if(f||row.length){row.push(f);rows.push(row)}return rows}
const r = await fetch('/spreadsheets/d/SHEET_ID/export?format=csv&gid=GID');
const rows = parse(await r.text());
const mathworks = rows.filter((x,i)=> i>0 && /math\s*works/i.test(x.join(' ')));
JSON.stringify({header: rows[0], count: mathworks.length, mathworks});
```
GIDs used: sheet 1 "Interview Info" = 0, "OA Info" = 1640707635; sheet 2 "Sheet1" = 0.
