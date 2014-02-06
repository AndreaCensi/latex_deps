from setuptools import setup, find_packages

setup(name='LatexDeps',
        author="Andrea Censi",
        author_email="censi@mit.edu",
        version="0.5",
        package_dir={'':'src'},
        packages=find_packages('src'),
        entry_points={
         'console_scripts': [
           'tex-deps = latex_deps.tex_deps:tex_deps_main',
           'tex-deps-all = latex_deps.tex_deps_all:tex_deps_all_main',
           'lyx-deps = latex_deps.lyx_deps:lyx_deps_main',
           'lyx-deps-all = latex_deps.lyx_deps_all:lyx_deps_all_main',
           ]
        },
        install_requires=[],
        extras_require={},
)

