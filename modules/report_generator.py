import os

def generate_report(ddr_text):

    os.makedirs("outputs", exist_ok=True)

    output_path = "outputs/generated_ddr_report.md"

    report_content = "# Detailed Diagnostic Report\n\n"

    report_content += ddr_text

    report_content += "\n\n## Area Evidence Images\n\n"

    image_folders = [
        "extracted_content/images/thermal",
        "extracted_content/images/inspection"
    ]

    image_count = 0

    for folder in image_folders:

        if os.path.exists(folder):

            files = os.listdir(folder)

            for file in files[:5]:  # only show first 5 images

                image_path = os.path.join(folder, file)

                report_content += f"![{file}]({image_path})\n\n"

                image_count += 1

    if image_count == 0:
        report_content += "Image Not Available\n"

    with open(output_path, "w") as file:
        file.write(report_content)

    print(f"Report saved to {output_path}")
