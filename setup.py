import setuptools

setuptools.setup(
    name="templated-dictionary",
    version="1.6",
    author="Miroslav Suchý",
    author_email="msuchy@redhat.com",
    description="Dictionary with Jinja2 expansion",
    long_description="""Dictionary where __getitem__() is run through Jinja2 template.""",
    long_description_content_type="text/markdown",
    url="https://github.com/xsuchy/templated-dictionary",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license='GPL-2.0-or-later',
    packages=['templated_dictionary'],
    include_package_data=True,
    zip_safe=False,
    install_requires = [
        'jinja2',
    ]
)
