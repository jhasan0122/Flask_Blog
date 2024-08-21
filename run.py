from flaskBlog import create_app

app = create_app()

if __name__ == "__main__":    # For run the project #
    app.run(debug=True)