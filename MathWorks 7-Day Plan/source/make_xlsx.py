"""Rebuild the offline workbook from ../index.html: python3 make_xlsx.py"""
import json, re, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
HERE = os.path.dirname(os.path.abspath(__file__))
h = open(os.path.join(HERE, "..", "index.html"), encoding="utf-8").read()
d = json.loads(re.search(r"const DATA = (.*?);\nconst store", h, re.S).group(1).replace("<\\/", "</"))
HDR = PatternFill("solid", fgColor="F3F3F3"); WRAP = Alignment(wrap_text=True, vertical="top")
def finish(ws, widths):
    for c in ws[1]: c.fill = HDR; c.font = Font(bold=True)
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP
    for i, w in enumerate(widths): ws.column_dimensions[chr(65 + i)].width = w
    ws.freeze_panes = "A2"
wb = Workbook()
ws = wb.active; ws.title = "Week Overview"
ws.append(["Day", "Date", "Type", "Theme", "Why this day", "Blocks", "9:30 PM Talk-aloud", "Done %"])
for i, x in enumerate(d["days"], 2):
    ws.append([f"Day {x['n']}", x["date"], x["kind"], x["title"], x["why"], " | ".join(f"{b['time']}: {b['name']}" for b in x["blocks"]), x["talk"],
               f"=COUNTIFS('Timetable Checklist'!A:A,A{i},'Timetable Checklist'!H:H,TRUE)/COUNTIF('Timetable Checklist'!A:A,A{i})"])
    ws.cell(row=i, column=8).number_format = "0%"
finish(ws, [8, 12, 10, 26, 45, 60, 45, 9])
ws = wb.create_sheet("Timetable Checklist")
ws.append(["Day", "Date", "Theme", "Block", "Time", "Task", "Exam-day?", "Done"])
for x in d["days"]:
    for bi, b in enumerate(x["blocks"]):
        blk = "Block " + "ABC"[bi] + ": " + b["name"]
        for it in b["items"]:
            q = f"  [Quiz: {len(d['quiz'][it['quiz']])} Qs]" if it.get("quiz") else ""
            ws.append([f"Day {x['n']}", x["date"], x["title"], blk, b["time"], ("★ " if it["c"] else "") + it["x"] + (f" [{it['tag']}]" if it.get("tag") else "") + q, "Core (★)" if it["c"] else "Extra", False])
        if b.get("game"): ws.append([f"Day {x['n']}", x["date"], x["title"], blk, b["time"], "Game: " + b["game"], "Extra", False])
    ws.append([f"Day {x['n']}", x["date"], x["title"], "Night: Talk-aloud", "9:30 - 9:55 PM", "★ " + x["talk"] + " Record it and listen once. Never skip, even on exam days.", "Core (★)", False])
finish(ws, [7, 11, 22, 30, 15, 70, 11, 8])
ws = wb.create_sheet("Quizzes")
ws.append(["Day", "Block", "Topic", "#", "Type", "Question", "Code", "Options / follow-ups", "Answer (cover it first!)", "Why", "Got it right"])
names = {"mcq": "MCQ", "out": "Predict output", "bug": "Find the bug", "chain": "Follow-up chain"}
for x in d["days"]:
    for bi, b in enumerate(x["blocks"]):
        for it in b["items"]:
            k = it.get("quiz")
            if not k: continue
            for i, q in enumerate(d["quiz"][k], 1):
                if q["t"] == "mcq":
                    opts = "\n".join(f"{chr(65+j)}. {o}" for j, o in enumerate(q["opts"])); ans = f"{chr(65+q['ans'])}. {q['opts'][q['ans']]}"; why = q["why"]
                elif q["t"] == "chain":
                    opts = "\n".join(f"{j}. {s['q']}" for j, s in enumerate(q["steps"], 1)); ans = "\n".join(f"{j}. {s['a']}" for j, s in enumerate(q["steps"], 1)); why = "Answer each follow-up out loud before reading the model answer."
                else:
                    opts = ""; ans = ("Bug: " if q["t"] == "bug" else "Output: ") + q["ans"]; why = q["why"]
                row = [f"Day {x['n']}", "Block " + "ABC"[bi] + ": " + b["name"], d["titles"][k], i, names[q["t"]], q["q"], q.get("code") or "", opts, ans, why, False]
                ws.append(row)
                for c in ws[ws.max_row]:
                    if isinstance(c.value, str) and c.value.startswith("="): c.data_type = "s"
finish(ws, [7, 26, 26, 4, 14, 45, 40, 45, 40, 50, 10])
ws = wb.create_sheet("Resume Depth")
ws.append(["Item", "Depth", "Priority", "When", "What exactly"])
for r in d["depth"]: ws.append(r)
finish(ws, [28, 20, 10, 12, 80])
ws.append([]); ws.append(["L1 = what it is and why you used it, in 30 sec", "L2 = how it works + trade-offs, draw it", "L3 = write the code and survive 3 follow-ups"])
out = os.path.join(HERE, "..", "MathWorks 7-Day Timetable.xlsx"); wb.save(out); print("saved", out)
