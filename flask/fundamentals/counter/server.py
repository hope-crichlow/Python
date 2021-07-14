# Import Flask to allow us to create our app
from flask import Flask, render_template, request, redirect, session
# Create a new instance of the Flask class called 'app'
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe'


# Have the root route render a template that displays the number of times the client has visited this site.
@app.route('/')
def visits():
    if 'visits' in session:
        session['visits'] = session['visits'] + 1
        print('visits exists!')
    else:
        session['visits'] = 1
        print("key 'visits' does NOT exist")
    return render_template('index.html')


# Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
@app.route('/destroy_session')
def destroy_session():
    session['visits'] = 0
    print("argggg")
    return redirect('/')


if __name__ == '__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
