# PRGX TECHNICAL CHALLENGE

## Technical assessment backend

## Description

Create two endpoints using python and the backend framework of your choice to read and extract information from PDFs file store in a path.

### Endpoint 1:

Receive the path for one of the pdfs file:

http://127.0.0.1:8000/extract?doc_path=/home/danicortes/PRGX_technical_challenge/Doc4.pdf'

Extract from the pdf file (images) the fields:

- Vendor Name
- Fiscal Number
- Contract Number
- Start Date
- End Date
- Comments paragraph

Store the extracted information in the database of your choice and returns:

- True if it was successfully added to the data base
- The data base id of the row.
- The extraction information.

### Endpoint 2:

Receive the name of the table where the extraction is stored.

http://127.0.0.1:8000/db_data/?table_name=EXTRACTION

Returns all the extractions ordered by the newest id to the oldest

Notes.

- You can you use python and the libraries that you want.
- You can use the database that you want.

## Installation

1.  Clone the repository:

    ```Bash
    $ git clone https://github.com/el-dani-cortes/PRGX_technical_challenge
    ```

2.  Use the package manager [pip](https://pip.pypa.io/en/stable/) to manage the installation of all the dependencies necessary for the application. Use next code to install:

    ```bash
    $ pip install -r requirements.txt
    ```

3.  Install Tesseract in your OS. For linux use:

    ```bash
    $ sudo apt-get update
    $ sudo apt-get install tesseract-ocr
    ```

    To use some features of Tesseract, you also need to set a new environment variable:

    ```bash
    $ export TESSDATA_PREFIX='/usr/share/tesseract-ocr/4.00/tessdata'
    ```

    Also is needed install all language that tesseract can support:

    ```bash
    $ sudo apt-get install tesseract-ocr-all
    ```

4.  Install a relational database of your choice. Remember to add your database credentials for 'SQLALCHEMY_DATABASE_URI' variable in an `.env` file of your project's root directory. This will let you make the right connection to your database. Example:

    Inside your `.env` created:

        DATABASE_URL=DATABASE + DIALECT://USER:PASSWORD@HOST/DATABASE_NAME

    In my case, I use `mysql` as database and `pymysql` as dialect

    Read [flask](https://flask.palletsprojects.com/en/2.0.x/) documentation for more details.

## Usage

Use this application like any other flask application. Just run the next commands to activate the virtual python enviroment, run the server and start your service database:

```bash
$ . env/bin/activate # Activate the virtual enviroment
$ sudo service mysql start # This is my case. I use mysql
$ flask run # Start the server
```

In the `PDFs` are the pdfs file to read and extract the information for the database.

Then you can go to [postman](https://www.postman.com/) and make the call to every endpoint according the HTTP method.

All this is done in your localhost.

## Author

Daniel Cortes Sully - Software developer

[Linkedin](https://www.linkedin.com/in/danielcortessully/) | [Github](https://github.com/el-dani-cortes)
