from setuptools import setup, find_packages

setup(
    name="complex-graph-kod",
    version="0.1",
    packages=find_packages(),
    install_requires=['ProjekatTim6>=0.1'],
    entry_points = {
        'graph.prikazati':
            ['complexGraphGenerate=complexGraph.kod.complexGraphGenerate:ComplexGraphPrikaz'],
    },
    package_data={'complexGraph': ['kod/*.html']},
    zip_safe=True
)