from ui import gui
from repositories.user_repository import UserRepository
from repositories.contact_data_repository import ContactDataRepository
from database_connection import get_database_connection



# text_based_ui.TextBasedUi().start()

# Initialize repositories
user_repository = UserRepository(get_database_connection())
contact_repository = ContactDataRepository(get_database_connection())
# For testing purposes
#users = user_repository.fetch_all_users()
gui.main()
