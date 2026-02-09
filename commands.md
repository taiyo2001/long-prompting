# Project Research Commands

Process: Calculate evaluation metrics
1. Generate images
2. Evaluate generated images
3. Calculate final evaluation metrics(No GPU)

## 0. Default Settings

### Naming Convention

* model name SL: sequence length limit tokens (e.g. SL256: 256 tokens)
* model name S: max 256 tokens
* model name M: max 512 tokens
* model name L: max 768 tokens

* model name EM: prompt weighting(no tokens limit)(https://github.com/xhinker/sd_embed) (e.g. EM-C: with clip embedding, EM-T: with t5 embedding, EM-A: with all embeddings)

* model name SP: system prompt
* model name NP: negative prompt
* model name DP: dense prompt
* model name ST: structured prompt

### MODEL_NAME Configuration Matrix
This section defines the mapping between Baseline Models and their Experimental Variants for both image and prompt generation tasks.

#### 1. Image Generation Models (T2I)
| Vanilla | Customized |
| --- | --- |
| SD1_5 | SD1_5_EM |
| SD3_5-medium | SD3_5-medium_EM |
| SD3_5-large-turbo | SD3_5-large-turbo_SL256 |
|| SD3_5-large-turbo_SL512 |
|| SD3_5-large-turbo_SL256_EM-C |
|| SD3_5-large-turbo_SL256_EM-T |
|| SD3_5-large-turbo_SL256_EM-A |
| FLUX1-schnell | FLUX1-schnell_SL256 |
| Qwen-Image-Lightning | Qwen-Image-Lightning_SL1024 |
| ParaDiffusion | ParaDiffusion_L |

#### 2. Prompt Generation Models (LLM)

| Base Model | Optimized Variant |
| --- | --- |
| Llama3 | Llama-3_3 |
| Qwen3 | Qwen3-14B-GGUF |
| Gemini | gemini-2.5-flash-lite |
|| gemini-3-flash-preview |
|| gemini-3-pro-preview |

## 1. Image Generation

### SD 1.5
```bash
conda activate Diffusion
python data-juicer/evaluation_pipeline/image_generation_example/generate_image_sd1_5.py --model_name $MODEL_NAME
# options: icl_num, icl_prompt, np_num, np_prompt_path, count
```

### SD 3.5
```bash
conda activate Diffusion
python data-juicer/evaluation_pipeline/image_generation_example/generate_image_sd3_5.py --model_name $MODEL_NAME
# options: icl_num, icl_prompt, icl_t5_only, count
```

### FLUX.1
```bash
conda activate Diffusion
python data-juicer/evaluation_pipeline/image_generation_example/generate_image_FLUX1.py --model_name $MODEL_NAME
# options: icl_num, icl_prompt, count
```

### Qwen-Image
```bash
conda activate Diffusion
python data-juicer/evaluation_pipeline/image_generation_example/generate_image_Qwen-Image.py --model_name $MODEL_NAME

# options: st_num, st_prompt_path, count
```

### ParaDiffusion
```bash
conda activate ParaDiffusion
python data-juicer/evaluation_pipeline/image_generation_example/generate_image_ParaDiffusion.py --model_name $MODEL_NAME
# options: icl_num, icl_prompt, count
```

## 2. Evaluation
```bash
conda activate DetailMaster
python data-juicer/evaluation_pipeline/eval_process.py \
  --image_folder ./data-juicer/outputs/image/output_image_$MODEL_NAME \
  --image_info_json ./data-juicer/outputs/image_info/output_image_info_$MODEL_NAME.json \
  --output_log_dir ./data-juicer/playground/evaluation/$MODEL_NAME \
  --output_name_prefix $MODEL_NAME
```

## 3. Calculate Metrics

A GPU is not required.

```bash
# all models
python data-juicer/evaluation_pipeline/cal_eval.py
# if you want to specify the model name, use the following command:
python evaluation_pipeline/cal_eval.py \
  --eval_output_log_dir_name ./playground/evaluation/$MODEL_NAME --name_prefix $MODEL_NAME
```

## 4. Other: Results Visualization & Utils

### Display generation image
```bash
python data-juicer/playground/display_generation_image.py --model_name $MODEL_NAME --image_id $IMAGE_ID
```

### Generate evaluation comparison table
```bash
 # all models
python data-juicer/playground/eval_comparison_generator.py
# if you want to specify the model list, use the following command:
python data-juicer/playground/eval_comparison_generator.py \
--model_list $MODEL_MAME1 $MODEL_MAME2
```

### Average evaluation metrics across same models
```
python data-juicer/playground/cal_metrics_averager.py
```

### Check not evaluation models
```
python data-juicer/playground/check_model_consistency.py
```

## 5. LLM Prompt Generation

### Llama-3
```bash
conda activate LLM
python data-juicer/evaluation_pipeline/prompt_generation_example/generate_np_prompt_Llama_3.py --model_name $MODEL_NAME
# options: np_instruction_path
```

### Qwen3
```bash
conda activate LLM
python data-juicer/evaluation_pipeline/prompt_generation_example/generate_np_prompt_Qwen3.py --model_name $MODEL_NAME
# options: np_instruction_path
```

### Gemini

A GPU is not required.

```bash
conda activate LLM
python data-juicer/evaluation_pipeline/prompt_generation_example/generate_st_prompt_Gemini.py --model_name $MODEL_NAME
# options: st_num
```
