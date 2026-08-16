# main.py
"""Command-line controller for the Multi-File Keyword Search Tool."""

from text_utils import prepare_keyword, is_valid_keyword
from file_utils import (
    search_folder,
    count_matching_files,
    save_results
)

DOCUMENTS_FOLDER = 'documents'
OUTPUT_FILE = 'results/search_results.txt'


def display_results(results, files_checked):
    """Display search results and summary information."""
    print(f'\nFiles checked: {files_checked}')

    if not results:
        print('No result found.')
        return

    print('\nSearch results:')
    for number, result in enumerate(results, start=1):
        print(
            f"{number}. {result['filename']} | "
            f"Line {result['line_number']}"
        )
        print(f"   {result['text']}")

    print('\nMatching files:', count_matching_files(results))
    print('Total matches:', len(results))


def main():
    print('=== Multi-File Keyword Search Tool ===')
    print("Type 'exit' to close the program.")

    while True:
        raw_keyword = input('\nEnter a keyword: ')
        keyword = prepare_keyword(raw_keyword)

        if keyword == 'exit':
            print('Search tool closed.')
            break

        if not is_valid_keyword(keyword):
            print('Keyword cannot be empty.')
            continue

        try:
            results, files_checked = search_folder(
                DOCUMENTS_FOLDER,
                keyword
            )
            display_results(results, files_checked)

            saved_path = save_results(
                results,
                keyword,
                OUTPUT_FILE
            )
            print(f'\nResults saved to: {saved_path}')

        except FileNotFoundError as error:
            print(error)
            print('Create the documents folder and add .txt files.')
        except PermissionError:
            print('Permission denied while accessing project files.')
        except Exception as error:
            print('An unexpected error occurred:', error)


if __name__ == '__main__':
    main()
