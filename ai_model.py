from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import json

# Charger le modèle léger
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# Charger les versets
with open("versets.json", "r", encoding="utf-8") as f:
    versets = json.load(f)

def get_verset_for_topic(message):
    for mot_clef, verset in versets.items():
        if mot_clef in message.lower():
            return verset
    return None

def generate_response(prompt):
    contexte = (
        "Tu es un enseignant chrétien parlant à des enfants de l’école du dimanche. "
        "Sois simple, biblique et encourageant. Explique avec douceur."
        "\n\n"
        "Question : " + prompt + "\n"
        "Réponse : "
    )
    
    inputs = tokenizer(contexte, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=150, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    final_response = response[len(contexte):].strip()
    verset = get_verset_for_topic(prompt)
    if verset:
        final_response += f"\n\n📖 Verset : {verset}"
    return final_response
