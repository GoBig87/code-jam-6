import yaml
# from passlib.context import CryptContext


class Database:

    message_template = {
        'user': None,
        'time': None,
        'sent': False,
        'party': [],
        'content': None,
        'attachment': [],
    }

    def __init__(self, users_filename, messages):
        self.users = users_filename
        self.hash_table = {}
        self.messages = messages
        self.load()

    @staticmethod
    def _encode(source):
        # TODO: This can be replaced with a more sophisticated method if we want/ have time
        return source

    def load(self):
        with open(self.users) as f:
            for line in f:
                user_hash, hashed_password = line.split(';')
                self.hash_table[user_hash] = hashed_password

    def register_user(self, user, password):
        """Check that user doesn't already exist, then check password strength requirements"""
        user_hash, pass_hash = self._encode(user), self._encode(password)

        if user_hash in self.hash_table:
            raise ValueError('Username already exists')
        self.check_password_strength(password)

        self.hash_table[user_hash] = pass_hash
        with open(self.users, 'a') as f:
            f.write(f'{user_hash};{pass_hash}\n')

    def validate_login(self, user, password):
        """Check hash table when login is attempted"""
        try:
            hashed_password = self.hash_table[self._encode(user)]
        except KeyError:
            return False
        else:
            return hashed_password == self._encode(password)

    def dump_message(self, **kwargs):
        """ First update the keys which have values passed and use default values for others.
        Format contents of the message dictionary into text.
        Finally, dump the formatted string to local database.
        """
        message = {**self.message_template, **kwargs}
        print(message)
        message_str = '- ' + '\n  '.join(f'{k}: {v}' for k, v in message.items()) + '\n\n'

        with open(self.messages, 'a') as f:
            f.write(message_str)

    def yield_messages(self, userhash):
        """Called when a user loads their messages.
        Uses yaml to load dictionaries representing sent and received messages.
        """

        for messages in yaml.load_all(self.messages, Loader=yaml.Loader):
            if userhash == messages['user']:  # User id matches
                yield messages

    def check_password_strength(self, password):
        if password is ...:  # TODO
            raise ...
