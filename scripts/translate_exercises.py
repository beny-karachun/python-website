import json
import time
import re
import os
from deep_translator import GoogleTranslator
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    print("Reading exercises_data.js...")
    with open(os.path.join(SCRIPT_DIR, '..', 'exercises_data.js'), 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract JSON part
    prefix = "// Auto-generated CodingBat exercises data\nconst EXERCISES_DATA = "
    if prefix in content:
        json_str = content[len(prefix):]
    else:
        json_str = content[content.find('{'):]
        
    json_str = json_str.strip()
    if json_str.endswith(';'):
        json_str = json_str[:-1]

    data = json.loads(json_str)
    
    translator = GoogleTranslator(source='en', target='iw') # iw is Hebrew in Google Translate

    hebrew_pack = {}
    
    total_problems = sum(len(cat['problems']) for cat in data['categories'])
    print(f"Translating {total_problems} problems...")

    count = 0
    for cat in data['categories']:
        for prob in cat['problems']:
            count += 1
            if count % 10 == 0:
                print(f"Translated {count}/{total_problems}...")
                
            pid = prob['id']
            name = prob['name']
            desc = prob['description']
            
            try:
                # We want to preserve markdown like `code` and **bold**, but Google Translate might mess them up.
                # However, for simplicity we will just pass it through. Usually it keeps `a` intact.
                # Let's do a simple translation
                he_name = translator.translate(name)
                he_desc = translator.translate(desc)
                
                # Small fixes for code blocks that might get spaced out
                he_desc = re.sub(r'`\s*(.*?)\s*`', r'`\1`', he_desc)
                he_desc = re.sub(r'\*\*\s*(.*?)\s*\*\*', r'**\1**', he_desc)
                
                hebrew_pack[pid] = {
                    "name": he_name,
                    "description": he_desc
                }
            except Exception as e:
                print(f"Failed to translate {pid}: {e}")
                # Fallback to English
                hebrew_pack[pid] = {
                    "name": name,
                    "description": desc
                }
            
            time.sleep(0.1) # Be nice to the API

    # Also we need to keep the Exam Prep ones we generated earlier, just to be safe.
    # We will read hebrew_pack.js, extract existing ones, and merge.
    print("Reading existing hebrew_pack.js...")
    existing = {}
    try:
        with open(os.path.join(SCRIPT_DIR, '..', 'hebrew_pack.js'), 'r', encoding='utf-8') as f:
            exist_content = f.read()
            # Extremely naive extraction for safety
            # But since we just want to merge, let's just write the newly translated dict,
            # and we will instruct the user or write a JS wrapper.
    except:
        pass

    # Let's actually write it back to hebrew_pack.js
    # Wait, we need to preserve the Exam Prep ones. Let's just dump ALL into hebrew_pack.js 
    # and the user already has the exam prep ones in exam_exercises_data.js. Wait, no, hebrew_pack.js contains exam prep!
    
    # We will just write a new file `hebrew_pack_new.json` and merge it in JS or here.
    with open(os.path.join(SCRIPT_DIR, 'hebrew_pack_new.json'), 'w', encoding='utf-8') as f:
        json.dump(hebrew_pack, f, ensure_ascii=False, indent=4)
        
    print("Done! Saved to hebrew_pack_new.json")

if __name__ == '__main__':
    main()
