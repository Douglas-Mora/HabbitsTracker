#------- Required modules
import requests
from datetime import datetime

#------- This is for rectifying a run.

TOKEN = "QEWrqqwrSDqwgtgetrStwertrdgthyt" #I created this Token when creating the user.
pixel_creation_endpoint = "https://pixe.la/v1/users/douglas-mora/graphs/graph1"


def date_for_pixela():
    date_response = input("Wanna correct a past run? Type 'Y' or 'N'?: ")
    if date_response == 'Y':
        past_year = input("Year (format must be 'YYYY'): ")
        past_month = input("Month (format must be 'MM'): ")
        past_day = input("Day (format must be 'DD'): ")
        run_in_km = input("Run in KM (format must be '##'): ")
        return f"{past_year}{past_month}{past_day}", run_in_km
    elif date_response == 'N':
        date = datetime.now()
        year = date.year
        month = date.month
        day = date.day
        if int(month) < 10:
            month = f"0{str(month)}"
        if int(day) < 10:
            day = f"0{str(day)}"
        run_in_km = input("Run in KM (format must be '##'): ")
        return f"{year}{month}{day}", run_in_km
    

date_to_use, run_km = date_for_pixela()



correcting_entry = {
    "quantity": run_km,
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.put(url=f"{pixel_creation_endpoint}/{date_to_use}",json=correcting_entry,headers=headers)
print(response.text)
