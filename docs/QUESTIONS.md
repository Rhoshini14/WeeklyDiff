# 10 real questions my user will ask

Write them the way your user would type them. At least 3 must need more than one page to answer, and at least 1 must be a question your documents cannot answer.

| # | Question | Where the answer is (document, page) | Needs more than one page? |
|---|----------|--------------------------------------|---------------------------|
| 1 | What has changed in Django recently, and how do those changes affect the code? | [Django GitHub repository](https://github.com/django/django) | Yes |
| 2 | Can you walk me through what happens when Django receives a request? | [django/core/handlers/](https://github.com/django/django/tree/main/django/core/handlers) | Yes |
| 3 | How does Django turn an ORM query into SQL and get the results from the database? | [django/db/models/](https://github.com/django/django/tree/main/django/db/models) and [django/db/backends/](https://github.com/django/django/tree/main/django/db/backends) | Yes |
| 4 | Where does Django check whether a form's CSRF token is valid? | [django/middleware/csrf.py](https://github.com/django/django/blob/main/django/middleware/csrf.py) | No |
| 5 | How does Django verify a user's username and password when they log in? | [django/contrib/auth/](https://github.com/django/django/tree/main/django/contrib/auth) | Yes |
| 6 | What exactly does Django middleware do before and after a view runs? | [django/core/handlers/base.py](https://github.com/django/django/blob/main/django/core/handlers/base.py) and [django/middleware/](https://github.com/django/django/tree/main/django/middleware) | Yes |
| 7 | If I enter an invalid value in a Django model field, where does Django catch the error? | [django/db/models/fields/](https://github.com/django/django/tree/main/django/db/models/fields) | Yes |
| 8 | If a database operation fails, how does Django undo the changes? | [django/db/transaction.py](https://github.com/django/django/blob/main/django/db/transaction.py) | Yes |
| 9 | Where should I look in the Django source code to understand how database connections work? | [django/db/](https://github.com/django/django/tree/main/django/db) and [django/db/backends/](https://github.com/django/django/tree/main/django/db/backends) | Yes |
| 10 | Can you tell me what changes the Django team will make next week, even if they haven't shared them publicly yet? | None — [Django GitHub repository](https://github.com/django/django) does not contain unpublished future plans | No |