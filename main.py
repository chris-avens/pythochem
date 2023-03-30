import pandas as pd

# Read data from Excel file
data = pd.read_excel("Perry Tables.xlsx")


def unit_convert(initial_unit, desired_unit, magnitude):
    # Find row in data table corresponding to initial unit and desired unit
    row = data[(data['Customary or commonly used unit'] == initial_unit) &
               ((data['SI unit'] == desired_unit) | (data['Alternate SI unit'] == desired_unit))]

    if row.empty:
        row = data[((data['SI unit'] == initial_unit) | (data['Alternate SI unit'] == initial_unit)) &
                   (data['Customary or commonly used unit'] == desired_unit)]

        if row.empty:
            print("Could not find conversion factor for given units.")
        else:
            # Extract conversion factor from row
            conversion_factor = row.iloc[0]['Conversion factor; multiply customary unit by factor to obtain SI unit']
            result = magnitude / conversion_factor
            print(f"{magnitude} {initial_unit} = {round(result,10)} {desired_unit}")
    else:
        # Extract conversion factor from row
        conversion_factor = row.iloc[0]['Conversion factor; multiply customary unit by factor to obtain SI unit']
        result = magnitude * conversion_factor
        print(f"{magnitude} {initial_unit} = {round(result,10)} {desired_unit}")


# Get user input
unit_convert(input("Enter initial unit: "),
             input("Enter desired unit: "),
             float(input("Enter magnitude: ")))
