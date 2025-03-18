import logging
from codecarbon import EmissionsTracker
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize the tracker for experiment 3
tracker = EmissionsTracker(
    project_name="GIATHEIA_3",
    log_level=logging.INFO,
    output_file="profiler.csv",
    save_to_file=True,
    measure_power_secs=5,
    #save_to_prometheus=True
)

# Loading the model and the tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

def generate_response(user_message):
    tracker.start()
    inputs = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    tracker.stop()
    
    return tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)

# Run the LLM with a message
if __name__ == "__main__":
    message = "Hello, how are you?"
    response = generate_response(message)
    print("LLM Response:", response)
