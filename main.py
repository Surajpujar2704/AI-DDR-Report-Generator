from modules.pdf_text_extractor import extract_text
from modules.image_extractor import extract_images
from modules.ai_processor import generate_ddr
from modules.report_generator import generate_report

inspection_pdf = "data/input/inspection_report.pdf"
thermal_pdf = "data/input/thermal_report.pdf"

print("Extracting inspection text...")
inspection_text = extract_text(inspection_pdf)

print("Extracting thermal text...")
thermal_text = extract_text(thermal_pdf)

print("Extracting images...")

inspection_images = extract_images(
    inspection_pdf,
    "extracted_content/images/inspection"
)

thermal_images = extract_images(
    thermal_pdf,
    "extracted_content/images/thermal"
)

print("Generating DDR report using AI...")

ddr_text = generate_ddr(
    inspection_text,
    thermal_text
)

print("Creating report file...")

generate_report(ddr_text)

print("DDR Report Generated Successfully!")
