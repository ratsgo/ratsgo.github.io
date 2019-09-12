import frontmatter
import glob
import yaml
import string
from konlpy.tag import Mecab
from sklearn.feature_extraction.text import TfidfVectorizer

def get_posts(folder='./_posts'):
    result = {}
    fm = frontmatter.Frontmatter()
    for filepath in glob.glob(folder + "/*"):
        filename = filepath.split('/')[-1]
        slug = filename[11:-3]
        post = fm.read_file(filepath)
        result[slug] = post['body'].replace('\n', ' ').replace('  ', ' ')
    return result

def write_result_to_file(related, file='./_data/related.yml'):
    data = []
    for r in related:
        r = {
            'post': r,
            'related': related[r]
        }
        data.append(r)
    with open(file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

stemmer = Mecab()

def tokenize(text):
    stems = stemmer.nouns(text)
    return stems

def cosine_sim(text1, text2, vectorizer):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]

def get_similarity(num_best=5):
    vectorizer = TfidfVectorizer(tokenizer=tokenize)
    posts = get_posts()
    cleaned_posts = {slug: post.lower().translate(str.maketrans('', '', string.punctuation)) for slug, post in posts.items()}
    slugs = list(cleaned_posts.keys())
    tfidf = vectorizer.fit_transform(list(cleaned_posts.values()))
    matrix = (tfidf * tfidf.T).A
    result = {}
    for i, row in enumerate(matrix):
        indices = row.argsort()[-num_best-1:-1][::-1]
        current_slug = slugs[i]
        result[current_slug] = [slugs[index] for index in indices]
    write_result_to_file(result)


get_similarity()
