# Experiment log

Newest first. One entry per run or decision.

| Date | Notebook | What was done | Result | Notes |
| --- | --- | --- | --- | --- |
| 2026-11-16 | 01 | Data prep: frontal only, one image per study, Findings ≥ 3 words, `XXXX` removed, stratified 70/10/20 split, seed 42 | 3,199 studies; 2,239 / 320 / 640; 63.6% abnormal | Saved `iu_xray_clean.csv` to HF dataset repo |
| 2026-11-15 | 00 | Smoke test with `chaoyinshe/llava-med-v1.5-mistral-7b-hf`, 4-bit NF4, fp16 | Loads; 4.3 GB GPU; 13.5 s per report | Zero-shot output hallucinates findings and repeats templates (expected baseline behaviour) |
| 2026-11-15 | 00 | Tried original `microsoft/llava-med-v1.5-mistral-7b` with the LLaVA-Med repo | Failed | Pinned `transformers==4.36.2` conflicts with Kaggle's accelerate 1.15 and Python 3.13; switched to the HF-native conversion |
