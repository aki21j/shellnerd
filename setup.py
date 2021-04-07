# from setuptools import setup
# setup(
#     ...
#     entry_points = {
#         'console_scripts': ['src.plonk:main'],
#     }
#     ...
# )


from setuptools import setup

setup(
    name='plonk',
    version='1.0',
    entry_points={
        'console_scripts': ['see-al-i=plonk.command_line:main'],
    },
    author='Ankit Gupta',
    description='Plonk everything!',
    include_package_data=True,
    zip_safe=False
)
