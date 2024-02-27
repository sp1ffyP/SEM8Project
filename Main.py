from CSVToJSONConverter import CSVToJSONConverter
import os

# (Sam) Check that /Input and /Output exist
if not os.path.exists("Input"):
    os.makedirs("Input")
if not os.path.exists("Output"):
    os.makedirs("Output")

print("Ensure all the files you wish to convert are in the \"Input\" directory, and press ENTER when ready.")
input("")

print("Converting files...")
converter = CSVToJSONConverter("Input", "Output")
converter.convert()
