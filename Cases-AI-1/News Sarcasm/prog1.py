import pandas as pd

df = pd.read_json('Sarcasm_Headlines_Dataset_v2.json',
                  lines=True)


"http://www.zeenews.com".split("/")[2].split(".")[1]
df['article_link'].apply(lambda x: re.findall(r'\w+', x)[2])
