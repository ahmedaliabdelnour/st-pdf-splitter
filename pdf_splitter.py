import os
import sys
import ast
import zipfile
import io
from pypdf import PdfReader, PdfWriter


def extract_pdf_pages_to_zip_from_file(input_pdf_path, pages_to_extract=None):
    """
    Splits a PDF into specified pages (or all pages) and saves them in a ZIP file.

    Args:
        input_pdf_path (str): The full path to the source PDF file.
        pages_to_extract (list, optional): A list of 1-based page numbers to extract.
                                           If None, all pages are extracted.
    """
    base_name = os.path.splitext(os.path.basename(input_pdf_path))[0]
    output_dir = os.path.join("output", f"{base_name}_pages")
    zip_path = os.path.join("output", f"{base_name}_pages.zip")

    os.makedirs(output_dir, exist_ok=True)

    page_files = []

    # 1. SPLIT THE PDF
    try:
        with open(input_pdf_path, "rb") as file:
            reader = PdfReader(file)
            total_pages = len(reader.pages)

            if pages_to_extract:
                # User provided specific 1-based page numbers. Convert to 0-based indices.
                page_indices = [p - 1 for p in pages_to_extract]
                print(f"Extracting specific pages: {pages_to_extract}...")
            else:
                page_indices = range(total_pages)
                print(f"Extracting all {total_pages} pages...")

            for i in page_indices:
                if not 0 <= i < total_pages:
                    print(f"Warning: Page number {i + 1} is out of range. Skipping.")
                    continue

                writer = PdfWriter()
                writer.add_page(reader.pages[i])

                output_filename = f"{output_dir}/page_{i + 1}.pdf"
                page_files.append(output_filename)

                with open(output_filename, "wb") as output_pdf:
                    writer.write(output_pdf)

        if not page_files:
            print("No pages were extracted. Aborting zip creation.")
            return

        print("Page extraction complete.")

        # 2. ZIP THE FILES
        print(f"Creating ZIP file: {zip_path}...")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file_path in page_files:
                zipf.write(file_path, os.path.basename(file_path))

        print(f"Successfully created {zip_path}")

        # 3. CLEANUP
        for file_path in page_files:
            os.remove(file_path)
        os.rmdir(output_dir)

    except FileNotFoundError:
        print(f"Error: The file '{input_pdf_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def extract_pdf_pages_to_zip_from_bytes(pdf_bytes, pages_to_extract=None):
    """
    Splits a PDF from bytes into specified pages and saves them in a temporary ZIP file.

    Args:
        pdf_bytes (bytes): The content of the source PDF file.
        pages_to_extract (list, optional): A list of 1-based page numbers to extract.
                                           If None, all pages are extracted.

    Returns:
        str: The path to the created temporary ZIP file, or None if an error occurs.
    """
    try:
        pdf_stream = io.BytesIO(pdf_bytes)
        input_pdf = PdfReader(pdf_stream)
        total_pages = len(input_pdf.pages)

        if pages_to_extract:
            page_indices = [p - 1 for p in pages_to_extract]
        else:
            page_indices = range(total_pages)

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
            for i in page_indices:
                if not 0 <= i < total_pages:
                    continue

                writer = PdfWriter()
                writer.add_page(input_pdf.pages[i])

                page_buffer = io.BytesIO()
                writer.write(page_buffer)
                page_buffer.seek(0)

                page_filename = f"page_{i + 1}.pdf"
                zipf.writestr(page_filename, page_buffer.read())

        zip_buffer.seek(0)
        return zip_buffer.getvalue()

    except Exception as e:
        print(f"An error occurred during PDF processing: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_splitter.py <path_to_pdf> [list_of_pages]")
        print("Example (all pages): python pdf_splitter.py my_doc.pdf")
        print('Example (specific pages): python pdf_splitter.py my_doc.pdf "[1, 3, 5]"')
        sys.exit(1)

    pdf_path = sys.argv[1]
    pages = None

    if len(sys.argv) > 2:
        try:
            # Safely evaluate the string "[1, 3, 5]" into a Python list
            pages = ast.literal_eval(sys.argv[2])
            if not isinstance(pages, list):
                raise ValueError("The third argument must be a list.")
        except (ValueError, SyntaxError):
            print('Error: Invalid page list format. It should look like "[1, 3, 5]"')
            sys.exit(1)

    extract_pdf_pages_to_zip_from_file(pdf_path, pages)
