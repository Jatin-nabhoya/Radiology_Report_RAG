"""Paths, model names and fixed settings used across all notebooks."""

SEED = 42

# Kaggle input (dataset "Chest X-rays (Indiana University)")
DATA_DIR = "/kaggle/input/datasets/raddar/chest-xrays-indiana-university"
IMG_DIR = f"{DATA_DIR}/images/images_normalized"
REPORTS_CSV = f"{DATA_DIR}/indiana_reports.csv"
PROJECTIONS_CSV = f"{DATA_DIR}/indiana_projections.csv"
WORK_DIR = "/kaggle/working"

# Hugging Face repos
HF_DATA_REPO = "jatinnabhoya/Radiology_Report_RAG-data"   # dataset repo, private
HF_MODEL_REPO = "jatinnabhoya/Radiology_Report_RAG"       # model repo for adapters, private
CLEAN_CSV = "iu_xray_clean.csv"

# Models
GENERATOR = "chaoyinshe/llava-med-v1.5-mistral-7b-hf"   # HF-native LLaVA-Med v1.5

# Retrieval
TOP_K = 3
NEIGHBOURS_SAVED = 5

# Generation (same for every condition)
MAX_NEW_TOKENS = 150
GEN_KWARGS = dict(max_new_tokens=MAX_NEW_TOKENS, do_sample=False)

# QLoRA (both adapters use identical settings)
LORA = dict(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
)
TRAIN = dict(
    learning_rate=2e-4,
    num_train_epochs=3,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=16,
    lr_scheduler_type="cosine",
    fp16=True,
    gradient_checkpointing=True,
)
