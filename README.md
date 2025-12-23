# DocuMint

DocuMint is a lightweight Python utility for **bulk-generating personalized PDF documents** (such as certificates, tickets, or passes) by overlaying text onto an existing PDF template using data from a CSV file.

The tool is designed to be **simple, fast, and dependency‑minimal**, relying only on standard fonts and precise coordinate-based placement — ideal for events, academic certificates, workshops, and conference passes.

---

## ✨ Features

* 📄 Works with any existing PDF template
* 📊 Reads **only the first column** of a CSV file (clean and predictable)
* 📍 Precise text placement using PDF coordinates (CLI-based input)
* 🔤 Uses standard built-in PDF fonts (no font embedding issues)
* 📦 Generates one PDF per row (bulk-friendly)
* 🧾 Clean output naming with safe filenames

---

## 📂 Project Structure

```text
DocuMint/
├── main.py           # Core script
├── IEEE.pdf          # Input PDF template (example)
├── data.csv          # CSV containing names (first column)
├── gen/              # Auto-generated output PDFs
└── README.md
```

---

## ⚙️ Requirements

* Python **3.8+**
* reportlab
* PyPDF2

Install dependencies:

```bash
pip install reportlab PyPDF2
```

---

## 🚀 Usage

1. **Prepare your PDF template**
   Place your base PDF (e.g. `IEEE.pdf`) in the project directory.

2. **Prepare the CSV file**
   Only the **first column** is read. Example:

   ```csv
   Alice Johnson
   Bob Smith
   Charlie Brown
   ```

3. **Run the script**

   ```bash
   python main.py
   ```

4. **Enter text box coordinates when prompted**

   Coordinates are in **PDF units (points)**:

   ```text
   x: 200
   y: 300
   width: 250
   height: 40
   ```

5. **Output**
   Generated PDFs will appear in the `gen/` directory, one per CSV row.

---

## 📐 Understanding Coordinates

* Origin `(0,0)` is at the **bottom-left** of the PDF
* Units are **points** (1 point = 1/72 inch)
* Text is automatically **centered** within the provided box

---

## 🛠 Customization

* Change font size by editing:

  ```python
  c.setFont("Helvetica", 18)
  ```
* Change output directory via the `output_dir` parameter
* Extend logic to support multiple fields if needed

---

## 🤝 Contributing

Contributions are welcome and appreciated! 🎉

### How to Contribute

1. **Fork the repository**
2. **Create a new branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**

   * Follow clean, readable Python code
   * Keep the tool minimal and dependency-light
4. **Test thoroughly**
5. **Commit and push**

   ```bash
   git commit -m "Add: meaningful description"
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request**

   * Clearly describe what you changed and why

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

**DocuMint** — *Precise. Minimal. Reliable PDF personalization.*
