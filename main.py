import os

# One-line entry for "Your AI Therapist's Diagnosis" (make.fun).
# Clinical-note frame, deadpan; the turn lands in the final words:
# stable -> terminal reliance -> the chatbot auto-renewed his $149 plan.
LINE = "Clinical note: patient is stable. Diagnosis: terminal reliance on a chatbot that just auto-renewed his $149 annual plan."

# Gate self-check: the scorer requires 1-200 chars of non-whitespace UTF-8.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the entry gate"
assert "\n" not in LINE, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(f"entry written: {len(LINE)} chars, single line")
