from services.contact_management import ContactManagement

contact_management = ContactManagement()

CONTACT_N = 30

result, status_msg = contact_management.create_random_contacts(CONTACT_N)

if result:
    print("Dummy data created successfully.")
else:
    print("Data creation failed. Status message: ", status_msg)
