# Run configurations

One JSON file per experiment run, saved next to its predictions, so every number in the paper can be traced to an exact setup.

Name: `<condition>_<short-description>.json`, for example `C_k3_biovilt.json`.

```json
{
  "condition": "C",
  "generator": "chaoyinshe/llava-med-v1.5-mistral-7b-hf",
  "adapter": null,
  "retriever": "BioViL-T",
  "top_k": 3,
  "prompt": "radrag.prompts.build_prompt",
  "max_new_tokens": 150,
  "do_sample": false,
  "split": "test",
  "seed": 42,
  "date": "2026-11-20"
}
```
