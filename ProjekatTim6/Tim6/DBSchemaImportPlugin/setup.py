from setuptools import setup, find_packages

setup(
    name="dbschema-import-kod",
    version="0.1",
    packages=find_packages(),
    install_requires=['ProjekatTim6>=0.1'],
    entry_points = {
        'data_import.ucitati':
            ['db_schema_ucitavanje_kod=DBSchemaImport.kod.ucitavanjeDBSchema:UcitavanjeIzBaze'],
    },
    zip_safe=True
)