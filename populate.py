import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import scraper

# Allows read + write
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of the job spreadsheet
SPREADSHEET_ID = "1mYjMrgk00FdvQ_SGBdPBSFcdTuYWzUpzKBmnJMgvoS8"
SAMPLE_RANGE_NAME = "Sheet1!A2:D2"


def main():
  
  # Try credentials in token.json
  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  
  # Login + update credentials if token is invalid
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = [
        ["Hirexe", "Software Engineer", "Yes", "100k"]
    ]

    body = {"values": values}

    # Write to spreadsheet (A2 through D2)
    sheet.values().update(
        spreadsheetId=SPREADSHEET_ID,
        range="Sheet1!A2:D2",  # Specify A2 through D2
        valueInputOption="RAW",
        body=body,
    ).execute()
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()