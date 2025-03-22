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

    # 5. Hapus emoji
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF"
        "\U00002500-\U00002BEF\U00002702-\U000027B0"
        "\U000024C2-\U0001F251\U0001F900-\U0001F9FF"
        "\U0001FA70-\U0001FAFF\U0001F018-\U0001F270"
        "\U0001F300-\U0001F64F\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF"
        "\U00002702-\U000027B0]+",
        flags=re.UNICODE
    )
    text = emoji_pattern.sub("", text)

    # 6. Tokenisasi (pecah menjadi kata-kata)
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