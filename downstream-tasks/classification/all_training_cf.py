# -*- coding: utf-8 -*-
import random
from transformers import set_seed,  DataCollatorWithPadding, AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import numpy as np
import sacremoses as sm
from datasets import load_metric, load_dataset, DatasetDict
set_seed(123)

metric1 = load_metric('precision')
metric2 = load_metric('recall')
metric3 = load_metric('f1')
metric4 = load_metric('accuracy')

model_name = ["albert-base-v1", "facebook/bart-base", "bert-base-uncased", "distilbert-base-uncased", "gpt2", "allenai/longformer-base-4096", "facebook/mbart-large-cc25", "roberta-base", "camembert-base", "xlnet-base-cased"]

mydata = load_dataset('csv', data_files='CFTrainerData.csv')
train_dataset, test_dataset= mydata['train'].train_test_split(test_size=0.15).values()
mydata = DatasetDict({'train': train_dataset, 'test': test_dataset})


training_args = TrainingArguments(
    output_dir="./results",
    learning_rate=2e-5,
    per_device_train_batch_size=50,
    per_device_eval_batch_size=50,
    num_train_epochs=15,
    weight_decay=0.01,
    #evaluation_strategy = "epoch"
)

for model_idx in range(len(model_name)):
    tokenizer = AutoTokenizer.from_pretrained(model_name[model_idx])
    #tokenizer = AutoTokenizer.from_pretrained("/content/drive/MyDrive/Security/Pretrained XLNet")

    def preprocess_function(examples):
        return tokenizer(examples["text"], truncation=True)

    tokenized_mydata = mydata.map(preprocess_function, batched=True)
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    model = AutoModelForSequenceClassification.from_pretrained(model_name[model_idx], num_labels=3)
    #model = AutoModelForSequenceClassification.from_pretrained("/content/drive/MyDrive/Security/Pretrained XLNet", num_labels=3)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_mydata["train"],
        eval_dataset=tokenized_mydata["test"],
        tokenizer=tokenizer,
        data_collator=data_collator,
        #compute_metrics=custom_metrics
    )

    trainer.train()
    trainer.evaluate()
    predictions = trainer.predict(tokenized_mydata["test"])

    # print(predictions.predictions.shape)
    # print(predictions.predictions.shape, predictions.label_ids.shape)

    # trained_cf = pipeline(task="text-classification", model=model, tokenizer=tokenizer, device = 'cuda:0')
    # print(trained_cf("This also enables authorization of small data delivery by specific AS and prevent unauthorized delivery of MT small data"))

    preds = np.argmax(predictions.predictions, axis=-1)
    labels = predictions.label_ids

    precision = metric1.compute(predictions=preds, references=labels, average="macro")["precision"]
    recall = metric2.compute(predictions=preds, references=labels, average="macro")["recall"]
    f1 = metric3.compute(predictions=preds, references=labels, average="macro")["f1"]
    accuracy = metric4.compute(predictions=preds, references=labels)["accuracy"]

    print(model_name[model_idx] + "precision "+ str(precision), "recall "+ str(recall), "f1 "+ str(f1), "accuracy "+ str(accuracy))
    with open('classification_results.txt', 'a') as f:
        f.write("Model Name: " + model_name[model_idx] + " precision: " + str(precision) + " recall: " + str(recall) + " f1: " + str(f1) + " accuracy: " + str(accuracy)+ "\n")

