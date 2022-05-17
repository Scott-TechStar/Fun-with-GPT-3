# TECHSTAR OPEN AI APP

<img src="{{ url_for('static', filename='page.png') }}" class="page" />
This is a list generator app using OpenAI API. It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework.

## Setup

1. Make sure you have python installed.

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this app project.
