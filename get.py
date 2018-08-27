import base64
import email
from apiclient import errors


def get_subject_inbox(service, user_id, msg_id):
    """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
    try:
        message = service.users().messages().get(
            userId=user_id, id=msg_id).execute()
        headerslist = message['payload']['headers']    # Cria lista de headers
        for i in headerslist:   # itera dentro da lista
            nameindict = i["name"]  # Encontra os campos nome
            if nameindict == "Subject":    # Caso o campo nome seja o titulo
                return(i["value"])   # retorna o valor em "name"
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def GetMimeMessage(service, user_id, msg_id):
    """Get a Message and use it to create a MIME Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A MIME Message, consisting of data from Message.
  """
    try:
        message = service.users().messages().get(
            userId=user_id, id=msg_id, format='raw').execute()

        print('Message snippet: %s' % message['snippet'])
        msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
        mime_msg = email.message_from_string(msg_str)
        return mime_msg
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
