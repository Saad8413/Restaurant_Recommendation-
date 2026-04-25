import pandas as pd
from flask import Flask, render_template, request, jsonify
import pickle
import warnings
import json

warnings.filterwarnings('ignore')
app = Flask(__name__)

# --- DATA INITIALIZATION ---
try:
    zomato_df = pd.read_csv("restaurant1.csv")
    df_percent = zomato_df.copy()
    df_percent.set_index('name', inplace=True)
    indices = pd.Series(df_percent.index)

    with open("restaurant.pkl", "rb") as f:
        cosine_similarities = pickle.load(f)
    print("✅ Aura Gastronomica: Data Engine Online.")
except Exception as e:
    print(f"⚠️ Initialization Error: {e}")

def recommend(name):
    if name not in indices.values:
        return pd.DataFrame(columns=['Error'])

    idx = indices[indices == name].index[0]
    score_series = pd.Series(cosine_similarities[idx]).sort_values(ascending=False)
    top_indexes = list(score_series.iloc[1:min(31, len(score_series))].index)

    recommend_restaurant = [list(df_percent.index)[each] for each in top_indexes]

    df_new = pd.DataFrame(columns=['cuisines', 'Mean Rating', 'cost'])
    for each in recommend_restaurant:
        selected_data = df_percent[['cuisines', 'Mean Rating', 'cost']][df_percent.index == each]
        if not selected_data.empty:
            df_new = pd.concat([df_new, selected_data.sample(n=1)])

    df_new = df_new.drop_duplicates(subset=['cuisines', 'Mean Rating', 'cost'], keep=False)
    df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(10)

    # Professional Editorial Renaming
    df_new.rename(columns={
        'cuisines': 'Gastronomic Profile',
        'Mean Rating': 'Sensory Score',
        'cost': 'Average Budget (2x)'
    }, inplace=True)

    return df_new

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/web')
def web():
    return render_template('web.html')

@app.route('/result', methods=['POST'])
def result():
    output = request.form.get('output', '')
    res = recommend(output)
    html_table = res.to_html(classes='dossier-table', border=0, index=True, index_names=False)
    
    names = res.index.tolist() if not res.empty else []
    ratings = res['Sensory Score'].tolist() if not res.empty else []
    cost = res['Average Budget (2x)'].tolist() if not res.empty else []

    return render_template('result.html', keyword=html_table, search_term=output, 
                           names=json.dumps(names), ratings=json.dumps(ratings), cost=json.dumps(cost))

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    term = request.args.get('term', '').lower()
    if not term: return jsonify([])
    matches = df_percent[df_percent.index.str.lower().str.contains(term, na=False)].index.tolist()
    return jsonify(sorted(list(set(matches)))[:10])

if __name__ == '__main__':
    app.run(debug=True)