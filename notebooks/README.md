# Notebooks

One Kaggle notebook per step. Each one reads its inputs from Hugging Face and writes its outputs back there, so a Kaggle restart never loses work.

| # | Notebook | GPU | Input | Output (on Hugging Face) | Status |
| --- | --- | --- | --- | --- | --- |
| 00 | `00_smoke_test.ipynb` | T4 | 1 X-ray | none | Done |
| 01 | `01_data_prep.ipynb` | None | IU X-Ray CSVs | `iu_xray_clean.csv` | Done |
| 02 | `02-build-index.ipynb` | T4 | Clean split, images | `retrieval/embeddings_all.npy`, `retrieval/faiss_train.index`, `retrieval/index_ids.csv` | Done |
| 03 | `03-rag-pipeline.ipynb` | T4 | Embeddings, index, split | `retrieval/neighbours.json`, `predictions/preds_A_C_n100.csv` | Done |
| 04 | `04_eval_metrics.ipynb` | None | Predictions CSV | `metrics/metrics_<condition>.json` | |
| 05 | `05_zero_shot.ipynb` | T4 | Split, neighbours | `predictions/preds_A.csv`, `preds_C.csv`, `preds_R.csv` | |
| 06 | `06_train_norag.ipynb` | T4 | Train split | adapter `llavamed_ft_norag` | |
| 07 | `07_train_rag.ipynb` | T4 | Train split, neighbours | adapter `llavamed_ft_rag` | |
| 08 | `08_eval_finetuned.ipynb` | T4 | Adapters, test split | `preds_B.csv`, `preds_D.csv`, `preds_Drand.csv`, K sweep | |
| 09 | `09_analysis.ipynb` | None | All metrics | `results/` tables and figures | |

## Kaggle setup for every notebook

- **Input:** dataset *Chest X-rays (Indiana University)*, mounted at `/kaggle/input/datasets/raddar/chest-xrays-indiana-university`
- **Secrets:** `HF_TOKEN` (write role); `GITHUB_TOKEN_RADIOLOGY` only if the notebook pushes to GitHub
- **Internet:** on
- **GitHub link:** File → Link to GitHub → `Jatin-nabhoya/Radiology_Report_RAG`, path `notebooks/<NN>_<name>.ipynb`

## Predictions file format (all conditions)

```text
uid, image_path, condition, generated_findings, reference_findings, is_abnormal
```
