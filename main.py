
import connect_me
import list
import get
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.modify'


def main():

    # Call the Gmail API - List messages and get them
    service = connect_me.connect()
    messages = list.ListMessagesMatchingQuery(
        service, 'me', 'after:2018/08/20')
    if not messages:
        print('No messages found.')
    else:
        print('Messages:')
        for message in messages:
            titulo = get.GetMimeMessage(service, 'me', message["id"])
            print(titulo)


if __name__ == '__main__':
    main()
