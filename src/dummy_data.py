from services.contact_management import ContactManagement

contact_management = ContactManagement()

CONTACT_N = 30

contact_management.create_random_contacts(CONTACT_N)
