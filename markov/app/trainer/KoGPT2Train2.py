from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel, DataCollatorForLanguageModeling, TrainingArguments, \
    Trainer
import torch
from datasets import Dataset
import os

MODEL_NAME = 'skt/kogpt2-base-v2'


def load_tokenizer():
    print(MODEL_NAME)
    return PreTrainedTokenizerFast.from_pretrained(MODEL_NAME, bos_token='▁', eos_token='</s>', pad_token='<pad>')


def load_model(tokenizer):
    model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
    model.resize_token_embeddings(len(tokenizer))
    return model


def tokenize_function(example, tokenizer):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)


def load_dataset_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # 빈 줄 제거하고 <|bos|> ~ <|eos|>가 있는 대화 단위로 만듦
    return Dataset.from_list([{"text": line.strip()} for line in lines if line.strip()])


def train():
    txt_path = "app/data/processed_data_for_kogpt2.txt"  # 수정된 경로!

    tokenizer = load_tokenizer()
    model = load_model(tokenizer)

    dataset = load_dataset_from_txt(txt_path)
    print(dataset)

    tokenized_dataset = dataset.map(lambda x: tokenize_function(x, tokenizer), batched=True)

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir="./kogpt2-modelv2",
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
        logging_dir="./kogpt2-model-logsv2",
        fp16=torch.cuda.is_available()
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset.select(range(5000)),
        eval_dataset=tokenized_dataset.select(range(500)),
        tokenizer=tokenizer,
        data_collator=data_collator
    )

    trainer.train()
    model.save_pretrained("./kogpt2-model-trainedv2")
    tokenizer.save_pretrained("./kogpt2-model-trainedv2")

    print("END")


if __name__ == "__main__":
    train()
