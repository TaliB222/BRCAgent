from app import create_app

app = create_app()
import os
print("CURRENT DIR:", os.getcwd())

if __name__ == "__main__":
    app.run(debug=True)