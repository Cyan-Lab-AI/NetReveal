# @Author: DennisShaw
# @Email: cyan.lab.ai@gmail.com
import os

def read_config(folder):
    lines = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    lines += f.readlines()
    return lines