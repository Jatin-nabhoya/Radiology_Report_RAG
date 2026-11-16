"""Prompt templates. Every condition uses these, so results are comparable."""

INSTRUCTION = (
    "You are an expert radiologist. Write the FINDINGS section of a radiology report "
    "for this frontal chest X-ray. Use short, factual sentences in standard report language. "
    "Comment on the heart size, mediastinum, lungs, pleura and bones. "
    "State normal findings as normal. Do not explain terms or give advice."
)

RAG_HEADER = "Reference reports from similar chest X-rays:"
RAG_CAUTION = "The references may not match this patient. Use the image as the main evidence."


def build_prompt(references=None):
    """Return a LLaVA-Med v1.5 (Mistral) prompt.

    references: list of Findings strings from retrieved X-rays, or None for no-RAG conditions.
    """
    if references:
        refs = "\n".join(f"[{i}] {r}" for i, r in enumerate(references, 1))
        body = f"{RAG_HEADER}\n{refs}\n{RAG_CAUTION}\n{INSTRUCTION}"
    else:
        body = INSTRUCTION
    return f"[INST] <image>\n{body} [/INST]"
