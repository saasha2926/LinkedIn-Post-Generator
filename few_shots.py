import json
import pandas as pd


def categorize_length(line_count):
    if line_count < 5:
        return "Short"
    elif 5 <= line_count <= 10:
        return "Medium"
    else:
        return "Long"


class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)

            if "line_count" in self.df.columns:
                self.df["length"] = self.df["line_count"].apply(categorize_length)

            if "tags" in self.df.columns:
                self.df["tags"] = self.df["tags"].apply(lambda x: x if isinstance(x, list) else [])
                all_tags = self.df["tags"].explode()
                self.unique_tags = set(all_tags.dropna())
            else:
                self.unique_tags = set()

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df["language"] == language) &
            (self.df["length"] == length) &
            (self.df["tags"].apply(lambda tags: tag in tags if isinstance(tags, list) else False))
            ]
        return df_filtered.to_dict(orient="records")

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("Long", "English", "Motivation")
    print(posts)
