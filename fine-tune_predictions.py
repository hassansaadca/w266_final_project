import os
import numpy as np

from transformers import MarianMTModel, MarianTokenizer

os.environ["WANDB_DISABLED"]="true"

source_language = "es"
target_language = "en"

model_name = "ES-to-EN"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

n = 1
with open('/home/ec2-user/data/UFAL/medical.test' , 'r') as f:
    for line in f:
        split = line.split('\t')
        if source_language == 'es':
            source, target = split[0], split[1]
        else:
            source, target = split[1], split[0]
        tokenized_input = tokenizer(source, return_tensors="pt", max_length = 512, truncation = True)
        tokenized_translation = model.generate(tokenized_input.input_ids)[0]
        translation = tokenizer.decode(tokenized_translation, skip_special_tokens=True)

    #write original text, translation, then actual target to new file
        with open(f'es_to_en_finetune_translations.txt', 'a') as w:
            w.write(f'{source}\t{translation}\t{target}\n')
        print(f'Current Row: {n}', end = '\r')
        n+=1
