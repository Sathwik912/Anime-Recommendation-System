from flask import Flask,render_template,request
import numpy as np
import pickle

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
anime = pickle.load(open('anime.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           Anime=list(popular_df['Anime Title'].values),
                           Studio=list(popular_df['Studios'].values),
                           image=list(popular_df['Image URL'].values),
                           votes=list(popular_df['num_rating'].values),
                           rating=list(popular_df['avg_rating'].values),
                           )

@app.route('/recommendations')
def recommend_ui():
    return render_template('recommendations.html')

@app.route('/recommend_anime',methods=['post'])
def reccomend():
    user_input=request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:20]

    data = []
    for i in similar_items:
        item = []
        temp_df = anime[anime['Anime Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Anime Title')['Anime Title'].values))
        item.extend(list(temp_df.drop_duplicates('Anime Title')['Studios'].values))
        item.extend(list(temp_df.drop_duplicates('Anime Title')['Image URL'].values))

        data.append(item)

    print(data)

    return render_template('recommendations.html',data=data)



if __name__ =='__main__':
    app.run(debug=True)