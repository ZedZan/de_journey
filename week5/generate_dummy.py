import csv
from pathlib import Path

output_path = Path("week5/data/sales_dummy.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

rows = [
    {"date": "2026-04-01", "product": "Widget A", "quantity": 10, "revenue": 250.0},
    {"date": "2026-04-01", "product": "Widget B", "quantity": 5, "revenue": 125.0},
    {"date": "2026-04-02", "product": "Widget A", "quantity": 8, "revenue": 200.0},
    {"date": "2026-04-02", "product": "Widget C", "quantity": 3, "revenue": 90.0},
    {"date": "2026-04-03", "product": "Widget B", "quantity": 12, "revenue": 300.0},
]

with open(output_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Created {output_path}")