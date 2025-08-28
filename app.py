import streamlit as st
import os
from pdf_splitter import extract_pdf_pages_to_zip_from_bytes
from utils import parse_page_numbers

st.set_page_config(layout="centered", page_title="PDF Page Extractor", page_icon="📄")

st.title("📄 PDF Page Extractor")
st.write(
    "Upload a PDF, choose which pages to extract, and get a ZIP file with the result."
)

if "zip_data" not in st.session_state:
    st.session_state.zip_data = None

uploaded_file = st.file_uploader(
    "1. Upload your PDF file",
    type="pdf",
    on_change=lambda: st.session_state.update(zip_data=None),
)

page_selection = st.text_input(
    "2. Enter pages to extract (e.g., '1, 3, 5-8')",
    placeholder="Leave blank to extract all pages",
)

col1, col2 = st.columns(2, vertical_alignment="center", gap="small")

with col1:
    split_button = st.button("Split PDF", type="primary")

if split_button and uploaded_file:
    with st.spinner("Splitting your PDF... Please wait."):
        pdf_bytes = uploaded_file.getvalue()
        pages_to_extract = parse_page_numbers(page_selection)

        zip_bytes = extract_pdf_pages_to_zip_from_bytes(pdf_bytes, pages_to_extract)

        if zip_bytes:
            st.session_state.zip_data = zip_bytes
            st.success(
                "PDF split successfully! Click the download button to get your file."
            )
        else:
            st.error(
                "Failed to split the PDF. Please check if the file is valid and not corrupted."
            )
            st.session_state.zip_data = None

if st.session_state.zip_data:
    original_filename = os.path.splitext(uploaded_file.name)[0]
    download_filename = f"{original_filename}_pages.zip"

    with col2:
        st.download_button(
            label="📥 Download ZIP",
            data=st.session_state.zip_data,
            file_name=download_filename,
            mime="application/zip",
        )
