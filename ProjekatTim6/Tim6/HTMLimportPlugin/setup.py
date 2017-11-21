from setuptools import setup, find_packages

setup(
    name="html-import-kod",
    version="0.1",
    packages=find_packages(),
    install_requires=['ProjekatTim6>=0.1'],
    entry_points = {
        'data_import.ucitati':
            ['html_ucitavanje_kod=HTMLimport.kod.ucitavanjeHTMLa:HTMLImport'],
    },
    zip_safe=True
)