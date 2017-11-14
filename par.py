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
    #numWspaces =  re.compile('/([\ ][0-9][\ ])+/g',productDescription)
    #numWspaces = re.search(r"([\ ][0-9][\ ])", productDescription)
    #regExpre = re.compile('/([\ ][0-9][\ ])+/')
    regExpre = re.compile('([\ ][0-9][\ ])+')

    #print(regExpre.match("[series] 2 Hour OR SAFE CE 2017 Online"))
    #print(regExpre.search("[series] 1 Hour KY SAFE CE 2017 Online"))

    numWspaces = regExpre.search(productDescription)

    print(numWspaces)













# Write to CSV -- Takes in array, returns CSV File





##Export file
# Send Get request with item key in URL






# Trim File


trimedUserInput = trimInput(pathToInputFile)


# print(trimedUserInput)


# trimedUserInput

parcedOutput = []

for row in trimedUserInput:

    parcedOutput.append(row)

    saleId = row[0]
    bankingFee = row[1]


    print(row)

    feeRow = [saleId,bankingFee]

    parcedOutput.append(feeRow)

    print(feeRow)

    parceNumOfHours(bankingFee)




##Parce File
# Every record insert a line item.
# Copy the Id -- Set ID
# Set Product/Service to NMLS Banking Fee

# Set ammount by calculating it.
## Parce the Product/Service for the # of hours
## Stip spaces and multiply by 1.50
# /([\ ][0-9][\ ])+/g













