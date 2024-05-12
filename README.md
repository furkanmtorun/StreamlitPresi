# 💈 Streamlit Presi

- This repository contains the example Streamlit project to be presented in my talks at [🇨🇿 PyData Prague 2023 meetup](https://pydata.cz/) and [🇩🇪 PyMunich 2024 Meetup](https://www.meetup.com/pymunich/).

## 🚀 Talks

| Talk & Event | Where | When | Organizer | Link |
|---|---|---|---|---|
| ["Become a Data Storyteller with Streamlit!"](https://www.meetup.com/pydata-prague/events/297072175/) | 🇩🇪 Munich, DE   | May 21, 2024 | [PyMunich](https://www.meetup.com/pymunich/)  | [![PyMunich-FurkanMTorun](http://img.youtube.com/vi/9h9sRkm72WM/0.jpg)](http://www.youtube.com/watch?v=9h9sRkm72WM "Become a Data Storyteller with Streamlit! - Furkan M. Torun") |
| ["Become a Data Storyteller with Streamlit!"](https://www.meetup.com/pydata-prague/events/297072175/) | 🇨🇿 Prague, CZ  | November 20, 2023 | [PyData Prague](https://pydata.cz/) | [![PyDataPrague-FurkanMTorun](http://img.youtube.com/vi/zi9KgTJjnjc/0.jpg)](http://www.youtube.com/watch?v=zi9KgTJjnjc "Become a Data Storyteller with Streamlit! - Furkan M. Torun") |


## 💊 Installation & Running

```bash
git clone https://github.com/furkanmtorun/StreamlitPresi.git
cd StreamlitPresi
conda create --name streamlit_presi python=3.11 -y
conda activate streamlit_presi
pip install -r requirements.txt
wget 'https://github.com/patrick013/Object-Detection---Yolov3/raw/master/model/yolov3.weights' -O utils/yolov3.weights
streamlit run Main.py
```

## ⚔️ Test
Run the tests in the parent folder:
```bash
pytest tests/* -v 
```


## 🎈 What can you do with Streamlit?
There are several projects and apps using Streamlit! Here, I collected few of them for different categories.
<details>
  <summary>Click here to see the list</summary>
  <p><strong>Examples</strong></p>
<ul>
<li>http://omiclearn.org/</li>
<li>https://prophet.streamlit.app/</li>
<li>https://github.com/jrieke/best-of-streamlit</li>
<li>https://traingenerator.streamlit.app/</li>
</ul>
<p><strong>Dashboard:</strong></p>
<ul>
<li>https://okld-gallery.streamlit.app/?p=elements</li>
<li>https://shamiraty-streamlit-dashboard-descriptive-analytics-home-5ks7sm.streamlit.app/</li>
<li>https://similobeta2.streamlit.app/</li>
</ul>
<p><strong>NLP</strong>:</p>
<ul>
<li>https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/</li>
<li>https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps</li>
<li>https://llm-examples.streamlit.app/</li>
<li>https://streamlit.io/gallery?category=nlp-language</li>
<li>https://blog.streamlit.io/chat-with-pandas-dataframes-using-llms/</li>
</ul>
<p><strong>Image</strong>:</p>
<ul>
<li>https://github.com/whitphx/streamlit-webrtc</li>
<li>https://streamlit.io/generative-ai</li>
<li>https://github.com/CodingMantras/yolov8-streamlit-detection-tracking</li>
<li>https://generateimages.streamlit.app/</li>
</ul>  
</details>



## 👨🏻‍💻 Author and Developer
- Furkan M. Torun
- Twitter: [@furkanmtorun](https://www.twitter.com/furkanmtorun)
- Mail: [furkanmtorun[at]gmail[dot]com](mailto:furkanmtorun@gmail.com) 
- Academia: [Google Scholar Profile](https://scholar.google.com/citations?user=d5ZyOZ4AAAAJ) 
- Website: [furkanmtorun.github.io](https://furkanmtorun.github.io)

Moreover, please do not hesitate to comment via opening an issue via GitHub if you have any suggestions or feedback!

