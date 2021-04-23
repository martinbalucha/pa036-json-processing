from faker import Faker
import json
import time

"""
Generate fake .json document of invoices.
To change the number of generated invoices, change the parameter of NUMBER_OF_INVOICES.
"""
NUMBER_OF_INVOICES = 2000000
FILE_NAME = 'fake_invoices.json'

fake = Faker(['cs_CZ'])


def fake_json_generator(length=1000):
    for i in range(1, length + 1):
        price_without_tax = fake.random_number(digits=5)
        including_tax = fake.boolean(chance_of_getting_true=75)

        if including_tax:
            tax = round(0.2 * price_without_tax, 2)
        else:
            tax = 0

        total_price = price_without_tax + tax

        items_count = fake.pyint(1, 5)
        items = []
        for _ in range(items_count):
            items.append({"catalogId": fake.uuid4().upper()[0:6], "itemName": fake.word(), "price": fake.pyint()})

        yield {
            "id": i,
            "invoiceNumber": fake.numerify("%######"),
            "issueDate": fake.date(),
            "issueTime": fake.time(),
            "includingTax": including_tax,
            "priceWithoutTax": price_without_tax,
            "tax": tax,
            "totalPrice": total_price,
            "issuerDetails": {
                "name": fake.company(),
                "streetAddress": fake.street_address(),
                "city": fake.city(),
                "zipCode": fake.postcode(),
                "country": fake.country(),
                "phoneNumber": fake.phone_number(),
                "email": fake.company_email()
            },
            "customerDetails": {
                "name": fake.name(),
                "companyName": fake.random_element((fake.company(), None)),
                "streetAddress": fake.street_address(),
                "city": fake.city(),
                "zipCode": fake.postcode(),
                "country": fake.country(),
                "phoneNumber": fake.phone_number(),
                "email": fake.email()
            },
            "description": items,
            "additionalInformation": fake.random_element((fake.sentence(), None))
        }


start = time.time()
fake_data = fake_json_generator(NUMBER_OF_INVOICES)

with open(f"../data/{FILE_NAME}", 'w') as output:
    output.write('[')
    for invoice in fake_data:
        json.dump(invoice, output, indent=4, ensure_ascii=False)
        if invoice.get('id') != NUMBER_OF_INVOICES:
            output.write(",")
    output.write(']')

end = time.time()
print(end - start)
