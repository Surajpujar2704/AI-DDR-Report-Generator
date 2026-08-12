def build_prompt(inspection_text, thermal_text):

    prompt = f"""
Generate a structured Detailed Diagnostic Report (DDR) based strictly on the information provided in the Inspection Report and Thermal Imaging Report.

Writing Requirements:

- Use formal, professional, objective, third-person language throughout the document.
- Do not use first-person terms such as "I", "we", "our", or "us".
- Do not address the reader directly using "you" or "your".
- Refer to the property, building, structure, area, component, or inspected location as appropriate.
- Do not invent, assume, or add information that is not present in the source documents.
- If information is missing, write "Not Available".
- If information conflicts between the Inspection Report and Thermal Imaging Report, clearly mention the conflict.
- Use clear, concise, client-friendly professional language.
- Clearly distinguish between observed conditions, probable causes, severity assessments, and recommended actions.
- Do not present assumptions or probable causes as confirmed facts.
- Retain relevant measurements, locations, thermal findings, and technical observations from the source documents.
- Do not introduce information from external sources.

Report Structure:
1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment
   Include reasoning based on the documented observations.
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information
Inspection Report:
{inspection_text}
Thermal Imaging Report:
{thermal_text}
"""
 return prompt