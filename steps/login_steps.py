from behave import given, when, then, step

class LoginPage:
    def __init__(self):
        self.email = ''
        self.password = ''
        self.logged_in = False
        self.error = ''
        self.remembered_email = ''

    def login(self, email, password):
        self.email  = email
        self.password = password

        if email == "ishmo@gmail.com" and password == "Lord":
            self.logged_in = True
        else: 
            self.logged_in = False
            self.error = "Invalid credetials"
            self.remembered_email = email

# Successful login 
@given('the user is on the login page')
def step_given_user_on_page(context):
    context.page = LoginPage() #creating an object 

@when('the user enters a valid email and password')
def step_when_user_enters_valid_credetials(context):
    context.page.login("ishmo@gmail.com", "Lord")

@when('clicks the login button')
def step_when_user_clicks_login(context):
    pass

@then('the user should be redirected to the dashboard')
def step_then_redirect_to_dashboard(context):
    assert context.page.logged_in is True

@then('see a welcome message')
def step_then_see_welcome_message(context):
    pass




# Unsuccessful login 
# @when('an incorrect password')
# def step_when_user_enters_invalid_password(context):
#     context.page.login("ishmo@gmail.com", "recall")

# @then('see an "Invalid credentials" error message')
# def step_then_see_invalid_message(context):
#     assert context.page.error == "Invalid credetials"









