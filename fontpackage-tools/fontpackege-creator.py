import sys
import json
from fontTools.ttLib import TTFont

def extract_metadata(font_path):
    # Load the font file using fonttools
    font = TTFont(font_path)

    # Initialize the JSON structure with default values
    data = {
        "name": font['name'].getDebugName(1) if 'name' in font else "My Font Family",
        "packagekey": font['name'].getDebugName(3) if 'name' in font else "My Font Family",
        "type": "family",
        "version": font['name'].getDebugName(5) if 'name' in font else "",
        "status": "",
        "authors": ["", ""],
        "license": "",
        "copyright": font['name'].getDebugName(0) if 'name' in font else "",
        "category": "",
        "licenseFile":  font['name'].getDebugName(14) if 'name' in font else "",
        "licenseDescription": font['name'].getDebugName(13) if 'name' in font else "",
        "description": font['name'].getDebugName(10) if 'name' in font else "",
        "repository": {
            "url": "",
            "type": "git"
        },
        "homepageUrl": "",
        "issuesUrl": "",
        "datePublished": "",
        "fontlog": "",
        "foundry": {
            "name": font['name'].getDebugName(8) if 'name' in font else "",
            "email": "",
            "url": "",
            "vendorId": ""
        },
        "designers": [
            {"name":  font['name'].getDebugName(9) if 'name' in font else "", "email": "", "url": ""},
            {"name": "", "email": "", "url": ""},
            {"name": "", "email": "", "url": ""}
        ],
        "private": "",
        "maintenance": {
            "status": "",
            "comment": ""
        },
        "versionsProvider": "",
        "tools": "",
        "tags": [
            {
                "style": "",
                "contrast": "",
                "width": "",
                "bodyHeight": "",
                "intendedUsage": "",
                "figures": "",
                "languages": "",
                "relatedFonts": ""
            }
        ],
        "displayTexts": [
            {"en_US": font['name'].getDebugName(19) if 'name' in font else ""},
            {"si_LK": ""},
            {"dv_IN": ""}
        ],
        "links": [
            {
                "fontInUse": "",
                "googleFonts": "",
                "fontLibraryOrg": "",
                "typekit": ""
            }
        ],
        "fonts": [
            {
                "name": font['name'].getDebugName(4) if 'name' in font else "",
                "path": font_path,
                "style": "",
                "weight": "",
                "fullName": font['name'].getDebugName(4) if 'name' in font else "",
                "previewImage": "",
                "protected": "",
                "purpose": "",
                "variableFont": "",
                "format": "OTF" if font.flavor == 'cff' else "TTF",
                "free": ""
            }
        ]
    }

    return data

def main():
    # Check if the font file path is given as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <font_path>")
        sys.exit(1)

    font_path = sys.argv[1]
    metadata = extract_metadata(font_path)

    # Write the metadata to the output JSON file
    with open("fontpackage.json", "w") as f:
        json.dump(metadata, f, indent=4)

    print("Font metadata extracted and written to fontpackage.json")

if __name__ == "__main__":
    main()
