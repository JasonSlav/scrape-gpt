import json
import re
import string

def preprocess_text(text):
    # 1. Konversi ke huruf kecil
    text = text.lower()

    # 2. Hapus tanda baca
    text = text.translate(str.maketrans("", "", string.punctuation))

    # 3. Hapus angka
    text = re.sub(r"\d+", "", text)

    # 4. Hapus spasi berlebih
    text = re.sub(r"\s+", " ", text).strip()

    # 5. Tokenisasi (pecah menjadi kata-kata)
    words = text.split()

    return words  # Mengembalikan list kata

def preprocess_conversation(json_text):
    # Parse JSON
    data = json.loads(json_text)
    
    # Pastikan data adalah list
    if not isinstance(data, list):
        raise ValueError("Data harus berupa list")

    # Proses setiap teks di dalam JSON
    processed_conversation = []
    for msg in data:
        role = msg.get("role", "unknown")
        text = preprocess_text(msg.get("text", ""))  # Proses teks
        processed_conversation.append({"role": role, "text": text})  # Simpan hasilnya

    return json.dumps(processed_conversation, ensure_ascii=False)  # Mengembalikan hasil sebagai JSON string