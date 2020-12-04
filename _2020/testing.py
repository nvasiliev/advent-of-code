import io
import pathlib
from contextlib import redirect_stdout


def assert_single(file, main_fn, in_file, out_file):
    print(f'\n--- TEST CASE: {in_file} {out_file}')

    path_prefix = str(pathlib.Path(file).parent.absolute())

    test_cases_template = '{}/data/'.format(path_prefix) + '{file_name}'

    output_holder = io.StringIO()
    with redirect_stdout(output_holder):
        input_file_path = test_cases_template.format(file_name = in_file)
        main_fn(input_file_path)

    result = _to_list(output_holder.getvalue().strip())

    expected_file_path = test_cases_template.format(file_name = out_file)
    with open(expected_file_path) as f:
        expected = _to_list(f.read().strip())
        assert result == expected


def _to_list(file_content: str):
    return [s.strip() for s in file_content.split("\n")]
