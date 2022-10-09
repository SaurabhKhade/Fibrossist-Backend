# Follow the instructions for project setup

#### Create a virtual environment

For Linux and Mac users:

```bash
python3 -m venv <name>
```

For Windows users:

```bash
py -m venv <name>
```

to create in root directory of the project, use `.` in the place of `<name>`

#### Activate the virtual environment

For Linux and Mac users:

```bash
source <name>/bin/activate
```

For Windows users:

```bash
.\<name>\Scripts\activate
```

#### Installing Dependencies

Run command

```bash
pip install -r requirements.txt
```

to install all the dependencies.

#### Starting the Server

Run command

```bash
flask --app app --debug run
```

It will start flask development server on port 5000.

To use different port, use command

```bash
flask --app app --debug --port <port_number> run
```

#### Visit Webpage

Open the browser and go to `http://localhost:5000/`

#### Deactivate the virtual environment

To deactivate the virtual environment, run command

```bash
deactivate
```
