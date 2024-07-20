import re

def convert_format(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # タブで単語とIPA表記を分割
            parts = line.strip().split('\t')
            if len(parts) != 2:
                continue  # 不正な行はスキップ

            word, ipa_list = parts
            # カンマで区切られたIPA表記の最初の1つだけを取得
            ipa = ipa_list.split(', ')[0]

            # IPAから不要な文字（スラッシュ）を除去
            ipa = re.sub(r'^/|/$', '', ipa)
            
            # 新しい形式で書き出し
            new_line = f"('en_us', '{word}', '{ipa}'),\n"
            outfile.write(new_line)

# ファイルの変換を実行
convert_format('cmudict-0.7b-ipa.txt', 'cmudict-0.7b-ipa_convert.txt')