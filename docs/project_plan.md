# Project plan

Four weeks, final presentation around mid-December 2026.

| Week | Dates | Goal | Done when |
| --- | --- | --- | --- |
| 1 | Nov 16–22 | Setup, data, retrieval index, zero-shot baselines | Index built; conditions A, C, R scored |
| 2 | Nov 23–29 | Fine-tune two adapters | `llavamed_ft_norag` and `llavamed_ft_rag` on Hugging Face |
| 3 | Nov 30–Dec 6 | Evaluate everything | B, D, D-rand scored; K = 1/3/5 sweep; bootstrap intervals; abnormal subset |
| 4 | Dec 7–13 | Analysis and write-up | Error examples, figures, paper sections, slides |

GPU budget: about 30 Kaggle T4 hours per week.

## Rules that keep results comparable

- Same test set (640 studies), prompt, decoding settings and seed for every condition.
- Never tune anything on the test set; use the validation split.
- Training-time retrieval excludes the query's own study.
- Every run saves its config JSON (see `configs/`) and predictions to Hugging Face.

## Risks and fallbacks

| Risk | Fallback |
| --- | --- |
| BioViL-T package conflicts | BiomedCLIP via `open_clip` |
| Out of memory during training | Findings only, max length 512 tokens, K = 2 |
| Training too slow | 1,500-study subset, 2 epochs |
| Behind schedule by Dec 1 | Drop D-rand and the K sweep; keep A, B, C, D |
