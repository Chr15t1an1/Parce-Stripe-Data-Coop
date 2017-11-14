pathToInputFile = "public/upload/in.csv"

pathToExportFolder = "/public/export"


import csv
import re




#Functions
##Trim file -- Takes in CSV File, returns array
def trimInput (filePath):
    # Opening Input File
    f = open(filePath)
    csv_f = csv.reader(f)

    # Temporay Store Variable for keeping rows
    temp = []

    for row in csv_f:
        # Catch all Keeping columns
        # Invoice ID
        invoiceID = row[0]
        product = row[1]
        invoiceDate = row[2]
        amount = row[3]
        email = row[16]
        client = row[24]
        billingAddress = row[25]
        billingAddressLineTwo = row[26]
        CardAddressCity = row[27]
        CardAddressState = row[28]
        CardAddressZip = row[30]

        rowItem = [invoiceID, product, invoiceDate, amount, email, client, billingAddress, billingAddressLineTwo,
                   CardAddressCity, CardAddressState, CardAddressZip]

        temp.append(rowItem)

    return temp





##Parce File


def parceNumOfHours(productDescription):
    #print(productDescription)
    num = re.findall(r'([\ ][0-9][\ ])+', productDescription)
    # Convert list to string and strip whitespace.
    num = ''.join(num)
    num = num.strip()
    return num












# Write to CSV -- Takes in array, returns CSV File





##Export file
# Send Get request with item key in URL






# Trim File
trimedUserInput = trimInput(pathToInputFile)


#print(trimedUserInput)


# trimedUserInput

parcedOutput = []

for row in trimedUserInput[1:]:
    productPrice = float(row[3])
    nmlsFee = int(parceNumOfHours(row[1]))*1.5
    adjustedPrice = productPrice - nmlsFee

    initRow = [row[0], row[1], row[2], str(adjustedPrice), row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
    parcedOutput.append(initRow)



    saleId = row[0]
    bankingFee = "NMLS Banking Fee"
    InvoiceDate = ''
    secondrowAmount = nmlsFee
    email = ''
    name = ''
    adrOne = ''
    adrTwo = ''
    cardCity = ''
    cardState = ''
    cardZip = ''


    bankingFeeRow = [saleId, bankingFee, InvoiceDate,secondrowAmount,email , name, adrOne , adrTwo , cardCity , cardState , cardZip ]



    print("--")
    print(productPrice)
    print(nmlsFee)
    print(adjustedPrice)
    print("--")



    print(row)
    print(initRow)
    print(bankingFeeRow)


#
#     print(row)
#
#     feeRow = [saleId,bankingFee]
#
#     parcedOutput.append(feeRow)
#
#     print(feeRow)
#
#     print(parceNumOfHours(row[1]))

    #print(Amount)



##Parce File
# Every record insert a line item.
# Copy the Id -- Set ID
# Set Product/Service to NMLS Banking Fee

# Set ammount by calculating it.
## Parce the Product/Service for the # of hours
## Stip spaces and multiply by 1.50
# /([\ ][0-9][\ ])+/g













