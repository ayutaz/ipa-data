import random

def load_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # 括弧と余分な空白を取り除く
            line = line.strip().strip('(),')
            parts = line.split(', ')
            if len(parts) == 3:
                lang, word, pronunciation = parts
                # 引用符を取り除く
                data.append((lang.strip("'"), word.strip("'"), pronunciation.strip("'")))
    return data

def split_data(data, train_ratio=0.8):
    random.shuffle(data)
    split_index = int(len(data) * train_ratio)
    return data[:split_index], data[split_index:]

def save_data(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item}\n")

# データを読み込む
all_data = load_data('ja_convert.txt')

# データを分割する
train_data, val_data = split_data(all_data)

# 分割したデータを保存する
save_data(train_data, 'train_data.txt')
save_data(val_data, 'val_data.txt')