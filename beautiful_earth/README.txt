Set up
    python3 -m venv venv
    virtualenv venv
    source venv/bin/activate
    venv\Scripts\activate
    pip install requirements.txt
    Haven’t tested this

To run locally
    Open the beautiful_earth folder in VSCode 
    Click terminal -> new terminal
    export FLASK_APP=main.py
    Flask run

To deploy:
Set up Azure in VSCode: https://docs.microsoft.com/en-us/azure/python/tutorial-deploy-app-service-on-linux-01#visual-studio-code-python-and-the-azure-app-service-extension
Then click deploy: https://docs.microsoft.com/en-us/azure/python/tutorial-deploy-app-service-on-linux-05