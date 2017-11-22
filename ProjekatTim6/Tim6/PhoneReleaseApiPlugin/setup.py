from setuptools import setup, find_packages

setup(
    name="Phone-release-api-kod",
    version="0.1",
    packages=find_packages(),
    install_requires=['ProjekatTim6>=0.1'],
    entry_points = {
        'data_import.ucitati':
            ['phoneReleaseApiKod=PhoneReleaseApi.kod.ucitavanjeTelefona:UcitavanjeTelefona'],
    },
    zip_safe=True
)