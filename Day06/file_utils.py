# file_utils.py
"""Utility functions for folder scanning, file searching, and saving results."""

import os
from datetime import datetime

from text_utils import contains_keyword


def get_text_files(folder_path):
    """Return full paths for valid .txt files in a folder."""
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(
            f'Documents folder not found: {folder_path}'
        )

    text_files = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.lower().endswith('.txt'):
            text_files.append(file_path)

    text_files.sort()
    return text_files


def search_file(file_path, keyword):
    """Search one text file and return result dictionaries."""
    matches = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            clean_line = line.strip()
            if clean_line == '':
                continue
            if contains_keyword(clean_line, keyword):
                matches.append({
                    'filename': os.path.basename(file_path),
                    'line_number': line_number,
                    'text': clean_line
                })
    return matches


def search_folder(folder_path, keyword):
    """Search every .txt file and return all results."""
    all_results = []
    text_files = get_text_files(folder_path)

    for file_path in text_files:
        try:
            file_results = search_file(file_path, keyword)
            all_results.extend(file_results)
        except PermissionError:
            print(f'Permission denied: {file_path}')
        except UnicodeDecodeError:
            print(f'Could not read as UTF-8: {file_path}')

    return all_results, len(text_files)


def count_matching_files(results):
    """Return the number of unique matching filenames."""
    filenames = {result['filename'] for result in results}
    return len(filenames)


def save_results(results, keyword, output_path):
    """Save search information and return the output path."""
    output_folder = os.path.dirname(output_path)
    if output_folder:
        os.makedirs(output_folder, exist_ok=True)

    matching_files = count_matching_files(results)
    searched_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write('MULTI-FILE KEYWORD SEARCH RESULTS\n')
        file.write('=' * 40 + '\n')
        file.write(f'Keyword: {keyword}\n')
        file.write(f'Searched at: {searched_at}\n')
        file.write(f'Matching files: {matching_files}\n')
        file.write(f'Total matches: {len(results)}\n\n')

        if not results:
            file.write('No result found.\n')
        else:
            for number, result in enumerate(results, start=1):
                file.write(
                    f"{number}. {result['filename']} | "
                    f"Line {result['line_number']}\n"
                )
                file.write(f"   {result['text']}\n\n")

    return output_path


if __name__ == '__main__':
    test_results, total_files = search_folder('documents', 'python')
    print('Files checked:', total_files)
    print('Matches:', len(test_results))
