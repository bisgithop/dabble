# This is the model connecting code taken from Hugging Face. 
# Just testing it out for various inputs 

from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigcode/santacoder"
device = "cpu" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True).to(device)

inputs = tokenizer.encode("10 lines code for encryting a password in java", return_tensors="pt").to(device)
outputs = model.generate(inputs)
for i in outputs:
    print(tokenizer.decode(i))