import pytest

from pathlib import Path

BASE_DIR = Path(__name__).absolute().parent
MAIN_DIR = BASE_DIR / 'pep_parse'


@pytest.fixture
def results_dir():
    results_dir = [
        d for d in BASE_DIR.iterdir() if d.is_dir() and d.name == 'results'
    ]
    results_dir += [
        d for d in MAIN_DIR.iterdir() if d.is_dir() and d.name == 'results'
    ]
    return results_dir


def test_results_dir_exists(results_dir):
    assert len(results_dir), (
        'Не обнаружена папка с результатами работы парсинга - results'
    )


def test_csv_files(results_dir):
    csv_files = [
        file for file in results_dir[0].iterdir() if file.glob('*.csv')
    ]

    assert len(csv_files), (
        'В папке results не обнаружено csv файлов. '
        'Пожалуйста сложите результаты работы парсера в папку '
        'results чтобы ревьюер мог их проверить.'
    )
    assert not len(csv_files) < 2, (
        'В папке results обнаружено меньше 2 csv файлов. '
        'Пожалуйста наполните папку results последними актуальными '
        'файлами с результами работы парсера'
    )
    assert not len(csv_files) > 2, (
        'В папке results слишком много файлов с результатами работы парсера. '
        'Пожалуйста оставьте 2 последних актуальных csv файла.'
    )
