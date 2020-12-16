# The Playlist Helper

The purpose of this program is the help make playlist editing for ENCO DAD easier for CapRadio employees. Current Features include:

- Creating a spreadsheet Database of all cuts in Library (from DAD XML file)
- Creating a spreadsheet representation of a playlist
- Creating a text file from a Spreadsheet that can be imported into DAD as a playlist.

## Environment

This was developed using
- Windows 10 Machine on WSL Ubuntu 20.04.
- Python 3.8.5

## Setup
1. run `environ` from root project directory
    ```
    $ . environ
    ```
    You also may have to make it executable. 
    ```
    $ sudo chmod +x environ
    ```
    If you have not set up a python virtual environment, this will do it for you. 

2. Install python library requirements
    ```
    $ pip3 install -r requirements.txt
    ```

3. Run once with no input.
    ```
    $ python3 -m run
    ```
    This will create all necessary folders for input and output. 

4. run DCL commands in ENCO DAD system to generate XML files (if needed)

    - `EXTRACT XML CUTS` to generate an XML file with info for the *entire* library (this may be very large)
    - `EXTRACT XML PLAYLIST <playlist name>` to generate an XML representation of a specific playlist

5. If needed, create an Excel file for a specific playlist that you are trying to create (NOTE: excel files that are output from step 4 can be used as input for this step)

6. Place files into the appropriate input folders
    
    - The `./input/excel_to_text_playlist` folder is for spreadsheet to text import file conversion
    - The `./input/xml_cuts_to_database` folder is for an entire XML cuts library to be converted to spreadsheet
    - The `./input/xml_to_excel` folder is for XML playlists to be converted to Excel.

7. Run again to process everything put into the input folders
    ```
    $ python3 -m run
    ```
    (NOTE: This application will currently not move files out of the input folders)

## Possible Feature Ideas
- Proper Database for Cut info
- Send DCL to DAD via raw UDP to trigger generation of XML files.
- Utilize `INJECT XML` to change playlists and cuts
- Google Sheets integration
- Ability to get `x` number of sequential unused cut numbers
- Ability to get list of all available cut numbers.
- Slack integration

## Contact
<james.tejada@capradio.org>
