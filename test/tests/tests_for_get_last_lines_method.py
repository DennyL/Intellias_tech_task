import pytest
from test.utils.helpers import Helpers
from src.some_api import SomeApi


@pytest.mark.parametrize('path_to_file', ('testdata/text_files/text_file.txt',))
@pytest.mark.parametrize('line_expected', ('from a callable.\n',))
def test_get_one_last_line_in_file(capsys, path_to_file, line_expected):
    """
        verifies, if the get_last_lines() prints exactly the last line from the file given
    """
    SomeApi.get_last_lines(path_to_file, 1)
    captured = capsys.readouterr()
    assert captured.out == line_expected


@pytest.mark.parametrize('path_to_file', ('testdata/text_files/text_file.txt',))
@pytest.mark.parametrize('ordered_lines_expected', ('it allows you to extract\nsignature information\nfrom a callable.\n',))
def test_get_three_last_lines_in_file(capsys, path_to_file, ordered_lines_expected):
    """
        verifies, if the get_last_lines method
        prints the last three lines from the file given, and in correct order
    """
    SomeApi.get_last_lines(path_to_file, 3)
    captured = capsys.readouterr()
    assert captured.out == ordered_lines_expected


@pytest.mark.parametrize('path_to_file', ('testdata/text_files/text_file.txt',))
@pytest.mark.parametrize('qty_of_last_lines', (19,))
def test_get_exact_number_of_lines_in_file(capsys, path_to_file, qty_of_last_lines):
    """
        verifies, if the get_last_lines method prints the entire content of a file given,
        in case the number of last lines passed is equal to the number of lines in the file
    """
    SomeApi.get_last_lines(path_to_file, qty_of_last_lines)
    captured = capsys.readouterr()
    file_content = Helpers.get_content_of_text_file(path_to_file)
    assert captured.out == file_content


@pytest.mark.parametrize('path_to_file', ('testdata/text_files/text_file.txt',))
@pytest.mark.parametrize('qty_of_last_lines', (20,))
def test_get_exceeding_number_of_lines_in_file(capsys, path_to_file, qty_of_last_lines):
    """
        verifies, if the get_last_lines method prints the entire content of a file given,
        in case the number of last lines passed exceeds the number of lines in the file
    """
    SomeApi.get_last_lines(path_to_file, qty_of_last_lines)
    captured = capsys.readouterr()
    file_content = Helpers.get_content_of_text_file(path_to_file)
    assert captured.out == file_content


@pytest.mark.parametrize('path_to_file', ('testdata/text_files/text_file_empty.txt',))
@pytest.mark.parametrize('expected_output', ('*** Warning! The file is empty ***\n',))
def test_get_lines_from_empty_file(capsys, path_to_file, expected_output):
    """
        verifies, if the get_last_lines method prints the warning specified,
        in case the target file is empty
    """
    SomeApi.get_last_lines(path_to_file, 1)
    captured = capsys.readouterr()
    assert captured.out == expected_output


@pytest.mark.parametrize('path_to_file', ('testdata/text_files/text_file.txt',))
@pytest.mark.parametrize('qty_of_last_lines', (-1, 0, "1", 1.5))
@pytest.mark.parametrize('expected_output', ('*** Warning! Incorrect input ***\n',))
def test_get_lines_with_incorrect_qty_input(capsys, path_to_file, qty_of_last_lines, expected_output):
    """
        verifies, if the get_last_lines method prints the warning specified,
        in case the number of last lines is passed incorrect value
    """
    SomeApi.get_last_lines(path_to_file, qty_of_last_lines)
    captured = capsys.readouterr()
    assert captured.out == expected_output


@pytest.mark.parametrize('path_to_file', ('testdata/text_files/txet_flie.txt',))
@pytest.mark.parametrize('expected_output', ('*** Error! File not found ***\n',))
def test_get_line_from_not_existing_file(capsys, path_to_file, expected_output):
    """
        verifies, if the get_last_lines method prints a "File not found" message,
        if the path passed as a parameter leads to a not existing file
    """
    SomeApi.get_last_lines(path_to_file, 1)
    captured = capsys.readouterr()
    assert captured.out == expected_output


@pytest.mark.parametrize('path_to_file', ('testdata/text_files/picture.jpg',))
@pytest.mark.parametrize('expected_output', ('*** Error! Cannot read the file ***\n',))
def test_get_line_from_not_text_file(capsys, path_to_file, expected_output):
    """
        verifies, if the get_last_lines method prints a "Error! Cannot read the file" message,
        if the path passed as a parameter leads to not a text file
    """
    SomeApi.get_last_lines(path_to_file, 1)
    captured = capsys.readouterr()
    assert captured.out == expected_output
