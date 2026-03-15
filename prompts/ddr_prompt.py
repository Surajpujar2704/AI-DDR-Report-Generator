def build_prompt(inspection_text, thermal_text):

    prompt = f"""
You are an expert building inspection analyst.

You are given two documents:

1. Inspection Report
2. Thermal Imaging Report

Your task is to generate a structured Detailed Diagnostic Report (DDR).

Important Rules:
- Do NOT invent information
- If information is missing write "Not Available"
- If information conflicts mention the conflict
- Use simple client friendly language

Report Structure:

1 Property Issue Summary
2 Area-wise Observations
3 Probable Root Cause
4 Severity Assessment (with reasoning)
5 Recommended Actions
6 Additional Notes
7 Missing or Unclear Information

Inspection Data:
{inspection_text}

Thermal Data:
{thermal_text}
"""
    return prompt
    return prompt
