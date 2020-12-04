import io
import pathlib
from contextlib import redirect_stdout


def assert_single(file, main_fn, test_case_number):
    print('\n--- TEST CASE NUMBER: {}'.format(test_case_number))

    path_prefix = str(pathlib.Path(file).parent.absolute())

    test_cases_template = '{}/data/'.format(path_prefix) + '{n}_{file_name}'

    output_holder = io.StringIO()
    with redirect_stdout(output_holder):
        input_file_path = test_cases_template.format(n = test_case_number, file_name = 'in.txt')
        main_fn(input_file_path)

    result = _to_list(output_holder.getvalue().strip())

    expected_file_path = test_cases_template.format(n = test_case_number, file_name = 'out.txt')
    with open(expected_file_path) as f:
        expected = _to_list(f.read().strip())
        assert result == expected


def _to_list(file_content: str):
    return [s.strip() for s in file_content.split("\n")]
