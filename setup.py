# setup.py

from setuptools import setup, find_packages

setup(
    name='weather_data_ingestion',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
        'azure-eventhub',
        'google-cloud-pubsub'  # Add other necessary libraries
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package to scrape weather data and send it to Azure Event Hubs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/weather_data_ingestion',  # Update with your repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
