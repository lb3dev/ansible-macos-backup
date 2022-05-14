#!/bin/bash

# Script to delete the entire Bitwarden repository without the Untitled folder
# Sample usage:
#
# ./bitwarden-delete.sh
#
# WARNING: THIS WILL FIRST REMOVE ALL ITEMS IN BITWARDEN VAULT BEFORE IMPORT

set -e
set -u
set -o pipefail

if ! command -v bw &> /dev/null; then
    echo "Bitwarden CLI not installed! Exiting script"
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo "jq not installed! Exited script"
    exit 1
fi

# Delete current list of items (excluding the default items in No Folder with folderId = null)

bw list items | jq -c '.[] | select(.folderId != null)' |

while IFS=$"\n" read -r item; do

    BW_ITEM_ID=$(echo "$item" | jq -r '.id')
    BW_ITEM_NAME=$(echo "$item" | jq -r '.name')
    bw delete item $BW_ITEM_ID
    echo "Deleted Item Id: $BW_ITEM_ID - $BW_ITEM_NAME"

done

# Delete current list of folders (excluding the default No Folder with id = null)

bw list folders | jq -c '.[] | select(.id != null)' |

while IFS=$"\n" read -r folder; do

    BW_FOLDER_ID=$(echo "$folder" | jq -r '.id')
    BW_FOLDER_NAME=$(echo "$folder" | jq -r '.name')
    bw delete --permanent folder $BW_FOLDER_ID
    echo "Deleted Folder Id: $BW_FOLDER_ID - $BW_FOLDER_NAME"

done