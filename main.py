import pandas as pd

# Read data from Excel file
data = pd.read_excel("Perry Tables.xlsx")
# relative path is not recognized if using scratch in python


def unit_convert(initial_unit, desired_unit, magnitude):
    # Find row in data table corresponding to initial unit and desired unit
    temp_units = ['Kelvin', 'Rankine', 'Celsius', 'Fahrenheit']

    row = data[(data['Customary or commonly used unit'] == initial_unit) &
               ((data['SI unit'] == desired_unit) | (data['Alternate SI unit'] == desired_unit))]

    if initial_unit in temp_units or desired_unit in temp_units:
        match initial_unit + ' to ' + desired_unit:
            case 'Kelvin to Rankine':
                result = magnitude * 1.8
            case 'Kelvin to Celsius':
                result = magnitude - 273.15
            case 'Kelvin to Fahrenheit':
                result = magnitude * 1.8 - 459.67
            case 'Celsius to Rankine':
                result = magnitude * 1.8 + 32 + 459.67
            case 'Celsius to Kelvin':
                result = magnitude + 273.15
            case 'Celsius to Fahrenheit':
                result = magnitude * 1.8 + 32
            case 'Rankine to Kelvin':
                result = magnitude / 1.8
            case 'Rankine to Celsius':
                result = (magnitude - 32 - 459.67) / 1.8
            case 'Rankine to Fahrenheit':
                result = magnitude - 459.67
            case 'Fahrenheit to Rankine':
                result = magnitude + 459.67
            case 'Fahrenheit to Kelvin':
                result = (magnitude + 459.67) / 1.8
            case 'Fahrenheit to Celsius':
                result = (magnitude - 32) / 1.8
            case True:
                print("Could not find conversion factor for given units.")
    elif row.empty:
        row = data[((data['SI unit'] == initial_unit) | (data['Alternate SI unit'] == initial_unit)) &
                   (data['Customary or commonly used unit'] == desired_unit)]

        if row.empty:
            print("Could not find conversion factor for given units.")
        else:
            # Extract conversion factor from row
            conversion_factor = row.iloc[0]['Conversion factor; multiply customary unit by factor to obtain SI unit']
            result = magnitude / conversion_factor
    else:
        # Extract conversion factor from row
        conversion_factor = row.iloc[0]['Conversion factor; multiply customary unit by factor to obtain SI unit']
        result = magnitude * conversion_factor

    return round(result, 10)

