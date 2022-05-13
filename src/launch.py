from gpg import Data
from ui import gui
from repositories.user_repository import default_user_repository

class DatabaseInitalizationError(Exception):
    pass

try:
    default_user_repository.fetch_all_users()
except(DatabaseInitalizationError):
    print("""There was an error with the database.
            Did you remember to run 'Poetry run invoke build'
            before launching the application?""")

gui.main()
