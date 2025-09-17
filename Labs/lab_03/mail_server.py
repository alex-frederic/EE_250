from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
import uuid
import json


app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file

# Function to load and save the mail to/from the json file

def load_mail() -> List[Dict[str, str]]:
    """
    Loads the mail from the json file

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    try:
        return json.loads(thisdir.joinpath('mail_db.json').read_text())
    except FileNotFoundError:
        return []

def save_mail(mail: List[Dict[str, str]]) -> None:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)

    Summary:
    Saves the mail parameter to the json file in the json format

    Args:
        mail (List[Dict[str, str]]): a list of dictionaries representing mail entries

    Returns:
        None
    """
    thisdir.joinpath('mail_db.json').write_text(json.dumps(mail, indent=4))

def add_mail(mail_entry: Dict[str, str]) -> str:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)

    Summary:
        Reads the current state of the mail_db.json file as python object, appends
        the parameter mail_entry to it, gives it a unique id, and saves it to the
        mail_db.json file in json format

    Args:
        mail_entry (Dict[str, str]): a dictionary representing the mail entries to add

    Returns:
        A string representing the unique id of the newly added mail entry
    """
    mail = load_mail()
    mail.append(mail_entry)
    mail_entry['id'] = str(uuid.uuid4()) # generate a unique id for the mail entry
    save_mail(mail)
    return mail_entry['id']

def delete_mail(mail_id: str) -> bool:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)

    Summary
        Identifies a mail entry in the mail_db.json file with the specified id
        mail_id and removes it from mail_db.json

    Args
        mail_id (st): the id of the mail entry to delete

    Returns:
        A boolean representing whether the function successfully deleted an
        entry with the specified id (True) or not (False)
    """
    mail = load_mail()
    for i, entry in enumerate(mail):
        if entry['id'] == mail_id:
            mail.pop(i)
            save_mail(mail)
            return True

    return False

def get_mail(mail_id: str) -> Optional[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)

    Summary:
        Finds the mail entry in the mail_db.json file with the specified id mail_id
        and returns it.

    Args:
        mail_id: id of the mail entry to find

    Returns:
        A dictionary representing the mail entry or None if a mail entry with
        the specified id wasn't found
    """
    mail = load_mail()
    for entry in mail:
        if entry['id'] == mail_id:
            return entry

    return None

def get_inbox(recipient: str) -> List[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)

    Summary:
        Searches the mail_db.json file for mail entries addressed to a certain
        recipient, stores them all in a list, and returns that list of mail entries
        as the inbox of the user recipient

    Args:
        recipient (str): the name of the recipient whose inbox you want to collect

    Returns:
        A list of dictionaries representing the mail entries of the specified
        recipient
    """
    mail = load_mail()
    inbox = []
    for entry in mail:
        if entry['recipient'] == recipient:
            inbox.append(entry)

    return inbox

def get_sent(sender: str) -> List[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)

    Summary:
        Searches the mail_db.json file for mail entries sent from a certain sender,
        stores them all in a list, and returns that list of mail entries as the
        sent mail from the user sender
    
    Args:
        sender (str): the name of the sender whose mail you want to collect

    Returns
        A list of dictionaries representing the mail entires of the specified
        sender
    """
    mail = load_mail()
    sent = []
    for entry in mail:
        if entry['sender'] == sender:
            sent.append(entry)

    return sent

# API routes - these are the endpoints that the client can use to interact with the server
@app.route('/mail', methods=['POST'])
def add_mail_route():
    """
    Summary: Adds a new mail entry to the json file

    Returns:
        str: The id of the new mail entry
    """
    mail_entry = request.get_json()
    mail_id = add_mail(mail_entry)
    res = jsonify({'id': mail_id})
    res.status_code = 201 # Status code for "created"
    return res

@app.route('/mail/<mail_id>', methods=['DELETE'])
def delete_mail_route(mail_id: str):
    """
    Summary: Deletes a mail entry from the json file

    Args:
        mail_id (str): The id of the mail entry to delete

    Returns:
        bool: True if the mail was deleted, False otherwise
    """
    # TODO: implement this function
    deleted_successfully = delete_mail(mail_id)
    res = jsonify(deleted_successfully)

    if deleted_successfully:
        res.status_code = 200 # Status code for "ok"
    else:
        res.status_code = 404 # Status code for "resource not found"

    return res
    

@app.route('/mail/<mail_id>', methods=['GET'])
def get_mail_route(mail_id: str):
    """
    Summary: Gets a mail entry from the json file

    Args:
        mail_id (str): The id of the mail entry to get

    Returns:
        dict: A dictionary representing the mail entry if it exists, None otherwise
    """
    res = jsonify(get_mail(mail_id))
    res.status_code = 200 # Status code for "ok"
    return res

@app.route('/mail/inbox/<recipient>', methods=['GET'])
def get_inbox_route(recipient: str):
    """
    Summary: Gets all mail entries for a recipient from the json file

    Args:
        recipient (str): The recipient of the mail

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    res = jsonify(get_inbox(recipient))
    res.status_code = 200
    return res

# TODO: implement a route to get all mail entries for a sender
# HINT: start with something like this:
#   @app.route('/mail/sent/<sender>', ...)
@app.route('/mail/sent/<sender>', methods=['GET'])
def get_sent_route(sender: str):
    """
    Summary: Gets all mail entries sent from a specific sender from the json file

    Args:
        recipient (str): The recipient of the mail

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    res = jsonify(get_sent(sender))
    res.status_code = 200 # Status code for "ok"
    return res


if __name__ == '__main__':
    app.run(port=5000, debug=True)