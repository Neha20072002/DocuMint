import os
import csv
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter


def generate_ticket(input_pdf, name, name_box, output_dir="gen"):
    """Generate a single PDF with name placed at fixed coordinates."""

    os.makedirs(output_dir, exist_ok=True)

    original = PdfReader(input_pdf)
    first_page = original.pages[0]
    page_width = float(first_page.mediabox.width)
    page_height = float(first_page.mediabox.height)

    overlay_path = "overlay.pdf"

    c = canvas.Canvas(overlay_path, pagesize=(page_width, page_height))
    c.setFont("Helvetica", 18)  # standard built-in font

    x, y, w, h = name_box
    text = str(name).upper()

    text_width = c.stringWidth(text, "Helvetica", 18)
    text_x = x + (w - text_width) / 2
    text_y = y + (h - 18) / 2

    c.drawString(text_x, text_y, text)
    c.save()

    overlay = PdfReader(overlay_path)
    writer = PdfWriter()

    for i in range(len(original.pages)):
        page = original.pages[i]
        if i < len(overlay.pages):
            page.merge_page(overlay.pages[i])
        writer.add_page(page)

    safe_name = text.replace(" ", "_") or "EMPTY_NAME"
    output_pdf = os.path.join(output_dir, f"{safe_name}.pdf")

    with open(output_pdf, "wb") as f:
        writer.write(f)


def process_csv(input_pdf, csv_file, name_box):
    """Reads ONLY the first column of the CSV."""

    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    print(f"Total rows: {len(rows)}")

    for row in rows:
        name = row[0] if row else ""
        generate_ticket(input_pdf, name, name_box)


if __name__ == "__main__":
    input_pdf = "IEEE.pdf"
    csv_file = "data.csv"

    print("Enter name box coordinates (PDF units):")
    x = int(input("x: "))
    y = int(input("y: "))
    w = int(input("width: "))
    h = int(input("height: "))

    name_box = (x, y, w, h)

    process_csv(input_pdf, csv_file, name_box)

    print("All PDFs generated successfully.")
