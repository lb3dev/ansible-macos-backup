#!/usr/bin/python3

import argparse
import copy
import json
from pathlib import Path


def convert_reddit_url(bookmark):
    if 'uri' in bookmark:
        url = bookmark['uri']
        if url.startswith('https://old.reddit.com'):
            compact = '.compact' if url[-1] == '/' else '/.compact'
            bookmark['uri'] = url + compact


def apply_new_ids(bookmarks, count):
    to_apply = count
    if len(bookmarks) == 0:
        return

    for bookmark in bookmarks:
        bookmark['id'] = to_apply

        convert_reddit_url(bookmark)

        if 'children' in bookmark:
            to_apply = apply_new_ids(bookmark['children'], to_apply + 1)
        to_apply += 1

    return to_apply


def get_max_id(item, max_id):
    max_id = max(item['id'], max_id)

    if 'children' in item:
        for bookmark in item['children']:
            max_id = max(get_max_id(bookmark, max_id), max_id)
    return max_id


def remove_guids(bookmarks):
    if len(bookmarks) == 0:
        return

    for bookmark in bookmarks:
        del bookmark['guid']
        if 'children' in bookmark:
            remove_guids(bookmark['children'])


def get_root_item(root, name):
    for item in root['children']:
        if 'guid' in item and item['guid'] == name:
            return item
    return None


def copy_bookmarks(bookmarks):
    copies = copy.deepcopy(bookmarks)
    remove_guids(copies)
    return copies


def add_mobile_bookmarks(input_file):
    input_filepath = Path(input_file)
    basename = input_filepath.stem
    ext = input_filepath.suffix

    with open(input_file) as bookmark_file:
        root = json.load(bookmark_file)
        if 'children' in root:

            # Erase existing mobile bookmarks

            mobile = get_root_item(root, 'mobile______')
            if 'children' in mobile:
                del mobile['children']

            # Deep copy all toolbar bookmarks

            toolbar = get_root_item(root, 'toolbar_____')
            toolbar_bookmarks_copy = copy_bookmarks(toolbar['children'])

            # Retrieve the max id count of the entire json

            max_id = get_max_id(root, 1)

            # Apply new ids to newly copied toolbar bookmarks and assign to mobile

            apply_new_ids(toolbar_bookmarks_copy, max_id + 1)
            mobile['children'] = toolbar_bookmarks_copy

            # Write to new output json

            with open(Path(input_filepath.parent, basename + '-and-mobile' + ext), 'w', encoding='utf-8') as output_file:
                output_json = json.dumps(root, indent=4, ensure_ascii=False)
                output_file.write(output_json)
        else:
            exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Existing Firefox bookmark json file path', required=True)
    args = vars(parser.parse_args())

    add_mobile_bookmarks(args['file'])
