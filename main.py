from hubspot import HubSpot
from pprint import pprint

from hubspot.crm.contacts import ApiException

#from hubspot.crm.contacts import SimplePublicObjectInput, ApiException
from hubspot.crm.deals import SimplePublicObjectInput, ApiException

api_client = HubSpot(access_token='pat-eu1-9492283a-09bc-4833-9dca-8c643d662007')

all_contacts = api_client.crm.contacts.get_all()

all_deals = api_client.crm.deals.get_all()

#print(all_deals)

response = []


def main():
    
    for contact in all_contacts:

        phone_number = validate_phone_number(contact)        

        if phone_number is None:

            #agregar numero telefonico al contacto
            response.append(add_new_number(contact)) 

            #create_deal(5)
        
        print(response)
    
    
           
def create_deal(id):

    properties = {
        "amount": "1500.00",
        "dealstage": "presentationscheduled",
        "hubspot_owner_id": id,
        "author" : "samuel Beltran"
        
    }

    simple_public_object_input = SimplePublicObjectInput(properties=properties)

    try:

        api_response = api_client.crm.deals.basic_api.create(simple_public_object_input=simple_public_object_input)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling basic_api->create: %s\n" % e)


def add_new_number(contact):

    id = contact.id
    upgradecontact = contact.properties
    upgradecontact.update({"phone":660049971})    
    return upgradecontact
    

def validate_phone_number(contact):

    return contact.properties.get("phone")

main()

