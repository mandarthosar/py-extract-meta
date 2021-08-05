import pandas as pd
import getTitleDesc
import extractDomainFromEmail
import extractFilename

# Declare input file name
path = input("Enter your full path of CSV file: ")
filename = extractFilename.name(path)
outputfile = "output-"+str(filename) # The output file will be stored in the same directory as of the code and will start with 'output-'

df = pd.read_csv(filename)
df_new = pd.DataFrame()

for index, row in df.iterrows():
    email = row["CONTACT EMAIL"]
    domain = extractDomainFromEmail.getDomain(email)
    title, description = getTitleDesc.extracttext(domain)
    row["Domain"] = domain
    row["Title"] = title
    row["Meta Description"] = description
    df_new = df_new.append(row.to_frame().T) # We are converting series to dataframe here
    
    print("Done with",index+1,"records.\n")

df_new.to_csv(outputfile)