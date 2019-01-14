![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-civic-biography

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-civic-biography
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'entity',
      'geography',
      'government',
      'election',
      'biography',
  ]

  #########################
  # biography settings

  BIOGRAPHY_API_AUTHENTICATION_CLASS = 'rest_framework.authentication.BasicAuthentication' # default
  BIOGRAPHY_API_PERMISSION_CLASS = 'rest_framework.permissions.IsAdminUser' # default
  BIOGRAPHY_API_PAGINATION_CLASS = 'biography.pagination.ResultsPagination' # default
  ```

### Models

##### Biography

A biography of a `Person`. This model is used as a foreign key for all the other models in this app.

##### Birthplace

Where a person was born. One-to-one to `Biography`.

##### Education

Where a person was educated. Built to handle all types of college degrees. Foreign keys to `Biography`.

##### Financials

A person's net worth. One-to-one to `Biography`.

##### Ideology

A person's political ideology (through `IdeologyCategory`) and DW-Nominate score. One-to-one to `Biography`

##### Legislation

A piece of legislation that someone took part in crafting. Handles sponsorship and signatory roles. Foreign keys to `Biography`.

##### Occupation

A job held. Tracks start and end dates, private/public sector. Foreign keys to `Biography`

##### PastCampaign

A (usually failed) campaign that happened in the past, e.g. Joe Biden's 2008 presidential campaign. Foreign keys to `Biography`.

##### Publication

A book or article published by a person. Foreign keys to `Biography`.

##### Residence

Current residence of the person. One-to-one to `Biography`.

### Developing

##### Running a development server

Developing python files? Move into example directory and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv run python manage.py runserver
  ```

Developing static assets? Move into the pluggable app's staticapp directory and start the node development server, which will automatically proxy Django's development server.

  ```
  $ cd biography/staticapp
  $ gulp
  ```

Want to not worry about it? Use the shortcut make command.

  ```
  $ make dev
  ```

##### Setting up a PostgreSQL database

1. Run the make command to setup a fresh database.

  ```
  $ make database
  ```

2. Add a connection URL to the `.env` file.

  ```
  DATABASE_URL="postgres://localhost:5432/biography"
  ```

3. Run migrations from the example app.

  ```
  $ cd example
  $ pipenv run python manage.py migrate
  ```
