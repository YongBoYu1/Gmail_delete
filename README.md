# Gmail_delete
This python script delete certain gmails from your inbox.

# Requirement
- Go to[ Google Developer Console](https://console.cloud.google.com)
- Create project an enable the gmail api
- Download crendeital(client_scret) json
- First run to generate the token.json
- The code will work afterwards.

# Common Search Operators:

- subject: Searches for emails with a specific subject

- from: Searches for emails from a specific sender

- to: Searches for emails sent to a specific recipient

- label: Searches for emails with a specific label

- is: Searches for emails with a specific status (e.g., is:unread)

- after: and before:: Searches for emails within a date range

# Common Operation for service.users().messages() in the Gmail API:

- Get a message:
Use messages().get() to retrieve a specific message by its ID.

- List messages:
Use messages().list() to get a list of messages, optionally filtered by a query.

- Delete a message:
Use messages().delete() to permanently remove a message.

- Modify message labels:
Use messages().modify() to add or remove labels from a message.

- Send a message:
Use messages().send() to send a new email message.

- Get message attachments:
Use messages().attachments().get() to retrieve attachments from a message.

- Insert a message:
Use messages().insert() to add a message to the mailbox without sending it.

- Import a message:
Use messages().import_() to import a message into the mailbox.

- Batch modify messages:
Use messages().batchModify() to modify labels for multiple messages at once.

- Trash a message:
Use messages().trash() to move a message to the trash.

- Untrash a message:
Use messages().untrash() to remove a message from the trash.