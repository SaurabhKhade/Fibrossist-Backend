# Follow the procedure for project setup

1. **Create a virtual environment**
   For Linux and Mac users:

   ```bash
   python3 -m venv <name>
   ```

   For Windows users:

   ```bash
   py -m venv <name>
   ```

   to create in root directory of the project, use `.` in the place of `<name>`

2. **Activate the virtual environment**
   For Linux and Mac users:

   ```bash
   source <name>/bin/activate
   ```

   For Windows users:

   ```bash
   .\<name>\Scripts\activate
   ```

3. **Run command**

   ```bash
   pip install -r requirements.txt
   ```

   to install all the dependencies.

4. **Run command**

   ```bash
   flask --app app --debug run
   ```

   It will start flask development server on port 5000.
   To use different port, use command

   ```bash
    flask --app app --debug --port <port_number> run
   ```

5. **Open the browser and go to** `http://localhost:5000/`

6. **To deactivate the virtual environment**
   ```bash
   deactivate
   ```
