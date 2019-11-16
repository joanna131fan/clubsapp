# Clubs Application
Introduction here

## Credits
Joanna Fan\
Paul Morenkov

### Route Key
When linking to routes, use the `url_for()` syntax whenever possible. Rememember, the argument is the **function name**, not the actual URL. When routing inside hmtl templates, **place double quotes around the jinja2 code brackets**. Remember, for simple variables, jinja 2 requires double brackets.\
Example: `href="{{ url_for('main.home') }}"`

### All Routes:
- main
	- home()
	- about()
- users
	- login()
	- register()
	- logout()
- clubs
	- user_clubs(user_id)
	- num_club_members(user_id)
	- add_club_members(user_id, num_members)
	- record(user_id) **Not Complete**
	- view() ***Not Complete*
	
	
### All Forms:
- main
- users
	- RegistrationForm
	- LoginForm
- clubs
	- ClubRegistrationForm
	- NumMembersToAddForm
	- create_member_entry_form(user, num_members) **factory function**
	- create_club_minutes_form(use) **factory function** **Not Completed**
