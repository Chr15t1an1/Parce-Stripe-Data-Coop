pathToInputFile = "public/upload/in.csv"

pathToExportFolder = "/public/export"


import csv




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


# Write to CSV -- Takes in array, returns CSV File





##Export file
# Send Get request with item key in URL






# Trim File


trimedUserInput = trimInput(pathToInputFile)


print(trimedUserInput)



# # Opening Input File
# f = open(pathToInputFile)
# csv_f = csv.reader(f)
#
# # Temporay Store Variable for keeping rows
# temp = []
#
# for row in csv_f:
#     # Catch all Keeping columns
#     #Invoice ID
#     invoiceID = row[0]
#     product = row[1]
#     invoiceDate = row[2]
#     amount = row[3]
#     email = row[16]
#     client = row[24]
#     billingAddress = row[25]
#     billingAddressLineTwo = row[26]
#     CardAddressCity = row[27]
#     CardAddressState = row[28]
#     CardAddressZip =  row[30]
#
#     rowItem = [invoiceID,product,invoiceDate,amount,email,client,billingAddress,billingAddressLineTwo,CardAddressCity,CardAddressState,CardAddressZip]
#
#     temp.append(rowItem)
#
#     # print(rowItem)
#     # print(row)
#
#
#



