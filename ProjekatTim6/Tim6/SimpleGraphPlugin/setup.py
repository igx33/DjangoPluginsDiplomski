from setuptools import setup, find_packages

setup(
    name="simple-graph-kod",
    version="0.1",
    packages=find_packages(),
    install_requires=['ProjekatTim6>=0.1'],
    entry_points = {
        'graph.prikazati':
            ['SimpleGraphGenerate=simpleGraph.kod.simpleGraphGenerateCode:SimpleGraphPrikaz'],
    },
    zip_safe=True
)