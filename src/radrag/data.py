"""Load the clean IU X-Ray split saved by notebook 01."""

import pandas as pd

from .config import CLEAN_CSV, HF_DATA_REPO


def load_split(token, split=None):
    """Download iu_xray_clean.csv from the Hugging Face dataset repo.

    split: "train", "val", "test" or None for all rows.
    Columns: uid, filename, image_path, findings, is_abnormal, split
    """
    from huggingface_hub import hf_hub_download

    path = hf_hub_download(HF_DATA_REPO, CLEAN_CSV, repo_type="dataset", token=token)
    df = pd.read_csv(path)
    return df if split is None else df[df["split"] == split].reset_index(drop=True)
