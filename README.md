# Simple TODO API

This is very simple TODO app API.  

## Installing / Getting started

A quick introduction of the minimal setup you need to get this backend running.

```shell
git clone https://github.com/RMaster121/simple-TODO-app.git
cd simple-TODO-app/
python pip install -r requirements.txt
python manage.py runserver
```

When you execute the code above, the server should be running.


## Features

You can do few operations on your notes: GET, POST, UPDATE, DELETE.
* You can create 3 types of notes:
  * List note
  * Text note
  * URL note
* List notes contains items with text and check status.
* You can change order of these items.

* The URL value field has implemented validating. It is handled by the Django Rest Framework model.
# Usage

## GET todo notes
Type: `GET`  
URL: `{server_url}/api/todo-items/`

You can filter data to suit your needs.  

Example response:  
```
[
    {
        "id": 1,
        "type": "L",
        "title": "Test list note #1",
        "due_date": null,
        "created_at": "2022-08-07T09:22:33.048777Z",
        "text_value": "",
        "url_value": "",
        "list_items": [
            {
                "id": 1,
                "value": "First list note",
                "checked": false,
                "position": 3
            },
            {
                "id": 2,
                "value": "Second list note",
                "checked": false,
                "position": 2
            },
            {
                "id": 5,
                "value": "Third list value",
                "checked": false,
                "position": 1
            },
            {
                "id": 6,
                "value": "Fourth list value",
                "checked": false,
                "position": 0
            }
        ]
    },
]
```

### Filter arguments:
Filter formula is very simple, it uses standard URL encoding patterns.

Add `?` char to the end of the URL.  
Every space has to be replaced with the `+` char.  
Arguments are separated by `&` char.  

#### Possible arguments:
* Search  
  Example:
  Search for notes containing text "ABC"
  URL: `{server_url}/api/todo-items/?search=ABC`
* Order  
  Order by creation date (ascending/descending)  
  Ascending = "created_at"  
  Descending = "-created_at"  
  >Example:  
  >Order descending:  
  >URL: `{server_url}/api/todo-items/?ordering=-created_at`
* Filter  
  You can filter by type and creation date.    
  > Filter by type:  
  There are 3 types of notes: L-List, T-Text, U-URL.  
  Get all URL notes:  
  URL: `{server_url}/api/todo-items/?type=U`

  > Filter by creation date range:  
  start_date=mm/dd/yyyy (Created before mm/dd/yyyy)  
  end_date=mm/dd/yyyy (Created after mm/dd/yyyy)  
  Replace every `/` with `%2F`  
  Example:  
  Get all items created between 30/12/2020 and 01/12/2023  
  URL: `{server_url}/api/todo-items/?end_date=12%2F30%2F2020&start_date=12%2F01%2F2023`

  > Filter by deadline status  
  There are 3 status choices:  
  > * Deadline before now
  > * Deadline after now
  > * No Deadline  
    
  > deadline_type={past|future|none}  
  Example:  
  Get all items with deadline in past date  
  URL: `{server_url}/api/todo-items/?deadline_type=past`
  

## POST todo note
General fields:
* type = L (List), T (Text), U (URL) (Type of note)
* title = String (Title of note)
* due_date = "dd-mm-yyyy" (Not required, it describes deadline date)

Fields related to the type of note are required.  
Fields related to the other types are not required, although you can provide them.
### List note
Value field: `list_items`  
Format:  
```
{
    "type": "L",
    "title": "Example list note",
    "due_date": "2022-12-30",
    "list_items": [
        {
            "value": "First list value",
            "checked": true
        },
        {
            "value": "Second list value"
        }
    ]
}
```

### Text note
Value field: `text_value`  
Format:  
```
{
    "type": "T",
    "title": "Test text note #1",
    "text_value": "Test text value",
    "due_date": null
}
```

### URL note
Value field: `url_value`  
Format:  
```
{
    "type": "U",
    "title": "Example url note",
    "due_date": null,
    "url_value": "https://www.google.com"
}
```
<strong>Important!!! </strong> There is URL validation, so you have to provide valid URL.  Otherwise you will get an error.

## Delete note
Type: `DELETE`  
URL: `{server_url}/api/todo-items/{note-id}`  

It also deletes list items related to note.

## Update note
Type: `PUT`  
URL: `{server_url}/api/todo-items/{note-id}`  
Format: It is very similar to the `POST` format.  

<strong>How to mark list item as checked?</strong>  
Change `checked` field value to `true`.

<strong>How to change position of list item?</strong>  
Update it's `position` field to position you want.  
It will replace item at the new position with item at the current position.

# Database credenitals
SQL:  
email: admin@admin.admin  
login: admin  
password: somesaypeople  
