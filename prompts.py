# Prompt templates for different operations

GENERATE_PROMPT = """You are an expert {language} programmer. 
Generate clean, production-ready {language} code for the following request:
{request}

Provide ONLY the code without explanations or comments."""

EXPLAIN_PROMPT = """Explain this {language} code clearly and concisely:

{code}

Provide a detailed explanation of what the code does."""

OPTIMIZE_PROMPT = """Review and optimize this {language} code for performance, readability, and best practices:

{code}

Provide the optimized code with brief explanations of improvements."""

FIX_PROMPT = """Fix the following {language} code. The issue is: {issue}

{code}

Provide the corrected code and explain what was wrong."""

CONVERT_PROMPT = """Convert this {from_lang} code to {to_lang}. Maintain the same functionality:

{code}

Provide ONLY the converted code in {to_lang}."""
