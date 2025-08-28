# 📄 PDF Page Extractor

A simple and efficient tool to split PDF files into individual pages. This project provides two convenient ways to extract pages: a user-friendly web application built with Streamlit and a flexible command-line interface (CLI) for scripting and automation.

The tool can extract all pages from a PDF or a custom selection of pages and ranges (e.g., "1, 3, 5-8"), packaging the output neatly into a ZIP archive.

---

## ✨ Features

- **Interactive Web UI**: Easy-to-use interface powered by Streamlit for uploading and processing files.
- **Command-Line Interface**: Powerful CLI for advanced users and automation scripts.
- **Flexible Page Selection**: Extract all pages, specific pages (`1, 5, 10`), or page ranges (`2-5`).
- **ZIP Archive Output**: All extracted pages are bundled into a single, convenient ZIP file.

---

## 🚀 Setup and Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/kelvinleandro/st-pdf-splitter.git
   cd st-pdf-splitter
   ```

2. **Create a Virtual Environment:**

   ```sh
   # Create the environment
   python -m venv venv

   # Activate it
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

---

## ▶️ How to Run

You can run this tool in two ways, depending on your needs.

### Method 1: The Streamlit Web App (Easy & Visual)

This method launches a web application in your browser, which is perfect for most users.

1.  Open your terminal in the project directory.
2.  Run the following command:
    ```bash
    streamlit run app.py
    ```
3.  Your web browser will open with the application. Simply upload your PDF, enter the pages you want to extract (or leave blank for all), and click the "Split PDF" button.

### Method 2: The Command-Line Script (Advanced & Scriptable)

This method is ideal for automation or for users who prefer working in the terminal.

1.  Open your terminal in the project directory.
2.  Use the `python` command followed by the script name and the path to your PDF.

**Syntax:**

```bash
python pdf_splitter.py <path_to_pdf> [list_of_pages]
```

- `<path_to_pdf>`: (Required) The path to the PDF file you want to split.
- `[list_of_pages]`: (Optional) A string representing a Python list of pages to extract. If omitted, all pages will be extracted.

**Examples:**

- **To extract all pages:**

  ```bash
  python pdf_splitter.py doc.pdf
  ```

- **To extract specific pages (e.g., 1, 5, and 10):**

  ```bash
  # Make sure to wrap the list in quotes
  python pdf_splitter.py "My Report.pdf" "[1, 5, 10]"
  ```

The resulting ZIP file will be saved in `./output/filename_pages.zip`.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.
