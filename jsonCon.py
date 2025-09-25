import pandas as pd

# ระบุ path ของไฟล์ (อยู่ในโฟลเดอร์ PTT EXCEL)
file_path = "PTT EXCEL/PTT FS.txt"

# อ่านไฟล์ (กรณีคั่นด้วย Tab)
df = pd.read_csv(file_path, sep="\t")

# แปลงเป็น JSON
json_str = df.to_json(orient="records", force_ascii=False, indent=2)

# บันทึกไฟล์ JSON ออกไปในโฟลเดอร์เดียวกัน
with open("PTT EXCEL/PTT_FS.json", "w", encoding="utf-8") as f:
    f.write(json_str)

print("✅ เสร็จแล้ว: PTT EXCEL/PTT_FS.json")
