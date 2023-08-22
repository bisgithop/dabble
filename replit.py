# Got below code from Hugging Face. 
# Tested it with few functions like quicksort, factorial - worked well.
# Sample client for code generator. Worked well so far. 
# But it downloads 10 GB on your local machine. and there are some errors. 

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('replit/replit-code-v1-3b', trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained('replit/replit-code-v1-3b', trust_remote_code=True)

x = tokenizer.encode('def quicksort(n): ', return_tensors='pt')
y = model.generate(x, max_length=100, do_sample=True, top_p=0.95, top_k=4, temperature=0.2, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)

# decoding, clean_up_tokenization_spaces=False to ensure syntactical correctness
generated_code = tokenizer.decode(y[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
print(generated_code)
