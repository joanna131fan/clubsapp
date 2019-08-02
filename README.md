# Clubs Application
Introduction here

## Credits
Joanna Fan\
Paul Morenkov

## Route Key
When linking to routes, use the `url_for()` syntax whenever possible. Rememember, the argument is the **function name**, not the actual URL. When routing inside hmtl templates, **place double quotes around the jinja2 code brackets**. Remember, for simple variables, jinja 2 requires double brackets.\
Example: `href="{{ url_for('main.home') }}"`

#### All Routes:
- main
	- home
	- about
- users
	- login
	- register
	- logout
- clubs
