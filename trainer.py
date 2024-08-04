import torch
from transformers import RobertaTokenizer, RobertaForMaskedLM, Trainer, TrainingArguments
from datasets import load_dataset
from github import Github

def fetch_github_file(github_token: str, repo_name: str, file_path: str) -> str:
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    return repo.get_contents(file_path).decoded_content.decode()

def save_file(content: str, local_path: str) -> None:
    with open(local_path, "w") as f:
        f.write(content)

def tokenize_function(examples, tokenizer):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

def train_model(tokenized_datasets, tokenizer, model):
    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        save_steps=10_000,
        save_total_limit=2,
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
    )
    trainer.train()
    model.save_pretrained("./fine_tuned_codebert")
    tokenizer.save_pretrained("./fine_tuned_codebert")

def main():
    github_token = "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"
    repo_name = "Slayer412/pythoncode"
    file_path = "MergeSort.py"
    local_file = "local_train.py"

    file_content = fetch_github_file(github_token, repo_name, file_path)
    save_file(file_content, local_file)

    dataset = load_dataset("text", data_files={"train": [local_file]})
    tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
    model = RobertaForMaskedLM.from_pretrained("microsoft/codebert-base")
    tokenized_datasets = dataset.map(lambda x: tokenize_function(x, tokenizer), batched=True)

    train_model(tokenized_datasets, tokenizer, model)

if __name__ == "__main__":
    main()
