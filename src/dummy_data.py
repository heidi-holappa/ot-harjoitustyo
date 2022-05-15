"""Used to create dummy data from command line. User can configure the number
of contacts to be created.

The condition check informs of failure if CONTACT_N < 1 or CONTACT_N > 100.
"""

from services.contact_management import ContactManagement

contact_management = ContactManagement()

CONTACT_N = 10

result, status_msg = contact_management.create_random_contacts(CONTACT_N)

if result:
    print("Dummy data created successfully.")
else:
    print("Data creation failed. Status message: ", status_msg)
