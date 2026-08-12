## Workflow
The application follows a simple document-processing workflow.

### 1. Input Reports
The system accepts two PDF documents:
- Inspection Report
- Thermal Imaging Report

### 2. Data Extraction
Text is extracted from both PDF reports. Embedded images are also extracted and stored separately for evidence.

### 3. DDR Generation
The extracted inspection and thermal information is processed to prepare the Detailed Diagnostic Report (DDR).

### 4. Report Generation
The generated DDR content is combined with the available evidence images and saved as a Markdown report.

### 5. Final Output
The completed report is generated at:

`outputs/generated_ddr_report.md`