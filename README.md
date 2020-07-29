# streamlit-demo

## Get started

[Create a new repository from this template.](https://github.com/rrherr/streamlit-demo/generate)

Clone the repo
```
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPO-NAME.git

cd YOUR-REPO-NAME
```

Install dependencies
```
pipenv install --dev

git add Pipfile.lock

git commit -m "Add Pipfile.lock"
```

Activate the virtual environment
```
pipenv shell
```

Launch the app
```
streamlit run app.py
```

## Deploy

Prepare Heroku
```
heroku login

heroku create YOUR-APP-NAME-GOES-HERE

heroku git:remote -a YOUR-APP-NAME-GOES-HERE
```

Deploy to Heroku
```
git add --all

git commit -m "Deploy to Heroku"

git push heroku main:master

heroku open
```

Deactivate the virtual environment
```
exit
```
