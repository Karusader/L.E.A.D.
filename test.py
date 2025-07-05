
from dataclasses import dataclass
@dataclass
class DigiKeyPackItem:
    DigiKeyPartNumber: str
    Quantity: int


testResponse = {
  "SalesorderId": 12345,
  "InvoiceId": 12345,
  "PackListNumber": 1,
  "PackListDetails": [
    {
      "DigiKeyPartNumber": "P189-ND",
      "Quantity": 5
    },
    {
      "DigiKeyPartNumber": "P189-ND@222",
      "Quantity": 5
    },
    {
      "DigiKeyPartNumber": "P189-NAAD",
      "Quantity": 5
    }
  ]
}

partList: (DigiKeyPackItem)

partList[0]
#partList = tuple(testResponse["PackListDetails"])



print(partList)

