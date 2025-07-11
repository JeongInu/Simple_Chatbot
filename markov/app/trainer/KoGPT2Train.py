from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel, DataCollatorForLanguageModeling, TrainingArguments, Trainer
import torch
from datasets import Dataset, load_dataset

MODEL_NAME = 'skt/kogpt2-base-v2'

def load_tokenizer():
    print(MODEL_NAME)
    return PreTrainedTokenizerFast.from_pretrained(MODEL_NAME, bos_token='▁', eos_token='</s>', pad_token='<pad>')

def load_model(tokenizer):
    model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
    model.resize_token_embeddings(len(tokenizer))
    return model

def tokenize_function(example, tokenizer):
    return tokenizer(example["Utterance"], truncation=True, padding="max_length", max_length=128)

def train():
    csv_path = "app/trainer/processed_data.csv"

    tokenizer = load_tokenizer()
    model = load_model(tokenizer)
    dataset = load_dataset("csv", data_files=csv_path)
    print(dataset)
    tokenized_dataset = dataset.map(lambda x: tokenize_function(x, tokenizer), batched=True)

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir="./kogpt2-model",
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_strategy="steps",
        logging_steps=100,
        save_total_limit=2,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        num_train_epochs=3,
        weight_decay=0.01,
        warmup_steps=100,
        load_best_model_at_end=True,
        logging_dir="./kogpt2-model-logs",
        fp16=torch.cuda.is_available()
    )

    trainer = Trainer(
        model = model,
        args = training_args,
        ##train_dataset=tokenized_dataset["train"],
        ##eval_dataset=tokenized_dataset["train"],
        train_dataset=tokenized_dataset["train"].select(range(5000)),  # 예: 5천개만 학습
        eval_dataset = tokenized_dataset["train"].select(range(500)),  # eval은 더 적게
        tokenizer = tokenizer,
        data_collator = data_collator
    )

    trainer.train()
    model.save_pretrained("./kogpt2-model-trained")
    tokenizer.save_pretrained("./kogpt2-model-trained")

    print("END")

if __name__ == "__main__":
    train()