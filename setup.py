from setuptools import setup,find_packages

setup(name='tfextended',
	version='0.1',
	description='Extensions to TensorFlow',
	url='http://gitlab.com/robb-brown/tfextended',
	author='Robert A. Brown',
	author_email='robb@shadowlabresearch.com',
	license='MIT',
	packages=find_packages(),
	install_requires=[
		'numpy',
		'tensorflow',
	],
	zip_safe=False)

