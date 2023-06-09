<div align="center">

<img src="assets/logo.png" width="300px">

______________________________________________________________________

<p align="center">
  <a href="#running-the-app">Getting Started</a> •
  <a href="ipl.gpt">IPL GPT App URL</a>
</p>

______________________________________________________________________

</div>

# iplGPT

With `iplGPT`, you can ask questions about the Indian Premier League (IPL). From searching stats, scores, standings, bios, and more, iplGPT is a one-stop search solution for all things IPL.

`iplGPT` takes a leap forward by transforming sports statistics into meangful, storytelling prose.

## Running the app

Create a virtual environment and install the dependencies.

```bash
python3 -m venv venv
source venv/bin/activate

pip install -e .
```

<!-- Populate the database with the data.

```bash
python3 populate.py
``` -->

Download the sql data from kaggle

```
python3 download_ipl_sql_data.py
```

Run the app.

```bash
streamlit run app.py
```
