# Radiology_Report_RAG

Retrieval-augmented radiology report generation on IU X-Ray, with BioViL-T + FAISS retrieval and LLaVA-Med (QLoRA).

Part 2 of an MS Data Science capstone (University of New Haven, Fall 2026). Team: Jatin Nabhoya, Emiliano Vega.

## Research question

Does showing a vision-language model the reports of the most similar past chest X-rays make its generated report more clinically accurate, and does that gain hold after domain fine-tuning?

## Method

1. **Index (offline):** embed every training X-ray with BioViL-T and store the vectors in a FAISS inner-product index (cosine on L2-normalised vectors).
2. **Retrieve:** for a new X-ray, find the top-K most similar training X-rays (K = 3 by default), excluding duplicate report texts.
3. **Generate:** LLaVA-Med v1.5 (Mistral-7B, 4-bit) reads the X-ray plus the K retrieved Findings and writes the Findings section.
4. **Score:** compare with the ground-truth Findings.

## Experimental conditions

| Condition | Fine-tuned | Context at inference | Tests |
| --- | --- | --- | --- |
| A | No | None | Zero-shot floor |
| B | Yes (no-RAG adapter) | None | Effect of fine-tuning |
| C | No | Top-K retrieved reports | Effect of RAG alone |
| D | Yes (RAG adapter) | Top-K retrieved reports | Main result: D − B |
| R | — | Top-1 retrieved report copied | Is generation better than copying? |
| D-rand | Yes (RAG adapter) | K random training reports | Does relevance matter? |

**Metrics:** RadGraph F1 (primary), CheXbert F1, BLEU-4, ROUGE-L, BERTScore. Reported on the full test set and on the abnormal-only subset.

## Data

IU X-Ray (Open-i, Indiana University), via the Kaggle dataset *Chest X-rays (Indiana University)* (`raddar/chest-xrays-indiana-university`).

After cleaning (one frontal image per study, non-empty Findings of at least 3 words, `XXXX` de-identification tokens removed):

| Split | Studies | Abnormal share |
| --- | --- | --- |
| train | 2,239 | 63.6% |
| val | 320 | 63.8% |
| test | 640 | 63.6% |
| **total** | **3,199** | |

Splits are stratified by `is_abnormal` with seed 42. Each `uid` is one patient study, so no patient appears in two splits. "Abnormal" means any non-normal entry in the dataset's `Problems` column, including minor incidental findings.

## Models

| Role | Model | Notes |
| --- | --- | --- |
| Generator | [`chaoyinshe/llava-med-v1.5-mistral-7b-hf`](https://huggingface.co/chaoyinshe/llava-med-v1.5-mistral-7b-hf) | Hugging Face-native conversion of [`microsoft/llava-med-v1.5-mistral-7b`](https://huggingface.co/microsoft/llava-med-v1.5-mistral-7b). Loads with current `transformers`; the original repo's pinned dependencies do not install on Kaggle's Python 3.13. Loaded in 4-bit NF4, fp16 compute (T4 has no bf16). |
| Retriever | BioViL-T image encoder (`hi-ml-multimodal`) | Fallback: BiomedCLIP via `open_clip`. Frozen. |

Prompt format (LLaVA-Med v1.5 / Mistral): `[INST] <image>\n{instruction} [/INST]`

## Repository layout

```text
Radiology_Report_RAG/
├── notebooks/        Kaggle notebooks, one per step (see notebooks/README.md)
├── src/radrag/       shared code: config, prompts, data loading
├── configs/          run configurations (one JSON per experiment)
├── results/          small result files: metrics JSON, tables, figures
├── docs/             project plan and experiment log
├── requirements.txt
└── LICENSE
```

Large files (images, embeddings, FAISS index, adapters, predictions) are **not** stored in git. They live on Hugging Face:

| What | Where |
| --- | --- |
| Clean split, retrieval files, predictions | Dataset repo `jatinnabhoya/Radiology_Report_RAG-data` (private) |
| LoRA adapters | Model repo `jatinnabhoya/Radiology_Report_RAG` (private) |

## Workflow

GitHub for code, Hugging Face for data and checkpoints, Kaggle (T4 GPU) for compute. Each Kaggle notebook is linked to its file in `notebooks/`, so **Save Version** in Kaggle commits it here.

## Progress

| # | Step | Status |
| --- | --- | --- |
| 00 | Smoke test: LLaVA-Med loads in 4-bit on a T4 and generates | Done (4.3 GB GPU, 13.5 s per report) |
| 01 | Data prep and split | Done (3,199 studies) |
| 02 | BioViL-T embeddings + FAISS index | Next |
| 03 | Neighbour lists | |
| 04 | Evaluation script | |
| 05 | Zero-shot runs: A, C, R | |
| 06 | Fine-tune no-RAG adapter | |
| 07 | Fine-tune RAG adapter | |
| 08 | Fine-tuned runs: B, D, D-rand, K sweep | |
| 09 | Analysis, bootstrap intervals, figures | |

## Disclaimer

Research prototype for a course project. Not for clinical use.
