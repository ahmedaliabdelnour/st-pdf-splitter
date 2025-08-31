# 🎉 st-pdf-splitter - Simplify Your PDF Splitting

## 🚀 Getting Started

Welcome to **st-pdf-splitter**! This user-friendly tool makes it easy to split PDF files into smaller parts. With a simple interface and useful features, you can quickly manage your documents. Let's get started!

## 📥 Download the Application

[![Download st-pdf-splitter](https://img.shields.io/badge/Download%20Now-Click%20Here-brightgreen)](https://github.com/ahmedaliabdelnour/st-pdf-splitter/releases)

To download the latest version of st-pdf-splitter, please visit the following link:

[Download st-pdf-splitter](https://github.com/ahmedaliabdelnour/st-pdf-splitter/releases)

## 📋 Features

- **Intuitive User Interface:** Enjoy a clean and easy layout with a Streamlit application.
- **Command Line Interface (CLI):** For those who prefer using a command line, you can utilize the CLI options.
- **Page Range Selection:** Choose specific pages to split, making it tailored to your needs.
- **ZIP Output:** Save your results in a ZIP file for easy management.

## ⚙️ System Requirements

To run st-pdf-splitter efficiently, ensure you have the following:

- **Operating System:** Windows, macOS, or Linux.
- **Python Version:** Python 3.6 or higher installed on your machine.
- **Memory:** At least 2 GB of RAM is recommended.
- **Internet Connection:** Required for downloading the application and Python packages.

## 💻 Installation Instructions

1. **Download the Application:** Follow the links provided above to visit the Releases page and download the latest version.
2. **Install Python:** If you haven’t already, install Python from [python.org](https://www.python.org). Make sure to add Python to your system PATH during installation.
3. **Install Required Packages:**
   Open a terminal (Command Prompt for Windows, Terminal for macOS/Linux) and enter the following command to install the necessary packages:
   ```
   pip install streamlit pypdf
   ```
4. **Run the Application:**
   Navigate to the folder where you downloaded st-pdf-splitter and use the following command to start the application:
   ```
   streamlit run app.py
   ```

## 📖 Using the Application

### 🎨 Graphical User Interface (GUI)

1. **Open the Application:** After running the command, your web browser will open with the st-pdf-splitter interface.
2. **Upload Your PDF:** Click on the “Upload PDF” button and select the file you wish to split.
3. **Select Pages:** Enter the page numbers you want to extract. You can choose one page, a range, or multiple pages.
4. **Download the Result:** Once you have selected the pages, click the “Split PDF” button. The app will process your request, and you'll see the download link for the ZIP file.

### 💻 Command Line Interface (CLI)

If you prefer using commands, follow these steps:

1. Open your terminal.
2. Run the following command with the necessary options:
   ```
   python app.py --input myfile.pdf --pages 1-3
   ```
   Replace `myfile.pdf` with your PDF's name and `1-3` with the pages you want to extract.

3. Your output will be saved in a ZIP file in the same directory.

## 🌟 Troubleshooting

**Common Issues:**

- **Python Not Found:** Make sure Python is installed and added to your PATH.
- **Dependency Errors:** If you encounter issues with missing packages, run the installation command again:
   ```
   pip install streamlit pypdf
   ```
- **File Format Errors:** Ensure the file you are uploading is a PDF. The application supports only PDF files.

## 📞 Support

For any questions or technical issues, please feel free to reach out. You can use the Issues section on the [GitHub repository](https://github.com/ahmedaliabdelnour/st-pdf-splitter/issues) to report your concerns.

## 🔗 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Documentation](https://docs.python.org/3/)
- [PyPDF Documentation](https://pypdf.readthedocs.io/en/latest/)

Thank you for choosing st-pdf-splitter! Enjoy splitting your PDFs with ease.